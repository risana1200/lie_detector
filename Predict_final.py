from NeuroPy import NeuroPy
from time import sleep
from time import time
import pandas as pd
import numpy as np
import csv
import pickle
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import preprocessing
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix

neuropy = NeuroPy("/dev/rfcomm1") 
neuropy.start()
sleep(3)


with open('Predict_Final.csv', 'w') as csvfile:
    fieldnames = ['attention', 'delta', 'meditation', 'rawValue', 'theta', 
    'lowAlpha', 'highAlpha', 'lowBeta', 'highBeta', 'lowGamma', 'midGamma', 'poorSignal', 'blinkStrength' ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    i = time()
    j = time()
    print "Perform the Action"
    sleep(4)
    while(j-i<10):
    	writer.writerow({'attention': neuropy.attention, 'delta': neuropy.delta, 
    		'meditation': neuropy.meditation, 'rawValue': neuropy.rawValue, 
    		'theta': neuropy.theta, 'lowAlpha': neuropy.lowAlpha, 'highAlpha': neuropy.highAlpha, 
    		'lowBeta': neuropy.lowBeta, 'highBeta': neuropy.highBeta, 
    		'lowGamma' : neuropy.lowGamma, 'midGamma' : neuropy.midGamma, 
    		'poorSignal' : neuropy.poorSignal, 'blinkStrength': neuropy.blinkStrength})
        sleep(0.1)
        j = time()
    i = time() 
csvfile.close()
neuropy.stop()

sleep (1)

#print "Read"



from sklearn.preprocessing import normalize

data1=pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/Predict_Final.csv")
###### importing the classfier

#print "Normalized"


data1 = data1.drop(data1.index[0:20])
data1 = data1.drop(data1.index[41:61])
data1 = data1.transpose()
#print data1
a = pd.DataFrame(normalize(data1))
b = a.transpose()
b.to_csv('Predict_Norm_Final.csv')
data_features =b
#data_labels = b.columns[1]
P=data_features
X_test=standardized_X_test=preprocessing.scale(P)

p=dataset=pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/priya_inspiring_india.csv")
data_feature=p.drop(columns=['label'])
labels='label'
data_label=p[labels]
Z=data_feature
X_train=standardized_X_train=preprocessing.scale(Z)
Y_train=data_label
logreg=MLPClassifier(hidden_layer_sizes=(30,30,30))
logreg.fit(X_train,Y_train)
#print X_train
#print X_train.size
#print X_test.size
#print X_test
Y_pred=logreg.predict(X_test)

sum1 = 0
sum2 = 0

for i in range(0,len(Y_pred) ): 
    if Y_pred[i] == 1 :
        sum1 = sum1+1
    else :
        sum2 = sum2+1

#print predict

#print "truth = ",sum1," lie = ",sum2

if sum1>sum2 :
    print "truth "
else :
   print "lie"