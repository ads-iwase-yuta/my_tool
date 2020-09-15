import sys
from urllib import request
from urllib import parse
from bs4 import BeautifulSoup

# 駅名を入力
from_station = input('出発駅を(全角で)入力してください: ')
to_station = input('到着駅を(全角で)入力してください: ')
via_stations = []
via_station = input('経由駅を(全角で)入力してください。指定しない場合は何も入力せずENTERしてください。: ')
if len(via_station)>0:
    via_stations.append(via_station)
    via_station = input('2つ目の経由駅を(全角で)入力してください。指定しない場合は何も入力せずENTERしてください。: ')
    if len(via_station)>0:
        via_stations.append(via_station)
        via_station = input('3つ目(これが最後です)の経由駅を(全角で)入力してください。指定しない場合は何も入力せずENTERしてください。: ')
        if len(via_station)>0:
            via_stations.append(via_station)

print()

# 入力値の表示
print('出発駅: {}  到着駅: {}'.format(from_station, to_station))
if len(via_stations)>0:
    print('経由駅: {}'.format(via_stations))

# urlを生成しからYahoo検索
from_station = parse.quote(from_station)
to_station = parse.quote(to_station)
via_str = ''
for s in via_stations:
    via_str = via_str + '&via={}'.format(parse.quote(s))
url = 'https://transit.yahoo.co.jp/search/result?from={}&to={}{}'.format(from_station, to_station, via_str)
response = request.urlopen(url)
soup = BeautifulSoup(response, 'html5lib')
response.close()
print('検索URL: {}'.format(url))

print()

# 片道運賃を抽出
fare_soup = soup.select_one('#rsltlst > li:nth-child(1) > dl > dd > ul > li.fare')
if not fare_soup:
    print('ERROR: 経路が見つかりませんでした')
    sys.exit(1)
else:
    fare = fare_soup.get_text()
    fare = fare.replace('円', '')
    fare = fare.replace(',', '')
    fare = int(fare)
print('往復運賃: {} 円'.format(fare*2))

# 定期代を抽出
passprice_soup = soup.select_one('#route01 > dl > dd.option > div.detail.commuterPass > dl > dd > ul > li:nth-child(1) > span')
if not passprice_soup:
    sys.exit(1)
else:
    passprice = passprice_soup.get_text()
    passprice = passprice.replace('円', '')
    passprice = passprice.replace(',', '')
    if '-' in passprice:
        print('ERROR: 定期代が見つかりませんでした。')
        sys.exit(1)
    passprice = int(passprice)
print('定期代: {} 円/月'.format(passprice))

# どちらが得か算出
div_day = passprice/(fare*2)
div_day = int(div_day)
mod = passprice%(fare*2)
if mod>0:
    print('{}日以下: 定期じゃないほうがお得'.format(div_day))
    print('{}日以上: 定期のほうがお得'.format(div_day+1))
else:
    print('{}日以下: 定期じゃないほうがお得'.format(div_day-1))
    print('{}日: どちらも同じ'.format(div_day))
    print('{}日以上: 定期のほうがお得'.format(div_day+1))