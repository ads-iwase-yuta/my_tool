import sys
import os
from pathlib import Path
from argparse import ArgumentParser
import re

import qrcode

# コマンドライン引数定義
argparser = ArgumentParser()
argparser.add_argument('content', type=str,
                        help='Specify number of epoch')
argparser.add_argument('-m', '--min', type=int,
                        default=1,
                        help='min size of box_size')
argparser.add_argument('-M', '--max', type=int,
                        default=15,
                        help='max size of box_size')

# コマンドライン引数取得
args = argparser.parse_args()
content = args.content
args_min = args.min
args_max = args.max

# 不正な数値の場合修正
if args_min<1:
    args_min = 1
    print('minが1より小さいです。 min=1として実行します.')
if args_max<1:
    args_max = args_min
    print('minが1より小さいです。 max={}として実行します.'.format(args_max))
if args_min>args_max:
    print(' min = {}\n max = {}'.format(args_min, args_max))
    print('minがmaxより大きいです。プログラムを強制終了します。')
    sys.exit(1)

# 本処理
escaped_content = re.sub(r'[\\/:*?"<>|]+', '', content)
output_dir = Path('./output') / escaped_content
os.makedirs(str(output_dir), exist_ok=True)
for s in range(args_min, args_max+1, 1):
    qr = qrcode.QRCode(
        version=1,
        box_size=s,
    )
    qr.add_data(content)
    qr.make(fit=True)

    img_path = output_dir / ('qr_' + str(s) + '.png')
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(str(img_path))