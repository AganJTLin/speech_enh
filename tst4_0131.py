# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 18:32:19 2021

@author: paul8
"""


str1 = 'hello python'
str2 = str1
# str2[0] = 'y'
# a = a + b could be written as a += b

str2 += ' journey'

print(str2 is str1)
print(str1)

result = str2.split(' ')
print(result)
 
result_back = '***'.join(result)
print(result_back)