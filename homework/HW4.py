import requests
import json

# r = requests.get('https://api.github.com/events')
# r.text
# json.loads(r.text)



###比較一下範例檔案中的「r.text」與「json.loads(r.text)」讀出來的內容有什麼差異
# r.text資料為字串形式
# json.loads(r.text)資料為json形式


###尋找一個合適的 API 接口做練習，並且查看其回傳內容

r = requests.get("http://odata.wra.gov.tw/v4/RealtimeWaterLevel")
b = json.loads(r.text)
print(b)
#出現{'@odata.context': 'http://odata.wra.gov.tw/v4/$metadata#RealtimeWaterLevel', '@odata.count': 0, 'value': []}


r = requests.get('https://cat-fact.herokuapp.com/facts')
c = json.loads(r.text)
print(c)