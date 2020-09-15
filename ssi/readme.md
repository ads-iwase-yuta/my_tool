
# Screen Saver Interrupter

キー(`F13`)を特定の間隔で打鍵し、スクリーンセーバーのようなスリープ機能の起動を抑制します。

## 環境構築
* Python3環境
* Pythonライブラリ
  * PyAutoGUI
  * wxPython

## 使い方
1. ライブラリがインストールされていない場合はインストール
    ```sh
    pip install pyautogui wxPython
    ```

2. 以下のコマンドで実行
    ```sh
    python main.py {秒数}
    ```
    ※秒数には、キーを打ち込む間隔を入力する

## 参考
* https://qiita.com/takanorimutoh/items/53bf44d6d5b37190e7d1#%E3%82%AA%E3%83%97%E3%82%B7%E3%83%A7%E3%83%B3
* 