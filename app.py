from flask import Flask, request
import traceback
import json
import MeCab

import preprocessing as pr

app = Flask(__name__)

def tokenize(sentences: list) -> list: # 名詞のみに分解
  nouns = []
  mecab = MeCab.Tagger("-Ochasen")
  mecab.parse("")
  for s in sentences:
    nouns_buf = []
    split_s = mecab.parseToNode(pr.preprocessing(s))
    while split_s:
      word = split_s.feature.split(",")[6]
      hinshi = split_s.feature.split(",")[0]
      if hinshi == u"名詞":
        nouns_buf.append(word)
      split_s = split_s.next
    nouns.append(nouns_buf)
  return nouns

@app.route('/nouns', methods=["POST"])
def SentenceToNouns():
  rescode = {
    'resCode': '500',
    'Message': 'error on API'
  }
  try:
    given_json = request.json
    sentences = given_json['sentences']
  except:
    traceback.print_exc()
    rescode.update(resCode='400', Message='Bad Request')
    return json.dumps(rescode)
  try:
    nouns = tokenize(sentences)
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
