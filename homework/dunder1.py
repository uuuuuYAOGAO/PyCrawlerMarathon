import csv


res = "http://opendata.hccg.gov.tw/dataset/432257df-491f-4875-8b56-dd814aee5d7b/resource/de014c8b-9b75-4152-9fc6-f0d499cefbe4/download/20150305140446074.csv"
urllib.request.urlretrieve(res, './data/example.csv')


fh = open("./data/example.csv", encoding="utf-8")
f = fh.read()   ###read出來為字串形式###

fh.close()

print(f)

import csv

# 開啟 CSV 檔案
with open('./data/example.csv', newline='') as csvfile:
    # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)
    # 以迴圈輸出每一列
    for row in rows:
        print(row)    ###csvreader資料出來為序列###

import csv
with open('./data/example.csv', newline='', encoding="utf-8") as csvfile:
    # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)
    # 以迴圈輸出每一列
    for row in rows:
        print(row[5])

import csv
with open('./data/example.csv', newline='', encoding="utf-8") as csvfile:
    # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)
    # 以迴圈輸出每一列
    x = []
    for row in rows:
        x.append(row[5])
    #print(x)


# 3. 將班次一到五與其所有時間用一種資料型態個別保存
import csv
#開啟 CSV 檔案
with open('./data/example.csv', newline='', encoding="utf-8") as csvfile:
    # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)
    # 以迴圈輸出每一列
    L = [[], [], [], [], []]
    for row in rows:
        L[0].append(row[5])
        L[1].append(row[6])
        L[2].append(row[7])
        L[3].append(row[8])
        L[4].append(row[9])
    Y={}
    Y[L[0][0]] = L[0][1:]
    Y[L[1][0]] = L[1][1:]
    Y[L[2][0]] = L[2][1:]
    Y[L[3][0]] = L[3][1:]
    Y[L[4][0]] = L[4][1:]
    print(Y)