# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 11:38:31 2018

@author: TOSHIBA
"""

from collections import Counter
import numpy
from nltk.tokenize import word_tokenize
file=open("F:\data_set.txt","r+")
#print (file.readlines())
lst=[]
for i in file:
    print(i)
    lst.append(i)
print(lst)
#print(word_tokenize(lst))
a='\n'.join(lst)
print (a)

split_it=a.split()
Counter=Counter(split_it)
most_occur=Counter.most_common()
math_array=numpy.array(most_occur)

print(math_array)