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
file_rest_Ip='rest/rest_NCU_Ip_35.txt'
file_rest_Ip2='rest/rest_NCU_Ip_35-2.txt'
file_NCU='pub_list_NCU.txt'
file_NCU_Ip='pub_list_NCU_Ip.txt'
shutil.copyfile(file_rest_Ip, file_rest_Ip2)
shutil.copyfile(file_NCU, file_NCU_Ip)

subprocess.call(["cat "+file_rest_Ip+" |grep Ip > "+file_rest_Ip2], shell=True)

list_1stauthor=cat rest_NCU_Ip_35.txt |grep Ip|cut -d ";" -f1| cut -d "." -f2 | cut -d " " -f2

