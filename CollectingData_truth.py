from NeuroPy import NeuroPy
from time import sleep
from time import time
import csv

neuropy = NeuroPy("/dev/rfcomm1") 

neuropy.start()
sleep(3)


with open('_jamanna blink.csv', 'w') as csvfile:
    fieldnames = ['attention', 'delta', 'meditation', 'rawValue', 'theta', 
    'lowAlpha', 'highAlpha', 'lowBeta', 'highBeta', 'lowGamma', 'midGamma', 'poorSignal', 'blinkStrength' ,'label']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    i = time()
    j = time()
    print "Action 1 = truth"
    while(j-i<140):
    	writer.writerow({'attention': neuropy.attention, 'delta': neuropy.delta, 
    		'meditation': neuropy.meditation, 'rawValue': neuropy.rawValue, 
    		'theta': neuropy.theta, 'lowAlpha': neuropy.lowAlpha, 'highAlpha': neuropy.highAlpha, 
    		'lowBeta': neuropy.lowBeta, 'highBeta': neuropy.highBeta, 
    		'lowGamma' : neuropy.lowGamma, 'midGamma' : neuropy.midGamma, 
    		'poorSignal' : neuropy.poorSignal, 'blinkStrength': neuropy.blinkStrength, 'label': '1'})
        sleep(0.1)
        j = time()
    
csvfile.close()
neuropy.stop()

"""
 #To connect headset to laptop
#sudo rfcomm bind /dev/rfcomm1 74:E5:43:D5:6C:07
#ls -l /dev/rfcomm1


 