import pandas as pd
import numpy as np
#from sklearn.neighbors import LocalOutlierFactor
from sklearn.svm import OneClassSVM
from sklearn.ensemble import IsolationForest
from sklearn.covariance import EllipticEnvelope
import sys
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")

algorithms = [#("Local Outlier Factor", LocalOutlierFactor()),
             ("One Class SVM", OneClassSVM()),
             ("Isolation Forest", IsolationForest()),
             ("Elliptical Envelope", EllipticEnvelope()),
              ]
white = pd.read_csv('C:/Users/gajja/Desktop/winequality-white.csv',sep=';')
X = white

for name, algo in algorithms:
    if name == "Local Outlier Factor":
        pred = algo.fit_predict(X)
    else:
        pred = algo.fit(X).predict(X)
    outliers = [x for x in pred if x==-1]
    print (*outliers, sep = '\n')
    print(name, ':', len(outliers), 'potential outliers detected.')