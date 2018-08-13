# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 20:01:16 2018

@author: TOSHIBA
"""

from nltk.stem import PorterStemmer
stemmer= PorterStemmer()
print("Stem %s: %s" % ("studying", stemmer.stem("fishes")))