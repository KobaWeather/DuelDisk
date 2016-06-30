#!/usr/bin/env python
#! -*- coding:utf-8 -*-

from PIL import Image
import sqlite3 as sq
import os
import sys

argvs = sys.argv
argc = len(argvs)

#resize用
SIZE = 56
#切抜範囲の設定(112x112)
box = (29,55,141,167)
# 画像フォルダの指定
#local_placeはYgoproが置かれているディレクトリを指定
local_place = "/Volumes/NO NAME/"
place = local_place+"Ygopro/"

def select_deck(deck_name):
	return [int(i.strip("\n")) for i in open(deck_name,"r").readlines() if i.strip("\n").isdigit()]

def create_deck():
	f = open("data.txt","r")
	if ".ydk" in argvs[-1]: #デッキ縛り
		#デッキの取得
		deck = select_deck(place+"deck/"+argvs[-1])
		#重複削除
		ones = list(set(deck))
		#比較データの取得
		data = [i.split(",") for i in f.readlines() if int(i.split(",")[0]) in ones]
	
	elif argvs[-1] == "monster": #モンスター縛り
		con = sq.connect(place+"cards.cdb")
		c = con.cursor()
		monster = [i[0] for i in c.execute("select id,type from datas") if i[1]%2 != 0]
		data = [i.split(",") for i in f.readlines() if int(i.split(",")[0]) in monster]
	
	else:#デッキ縛りしない場合はこっち
		data = [i.split(",") for i in f.readlines() if int(i.split(",")[0])]

	f.close()		
	return data

#スクリプトデータの取得
def search_lua(lua):
	try:
		f = open(lua,"r")
		card = f.readlines()
		f.close()
		return card
	except IOError:
		return 0

#データベース検索
def search_cdb(cdb,decide_card):
	con = sq.connect(cdb)
	c = con.cursor()
	data = [i for i in c.execute(u"select * from datas where id = ?",(decide_card,))]
	text = [i for i in c.execute(u"select name,desc from texts where id = ?",(decide_card,))]
	con.close()
	return data,text

#Average Hash法
def avhash(im):
    avg = reduce(lambda x, y: x + y, im.getdata()) / (SIZE*SIZE)
    return reduce(lambda x, (y, z): x | (z << y),
                  enumerate(map(lambda i: 0 if i < avg else 1, im.getdata())),
                  0)

#ハミング距離の計算
def hamming(h1, h2):
    h, d = 0, h1 ^ h2
    while d:
        h += 1
        d &= d - 1
    return h