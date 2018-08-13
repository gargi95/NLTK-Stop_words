# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 20:01:16 2018

@author: TOSHIBA
"""

from nltk.stem import PorterStemmer
stemmer= PorterStemmer()
print("Stem %s: %s" % ("studying", stemmer.stem("fishes")))
# This is a very simple program using NLTK demonstarting the process of stemming (used in the initial phase of NLP).
#The algorithm used is Porter Stemmer - It gives the root form of the word
# This algorithm maps the longest suffix. Following suffixes are replaces by:
#1. sses -> ss
#2. ies -> i
#3. ss ->ss
#4. s -> Null(fi symbol in mathematics)
# this algorithm fails and not always give the correct root word for example for ponies it gves poni which is incorrect word"
