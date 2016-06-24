#!/usr/bin/env python
#! -*- coding:utf-8 -*-

from __init__ import *

#比較用データの取得
data = create_deck()

#調べたい画像の取得
h = Image.open(argvs[1]).convert("L")
h = h.resize((177,254),Image.ANTIALIAS).crop(box)
h = h.resize((SIZE,SIZE))
#h.save("gray.png")
#h.convert("1").save("one.png")
h = avhash(h)


	
#ハミング距離の測定
seg = [(i[0],hamming(int(i[1]),h)) for i in data]

for f, ham in sorted(seg, key=lambda i: i[1])[:5]:
	print str(f)+":"+str(ham)
	
#順位設定
card = [f for f, ham in sorted(seg, key=lambda i: i[1])[:5]]

#カードの決定
decide_card = card[0]

print "\nカード番号:\n",decide_card
Image.open(place+"pics/"+decide_card+".jpg").show()
#Image.open(place+"pics/"+decide_card+".jpg").save("resullt.png")

#スクリプトデータの取得
lua = [place+"script/c"+decide_card+".lua",place+"expansions/live/script/c"+decide_card+".lua",place+"expansions/script/c"+decide_card+".lua"]

for i in lua:
	card = search_lua(i)
	if card != 0:
		break

#カードの表示
#print card[0].strip("--")

#データベースへ接続->データ抽出
#英語版で探したい場合は日本語版をコメントアウト(#)
c = place+"/0x1339-20160207-nopics/cards.cdb"#日本語版
c = place + "cards.cdb"#英語版

cdb_place = place+"/expansions/live/"
cdb = [c,place+"/expansions/cards-tf.cdb"]+[cdb_place+base for base in os.listdir(cdb_place) if ".cdb" in base]

data = []
#通常のcdbで見つからなかった時はliveフォルダ内のcdbから検索
for base in cdb:
	if len(data) == 0:
		data,text = search_cdb(base,decide_card)
	else:
		break
		
#カード名と効果を表示
print "\nカード名:\n",text[0][0]
print "\nカード効果:\n",text[0][1]



#http://www3.atwiki.jp/ads-wiki/pages/30.html
