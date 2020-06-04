import requests
import json
import statistics

r = requests.get(' https://www.dcard.tw/_api/forums/pet/posts?popular=true')
response = r.text
data = json.loads(response)
#第一題
for d in data:    
    n+=1
print(n) #一次總共幾筆資料
for c in data[0]:
    print(c)  #每一筆資料包含哪些欄位


#第2題取出每一筆資料的「標題」、「貼文時間」、「留言人數」、「按讚人數」
for k in data:
    print(k['title'])#資料的標題
    print(k['createdAt'])#貼文發布時間
    print(k['commentCount'])#留言人數
    print(k['likeCount'])#按讚人數


#第三題計算熱門文章的「平均留言人數」與「平均按讚人數」
comment = []
like = []
for i in data:
    comment.append(i['commentCount'])#留言人數
for j in data:
    like.append(j['likeCount'])#按讚人數
print(statistics.mean(comment))
print(statistics.mean(like))


