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

file_custom_IANCU='export-custom_lYFTJVpu_pipe.txt'
#file_custom2='export-custom_lYFTJVpu_pipe_AA.txt'
file_custom_Ip='export-custom_lYFTJVpu_pipe_Ip.txt'
file_custom_Ip='export-custom_lYFTJVpu_pipe_Ip.txt'
file_custom_NCUIA='export-custom_lYFTJVpu_pipe_NCUIA.txt'
file_custom_Institution='export-custom_lYFTJVpu_pipe_Institution.txt'
file_custom_Graduate='export-custom_lYFTJVpu_pipe_Graduate.txt'
file_custom_Chen='export-custom_lYFTJVpu_pipe_Chen2.txt'
file_custom_Zhonda='export-custom_lYFTJVpu_pipe_Zhongda2.txt'
file_custom_Multidisciplinary='export-custom_lYFTJVpu_pipe_Multidisciplinary2.txt'
file_custom_CentaurusA='export-custom_lYFTJVpu_pipe_CentaurusA2.txt'
file_custom_SpaceScience='export-custom_lYFTJVpu_pipe_SpaceScience2.txt'
file_custom_Ko='export-custom_lYFTJVpu_pipe_Ko2.txt'
file_custom_KoDOI='export-custom_lYFTJVpu_pipe_Ko_DOI2.txt'
file_custom_ZYLin_No300='export-custom_lYFTJVpu_pipe_ZYLin_No3002.txt'
file_custom_ZYLin_other='export-custom_lYFTJVpu_pipe_ZYLin_other2.txt'
file_custom_Ip_other='export-custom_lYFTJVpu_pipe_Ip_other2.txt'
file_custom_Yuji='export-custom_lYFTJVpu_pipe_Yuji.txt'

file_combine='export-custom_combine.txt'
file_sorted='export-custom_sorted.txt'

shutil.copyfile(file_custom_IANCU, file_combine)

subprocess.call(["cat "+file_custom_Ip+">> "+file_combine],shell=True)
subprocess.call(["cat "+file_custom_NCUIA+">> "+file_combine],shell=True)
subprocess.call(["cat "+file_custom_Institution+">> "+file_combine],shell=True)
subprocess.call(["cat "+file_custom_Graduate+">> "+file_combine],shell=True)
subprocess.call(["cat "+file_custom_Chen+">> "+file_combine],shell=True)
subprocess.call(["cat "+file_custom_Zhonda+">> "+file_combine],shell=True)
subprocess.call(["cat "+file_custom_Multidisciplinary+">> "+file_combine],shell=True)
subprocess.call(["cat "+file_custom_CentaurusA+">> "+file_combine],shell=True)
subprocess.call(["cat "+file_custom_SpaceScience+">> "+file_combine],shell=True)
subprocess.call(["cat "+file_custom_Ko+">> "+file_combine],shell=True)
subprocess.call(["cat "+file_custom_KoDOI+">> "+file_combine],shell=True)
subprocess.call(["cat "+file_custom_ZYLin_No300+">> "+file_combine],shell=True)
subprocess.call(["cat "+file_custom_ZYLin_other+">> "+file_combine],shell=True)
subprocess.call(["cat "+file_custom_Ip_other+">> "+file_combine],shell=True)
subprocess.call(["cat "+file_custom_Yuji+">> "+file_combine],shell=True)

