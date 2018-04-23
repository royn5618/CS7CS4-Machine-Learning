# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 04:25:43 2017

@author: team_31 ((Nabanita Roy)17305618, (Abhimanyu Hazarika)17314158, (Bhavik Mer)17304936)
"""

import sys
import pandas as pd
import numpy as np
import config
import algorithm
import zipfile

def main():

    for name, data_set in config.DATA_SETS.items():
        if data_set['zip']:
            print "Unziping file"
            zip_ref = zipfile.ZipFile(data_set['zipLocation'], 'r')
            zip_ref.extractall(config.extract_path)
            zip_ref.close()
            print "File Unzipped"
            
        df = pd.read_csv(data_set['location'], sep=data_set['sep'])
        
        if name == "online_news_popularity":
            shares = df[0:]['shares']
            classlabel = []
            percentiles = [np.percentile(shares, 25),np.percentile(shares, 50),np.percentile(shares, 75),np.percentile(shares, 100)]
            for value in shares:
                if value < percentiles[0]:
                    classlabel.append('Not popular')
                elif value < percentiles[1]:
                    classlabel.append('Almost popular')
                elif value < percentiles[2]:
                    classlabel.append('Popular')
                else:
                    classlabel.append('Very popular')
            
            df = df.assign(sharesClass=classlabel)
        
        if name == "skin_nonskin":
            df = pd.read_csv(data_set['location'], sep=data_set['sep'],  names= ['B', 'G', 'R', 'Skin'])
            df = df.reindex(np.random.permutation(df.index))
        
        for chunk_size in config.CHUNKS:
            if chunk_size < len(df.index):
                df_chunk = df.head(chunk_size)
                print "chunk size", chunk_size
                print "dataset", name
                algorithm.execute_algorithm(df_chunk, name, chunk_size, config.REGRESSION, data_set['featuresX'], data_set['regressionFeaturesY'], data_set['classifierFeaturesY'], data_set['classifierLabelsY'],  data_set['scaleData'])
                algorithm.execute_algorithm(df_chunk, name, chunk_size, config.CLASSIFICATION, data_set['featuresX'], data_set['regressionFeaturesY'], data_set['classifierFeaturesY'], data_set['classifierLabelsY'],  data_set['scaleData'])


if __name__ == "__main__":
    main()
