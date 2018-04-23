# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 04:25:43 2017

@author: team_31 ((Nabanita Roy)17305618, (Abhimanyu Hazarika)17314158, (Bhavik Mer)17304936)
"""

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
extract_path = os.path.join(dir_path,'..','..')

CHUNKS = [100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000, 50000000, 100000000]

#SUM WITHOUR NOISE AND WITH NOISE DATASET RELATED CONSTANTS
SUM_FEATURES_X_COMMON = ['Feature 1', 'Feature 2','Feature 3','Feature 4',
				'Feature 5 (meaningless but please still use it)','Feature 6',
				'Feature 7','Feature 8','Feature 9','Feature 10']
SUM_CLASSIFIERLABELS_Y_COMMON = ["Very Large Number","Large Number","Medium Number","Small Number","Very Small Number"]
SUM_REGRESSIONFEATURE_Y = ['Target']
SUM_CLASSIFIERFEATURE_Y = ['Target Class']
SUM_NOISE_REGRESSIONFEATURE_Y = ['Noisy Target']
SUM_NOISE_CLASSIFIERFEATURE_Y = ['Noisy Target Class']

#SKIN DATASET RELATED CONSTANTS
SKIN_FEATURES_X = ['B', 'G', 'R']
SKIN_FEATURES_Y = ['Skin']
SKIN_CLASSIFIERLABELS_Y = [1, 2]

#NEWS DATASET RELATED CONSTANTS
NEWS_FEATURES_X = ['n_tokens_title', 'n_tokens_content', 'n_unique_tokens', 'n_non_stop_words', 
		'n_non_stop_unique_tokens', 'num_hrefs', 'num_self_hrefs', 'num_imgs', 'num_videos', 'average_token_length',
		'num_keywords', 'data_channel_is_lifestyle', 'data_channel_is_entertainment', 'data_channel_is_bus',
		'data_channel_is_socmed', 'data_channel_is_tech', 'data_channel_is_world', 'kw_min_min', 'kw_max_min',
		'kw_avg_min', 'kw_min_max', 'kw_max_max', 'kw_avg_max', 'kw_min_avg', 'kw_max_avg', 'kw_avg_avg',
		'self_reference_min_shares', 'self_reference_max_shares', 'self_reference_avg_sharess', 'weekday_is_monday',
		'weekday_is_tuesday', 'weekday_is_wednesday', 'weekday_is_thursday', 'weekday_is_friday', 'weekday_is_saturday',
		'weekday_is_sunday', 'is_weekend', 'LDA_00', 'LDA_01', 'LDA_02', 'LDA_03', 'LDA_04', 'global_subjectivity',
		'global_sentiment_polarity', 'global_rate_positive_words', 'global_rate_negative_words', 'rate_positive_words',
		'rate_negative_words', 'avg_positive_polarity', 'min_positive_polarity', 'max_positive_polarity',
		'avg_negative_polarity', 'min_negative_polarity', 'max_negative_polarity', 'title_subjectivity',
		'title_sentiment_polarity', 'abs_title_subjectivity', 'abs_title_sentiment_polarity']
NEWS_REGRESSIONFEATURE_Y = ['shares']
NEWS_CLASSIFIERFEATURE_Y = ['sharesClass']
NEWS_CLASSIFIERLABELS_Y = ['Not popular','Almost popular','Popular','Very popular']


DATASET_ROOT = 'C:/Users/clantroops/Desktop/ML Assignment'

REGRESSION = "regression"
CLASSIFICATION = "classification"

DATA_SETS = {
    'sum_without_noise': {
        'location': os.path.join(dir_path,'..','..','without noise','The SUM dataset, without noise.csv'),
        'sep': ';',
        'zip': True,
        'zipLocation': os.path.join(dir_path,'..','..','The SUM dataset.zip'),
        'scaleData': True,
        'featuresX': SUM_FEATURES_X_COMMON,
        'regressionFeaturesY' : SUM_REGRESSIONFEATURE_Y,
        'classifierFeaturesY' : SUM_CLASSIFIERFEATURE_Y,
        'classifierLabelsY' : SUM_CLASSIFIERLABELS_Y_COMMON
    },
    'sum_with_noise': {
        'location': os.path.join(dir_path,'..','..','with noise','The SUM dataset, with noise.csv'),
        'sep': ';',
        'zip': True,
        'zipLocation': os.path.join(dir_path,'..','..','The SUM dataset.zip'),
        'scaleData': True,
        'featuresX': SUM_FEATURES_X_COMMON,
        'regressionFeaturesY' : SUM_NOISE_REGRESSIONFEATURE_Y,
        'classifierFeaturesY' : SUM_NOISE_CLASSIFIERFEATURE_Y,
        'classifierLabelsY' : SUM_CLASSIFIERLABELS_Y_COMMON
    },
    'skin_nonskin': {
        'location': os.path.join(dir_path,'..','..','SkinNonSkin','Skin_NonSkin.txt'),
        'sep': '	',
        'zip': False,
        'scaleData': False,
        'featuresX': SKIN_FEATURES_X,
        'regressionFeaturesY' : SKIN_FEATURES_Y,
        'classifierFeaturesY' : SKIN_FEATURES_Y,
        'classifierLabelsY' : SKIN_CLASSIFIERLABELS_Y
    },
    'online_news_popularity': {
        'location': os.path.join(dir_path,'..','..','OnlineNewsPopularity', 'OnlineNewsPopularity.csv'),
        'zip': True,
        'zipLocation': os.path.join(dir_path,'..','..','OnlineNewsPopularity.zip'),
        'sep': ', ',
        'scaleData': True,
        'featuresX': NEWS_FEATURES_X,
        'regressionFeaturesY' : NEWS_REGRESSIONFEATURE_Y,
        'classifierFeaturesY' : NEWS_CLASSIFIERFEATURE_Y,
        'classifierLabelsY' : NEWS_CLASSIFIERLABELS_Y
    }
}