#set working directory
setwd("C:/Users/clantroops/Desktop/Trinity/Machine Learning/Assignment 3")
library("psych")
library('ggplot2')

whitewine_dataset_raw <- read.csv("winequality-white.csv", sep = ';', header= TRUE)

describe(whitewine_dataset_raw)
summary(whitewine_dataset_raw)

## Univariate analysis
qplot(factor(whitewine_dataset_raw$quality), xlab="Quality", ylab = "Frequency", main = "White wine quality frequency distribution")

#outliers can be eliminated to bring dataset to normal distribution
hist(whitewine_dataset_raw$fixed.acidity, col="slategray")
hist(whitewine_dataset_raw$volatile.acidity, col="slategray3")
hist(whitewine_dataset_raw$citric.acid, col="slategray3")
# ends

#this wil remains positively skew even after outlier removal
hist(whitewine_dataset_raw$residual.sugar, col="slategray3")

hist(whitewine_dataset_raw$chlorides, col="slategray3")
hist(whitewine_dataset_raw$total.sulfur.dioxide, col="slategray3")
##lower outlier
hist(whitewine_dataset_raw$free.sulfur.dioxide, col="slategray3")
hist(whitewine_dataset_raw$density, col="slategray3")
##lower outlier ends
hist(whitewine_dataset_raw$pH, col="slategray3")
hist(whitewine_dataset_raw$sulphates, col="slategray3")
hist(whitewine_dataset_raw$alcohol, col="slategray3")

boxplot(whitewine_dataset_raw$fixed.acidity, col="yellow", pch=1)
boxplot(whitewine_dataset_raw$volatile.acidity, col="yellow", pch=1)
boxplot(whitewine_dataset_raw$citric.acid, col="yellow", pch=1)
boxplot(whitewine_dataset_raw$residual.sugar, col="yellow", pch=1)
boxplot(whitewine_dataset_raw$chlorides, col="yellow", pch=1)
boxplot(whitewine_dataset_raw$free.sulfur.dioxide, col="yellow", pch=1)
boxplot(whitewine_dataset_raw$total.sulfur.dioxide, col="yellow", pch=1)
boxplot(whitewine_dataset_raw$density, col="yellow", pch=1)
boxplot(whitewine_dataset_raw$pH, col="yellow", pch=1)
boxplot(whitewine_dataset_raw$sulphates, col="yellow", pch=1)
boxplot(whitewine_dataset_raw$alcohol, col="yellow", pch=1)



describe(whitewine_dataset_raw)
summary(whitewine_dataset_raw)
