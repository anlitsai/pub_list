#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 20:16:12 2020

@author: altsai
"""
import os
import sys
import shutil
import re
import numpy as np
import pandas as pd
file_AA_idx='AA_idx.list'
file_AA='AA.list'
file_author='export-ads_A00.txt'
file_affiliation='export-custom_aff_all.txt'

cmd_AA_idx="cat "+file_AA_idx
list_AA_idx=os.popen(cmd_AA_idx,"r").read().splitlines()

list_idx=[]
list_AA=[]
for i in list_AA_idx:
    #print(i)
    AA_idx=[i.split(' ',-1)][0]
#    print(AA_idx)
    AA=AA_idx[0]
#    print(AA)
    idx=AA_idx[1]
#    print(AA,idx)   
    list_AA.append(AA)
    list_idx.append(idx)
    
#print(list_AA)
#print(list_idx)

pd_AA=pd.read_csv(file_AA,sep=' ',header=None)
idx_AA=pd_AA[0]

    
cmd_authors="cat "+file_author
list_authors=os.popen(cmd_authors,"r").read().splitlines()

for i in list_authors:
    #print(i)
    author_per_paper=[i.split(';',-1)][0]
    print(author_per_paper)
    
cmd_affiliation="cat "+file_affiliation
list_affiliation_per_paper=os.popen(cmd_affiliation,"r").read().splitlines()

list_NCU_AA=[]
list_NCU_idx=[]

NCU_key="Institute of Astronomy, National Central University"
idx_i=-1
for i in list_affiliation_per_paper:
    #print(i)
    idx_i=idx_i+1
    affiliation_per_paper=[i.split(");",-1)][0]
    print(affiliation_per_paper)
#    jj=0
    list_author_per_paper=[]
    list_NCU_AA_per_paper=[]
    list_NCU_idx_per_paper=[]
    for j in affiliation_per_paper:
#        jj=jj+1
        if NCU_key in j:
            NCU_AA_in_paper=j.split("(",-1)[0][-2:]
#            print(NCU_AA_in_paper)
            list_NCU_AA_per_paper.append(NCU_AA_in_paper)
#            NCU_idx=list_idx
            NCU_idx_in_paper=idx_AA[idx_AA==NCU_AA_in_paper].index[0]
#            print(NCU_idx_in_paper)
            list_NCU_idx_per_paper.append(NCU_idx_in_paper)            
#            print(list_NCU_idx_per_paper)
    list_NCU_idx.append(list_NCU_idx_per_paper)
#    n_NCU_idx_per_paper=len(list_NCU_idx_per_paper)
    list_author_per_paper=list_authors[idx_i].split(';',-1)
    n_author_per_paper=len(list_author_per_paper)
    if n_author_per_paper==1:
        print("1")
        author=list_author_per_paper[0]
        print(author)
    elif n_author_per_paper==2:
        print("2")
        author=list_author_per_paper[0:2]
        print(author)
    elif n_author_per_paper==3:
        print("3")
        author=list_author_per_paper[0:3]
        print(author)
    elif n_author_per_paper>3:
        print("4")
        author3=list_author_per_paper[0:3]
#        author4=" including "
#        author=string(author3)+string(author4)
#        print(author)
        


#    for k in list_NCU_idx_per_paper:
        
#        if k=1:
#            author=list_authors[idx_i][0]
#        elif k=2
#        if k>3:
#            author3=list_authors[idx_i].split(';',-1)[0:4]
##            print(author3)
#            author4="et al. (including )"
##            print(author4)
#            author=author3+author4
#            print(author)
#        elif k<=3:
#            print("including")

print(list_NCU_idx)

    