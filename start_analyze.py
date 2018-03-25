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
def analyze_cloud(keywords='all',pages=1,content='all'):
    result=v2ex_cloud_spider.get_words(keywords='all',pages=1)
    allwords=[]
    dic_words={}
    sort_words=[]
    if content=='all':
        for num in range(0,3):
            for word in result[num]:
                allwords.append(word)
        for word in allwords:
            if word in dic_words:
                dic_words[word]+=1
            else:
                dic_words[word]=1
        sort_words=[(dic_words[j],j) for j in dic_words]
        #sort_words.sort()
        #sort_words.reverse()
    return(sort_words)
            
        
        
    