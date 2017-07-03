#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
from urllib import request

baseurl = "http://daily.python_days.com/"
f = request.urlopen(baseurl)
firstline = f.read().decode('utf-8')


pattern = re.compile(r"""<a href="/story/(.*?)" class=".*?">""", re.S)
theseurls = re.findall(pattern, firstline)
#print(theseurls)
def writewenjian(words):
    wenjian = open('C:/Users/joeya/Desktop/b.txt','a',encoding='utf-8')
    wenjian.write(words + '\n')

def openurl(url):
    url = "http://daily.python_days.com/story/" + str(url)
    f = request.urlopen(url)
    f2 = f.read().decode('utf-8')
    pattern = re.compile(r"""<title>(.*?)</title>.*<span class="author">(.*?)</span>.*?<div class="content">(.*?)</div>""",re.S )
    
    f3 = re.findall(pattern, f2)
    #shuchu = ();
    for outwrite in f3:
        print('标题：')
        writewenjian('标题：')
        #shuchu = shuchu + (('标题：'))
        print(outwrite[0])
        writewenjian(outwrite[0])
        #shuchu = shuchu + outwrite[0]
        print('作者：')
        writewenjian('作者：')
        #shuchu = shuchu + (('作者：'))
        print(outwrite[1])
        writewenjian(outwrite[1])
        #shuchu = shuchu + outwrite[1]
        print('内容：')
        writewenjian('内容：')
        #shuchu = shuchu + (('内容：'))
        patternout = re.compile('<.*?>')
        outwrite3=outwrite[2]
        outwrite3 = re.sub(patternout,"", outwrite3)
        patternout2 = re.compile('&.*?;')
        outwrite3 = re.sub(patternout2,"", outwrite3)
        print(outwrite3)
        writewenjian(outwrite3)
        writewenjian('\n\n')
        #shuchu = shuchu + outwrite3
        #outwrite[2]=outwrite3
        #outwrite[2] = outwrite3;
        #outwrite3 = re.findall(pattern3,outwrite[2])
    #wenjian.write(str(outwrite3)); 
    #wenjian.close();
    #print(shuchu)    
        
        

def handurl(urls):
    a=1
    for oneurl in urls:
        print(a)
        cixu = '第  %d 篇'%(a)
        writewenjian(cixu)
        openurl(oneurl)
        a=a+1
        
theseurls = theseurls[1:5]
#wenjian = open('C:/Users/joeya/Desktop/b.txt','a');
handurl(theseurls)