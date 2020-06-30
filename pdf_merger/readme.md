# pdf_merger

## 概要
複数のpdfを1つに結合します。

## 使い方
1. PythonにPyPDF2をインストール
    ```sh
    pip install PyPDF2
    ```

2. pdf_merger/input 配下に結合したいpdfファイルを全て配置  
   注) **結合の順序はOS標準のファイル名順となります。確実に望んだ順序にしたい場合は、ファイル名の先頭に番号を振るなどの工夫を行ってください。**

3. プログラム実行
    ```sh
    cd pdf_merger
    python run.py
    ```

4. 結合されたpdfは pdf_merger/output にあります。