subprocess.call(["sed -i -e 's/|257|/||257|/g' "+file_combine], shell=True)
subprocess.call(["sed -i -e 's/UPSay);/UPSay) ;/g' "+file_combine], shell=True)
subprocess.call(["sed -i -e 's/Univ.);/Univ.) ;/g' "+file_combine], shell=True)
subprocess.call(["sed -i -e 's/CAASTRO);/CAASTRO) ;/g' "+file_combine], shell=True)
subprocess.call(["sed -i -e 's/#50/#50|/g' "+file_combine], shell=True)
subprocess.call(["sed -i -e 's/#49/#49|/g' "+file_combine], shell=True)
subprocess.call(["sed -i -e 's/|8|/||8|/g' "+file_combine], shell=True)
subprocess.call(["sed -i -e 's/|EPSC2017-784|/||EPSC2017-784|/g' "+file_combine], shell=True)
subprocess.call(["sed -i -e 's/|EPSC2017-174|/||EPSC2017-174|/g' "+file_combine], shell=True)
subprocess.call(["sed -i -e 's/|6054|/||6054|/g' "+file_combine], shell=True)
subprocess.call(["sed -i -e 's/|12374|/||12374|/g' "+file_combine], shell=True)
subprocess.call(["sed -i -e 's/gmail.com)/gmail.com) /g' "+file_combine], shell=True)
subprocess.call(["sed -i -e 's/|1872|/||1872|/g' "+file_combine], shell=True)

subprocess.call(["sort "+file_combine+"|uniq > "+file_sorted],shell=True)

#sys.exit(0)



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

pd_AA=pd.read_csv(file_AA_idx,sep=' ',header=None)
idx_AA=pd_AA[1]

    
#cmd_authors="cat "+file_author
#list_authors=os.popen(cmd_authors,"r").read().splitlines()


#list_authors=[list_authors.replace('&','') for list_authors in list_authors]



df_all=pd.read_csv(file_sorted,sep='|',header=None)
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
    print('#',str(i+1),'paper')
    author_in1paper=col_author[i]
    affi_in1paper=col_affi[i]
    
#    list_author_in1paper=[author_in1paper.split('.,',-1)][0]
    list_affi_in1paper=[affi_in1paper.split(');',-1)][0]
#    print(list_affi_in1paper)
    list_affi_AA_in1paper=[]
    list_affi_name_in1paper=[]

    for j in list_affi_in1paper:
        affi_AA_name=j.split('(',2)
#        print(affi_AA_name)
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



NCU_key1="of Astronomy, National Central University"
NCU_key2="Ip"
NCU_key3="National Central University, Graduate Institute of Astronomy, "
#'Institution of Astronomy, National Central University'
NCU_key=[NCU_key1, NCU_key2, NCU_key3]

idx_i=-1

#sys.exit(0)

for i in range(n_paper):
    print('#',i,'paper')
    list_affi_name_in1paper=col_affi_name[i]
    list_author_in1paper=col_author[i].split('., ',-1)
    n_author_in1paper=len(list_author_in1paper)
    df_all['author_number'][i]=n_author_in1paper
    print("# of authors = ", n_author_in1paper)
    df_all['author'][i]=list_author_in1paper


    
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
        
        for key in NCU_key:
            if key in j:
                NCU_idx=idx_j
                list_NCU_author_idx_in1paper.append(NCU_idx)
                list_NCU_AA_in1paper.append(col_affi_AA[i][NCU_idx])
#                print("=== found NCU ===")
#                print(NCU_idx,j)
                if NCU_idx<3:
                    list_NCU_author3_idx_in1paper.append(NCU_idx)
                    list_NCU_author3_in1paper.append(list_author_in1paper[NCU_idx])                
                else:
                    list_NCU_author4_idx_in1paper.append(NCU_idx)
                    list_NCU_author4_in1paper.append(list_author_in1paper[NCU_idx])
            
                
#    print(list_NCU_author_idx_in1paper)
    df_all['NCU_author_idx'][i]=list_NCU_author_idx_in1paper
    for k in list_NCU_author_idx_in1paper:
        list_NCU_author_in1paper.append(list_author_in1paper[NCU_idx])
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

#sys.exit(0)

df_all.drop_duplicates(subset=['title'],keep=False)
#sys.exit(0)

#col_author=df_all['author']
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

sep_author='; '

file_pub='pub_list_NCU.txt'

if os.path.exists(file_pub):
    os.remove(file_pub)
       
f_pub=open(file_pub,'w')


for i in range(n_paper):
    Nr_paper='# '+str(i)+' paper'
    print(Nr_paper)
#    f_pub.write(Nr_paper+'\n')
#    f_pub.write(str(n_paper)+'\n')
    paper_url=col_url[i]


    list_author_in1paper=col_author[i][:-1].split('., ',-1)
    n_author_in1paper=len(list_author_in1paper)
    n_author_in1paper=col_author_number[i]
    i_author=-1

