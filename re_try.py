#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/22 16:29
# @Author  : Feng_xia
# @File    : re_try

import re
t= '<td align="center">1*24</td>'
# pattern = re.compile(r'\<td\s.*\"\>(.+?)\<\/td\>')
pattern = re.compile(r'\>(.+?)\<')
match = pattern.findall(t)
print(match)