# -*- coding: utf-8 -*-

import random

def gacha():
	temp = random.randrange(1,1000)
	if temp <= 30: return "SSRare"
	elif temp <= 130: return "SRare"
	else: return "Rare"

def gachaone():
	ssr = 0
	sr = 0
	r = 0
	if gacha() == "SSRare" : ssr = ssr + 1
	elif gacha() == "SRare" : sr = sr + 1
	else : r = r + 1

	return resultprint(ssr,sr,r)

def gachaten():
	ssr = 0
	sr = 0
	r = 0
	for i in range(0,9):
		if gacha() == "SSRare" : ssr = ssr + 1
		elif gacha() == "SRare" : sr = sr + 1
		else : r = r + 1

	if gacha() == "SSRare" : ssr = ssr + 1
	else : sr = sr + 1
	
	return resultprint(ssr,sr,r)

def resultprint(ssr, sr, r):
	return "Gacha Result \nSSR : "+str(ssr)+"\n"+"SR : "+str(sr)+"\n"+"R : "+str(r)