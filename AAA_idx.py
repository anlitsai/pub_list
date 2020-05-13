#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 00:43:08 2020

@author: altsai
"""

import string
import os
import sys


a2z=string.ascii_uppercase



file_AAA='AAA_idx.txt'
if os.path.exists(file_AAA):
    os.remove(file_AAA)    
    
with open(file_AAA,'w') as f_AAA:

    idx_ij=-1
    for i in a2z:
        for j in a2z:
            idx_ij=idx_ij+1
            AA=i+j
            print(idx_ij,AA)
            f_AAA.write(str(idx_ij)+" "+str(AA)+"\n")
    for i in a2z:
        for j in a2z:
            for k in a2z:
                idx_ij=idx_ij+1
                AA=i+j+k                                          
                print(idx_ij,AA)
                f_AAA.write(str(idx_ij)+" "+str(AA)+"\n")
        