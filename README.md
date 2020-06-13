# API_SentenseToNouns
pythonにて文章を名詞のみに分割するAPIを実装しました(作成中)

現在はローカルのみ実装済みです．

EC2上に実装し，どこからでも叩けるAPIにする予定です．

# API Specification

## Description

任意の文章に対して，文章中の名詞のみを取り出してくれるAPIです．

## URL 

(現在)

`python app.py` 実行後

http://localhost:5000/

## Input

URLの後に処理させたい文章をくっつけてポストしてください．

## Output
| Return value | Description |
| --- | --- |
| content | 文章の名詞のみが入ったリスト |

### resCode
| resCode | status | Description |
| --- | --- | --- |
| 200 | success | |
| 500 | error | error on API |
| 503 | error | Service Unavailable |
