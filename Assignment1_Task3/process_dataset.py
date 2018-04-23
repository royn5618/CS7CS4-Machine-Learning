# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 04:25:43 2017

@author: team_31 ((Nabanita Roy)17305618, (Abhimanyu Hazarika)17314158, (Bhavik Mer)17304936)
"""
# Imports
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.model_selection import cross_validate
from sklearn import svm
from sklearn import metrics
from sklearn import neighbors
from sklearn import tree
from sklearn.preprocessing import LabelEncoder

def process_dataset(df, name):
    x = np.array([])
    y = np.array([])

    if name == 'sum_without_noise':
        x,y = get_xy_clf_sum_without_noise(df)

    if name == 'skin_nonskin':
        x,y = get_xy_clf_skin_nonskin(df)
           
    return x, y

def get_xy_clf_sum_without_noise(df):
    df["Target Class"] = df["Target Class"].astype('category')
    #df["Target Class"] = df["Target Class"].cat.codes
    #dataset_sum["Target Class"].value_counts()
    #Target class had more number of Very Large Number we are converting it into 1
    df["Target Class"] = np.where(df["Target Class"] == "Very Large Number", 1, 0)
    x = df.iloc[:, 0:11]
    y = df.iloc[:, 12]
    
    return x,y

def get_xy_clf_skin_nonskin(df):
    df.columns = ["R", "G" , "B", "Skin_NonSkin"]
    df["Skin_NonSkin"] = df["Skin_NonSkin"].astype('category')
    df["Skin_NonSkin"] = df["Skin_NonSkin"].cat.codes
    x = df.iloc[:, 0:3].values
    y = df["Skin_NonSkin"]
    return x,y



