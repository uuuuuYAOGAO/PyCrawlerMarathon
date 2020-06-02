# # <?xml version="1.0" encoding="UTF-8"?>
# # <CUPOY>    
# #   <Title>爬蟲⾺馬拉松</Title>    
# #   <Author>Wei</Author>    
# #   <Chapters>        
# #       <Chapter name="01">資料來來源與存取</Chapter>        
# #       <Chapter name="02">靜態網⾴頁爬蟲</Chapter>        
# #        <Chapter name="03">動態網⾴頁爬蟲</Chapter>    
# #   </Chapters>
# # </CUPOY>
# # 如果我們想要取出檔案中，中文的部分該怎麼做？

# #方法一 xml.dom
# #存取資料
# import xml.dom.minidom
# #存取檔案
# doc = xml.dom.minidom.parse("./sample.xml")
# #存取第一個要的中文部分
# print(doc.getElementsByTagName("Title")[0].firstChild.nodeValue)

# #有重複抬頭用for取
# chapters = doc.getElementsByTagName("Chapter")
# for chapter in chapters:
#     print(chapter.getAttribute('name'), chapter.firstChild.nodeValue)


# #方法二 xml.etree
# import xml.etree.ElementTree as etree
# #存取檔案
# tree = ET.parse("./sample.xml")
# root = tree.getroot()

# #存取我們的資訊
# print(root[0].text)

# #用迴圈儲存
# chapters = root[2]
# for chapter in chapters:
#     print(chapter.attrib['name'], chapter.text)


# #方法三 xmltodict
# import xmltodict

# #存取檔案
# with open("./sample.xml") as fd:
#     doc = dict(xmltodict.parse(fd.read()))

# #存取第一個
# print(doc['CUPOY']['Title'])

# #迴圈存取
# chapters = doc['CUPOY']['Chapters']['Chapter']
# for chapter in chapters:
#     print(chapter['@name'], chapter['#text'])
-------------------------------------------------------------------------------------------------------------------------
#file I/O和xmltodict的差異
#file I/O 資料形式仍為xml
#xmltodict 資料形式為dictionary



import os, sys
import xmltodict
fh = open("./example/64_72hr_CH.xml", "r", encoding='UTF-8')
xml = fh.read()
fh.close()


#1. 請問高雄市有多少地區有溫度資料？
d = dict(xmltodict.parse(xml))

datasetDescription = d['cwbopendata']['dataset']['locations']['location']
print(len(datasetDescription))

# 2. 請取出每一個地區所記錄的第一個時間點跟溫度
datasetDescription = d['cwbopendata']['dataset']['locations']['location']

for weatherElement in datasetDescription:
# print(weatherElement['weatherElement'][0]['time'][0]['dataTime'], weatherElement['weatherElement'][0]['time'][0]['elementValue']['value']['#text'])


    print(weatherElement['locationName'])
    print(weatherElement['weatherElement'][0]['time'][0]['dataTime'] )
    print(weatherElement['weatherElement'][0]['time'][0]['elementValue']['value'], weatherElement['weatherElement'][0]['time'][0]['elementValue']['measures'] )

#3. 請取出第一個地區所記錄的每一個時間點跟溫度
first = datasetDescription[0]
print(first['locationName'])
for everyrecord in first['weatherElement'][0]['time']:
    print(everyrecord['dataTime'])
    print(everyrecord['elementValue']['value'], everyrecord['elementValue']['measures'])