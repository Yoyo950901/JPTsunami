# -*- coding: utf-8 -*-
from asyncore import write
import time
import requests
import urllib3
import os
urllib3.disable_warnings()

url = "https://api.p2pquake.net/v2/jma/tsunami?limit=1&offset=0"

data = requests.get(url, verify=False).json()[0]
areas = data["areas"]

logfile = open('log.txt', encoding="utf8")
logid1 = logfile.read()
logfile.close
#讀取上次情報ID
logid2 = data["id"]
#讀取此次情報ID

if logid1 == logid2:
    exit()
#判定資料是否為重複

f = open("log.txt", "w",encoding="utf8")
f.write(data["id"])
f.close()
#寫入情報ID


if data["cancelled"] == True:

    for i in range(10):

        output = ("津波警報・注意報が解除されました")

        f = open("output.txt", "w",encoding="utf8")
        f.write(output)
        f.close()
        time.sleep(10)

        logfile = open('log.txt', encoding="utf8")
        logid3 = logfile.read()
        logfile.close
        if logid2 != logid3:
            exit()

        output = ("引き続き海面変動に注意してください")

        f = open("output.txt", "w",encoding="utf8")
        f.write(output)
        f.close()
        time.sleep(10)

        logfile = open('log.txt', encoding="utf8")
        logid3 = logfile.read()
        logfile.close
        if logid2 != logid3:
            exit()

    f = open("output.txt", "w",encoding="utf8")
    f.write("")
    f.close()
    exit()



a = 0
name = ""

for i in areas:
    if areas[a]["grade"] == "MajorWarning":
        name = name + areas[a]["name"] + "　"
    a = a + 1
ootsunami = "＜大津波警報＞" + name[0:-1]

a = 0
name = ""
for i in areas:
    if areas[a]["grade"] == "Warning":
        name = name + areas[a]["name"] + "　"
    a = a + 1
tsunami = "＜津波警報＞" + name[0:-1]

a = 0
name = ""
for i in areas:
    if areas[a]["grade"] == "Watch":
        name = name + areas[a]["name"] + "　"
    a = a + 1
tsunamichuui = "＜津波注意報＞" + name[0:-1]

a = 0
name = ""
for i in areas:
    if areas[a]["grade"] == "Unknown":
        name = name + areas[a]["name"] + "　"
    a = a + 1
humei = "＜種類不明＞" + name[0:-1]

print(ootsunami)
print(tsunami)
print(tsunamichuui)
print(humei)


for i in range(1000):

    output = "津波警報・注意報が発表されました"
    f = open("output.txt", "w",encoding="utf8")
    f.write(output)
    f.close()
    time.sleep(10)

    logfile = open('log.txt', encoding="utf8")
    logid3 = logfile.read()
    logfile.close
    if logid2 != logid3:
        exit()
    
    #大海嘯警報
    if ootsunami != "＜大津波警報＞":

        length = 0
        for i in ootsunami:
            length+=1
        #判定情報字數
        row = length//36+1
        a1 = 0
        a2 = 0
        for i in range(row):
            a1 = 36 * i
            a2 = a1 + 36
            output = ootsunami[a1:a2]
            f = open("output.txt", "w",encoding="utf8")
            f.write(output)
            f.close()
            a1 = a1 + 1
            time.sleep(10)

            logfile = open('log.txt', encoding="utf8")
            logid3 = logfile.read()
            logfile.close
            if logid2 != logid3:
                exit()


    #海嘯警報
    if tsunami != "＜津波警報＞":

        length = 0
        for i in tsunami:
            length+=1
        #判定情報字數
        row = length//36+1
        a1 = 0
        a2 = 0
        for i in range(row):
            a1 = 36 * i
            a2 = a1 + 36
            output = tsunami[a1:a2]
            f = open("output.txt", "w",encoding="utf8")
            f.write(output)
            f.close()
            a1 = a1 + 1
            time.sleep(10)

            logfile = open('log.txt', encoding="utf8")
            logid3 = logfile.read()
            logfile.close
            if logid2 != logid3:
                exit()


    #海嘯注意報
    if tsunamichuui != "＜津波注意報＞":

        length = 0
        for i in tsunamichuui:
            length+=1
        #判定情報字數
        row = length//36+1
        a1 = 0
        a2 = 0
        for i in range(row):
            a1 = 36 * i
            a2 = a1 + 36
            output = tsunamichuui[a1:a2]
            f = open("output.txt", "w",encoding="utf8")
            f.write(output)
            f.close()
            a1 = a1 + 1
            time.sleep(10)

            logfile = open('log.txt', encoding="utf8")
            logid3 = logfile.read()
            logfile.close
            if logid2 != logid3:
                exit()


    #不明
    if humei != "＜種類不明＞":

        length = 0
        for i in humei:
            length+=1
        #判定情報字數
        row = length//36+1
        a1 = 0
        a2 = 0
        for i in range(row):
            a1 = 36 * i
            a2 = a1 + 36
            output = humei[a1:a2]
            f = open("output.txt", "w",encoding="utf8")
            f.write(output)
            f.close()
            a1 = a1 + 1
            time.sleep(10)

            logfile = open('log.txt', encoding="utf8")
            logid3 = logfile.read()
            logfile.close
            if logid2 != logid3:
                exit()


    f = open("output.txt", "w",encoding="utf8")
    f.write("")
    f.close()
    time.sleep(60)

    logfile = open('log.txt', encoding="utf8")
    logid3 = logfile.read()
    logfile.close
    if logid2 != logid3:
        exit()