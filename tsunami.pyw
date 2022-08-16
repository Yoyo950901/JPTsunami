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
        print(output)
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
        print(output)
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

警報種類 = ["MajorWarning","Warning","Watch","Unknown"]
警報列表 = ["大津波警報　","津波警報　","津波注意報　","種類不明　"]


def scale(y):
#各地警報函數
    a=0
    output = ""
    for i in areas:
        if (areas[a]["grade"]) == 警報種類[y]:
            output = output + areas[a]["name"] + "　"
        a=a+1
    #獲取完全資料以供下面分辨

    if 警報列表[y] + output[0:-1] != 警報列表[y]:
    #分辨此警報種類是否有資料，若無跳過
    

        output=''
    #初始化正式迴圈
        a=0
        for i in areas:
            if (areas[a]["grade"]) == 警報種類[y]:
            #分離所需震度

                本次輸出 = output + areas[a]["name"] + "　"

                字數=0
                for b in 本次輸出:
                    字數=字數+1
                #本次迴圈字數


                if 字數 > 31:
                    output = (警報列表[y]+output[0:-1])
                    f = open("output.txt", "w",encoding="utf8")
                    f.write(output)
                    f.close()
                    time.sleep(10)

                    logfile = open('log.txt', encoding="utf8")
                    logid3 = logfile.read()
                    logfile.close
                    if logid2 != logid3:
                        exit()
                    output=''

                output=output + areas[a]["name"] + "　"
            a=a+1
        output = 警報列表[y]+output[0:-1]
        print(output)
        f = open("output.txt", "w",encoding="utf8")
        f.write(output)
        f.close()
        time.sleep(10)

        logfile = open('log.txt', encoding="utf8")
        logid3 = logfile.read()
        logfile.close
        if logid2 != logid3:
            exit()



for i in range(1000):

    output = "津波警報・注意報が発表されました"
    f = open("output.txt", "w",encoding="utf8")
    f.write(output)
    f.close()
    print(output)
    time.sleep(5)

    logfile = open('log.txt', encoding="utf8")
    logid3 = logfile.read()
    logfile.close
    if logid2 != logid3:
        exit()
    
    for j in range(0,4):
        scale(j)
