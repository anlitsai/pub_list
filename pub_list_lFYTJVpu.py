#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 20:16:12 2020

@author: altsai
"""
import os
import sys
import shutil
#import re
import subprocess
#import numpy as np
import pandas as pd
#file_AA_idx='AA_idx.list'
file_AA_idx='AAA_idx.txt'
#file_AA='AA.list'
file_author='export-ads_A00.txt'
file_author='export-custom_author_all.txt'

file_affiliation='export-custom_aff_all.txt'

#file_all='export-custom_all_author_all_aff.txt'
#file_all='export-custom_lFYTQu_tab.txt'

file_custom='export-custom_lYFTJVpu_pipe.txt'
file_all='export-custom_lYFTJVpu_pipe2.txt'

shutil.copyfile(file_custom, file_all)

subprocess.call(["sed -i -e 's/|257|/||257|/g' "+file_all], shell=True)
subprocess.call(["sed -i -e 's/(UPSay);/(UPSay) ;/g' "+file_all], shell=True)
subprocess.call(["sed -i -e 's/(CAASTRO);/(CAASTRO) ;/g' "+file_all], shell=True)
subprocess.call(["sed -i -e 's/#50/#50|/g' "+file_all], shell=True)
subprocess.call(["sed -i -e 's/#49/#49|/g' "+file_all], shell=True)
subprocess.call(["sed -i -e 's/|8|/||8|/g' "+file_all], shell=True)
subprocess.call(["sed -i -e 's/|EPSC2017-784|/||EPSC2017-784|/g' "+file_all], shell=True)
subprocess.call(["sed -i -e 's/|6054|/||6054|/g' "+file_all], shell=True)

#sys.exit(0)

#list_AA_idx=



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

    
#cmd_authors="cat "+file_author
#list_authors=os.popen(cmd_authors,"r").read().splitlines()


#list_authors=[list_authors.replace('&','') for list_authors in list_authors]



df_all=pd.read_csv(file_all,sep='|',header=None)
#print(df_all)
#sys.exit(0)

col=['author','year', 'affi','title','journal','volumn','page','url']
df_all.columns=col
#print(df_all)
n_paper=len(df_all)
#print(n_paper)


col_author=df_all['author']
#print(col_author)
col_year=df_all['year']
#print(col_year)
col_affi=df_all['affi']
#print(col_affi)

col_title=df_all['title']
#print(col_title)
col_journal=df_all['journal']
#print(col_journal)
col_volumn=df_all['volumn']

col_page=df_all['page']

col_url=df_all['url']
#print(col_url)

#sys.exit(0)  


col_author=col_author.str.replace('& ','')
#print(col_author[0])

#df_all['author_number']=[len(i) for i in col_author]


#print(col_author_number)
#sys.exit(0)  


#list_affiliation_in_paper=[]

list_affi_AA=[]
list_affi_name=[]
list_affi_number=[]
list_author_number=[]

for i in range(n_paper):
    print('#',i,'paper')
    author_in1paper=col_author[i]
    affi_in1paper=col_affi[i]
    
#    list_author_in1paper=[author_in1paper.split('.,',-1)][0]
    list_affi_in1paper=[affi_in1paper.split(');',-1)][0]
    print(list_affi_in1paper)
    list_affi_AA_in1paper=[]
    list_affi_name_in1paper=[]

    for j in list_affi_in1paper:
        affi_AA_name=j.split('(',2)
        print(affi_AA_name)
        affi_AA=affi_AA_name[0]
        affi_AA=affi_AA.replace(" ","")
        list_affi_AA_in1paper.append(affi_AA)
        affi_name=affi_AA_name[1]
        list_affi_name_in1paper.append(affi_name)
        
    n_affi_in1paper=len(list_affi_in1paper)
    
#    print(len(list_affi_in1paper),len(list_affi_AA_in_paper),len(list_affi_name_in_paper))

    list_affi_AA.append(list_affi_AA_in1paper)
    list_affi_name.append(list_affi_name_in1paper)
    list_affi_number.append(n_affi_in1paper)


#print(list_affi_AA)
#print(len(list_affi_AA))

#print(list_affi_name)
#print(len(list_affi_name))

#print(list_affi_number)
#print(len(list_affi_number))

#sys.exit(0)  

df_all['affi_AA']=list_affi_AA
df_all['affi_name']=list_affi_name
df_all['affi_number']=list_affi_number
col_affi_AA=df_all['affi_AA']
col_affi_name=df_all['affi_name']
col_affi_number=df_all['affi_number']
#col_author_number=df_all['author_number']


#sys.exit(0)  

#list_affiliation_in_paper

#sys.exit(0)  
#cmd_affiliation="cat "+file_affiliation
#list_affiliation_in_paper=os.popen(cmd_affiliation,"r").read().splitlines()

list_NCU_AA=[]
list_NCU_idx=[]
#list_NCU_author=[]
#list_NCU_author_number=[]

df_all['author_number']=""
df_all['NCU_author']=""
df_all['NCU_author_idx']=""
df_all['NCU_author_number']=""

df_all['NCU_author3']=""
df_all['NCU_author3_idx']=""
df_all['NCU_author3_number']=""

df_all['NCU_author4']=""
df_all['NCU_author4_idx']=""
df_all['NCU_author4_number']=""

df_all['NCU_AA']=""



NCU_key="Institute of Astronomy, National Central University"
idx_i=-1

#sys.exit(0)

for i in range(n_paper):
    print('#',i,'paper')
    list_affi_name_in1paper=col_affi_name[i]
    list_author_in1paper=col_author[i].split('., ',-1)
    n_author_in1paper=len(list_author_in1paper)
    df_all['author_number'][i]=n_author_in1paper
    print("# of authors = ", n_author_in1paper)
    
    list_NCU_author_idx_in1paper=[]
    list_NCU_author_in1paper=[]
    list_NCU_author4_idx_in1paper=[]
    list_NCU_author4_in1paper=[]
    list_NCU_author3_idx_in1paper=[]
    list_NCU_author3_in1paper=[]    
    list_NCU_AA_in1paper=[]

    idx_j=-1
    for j in list_affi_name_in1paper:
        idx_j=idx_j+1
        
        if NCU_key in j:
            NCU_idx=idx_j
            list_NCU_author_idx_in1paper.append(NCU_idx)
            list_NCU_AA_in1paper.append(col_affi_AA[i][NCU_idx])
#            print("=== found NCU ===")
#            print(NCU_idx,j)
            if NCU_idx<3:
                list_NCU_author3_idx_in1paper.append(NCU_idx)
                list_NCU_author3_in1paper.append(list_author_in1paper[NCU_idx])
            else:
                list_NCU_author4_idx_in1paper.append(NCU_idx)
                list_NCU_author4_in1paper.append(list_author_in1paper[NCU_idx])
            
                
#    print(list_NCU_author_idx_in1paper)
    df_all['NCU_author_idx'][i]=list_NCU_author_idx_in1paper
    for k in list_NCU_author_idx_in1paper:
        list_NCU_author_in1paper.append(list_author_in1paper)
#    print(list_NCU_author_in1paper)
    df_all['NCU_author'][i]=list_NCU_author_in1paper
    n_NCU_author_in1paper=len(list_NCU_author_in1paper)
    df_all['NCU_author_number'][i]=n_NCU_author_in1paper
#    print("found",n_NCU_author_in1paper,"NCU")
    df_all['NCU_author3'][i]=list_NCU_author3_in1paper
    df_all['NCU_author3_idx'][i]=list_NCU_author3_idx_in1paper
    n_NCU_author3_in1paper=len(list_NCU_author3_in1paper)
    df_all['NCU_author3_number'][i]=n_NCU_author3_in1paper

    df_all['NCU_author4'][i]=list_NCU_author4_in1paper
    df_all['NCU_author4_idx'][i]=list_NCU_author4_idx_in1paper
    n_NCU_author4_in1paper=len(list_NCU_author4_in1paper)
    df_all['NCU_author4_number'][i]=n_NCU_author4_in1paper
    df_all['NCU_AA'][i]=list_NCU_AA_in1paper

col_author_number=df_all['author_number']
col_NCU_author=df_all['NCU_author']
col_NCU_author_idx=df_all['NCU_author_idx']
col_NCU_author_number=df_all['NCU_author_number']

col_NCU_author3=df_all['NCU_author3']
col_NCU_author3_idx=df_all['NCU_author3_idx']
col_NCU_author3_number=df_all['NCU_author3_number']

col_NCU_author4=df_all['NCU_author4']
col_NCU_author4_idx=df_all['NCU_author4_idx']
col_NCU_author4_number=df_all['NCU_author4_number']

col_NCU_AA=df_all['NCU_AA']

#sys.exit(0)

file_pub='pub_list_NCU.txt'

if os.path.exists(file_pub):
    os.remove(file_pub)
       
f_pub=open(file_pub,'w')

for i in range(n_paper):
    print('#',i,'paper')
    paper_url=col_url[i]
    list_author_in1paper=col_author[i][:-1].split('., ',-1)
    n_author_in1paper=col_author_number[i]
    paper_title=col_title[i]
    print(paper_title)
    paper_journal=col_journal[i]
    print(paper_journal)

    paper_volumn=col_volumn[i]
    print('volumn',paper_volumn)
    paper_page=col_page[i]
    print('page',paper_page)
    
    paper_affi_AA=col_affi_AA[i]
    print(paper_affi_AA)
    paper_NCU_AA=col_NCU_AA[i]
    print(paper_NCU_AA)
    paper_year=col_year[i]
    print(paper_year)


    author1=list_author_in1paper[0]
    if "AA" in paper_NCU_AA:
        author1='{'+author1+'.}'
        print("AA")
    else:
        author1=author1+'.'
     
 
    if n_author_in1paper==1:
#        print("1")
        author=author1
        print(paper_affi_AA)
        print(author1)
        print(author)
        print(paper_url+"\n")
    elif n_author_in1paper==2:
#        print("2")
        author2=list_author_in1paper[1]
        if "AB" in paper_NCU_AA:
            author2='{'+author2+'.}'
            print("AB")
        else:
            author2=author2+'.'
        author=author1+" and "+author2
        print(paper_affi_AA)
        print(author1,author2)
        print(author)
        print(paper_url+"\n")
    elif n_author_in1paper==3:
#        print("3")        
        author2=list_author_in1paper[1]
        if "AB" in paper_NCU_AA:
            author2='{'+author2+'.}'
            print("AB")
        else:
            author2=author2+'.'
        author3=list_author_in1paper[2]
        if "AC" in paper_NCU_AA:
            author3='{'+author3+'.}'                
            print("AC")
        else:
            author3=author3+'.'
        author=author1+", "+author2+", and "+author3
        print(paper_affi_AA)
        print(author1,author2,author3)
        print(author)
        print(paper_url+"\n")
    else:
#        print(">3")
#        author_NCU=""
        author1=list_author_in1paper[0]
        if "AA" in paper_NCU_AA:
            author1='{'+author1+'.}'
            print("AA")
        else:
            author1=author1+'.'
        author2=list_author_in1paper[1]
        if "AB" in paper_NCU_AA:
            author2='{'+author2+'.}'
            print("AB")
        else:
            author2=author2+'.'
        author3=list_author_in1paper[2]
        if "AC" in paper_NCU_AA:
            author3='{'+author3+'.}'                
            print("AC")
        else:
            author3=author3+'.'
        author123=author1+", "+author2+", "+author3
        
        # NCU author after the 3rd authorship
#        author_NCU=""
#        print(list_NCU_author_idx_in1paper)
        
#        idx_k=-1
        #list_more_NCU_author=[]
        author_kk=""
        if col_NCU_author4_number[i]==0:
#            author=str(author1)+", "+str(author2)+", "+str(author3)+", and et al."
            author=author123+", et al."
            print(author)
            print(paper_url+"\n")

        elif col_NCU_author4_number[i]==1:
            author_k1=col_NCU_author4[i][0]
            author4=str(author_k1)
#            author=str(author1)+", "+str(author2)+", "+str(author3)+", and et al. (including "+str(author4)+" from NCU)"
            author=author123+", et al. (including "+str(author4)+" from NCU)"
#            author=author.replace('.. from','. from')            
            print(author)            
            print(paper_url+"\n")

        else:
            author_k1=col_NCU_author4[i][0]
            for k in col_NCU_author4_idx[i][1:]:                
                author_k2=col_author[i].split(", ",-1)[k]
                author_kk=author_kk+", "+author_k2            
            author4=str(author_k1)+str(author_kk)
#            author=str(author1)+", "+str(author2)+", "+str(author3)+", and et al. (including "+str(author4)+" from NCU)"
            author=author123+", et al. (including "+str(author4)+" from NCU)"            
            print(author)
            print(paper_url+"\n")

#    author=author.replace("(including NESS Collaboration. from NCU)","")
    paper_journal=paper_journal.replace("&amp;","&")
    paper_journal=paper_journal.replace('Online at <A href="http://coolstars20.cfa.harvard.edu/">http://coolstars20.cfa.harvard.edu/</A>, cs20, id.8','')    
    paper_title=paper_title.replace("<SUB>","")
    paper_title=paper_title.replace("</SUB>","")
    pub_info=str(i)+'\n'+author+'\n'+str(paper_year)+'\n'+paper_title+'\n'+paper_journal+'\n'+paper_url+'\n\n'
    f_pub.write(pub_info)

f_pub.close()