#    for author_name in list_author_in1paper:
#        i_author=i_author+1
#        author_name=author_name+'.'
#        author_name=author_name.replace('..','.')
#        print(author_name)
#        list_author_in1paper[i_author]=author_name
    for i_author in range(n_author_in1paper):        
        author_name=list_author_in1paper[i_author]+'.'
        author_name=author_name.replace('..','.')
#        print(author_name)
        list_author_in1paper[i_author]=author_name
    print(list_author_in1paper)    


#    list_author3_in1paper=[]
#    list_author4_in1paper=[]
    for i_NCU_idx in col_NCU_author_idx[i]:
        list_author_in1paper[i_NCU_idx]='{'+list_author_in1paper[i_NCU_idx]+'}'
#        list_author3_in1paper[i_NCU_idx]='{'+list_author3_in1paper[i_NCU_idx]+'}'
#        list_author4_in1paper[i_NCU_idx]='{'+list_author4_in1paper[i_NCU_idx]+'}'
    print(list_author_in1paper)    
#    col_NCU_author[i]=list_author_in1paper


    paper_title=col_title[i]
    print(paper_title)
    paper_journal=col_journal[i]
#    print(paper_journal)
    paper_volumn=col_volumn[i]
    paper_page=col_page[i]
    print(paper_journal,',',paper_volumn, ',',paper_page)
    
    paper_affi_AA=col_affi_AA[i]
    print(paper_affi_AA)
    paper_NCU_AA=col_NCU_AA[i]
    print(paper_NCU_AA)
    paper_year=col_year[i]
    print(paper_year)


    

    author1=list_author_in1paper[0]
     
    if n_author_in1paper==1:
#        print("1")
        author=author1
        print(paper_url+"\n")
    elif n_author_in1paper==2:
#        print("2")
        author2=list_author_in1paper[1]
        author=author1+" and "+author2
        print(paper_affi_AA)
        print(author1,author2)
        print(author)
        print(paper_url+"\n")
    elif n_author_in1paper==3:
#        print("3")        
        author2=list_author_in1paper[1]
        author3=list_author_in1paper[2]
        author=author1+sep_author+author2+sep_author+"and "+author3
        print(paper_affi_AA)
        print(author1,author2,author3)
        print(author)
        print(paper_url+"\n")
    else:
#        print(">3")
#        author_NCU=""
        author1=list_author_in1paper[0]
        author2=list_author_in1paper[1]
        author3=list_author_in1paper[2]
        author123=author1+sep_author+author2+sep_author+author3
        
        # NCU author after the 3rd authorship
#        author_NCU=""
#        print(list_NCU_author_idx_in1paper)
        
#        idx_k=-1
        #list_more_NCU_author=[]
        author_kk=""
        if col_NCU_author4_number[i]==0:
#            author=str(author1)+", "+str(author2)+", "+str(author3)+", and et al."
            author=author123+sep_author+"et al."
            print(author)
            print(paper_url+"\n")

        elif col_NCU_author4_number[i]==1:
            author_k1=col_NCU_author4[i][0]
            author_k1='{'+author_k1+'.}'
            author4=str(author_k1)
#            author=str(author1)+", "+str(author2)+", "+str(author3)+", and et al. (including "+str(author4)+" from NCU)"
            author=author123+sep_author+"et al. (including "+str(author4)+" from NCU)"
#            author=author.replace('.. from','. from')            
            print(author)            
            print(paper_url+"\n")

        else:
            author_k1=col_NCU_author4[i][0]
            author_k1='{'+author_k1+'.}'
            for k in col_NCU_author4_idx[i][1:]:                
                author_k2=col_author[i].split("., ",-1)[k]
                author_k2='{'+author_k2+'.}'
                author_kk=author_kk+sep_author+author_k2            
            author4=str(author_k1)+str(author_kk)
