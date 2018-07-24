# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:27:20 2018

@author: matth
"""

# Open a spreadsheet and read it! 

import pandas as pd

fn = 'data/00 - merged spreadsheets/04-09 Monday, Week 02 MERGED/BeholderVideoApr09-12noon1of3MERGED.xlsx'

xl = pd.ExcelFile(fn)
print(xl.sheet_names)

df = xl.parse('Participant 01')
# ... now double-click "df" in the Variable explorer! 
