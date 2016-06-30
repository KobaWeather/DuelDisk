#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import urllib2
import lxml.html as hx
import sys
import time
import os
from tqdm import tqdm

root = "https://ocg.xpg.jp/deck/"
url = root + "deck.fcgi?Flt=2&Sort=1&p="+sys.argv[-1]

deckNo = [i.attrib["href"] for i in hx.fromstring(urllib2.urlopen(url).read()).xpath("//a") if "deck.fcgi?ListNo=" in i.attrib["href"]]

for No in tqdm(deckNo):
	url = root + No + "&Text=5"
	data = hx.fromstring(urllib2.urlopen(url).read()).xpath("//pre")[0].text_content().split("\n")[:-1]
	filename = No.strip("deck.fcgi?ListNo=")+".ydk"
	if filename not in os.listdir("./deck"):
		f = open("./deck/"+filename,"w")
		for i in data:
			f.write(i+"\n")
		f.close()
	time.sleep(5)
