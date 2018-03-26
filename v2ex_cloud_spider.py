# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 21:35:55 2018

@author: v-beshi
"""

import requests
from bs4 import BeautifulSoup as bs
import re
from snownlp import SnowNLP
import jieba
import time
import random
jieba.add_word('微软云')
jieba.add_word('阿里云')
jieba.add_word('腾讯云')
jieba.add_word('华为云')
jieba.add_word('京东云')
jieba.add_word('美团云')
jieba.add_word('出海')
#jieba中添加专有词汇

def get_all_links(pages):
    links=[]
    user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers={'User-Agent':user_agent}
    for i in range(1,pages+1):
        url='https://www.v2ex.com/go/cloud?p={pages}'.format(pages=i)
        page=requests.get(url,headers=headers)
        opt_page=bs(page.text)
        posts=opt_page.find_all('span',class_='item_title')
        for j in posts:
            link=j.find('a').attrs['href']
            links.append(link)
    return links
#获取v2ex cloud channel的所有链接

def get_words(keywords='all',pages=1):
    user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers={'User-Agent':user_agent}
    links=get_all_links(pages)
    post_words=[]
    post_sen=[]
    header_words=[]
    header_sen=[]
    reply_words=[]
    reply_sen=[]
    for i in links:
        url='https://www.v2ex.com{link}'.format(link=i)
        tiezi=requests.get(url,headers=headers)
        opt_tiezi=bs(tiezi.text)
        if keywords=='all':
		#如果没有选择关键词
            try:         
                post=opt_tiezi.find('div',class_='markdown_body').get_text()
                pw=jieba.lcut(post)
                s1=SnowNLP(post)
                post_sens=s1.sentiments
                post_sen.append(post_sens)
                for post_word in pw:
                    post_words.append(post_word)
            except:
               continue
			#主题内容抓取
            try:
                header=opt_tiezi.find('div',class_='header').find('h1').get_text()
                hw=jieba.lcut(header)
                s2=SnowNLP(header)
                header_sens=s2.sentiments
                header_sen.append(header_sens)
                for header_word in hw:
                    header_words.append(post_word)
            except:
                continue
			#标题内容抓取
            try:
                replys=opt_tiezi.find_all('div',class_='reply_content')
                for reply in replys:
                    try:
                        reply=reply.get_text()
                        s3=SnowNLP(reply)
                        reply_sens=s3.sentiments
                        reply_sen.append(reply_sens)
                        rw=jieba.lcut(reply)
                        for reply_word in rw:
                            reply_words.append(reply_word)
                    except:
                        continue
            except:
                continue
			#回复内容抓取
			
        else:
		#如果选择了关键词
            try:
                post=opt_tiezi.find('div',class_='markdown_body').get_text()
                pw=jieba.lcut(post)
                a=0
                for keyword in keywords:
                    if keyword in pw:
                        a=1
                if a==1:
                    for post_word in pw:
                        post_words.append(post_word)
                    s1=SnowNLP(post)
                    post_sens=s1.sentiments
                    post_sen.append(post_sens)
            except:
                continue
            
            try:
                header=opt_tiezi.find('div',class_='header').find('h1').get_text()
                hw=jieba.lcut(header)
                b=0
                for keyword in keywords:
                    if keyword in hw:
                        b=1
                if b==1:              
                    for header_word in hw:
                        header_words.append(post_word)    
                    s2=SnowNLP(header)
                    header_sens=s2.sentiments
                    header_sen.append(header_sens)
            except:
                continue
            
            try:
                replys=opt_tiezi.find_all('div',class_='reply_content')
                c=0
                for reply in replys:
                    try:
                        reply=reply.get_text()
                        rw=jieba.lcut(reply)
                        for keyword in keywords:
                            if keyword in hw:
                                c=1
                        if c==1:
                            for reply_word in rw:
                                reply_words.append(reply_word)  
                                s3=SnowNLP(reply)
                                reply_sens=s3.sentiments
                                reply_sen.append(reply_sens) 
                    except:
                        continue
            except:
                continue
        time.sleep(random.random()*2)
		#停止时间不确定，以免被反爬虫软件探测
    return(post_words,header_words,reply_words,post_sen,header_sen,reply_sen)