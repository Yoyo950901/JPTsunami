import requests
import urllib3
from bs4 import BeautifulSoup
# import xml.etree.ElementTree as ET
urllib3.disable_warnings()

url1 = "https://www.data.jma.go.jp/developer/xml/feed/eqvol.xml"
url2 = "http://www.yoyo0901.byethost16.com/32-39_11_02_120615_VTSE41.xml?i=2"

headers1 = dict()
headers1["Cookie"]="__test=517bdd790ceba5c7a340e606ac618072"

xml = requests.get(url2,headers=headers1)
xml.encoding = "utf-8"
#取得気象庁XML(地震/火山相關)
sp = BeautifulSoup(xml.text,features="xml")
print(sp)

