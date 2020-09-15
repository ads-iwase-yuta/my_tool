import sys
import time
import datetime
import threading
import pyautogui

def init():
    duration = 120
    args = sys.argv
    if len(args)>1:
        try:
            duration = int(args[1])
        except:
            pass

    key = 'f13'

    return (duration, key)


def press_loop(duration, key):
    print('Screen Saver Interrupter start. duration = {}[sec], key = \'{}\''.format(duration, key))
    while True:
        # 現在時刻取得
        now = datetime.datetime.now()
        now = now.strftime('%Y-%m-%d %H:%M:%S')
        # 指定されたキーを押す
        pyautogui.press(key)
        print('press {} at {}'.format(key, now))
        # 指定された時間スリープする
        time.sleep(duration)

if __name__ == "__main__":
    # 設定初期化
    (duration, key) = init()
    # キー入力ループ
    t1 = threading.Thread(target=press_loop, args=(duration, key))
    t1.start()
    # タスクトレイ常駐化
    import app
    window = app.App(False)
    window.MainLoop()
