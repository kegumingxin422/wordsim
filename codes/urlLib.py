# -*- coding: utf-8 -*-
import urllib.request
from lxml import etree
import sys,re
from bs4 import BeautifulSoup
import pdb
import time
import string
def google_return_count(querystr):
	url ='https://www.google.com.hk/search?hl=en&q=%s'%querystr
	request =urllib.request.Request(url)
	user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0'
	print(user_agent)
	request.add_header('User-agent', user_agent)
	response =urllib.request.urlopen(request)
	html =response.read().decode("utf-8")
	soup = BeautifulSoup(html,"lxml")
	print (soup.title)
	newstext=soup.find(id="resultStats").encode("utf-8")
	print(newstext)
	temp = str(newstext).split(" ")[2].split(",")
	newstr=""
	i=0
	for i in range(len(temp)):
		newstr += temp[i]
	return str(newstr)

def main():
	inFile = open("C:\\Users\\Aaron_Huang\\Desktop\\combined.csv","r")
	outFile = open("E:\\Homework1\\afterCompute\\googleSimilarity.csv","w")
	line = inFile.readline()
	i = 0
	while line:
		i += 1
		line = line.strip()
		list = line.split(',')
		P = int(google_return_count(list[0])
		print(P)
		Q = int(google_return_count(list[1])
		PandQ = int(google_return_count(list[0]+"%20"+list[1]))
		if PandQ <= 5:
			score = 0
		else:
			score = float(PandQ/(P+Q-PandQ))
		print(score)
		outFile.write(list[0]+","+list[1]+","+str(score)+"\n")
		line = inFile.readline()


if __name__ == '__main__':
		start = time.clock()
		main()
		end = time.clock()
		print ("process: %f s" % (end - start))