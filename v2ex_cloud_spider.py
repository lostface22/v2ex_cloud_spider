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

def get_words(pages=1):
    user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers={'User-Agent':user_agent}
    links=get_all_links(pages)
    post_words=[]
    header_words=[]
    reply_words=[]
    for i in links:
        url='https://www.v2ex.com{link}'.format(link=i)
        tiezi=requests.get(url,headers=headers)
        opt_tiezi=bs(tiezi.text)
        try:           
            post=opt_tiezi.find('div',class_='markdown_body').get_text()
            pw=jieba.lcut(post)
            for post_word in pw:
                post_words.append(post_word)                
        except:
            continue
        try:
            header=opt_tiezi.find('div',class_='header').find('h1').get_text()
            hw=jieba.lcut(header)
            for header_word in hw:
                header_words.append(post_word) 
        except:
            continue
        replys=opt_tiezi.find_all('div',class_='reply_content')
        for reply in replys:
            reply=reply.get_text()
            rw=jieba.lcut(reply)
            for reply_word in rw:
                reply_words.append(reply_word)
        time.sleep(random.random())
    return(post_words,header_words,reply_words)