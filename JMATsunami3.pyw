import requests
from bs4 import BeautifulSoup
import urllib3
import xml.etree.ElementTree as ET
import xmltodict
urllib3.disable_warnings()


time_url= "https://www.data.jma.go.jp/developer/xml/feed/eqvol.xml"

xml = requests.get(time_url)
xml.encoding = "utf-8"
#取得気象庁XML(地震/火山相關)

if xml.status_code == 200:
    print("時間取得正常")
else:
    print("時間取得失敗，請檢查網路或氣象廳網站是否正常")
    exit()
#判定資料是否取得正常

sp = BeautifulSoup(xml.text,features="xml")


logfile = open('log.txt', encoding="utf8")
logid1 = logfile.read()
logfile.close
#讀取上次情報ID
logid2 = sp.feed.updated.text
#讀取此次情報ID

if logid1 == logid2 and 2==1:
    exit()
#判定資料是否為重複

f = open("log.txt", "w",encoding="utf8")
f.write(sp.feed.updated.text)
f.close()
#寫入情報ID



url1 = "https://www.data.jma.go.jp/developer/xml/feed/eqvol.xml"
url2 = "http://www.yoyo0901.byethost16.com/32-39_11_02_120615_VTSE41.xml"

headers1 = dict()
headers1["Cookie"]="__test=517bdd790ceba5c7a340e606ac618072"

xml = requests.get(url2,headers=headers1)
xml.encoding = "utf-8"
#取得気象庁XML(地震/火山相關)

a=xmltodict.parse(xml.text)
print(a)
'''sp = BeautifulSoup(xml.text,features="xml")
# for i in sp.Body.Tsunami.Forecast.Item.MaxHeight:
#     print(i['condition'])
tree = ET.fromstring(str(sp.Body.Tsunami.Forecast.Item.MaxHeight))
# print(tree[2])
# for i in tree:
#     print(i.tag,i.attrib) 
#print(sp.Body.Tsunami.Forecast.Item.MaxHeight)
#exit()'''
