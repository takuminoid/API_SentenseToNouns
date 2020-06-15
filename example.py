import requests
from pprint import pprint

local_url = "http://localhost:5000/nouns"

if __name__ == "__main__":
  request_para = {
    'sentences': ["こんにちは！今日はいい天気ですねえ，こんな日は釣りにでもいきたいですよねえ", "あ，ジョン！ハロー！今日は雨ですねえ，明日は曇りだそうですよ，頑張りましょうね！", "僕の水を飲んだのは誰ですか？"]
  }
  res = requests.post(local_url, json=request_para)
  json_data = res.json()
  # pprint(json_data)
  print(json_data['content'])
  # [['今日', '天気', '日', '釣り'], ['ジョン', 'ハロー', '今日', '雨', '明日'], ['僕', '水', 'の', '誰']]
