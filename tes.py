import requests
from pprint import pprint

local_url = "http://localhost:5000/"

if __name__ == "__main__":
  request_para = "こんにちは！私の名前はジョンです．今日の天気は気持ちが良いですね！"
  res = requests.post(local_url+request_para)
  # pprint(res.json())
  json_data = res.json()
  print(json_data['content'])
