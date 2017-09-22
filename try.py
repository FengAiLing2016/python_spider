#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/18 9:27
# @Author  : Feng_xia
# @File    :
import requests
from bs4 import BeautifulSoup
import re
# 登录
session = requests.Session()
# pattern = re.compile(r'\<td\s.*\"\>(.+?)\<\/td\>') #正则表达式
pattern = re.compile(r'\>(.+?)\<')
t_line=[]
p_line=[]
params={'hyuser':'48','hypass':'2687268','x':'48','y':'9'}
r=session.post("http://218.14.255.205:82/cklogin.aspx",data=params)
print("cookie us set to:")
print(r.cookies.get_dict())
print("^^^^^^^^")
print("Going to profile page")
r=session.get("http://218.14.255.205:82/jsp.aspx")
bsObj = BeautifulSoup(r.content)
namelist = bsObj.find_all("tr",{"class":{"bg2","bg1"}})
for name in namelist:
    for t in name:
        t=pattern.findall(str(t))
        t_line.append(','.join(t))
    p_line.append(t_line)
    t_line = []
print(p_line)