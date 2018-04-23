# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 04:25:43 2017

@author: team_31 ((Nabanita Roy)17305618, (Abhimanyu Hazarika)17314158, (Bhavik Mer)17304936)
"""

import sys
import re
import pandas as pd
import numpy as np
import config
import zipfile
#for task 3
import algorithmTask3

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]
    
    for name, data_set in config.DATA_SETS.items():
        if name == "sum_without_noise":
            print "Unziping file"
            zip_ref = zipfile.ZipFile(data_set['zipLocation'], 'r')
            zip_ref.extractall(config.extract_path)
            zip_ref.close()
            print "File Unzipped"
        if data_set['header_present']:
            df = pd.read_csv(data_set['location'], sep=data_set['sep'])
        else:
            df = pd.read_csv(data_set['location'], sep=data_set['sep'], header=None)
        
        df_chunk = df.head(df.shape[0])
        print "dataset", name
        algorithmTask3.execute_algorithm(df_chunk, name)

if __name__ == "__main__":
    main()
