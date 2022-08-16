from asyncore import write
from encodings import utf_8
import time
import requests
import urllib3
import xmltodict
import os
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
urllib3.disable_warnings()

xml = requests.get("https://www.data.jma.go.jp/developer/xml/feed/eqvol.xml")
xml.encoding = "utf-8"
#取得気象庁XML(地震/火山相關)

sp = BeautifulSoup(xml.text, 'xml')

if xml.status_code == 200:
    print("資料取得正常")
else:
    print("資料取得失敗，請檢查網路或氣象廳網站是否正常")
    exit()
#判定資料是否取得正常



logfile = open("JMAlog.txt", encoding="utf8")
logid1 = logfile.read()
logfile.close
#讀取上次情報ID

#print(sp.title.text)
z = ""
for i in sp.select("entry"): #搜尋標題為"津波警報・注意報・予報a"的XML
    if i.title.text == "津波警報・注意報・予報a":
        url = i.id.text #若取得標題為海嘯警報的資料 設定URL
        logid2 = i.update.text
        if logid1 == logid2: #判定情報是否為新的
          exit()
        f = open("JMAlog.txt", "w",encoding="utf8")
        f.write(logid2)
        f.close()
        #寫入情報ID
        z = "a"
        break

if z == "": #如果未在XML取得海嘯資訊則退出
    print("未取得海嘯資訊")
    exit()

def log(): #讀取Log檔ID 若跟此次ID不一樣則退出
    logfile = open('JMAlog.txt', encoding="utf8")
    logid3 = logfile.read()
    logfile.close
    if logid2 != logid3:
        exit()

def file(y=8): #寫入資料到output文字檔
    f = open("JMAoutput.txt", "w",encoding="utf8")
    f.write(output)
    f.close()
    print(output)
    time.sleep(y)



# url = "http://www.yoyo0901.byethost16.com/津波警報/32-39_11_02_120615_VTSE41.xml"#測試用(東日本大震災 第1報) (三陸沖M8.9)
# url = "http://www.yoyo0901.byethost16.com/津波警報/32-39_11_09_120615_VTSE41.xml"#測試用(東日本大震災 第3報) (三陸沖M8.9)
# url = "http://www.yoyo0901.byethost16.com/津波警報/32-39_12_02_191025_VTSE41.xml"#測試用(2016訓練報1) (南海トラフM9.1)
# url = "http://www.yoyo0901.byethost16.com/津波警報/32-39_12_07_191025_VTSE41.xml"#測試用(2016訓練報2) (南海トラフM9.1)
# url = "http://www.yoyo0901.byethost16.com/津波警報/32-39_12_13_191025_VTSE41.xml"#測試用(2016訓練報3) (南海トラフM9.1)
# url = "http://www.yoyo0901.byethost16.com/津波警報/32-39_13_02_191025_VTSE41.xml"#測試用(2018訓練報) (東京都23区M7.3)
# url = "http://www.yoyo0901.byethost16.com/津波警報/32-39_13_07_191025_VTSE41.xml"#測試用(2018訓練報 解除) (東京都23区M7.3)
# url = "http://www.yoyo0901.byethost16.com/津波警報/20220621072020_0_VTSE41_010000.xml"#測試用(父島近海 預報) (M6.2)
xml2 = requests.get(url) #取得資料

# headers1 = dict()
# headers1["Cookie"]="__test=31d1719ea681dba26cafe6acb0fa6548"

# xml2 = requests.get(url,headers=headers1)
xml2.encoding = "utf-8"
xml2=xmltodict.parse(xml2.text) #XML轉JSON

data = xml2["Report"] #資料主體

title = data["Head"]["Title"] #標題
headline = data["Head"]["Headline"]["Text"] #註解文
tsunami = data["Body"]["Tsunami"] #海嘯注警報詳細


if data["Control"]["Status"] == "訓練": #判定是否為訓練報
    print("これは訓練です")
    exit()


#判定警報類型
if "取消" in data["Head"]["InfoType"]:
    warntype = "取消"
elif "解除" in headline:
    warntype = "注警報解除"
    if "警報" in headline:
        cancel = "warn"
    elif "注意報" in headline:
        cancel = "watch"
elif "大津波警報" in data["Head"]["Title"]:
    warntype = "大津波警報"
elif "津波警報" in data["Head"]["Title"]:
    warntype = "津波警報"
elif "津波注意報" in data["Head"]["Title"]:
    warntype = "津波注意報"
elif "津波予報" in data["Head"]["Title"]:
    warntype = "津波予報"

#判定海嘯警報是否為"東日本大震災級"
if "東日本大震災クラス" in headline:
    geq = "y"
else:
    geq = ""

print(warntype)

warningname = ["大津波警報","津波警報","津波注意報","津波予報（若干の海面変動）"] #各海嘯警報種類列表
warninglist = ["大津波警報","津波警報","津波注意報","津波予報"]

if warntype != "津波予報" and warntype != "注警報解除": #判定警報種類並決定要循環幾次
    g = 1000
elif warntype == "津波予報":
    g = 10
elif warntype == "注警報解除":
    g = 20
elif warntype == "取消":
    g = 1


