# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 04:25:43 2017

@author: team_31 ((Nabanita Roy)17305618, (Abhimanyu Hazarika)17314158, (Bhavik Mer)17304936)
"""

import numpy as np
import config
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.metrics import accuracy_score, log_loss, precision_score, f1_score
from sklearn import preprocessing
from sklearn import linear_model
from sklearn.model_selection import StratifiedKFold, cross_val_score,cross_val_predict
import math

def compute_metrics_regression(X, y, regressionAlgo):
    MSE = -cross_val_score(regressionAlgo, X, y, cv=10, scoring='neg_mean_squared_error')
    print ("RMSE: %0.5f" %(np.sqrt(np.abs(MSE.mean()))))
    scoresR2 = cross_val_score(regressionAlgo, X, y, cv=10, scoring='r2').mean()
    print ("R2: %0.5f"  %(scoresR2.mean()))
    print "\n"

def compute_metrics_classification(X, y, classificationAlgo):
    y_pred = cross_val_predict(classificationAlgo, X, y, cv=10)
    print "Accuracy: " ,accuracy_score(y, y_pred)
    print "Log-loss: ",log_loss(y, cross_val_predict(classificationAlgo, X, y, cv=10, method='predict_proba'))
    
def process_data(dataFrame, name, numChunks, algorithm, featuresX, regressionFeaturesY, classifierFeaturesY,
	classifierLabelsY, scaleData):
    print("Processing ", name ,"chunk of size", numChunks)
    X = dataFrame[0:numChunks][featuresX]
    if scaleData:
        X = preprocessing.scale(X)
    if algorithm == config.REGRESSION:
        print regressionFeaturesY
        y = dataFrame[0:numChunks][regressionFeaturesY]
        if scaleData:
            y= preprocessing.scale(y)
    else:
        y = dataFrame[0:numChunks][classifierFeaturesY]
        le = preprocessing.LabelEncoder()
        le.fit(classifierLabelsY)
        y = le.transform(y.values.ravel())
        
    return X,y    

def execute_algorithm(df, name, chunk_size, algorithm, featuresX, regressionFeaturesY, classifierFeaturesY,
	classifierLabelsY, scaleData):
    
    if algorithm == config.CLASSIFICATION:        
        X, y = process_data(df, name, chunk_size, algorithm, featuresX, regressionFeaturesY, classifierFeaturesY,
	classifierLabelsY, scaleData)
        #Compute logistic regression
        print "Classification: \n"
        print "Logistic regression:"
        compute_metrics_classification(X, y, linear_model.LogisticRegression())
        
        print "kneighbor classification:"
        #Compute kneighbor regression
        compute_metrics_classification(X, y, KNeighborsClassifier(n_neighbors=5))
        
    if algorithm == config.REGRESSION:
        X, y = process_data(df, name, chunk_size, algorithm, featuresX, regressionFeaturesY, classifierFeaturesY,
	classifierLabelsY, scaleData)
        print "Regression: \n"
        print "Linear Regression:"
        #Compute Linear Regression
        compute_metrics_regression(X, y, linear_model.LinearRegression())
        
        print "Lasso Regression:"
        #Compute Lasso Regression
        #sumdataset perfect
        compute_metrics_regression(X, y, linear_model.Lasso(alpha=0.1))
