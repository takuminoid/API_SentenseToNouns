# API_SentenseToNouns
pythonにて文章を名詞のみに分割するAPIをFlask実装してみました．

現在はローカルのみ実装済みです．

EC2上に実装し，どこからでも叩けるAPIにする予定です．

# API Specification

## Description

任意の文章を入力すると，文章中の名詞のみを取り出してくれるAPIです！

例：こんにちは！今日はいい天気ですね！ → ['今日'，'天気']

## Usage

`python app.py` 実行後

http://localhost:5000/nouns

## Input

JSON形式で複数の文章を入力できます．以下の形式に従ってPOSTしてください．

| Argument | Description |
| --- | --- |
| sentences | 文章が入ったリスト |

## Output

JSON形式で返ってきます．

| Return value | Description |
| --- | --- |
| content | 各文章の名詞のみが入ったリスト |

### resCode
| resCode | status | Description |
| --- | --- | --- |
| 200 | success | |
| 400 | error | Bad Request |
| 500 | error | error on API |
| 503 | error | Service Unavailable |