for i in range(g): #輸出資料

    output = "津波情報"
    file(2)

    if warntype == "大津波警報" or warntype == "津波警報" or warntype == "津波注意報": #輸出各海嘯預報及解除警報以外的海嘯預報區的警報種類
        
        if warntype == "大津波警報":
            output = "大津波警報を発表されました　直ちに避難してください"
            file(5)
            log()
            if geq == "y":
                output = "東日本大震災クラスの巨大津波　直ちに避難"
                file(5)
                log()
        elif warntype == "津波警報":
            output = "津波警報を発表されました　直ちに避難してください"
            file(5)
            log()
        elif warntype == "津波注意報":
            output = "津波注意報を発表されました　海岸から離れてください"
            file(5)
            log()

        l = 0
        for i in range(3): #重複3次 判定大海嘯、海嘯警報、海嘯注意等
            a = 0
            output = ""
            nextoutput = ""
            for i in tsunami["Forecast"]["Item"]:
                if type(i) != str:
                    if (i["Category"]["Kind"]["Name"]).replace("大津波警報：発表","大津波警報") == warningname[l]:
                        nextoutput = output +  "　" + i["Area"]["Name"]

                        outputlen = 0
                        for w in nextoutput:
                            outputlen += 1

                        if outputlen > 31:
                            output = warninglist[l] + output
                            file(5)
                            log()
                            output = ""


                        output += "　" + i["Area"]["Name"]
                else:
                    output = "　" + tsunami["Forecast"]["Item"]["Area"]["Name"]
            l += 1
            if output == "":
                continue
            output = warninglist[l-1] + output
            file(5)
            log()


    if warntype == ("注警報解除"):
        if cancel == "warn":
            output = "大津波警報・津波警報を解除されました"
            file(10)
            log()
        if cancel == "watch":
            output = "津波注意報を解除されました"
            file(10)
            log()
        output = "今後数時間程度は海面変動に注意してください"
        file(10)
        log()

    if warntype == "津波予報": #輸出地震發布海嘯預報時的資料(包含海嘯注警報解除時發布的海面變動等)
        output = "津波予報を発表されました"
        file(10)
        log()
        output = "今後２、３時間程度は若干の海面変動が予想されますが　被害の心配はありません"
        file(10)
        log()
        output = ""
        nextoutput = ""
        for i in tsunami["Forecast"]["Item"]:
            if type(i) != str:
                if i["Category"]["Kind"]["Name"] == "津波予報（若干の海面変動）":
                    nextoutput = output +  "　" + i["Area"]["Name"]

                    outputlen = 0
                    for w in nextoutput:
                        outputlen += 1

                    if outputlen > 31:
                        output = "津波予報" + output
                        file(5)
                        log()
                        output = ""

                    output += "　" + i["Area"]["Name"]
            else:
                output = "　" + tsunami["Forecast"]["Item"]["Area"]["Name"]

        output = "津波予報" + output
        file(5)
        log()

    if warntype == "取消": #輸出取消報資料
        output = "先ほどの津波警報・注意報を取り消しました"
        file(120)
        log()


    #輸出"各預報區預測高度及預測到達時間"
    b = 0
    if warntype == "大津波警報" or warntype == "津波警報" or warntype == "津波注意報":
        output = "津波の到達予想時刻と予想される津波の高さは次の通りです"
        file(5)
        log()

        def test(x):
            try:
                return x["FirstHeight"]["ArrivalTime"]
            except:
                return '99999999999999999999'
        ab=sorted(tsunami["Forecast"]["Item"],key=lambda x:test(x))
        warning = ["大津波警報","津波警報","津波注意報"]
        for j in range(3):
            for f in range(3):
                for i in ab:
                    try:
                        if warning[j] == i["Category"]["Kind"]["Name"].replace("：発表",""): #輸出不包含"海嘯預報"的資料
                            Condition = ["第１波の到達を確認","津波到達中と推測","ただちに津波来襲と予測"]
                            if i["FirstHeight"]["Condition"] == Condition[f]:
                                output = ""
                                warn = (i["Category"]["Kind"]["Name"]).replace("：発表","") #警報種類
                                areaname = i["Area"]["Name"] #預報區

                                try: #預測到達時間
                                    arrtime = i["FirstHeight"]["Condition"] #此區為即將到達及第1波到達確認
                                except:
                                    pass
                                
                                height = i["MaxHeight"]["jmx_eb:TsunamiHeight"]["@description"] #預測高度
                                output = (f"{warn}　{areaname}　{arrtime}　{height}").replace("第１波の到達を確認","すでに到達").replace("津波到達中と推測","到達が").replace("ただちに津波来襲と予測","すぐ来る")
                                file(5)
                                log()
                    except:
                        pass

            
            for i in ab:
                if warning[j] == i["Category"]["Kind"]["Name"].replace("：発表",""): #輸出不包含"海嘯預報"的資料
                    output = ""
                    warn = (i["Category"]["Kind"]["Name"]).replace("：発表","") #警報種類
                    areaname = i["Area"]["Name"] #預報區

                    try: #預測到達時間
                        ampm = ""
                        arrtime = i["FirstHeight"]["ArrivalTime"] #此區為正常預測時間(包含年月日時分秒等)
                        
                        arrtimeh = arrtime[11:13]
                        if int(arrtimeh) > 12:
                            arrtimeh = int(arrtimeh) - 12
                            ampm = "午後"
                        else:
                            ampm = "午前"

                        if str(arrtimeh)[:1] == "0":
                            arrtimeh = str(arrtimeh).replace("0","",1)
                    
                        arrtimem = arrtime[14:16]
                        if arrtimem[:1] == "0":
                            arrtimem = arrtimem.replace("0","",1)

                        arrtime = f"{arrtimeh}時{arrtimem}分頃"
                    except:
                        pass
                    
                    height = i["MaxHeight"]["jmx_eb:TsunamiHeight"]["@description"] #預測高度
                    output = (f"{warn}　{areaname}　{ampm}{arrtime}　{height}")
                    file(5)
                    log()

output = ""
file(0)