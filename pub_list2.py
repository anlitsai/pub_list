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
#file_AA_idx='AA_idx.list'
file_AA_idx='AAA_idx.txt'
#file_AA='AA.list'
file_author='export-ads_A00.txt'
file_author='export-custom_author_all.txt'

file_affiliation='export-custom_aff_all.txt'

#file_all='export-custom_all_author_all_aff.txt'
file_all='export-custom_lFYTQu_tab.txt'
pd_all=pd.read_csv(file_all,sep='\t')




cmd_AA_idx="cat "+file_AA_idx
list_AA_idx=os.popen(cmd_AA_idx,"r").read().splitlines()

#sys.exit(0)

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

pd_AA=pd.read_csv(file_AA_idx,sep=' ',header=None)
idx_AA=pd_AA[1]

    
cmd_authors="cat "+file_author
list_authors=os.popen(cmd_authors,"r").read().splitlines()


#list_authors=[list_authors.replace('&','') for list_authors in list_authors]


for i in list_authors:
#    print(i)
    if "&" in i:
        i=i.replace('& ','')
#    print(i)
    #author_per_paper=[i.split(';',-1)][0]
    author_per_paper=[i.split('.,',-1)]
    print(author_per_paper)

#sys.exit(0)    

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
#    print(affiliation_per_paper)
#    jj=0
    list_author_per_paper=[]
    list_NCU_AA_per_paper=[]
    list_NCU_idx_per_paper=[]
    for j in affiliation_per_paper:
#        jj=jj+1
        if NCU_key in j:
            NCU_AA_in_paper=j.split("(",-1)[0][-3:]
            NCU_AA_in_paper=NCU_AA_in_paper.replace(" ","")
#            print(NCU_AA_in_paper)
            list_NCU_AA_per_paper.append(NCU_AA_in_paper)
#            NCU_idx=list_idx
            NCU_idx_in_paper=idx_AA[idx_AA==NCU_AA_in_paper].index[0]
#            print(NCU_idx_in_paper)
            list_NCU_idx_per_paper.append(NCU_idx_in_paper)            
#            print(list_NCU_idx_per_paper)




    list_author_per_paper=list_authors[idx_i].split('.,',-1)
#    list_author_per_paper.replace('&','')
    
    n_author_per_paper=len(list_author_per_paper)
    print("# of authors = ", n_author_per_paper)
    list_NCU_idx.append(list_NCU_idx_per_paper)

    author1=list_author_per_paper[0]    
    if n_author_per_paper==1:
#        print("1")
        author=str(author1)
        print(author)
    elif n_author_per_paper==2:
#        print("2")
        author2=list_author_per_paper[1]
        author=str(author1)+" and"+str(author2)
        print(author)
    elif n_author_per_paper==3:
#        print("3")
        author2=list_author_per_paper[1]
        author3=list_author_per_paper[2]
        author=str(author1)+","+str(author2)+", and"+str(author3)
        print(author)
    else:
#        print(">3")
        author_NCU=""
        author2=list_author_per_paper[1]
        author3=list_author_per_paper[2]
        idx_k=-1
        
        for k in list_NCU_idx_per_paper[:-1]:
            if k>2:
                idx_k=idx_k+1
                n_NCU_idx_per_paper=len(list_NCU_idx_per_paper)
#                author_k=list_author_per_paper[k]
#                n_NCU_idx_per_paper=len(list_NCU_idx_per_paper)
#                author_NCU=author_NCU+str(author_k)+', '
                author_k1=list_author_per_paper[k]
            
                if n_NCU_idx_per_paper==0:
                    author_NCU=""
                elif n_NCU_idx_per_paper==1:
                    author_NCU=str(author_k1)
                else:
                    author_k2=list_author_per_paper[k]
                    author_NCU=author_NCU+str(author_k2)+".,"
                author4=author_NCU+" and"+str(list_author_per_paper[-1])
#        author4=str(author_NCU)
        author=str(author1)+","+str(author2)+".,"+str(author3)+"., et al. (including"+str(author4)+" from NCU)"
        print(author)
        
print("")
