# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 04:25:43 2017

@author: team_31 ((Nabanita Roy)17305618, (Abhimanyu Hazarika)17314158, (Bhavik Mer)17304936)
"""
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
extract_path = os.path.join(dir_path,'..','..')

DATASET_ROOT = 'C:/Users/clantroops/Desktop/ML Assignment'

DATA_SETS = {
    'sum_without_noise': {
        'zipLocation': os.path.join(dir_path,'..','..','The SUM dataset.zip'),
        'location': os.path.join(dir_path,'..','..','without noise','The SUM dataset, without noise.csv'),
        'header_present': True,
        'sep': ';',
        'classification_labels_present': True
    },
    'skin_nonskin': {
        'location': os.path.join(dir_path,'..','..','SkinNonSkin','Skin_NonSkin.txt'),
        'header_present': True,
        'sep': '	'
    }
}