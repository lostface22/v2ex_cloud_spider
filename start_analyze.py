# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 11:51:43 2018

@author: v-beshi
"""

import v2ex_cloud_spider
from matplotlib import pyplot as plt
ali=['阿里云','阿里','Aliyun','aliyun']
qcloud=['腾讯云','腾讯','qcloud','Qcloud']
azure=['azure','AZURE','Azure','微软云','微软']
jd=['京东云','京东']
huawei=['华为云','华为']
oversea=['出海','海外','国际版','国际','国外']
fakewords=['\n','，','的',' ','。','\r','@','/','*','\r\n','到','不','了','是','在','我','\xa0','-','、','有','和','也','你',':','就','都','.','？','：']
def analyze_cloud(keywords='all',pages=1,content='all'):
    result=v2ex_cloud_spider.get_words(keywords,pages)
    allwords=[]
    dic_words={}
    sort_words=[]
    if content=='all':
        for num in range(0,3):
            for word in result[num]:
                if word not in fakewords:
                    allwords.append(word)
        for word in allwords:
            if word in dic_words:
                dic_words[word]+=1
            else:
                dic_words[word]=1
        sort_words=[(dic_words[j],j) for j in dic_words]
        sort_words.sort()
        sort_words.reverse()
        sen=result[3]+result[4]+result[5]
    plt.hist(sen)
    return(sort_words)      
    