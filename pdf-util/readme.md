
* ビルド  
  ```sh
  pyinstaller pdf-util.py --onefile
  ```
* exe  
  [ここ](https://github.com/ads-iwase-yuta/my_tool/releases/download/pdf_merge0.0.1/pdf_merge.exe)
* 使い方
  ```sh
  pdf-util.exe a.pdf0:2 b.pdf1:2
  ```
  でa.pdfの0ページ目から2ページ目(2も含む)と、b.pdfの1～2ページ目を結合します。  
  結果的に結合後の構成は以下になる
  ```
  0ページ目: a.pdf 0ページ
  1ページ目: a.pdf 1ページ
  2ページ目: a.pdf 2ページ
  3ページ目: b.pdf 1ページ
  4ページ目: b.pdf 2ページ
  ```