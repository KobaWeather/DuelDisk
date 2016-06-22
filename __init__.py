#!/usr/bin/env python
#! -*- coding:utf-8 -*-

from PIL import Image
import sqlite3 as sq
import os

#resize用
SIZE = 56
#切抜範囲の設定(112x112)
box = (29,55,141,167)
# 画像フォルダの指定
#local_placeはYgoproが置かれているディレクトリを指定
local_place = "/Volumes/NO NAME/"
place = local_place+"Ygopro/"

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