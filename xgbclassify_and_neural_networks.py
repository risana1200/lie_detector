import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn import preprocessing
from sklearn.neural_network import MLPClassifier
import xgboost as xgb
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
from sklearn.metrics import confusion_matrix
p=dataset=pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/priya_inspiring_india.csv")
data_features=p.drop(columns=['label'])
labels='label'
data_labels=p[labels]
Z=data_features
X=standardized_X=preprocessing.scale(Z)
Y=data_labels
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.15,random_state=123)
#logreg=MLPClassifier(hidden_layer_sizes=(30,30,30))
logreg=XGBClassifier()
logreg.fit(X_train,Y_train)
A=Y_pred=logreg.predict(X_test)
print('Accuracy of logistic regression classifier on test set :{:.2f}'.format(logreg.score(X_test,Y_test)))
B=Y_pred=logreg.predict(X_train)
print('Accuracy of logistic regression classifier on train set :{:.2f}'.format(logreg.score(X_train,Y_train)))
cm=confusion_matrix(y_true=Y_test,y_pred=A)
