#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 00:41:56 2020

@author: altsai
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
file_custom_ZYLin_wrong='export-custom_lYFTJVpu_pipe_ZYLin_wrongname2.txt'
file_custom_Ip_other='export-custom_lYFTJVpu_pipe_Ip_other2.txt'
file_custom_Yuji='export-custom_lYFTJVpu_pipe_Yuji.txt'
file_custom_Hwang_malaysia='export-custom_lYFTJVpu_pipe_Hwang_malaysia2.txt'
