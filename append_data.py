#!/usr/bin/env python
#! -*- coding:utf-8 -*-

from __init__ import *

#既存ファイル取得
f = open("data.txt","r")
data = [i.split(",") for i in f.readlines()]
f.close()
old_data = [i[0] for i in data]

#画像のタイトル抽出
lists = [i for i in os.listdir(place+"pics/") if ".jpg" in i and "._" not in i and i.strip(".jpg") not in old_data]

#画像の切り抜き
all = dict([(i.strip(".jpg"),Image.open(place+"pics/"+i).resize((177,254), Image.ANTIALIAS).crop(box).convert("L")) for i in lists if i != "99940363.jpg"])

#縮小&データ取得
for i in all:
	data.append([i,avhash(all[i].resize((SIZE,SIZE)))])

#data = [[i,avhash(all[i].resize((SIZE,SIZE)))] for i in all]

#データの保管(事前に行っておく)
f = open("data.txt","w")
for i in data:
	f.writelines(str(i[0]))+","+str(i[1])+"\n")
f.close()
