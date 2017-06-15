#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Workspace/Python/validateEmail.py
#
# Vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
# Python source code - replace this with a description
# of the code and write the code below this text
#

import re # 引用正则表达式模块


def validateEmail(email):
    if len(email) > 7:
        if re.match(r"^.+\@(\[?)[a-zA-Z0-9\-\.]+\.([a-zA-Z]{2,3}|[0-9]{1,3})(\]?)$", email) != None:
            return 1
    return 0


# Test
list = ["abc@163.com", "abc123@example.com", "123dfg.swe@.24.com",
        "afdj21u342=-1i", "jdlajp12231jo.io.-dso", "lllisj@gmail.com",
        "ade12-12sa@mom"]
for e in list:
    val = validateEmail(i)
    print(val,"  ",i)




"""
元字符:
 ^      匹配字符串的开始
 $      匹配字符串的结束
 .      匹配换行符以外的任意字符
 +      重复一次或更多
 \@     @
 ?      重复0次或1次
 []     匹配[]里的字符
 {n}    重复n次
 {n,}   重复n次或更多
 {n,m}  重复n到m次
"""
