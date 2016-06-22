#!/usr/bin/env python
#! -*- coding:utf-8 -*-

from __init__ import *

import sys

argvs = sys.argv
argc = len(argvs)

if argc >= 3:
	deck_name = place+"deck/"+argvs[-1]
	#デッキの取得
	deck = [int(i.strip("\n")) for i in open(deck_name,"r").readlines() if not("e" in i or "a" in i)]
	#重複削除
	ones = list(set(deck))
	#比較データの取得
	f = open("data.txt","r")
	data = [i.split(",") for i in f.readlines() if int(i.split(",")[0]) in ones]
	f.close()

else:
	f = open("data.txt","r")
	data = [i.split(",") for i in f.readlines() if int(i.split(",")[0])]#デッキ縛りしない場合はこっち
	f.close()

#調べたい画像の取得
h = Image.open(argvs[1]).convert("L")
par = float(h.size[0])/float(h.size[1])
if 0.6 < par < 0.7:
	h = h.resize((177,254),Image.ANTIALIAS).crop(box)
h = h.resize((SIZE,SIZE))
h = avhash(h)
	
#ハミング距離の測定
seg = [(i[0],hamming(int(i[1]),h)) for i in data]
	
#順位設定
card = [f for f, ham in sorted(seg, key=lambda i: i[1])[:5]]

decide_card = card[0]

print "\nカード番号:\n",decide_card
Image.open(place+"pics/"+decide_card+".jpg").show()

#スクリプトデータの取得
try:
	f = open(place+"script/c"+decide_card+".lua","r")
	card = f.readlines()
	f.close()
except IOError:#通常のスクリプトにない場合は別フォルダに入っている
	f = open(place+"expansions/live/script/c"+decide_card+".lua","r")
	card = f.readlines()
	f.close()

#カードの表示
#print card[0].strip("--")

#データベースへ接続->データ抽出
#英語版で探したい場合は日本語版をコメントアウト(#)
cdb = place + "cards.cdb"#英語版
cdb = place+"/0x1339-20160207-nopics/cards.cdb"#日本語版

con = sq.connect(cdb)
c = con.cursor()
data = [i for i in c.execute(u"select * from datas where id = ?",(decide_card,))]
#データ取得完了？？
text = [i for i in c.execute(u"select name,desc from texts where id = ?",(decide_card,))]

con.close()

#通常のcdbで見つからなかった時はliveフォルダ内のcdbから検索
cdb = place+"/expansions/live/"
for base in os.listdir(cdb):
	if len(data) == 0 and ".cdb" in base:
		con = sq.connect(cdb+base)
		c = con.cursor()
		data = [i for i in c.execute(u"select * from datas where id = ?",(decide_card,))]
		text = [i for i in c.execute(u"select name,desc from texts where id = ?",(decide_card,))]
		con.close()

#カード名と効果を表示
print "\nカード名:\n",text[0][0]
print "\nカード効果:\n",text[0][1]



#http://www3.atwiki.jp/ads-wiki/pages/30.html