#            author=str(author1)+", "+str(author2)+", "+str(author3)+", and et al. (including "+str(author4)+" from NCU)"
            author=author123+sep_author+"et al. (including "+str(author4)+" from NCU)"            
            print(author)
            print(paper_url+"\n")

#    author=author.replace("(including NESS Collaboration. from NCU)","")
#    paper_journal=paper_journal.replace("&amp;","&")
#    paper_journal=paper_journal.replace('Online at <A href="http://coolstars20.cfa.harvard.edu/">http://coolstars20.cfa.harvard.edu/</A>, cs20, id.8','')    
#    paper_title=paper_title.replace("<SUB>","")
#    paper_title=paper_title.replace("</SUB>","")
    
#    pub_info='('+str(i+1)+') '+author+', '+str(paper_year)+', '+paper_journal+', '+str(paper_volumn)+', '+str(paper_page)+', '+paper_title+', '+paper_url+'\n'    
    pub_info=author+', '+str(paper_year)+', '+paper_journal+', '+str(paper_volumn)+', '+str(paper_page)+', '+paper_title+', '+paper_url+'\n'        
#    pub_info=author+'|'+str(paper_year)+'|'+paper_journal+', '+str(paper_volumn)+', '+str(paper_page)+'|'+paper_title+'|'+paper_url+'\n'    
#    pub_info='('+str(i)+') '+author+', '+str(paper_year)+', '+paper_title+', '+paper_journal+', '+str(paper_volumn)+', '+str(paper_page)+'\n'
    print(pub_info)
    f_pub.write(pub_info)



f_pub.close()

subprocess.call(["sed -i -e 's/nan,//g' "+file_pub], shell=True)
subprocess.call(["sed -i -e 's/\.\.}/\.}/g' "+file_pub], shell=True)
subprocess.call(["sed -i -e 's/<SUB>//g' "+file_pub], shell=True)
subprocess.call(["sed -i -e 's/<\/SUB>//g' "+file_pub], shell=True)
#subprocess.call(["sed -i -e 's/&amp;/&/g' "+file_pub], shell=True)
subprocess.call(["sed -i -e 's/Historical &amp;/Historical \&/g' "+file_pub], shell=True)
subprocess.call(["sed -i -e 's/\.0//g' "+file_pub], shell=True)
subprocess.call(["sed -i -e 's/ (including {NESS Collaboration.} from NCU)//g' "+file_pub], shell=True)
subprocess.call(["sed -i -e 's/Ip, W.-H.,/{Ip, W.-H.},/g' "+file_pub],shell=True)
subprocess.call(["sed -i -e 's/Chen, W.-. ping ./Chen, W.-P./g' "+file_pub], shell=True)

file_2017=' pub_list_NCU_2017.txt'
file_2018=' pub_list_NCU_2018.txt'
file_2019=' pub_list_NCU_2019.txt'
file_201789='pub_list_NCU_2017-2019.txt'
#print(file_2017)
#subprocess.call(["cat "+file_pub+"| grep \/2017 -B3 > "+file_2017],shell=True)
subprocess.call(["cat "+file_pub+" |grep \/2019 | cat -n > "+file_2019],shell=True)
subprocess.call(["cat "+file_pub+" |grep \/2018 | cat -n > "+file_2018],shell=True)
subprocess.call(["cat "+file_pub+" |grep \/2017 | cat -n > "+file_2017],shell=True)


subprocess.call(["echo 2019  > "+file_201789],shell=True)
subprocess.call(["echo   >> "+file_201789],shell=True)
subprocess.call(["cat"+file_2019+"  >> "+file_201789],shell=True)
subprocess.call(["echo   >> "+file_201789],shell=True)
subprocess.call(["echo 2018  >> "+file_201789],shell=True)
subprocess.call(["echo   >> "+file_201789],shell=True)
subprocess.call(["cat"+file_2018+"  >> "+file_201789],shell=True)
subprocess.call(["echo   >> "+file_201789],shell=True)
subprocess.call(["echo 2017  >> "+file_201789],shell=True)
subprocess.call(["echo   >> "+file_201789],shell=True)
subprocess.call(["cat"+file_2017+"  >> "+file_201789],shell=True)
