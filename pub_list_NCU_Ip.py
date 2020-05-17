#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 02:33:49 2020

@author: altsai
"""


import os
import sys
import shutil
#import re
import subprocess
#import numpy as np
import pandas as pd
file_rest_Ip='rest_NCU_Ip_38.txt'
file_rest_Ip='rest_NCU_Ip_38-2.txt'
file_NCU='pub_list_NCU.txt'
file_NCU_Ip='pub_list_NCU_Ip.txt'
shutil.copyfile(file_custom1, file_combine)

subprocess.call(["sed -i -e 's/|8|/||8|/g' "+file_combine], shell=True)



