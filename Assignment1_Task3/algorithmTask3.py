# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 04:25:43 2017

@author: team_31 ((Nabanita Roy)17305618, (Abhimanyu Hazarika)17314158, (Bhavik Mer)17304936)
"""
import process_dataset
import pandas as pd
import numpy as np
from sklearn.model_selection import cross_validate
from sklearn import metrics
#classifiers
from sklearn import linear_model
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis


    

def calculate_scores_cv(regression_model, X, y, scoring):
    scores = cross_validate(regression_model, X, y, cv=10, scoring=scoring, n_jobs= 4)

    for score in scoring:
        print "for", score, " value:", scores['test_' + score].mean()

def execute_algorithm(df, name):
    X, y = process_dataset.process_dataset(df, name)
    scoring = ['accuracy', 'average_precision','r2', 'recall', 'roc_auc' ]
    print "Logistic Regression"
    calculate_scores_cv(linear_model.LogisticRegression(), X, y, scoring)       # Logistic Regression
    #print "K Neighbors Classifier"
    #calculate_scores_cv(KNeighborsClassifier(),X, y, scoring)           #5 is the default value
    print "AdaBosstClassifier"
    calculate_scores_cv(AdaBoostClassifier(), X, y, scoring)
    print "GaussianNB"
    calculate_scores_cv(GaussianNB(), X, y, scoring)
    print "Quadratic DiscriminantAnalysis"
    calculate_scores_cv(QuadraticDiscriminantAnalysis(), X, y, scoring)




			