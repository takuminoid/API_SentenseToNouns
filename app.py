from flask import Flask, request
import traceback
import json
import MeCab

import preprocessing as pr

app = Flask(__name__)

def tokenize(sentence: str): # 名詞のみに分解
  nouns = []
  mecab = MeCab.Tagger("-Ochasen")
  mecab.parse("")
  split_s = mecab.parseToNode(pr.preprocessing(sentence))
  while split_s:
    word = split_s.feature.split(",")[6]
    hinshi = split_s.feature.split(",")[0]
    if hinshi == u"名詞":
      nouns.append(word)
    split_s = split_s.next
  return nouns

@app.route('/<sentence>', methods=["POST"])
def SentenceToNouns(sentence):
  rescode = {
    'resCode': '500',
    'Message': 'error on API'
  }

  try:
    nouns = tokenize(sentence)
    res = {
    "content": nouns
    }
    return res
  except:
    traceback.print_exc()
    rescode.update(resCode='503', Message='Service Unavailable')
    return json.dumps(rescode)

  return json.dumps(rescode)

if __name__ == "__main__":
  print(" * Flask starting server...")
  app.run(debug=False, host='0.0.0.0', port=5000)
