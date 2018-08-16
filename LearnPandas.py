#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import re
data1 = [1, 2, 3, 4]
arr1 = np.array(data1)
print data1
print arr1
arry2 = np.zeros([10, 10])
print arry2.reshape([20, 5]).shape
stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
# 平时成绩占40% 期末成绩占60%, 计算结果
#
q = np.array([[0.4], [0.6]])
result = np.dot(stus_score, q)
print("最终结果为:")
print(result)

str1 = '(1, 0.123) (2, 0.345)'

print re.findall(r'[(](.*?)[)]', str1)


str2 = "ant[1][2]=14.23"
str3 = re.split('\]|\[|\(|\)|=', str2)
str3 = [item for item in filter(lambda x:x != '', str3)]
print str2
print str3
str4 = re.findall(r'\d+\.?\d*', str2)
print "str4:"
k = float(str4[2]) + 1
print k

strs = '1(2(3(4(5(67)6)7)8)9)0'
reg1 = re.compile('([()])∗') #一对括号
reg2 = re.compile('([()]|\([()]∗)*\)') #两对括号
reg3 = re.compile('([()]|\([()]∗|([()]|\([()]∗)*\))*\)') #三层




