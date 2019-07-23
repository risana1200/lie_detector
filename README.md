# lie_detector
Signal Processing Of EEG Signals Using Machine Learning and truth/lie detection

The aim of this project is to collect the raw electrical signals from a human brain using a neuro headset and then process these signals using machine learning so as to recognise the statements made by the user as truth or lie..
Applications:

    This project can be used in polygraphy tests replacing the conventional methods of polygraphy.
    It may also have application in law and order,investigation etc. using the brain signal analysis.

Requirements:

    Neurosky Mindwave Mobile Headset
    Python 2.7 / jupyter notebook (python 2.7 compatible)

If you have the neuro Headset, go to With HeadSet, else go to Without HeadSet
With HeadSet

For those who have the neuro headset, they may proceed as following to utilise my project-

    Switch On the headset and hold the key for On position until the headset flash starts blinking faster, which means it is in pairing mode.

    Pair your computer with the headset using bluetooth of your computer(The name of the headset for bluetooth connections is Mindwave Mobile).

    You only have to pair using the bluetooth. To connect the headset, you have to use the following python code in Terminal

sudo rfcomm bind /dev/rfcomm1 74:E5:43:D5:6C:07
ls -l /dev/rfcomm1

You need to go to your bluetooth settings and then find out the port by which you are connecting to the headset(example-COM3,COM2 etc.) and then replace that port instead of rfcomm1 in the above code(example- rfcomm2,rfcomm3 etc.)

    You are now connected to the headset.

    To implement my model, you may use "Predict_final.py" script present in my repository.In this script you have to make a change in the following line of code-

data1=pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/Predict_Final.csv")

Actually the data you collected is written in a csv file in the directory where you have run the above script "Predict_final.py" in a file named Predict_Final.csv , so instead of "/media/arpit/New Volume/3.Projects/EEG_Project/Raw_Data/Total_Normalised_data_Collection" in above line of code you have to put the address of the directory in which you have run the script "Predict_final.py".

    make sure you change only the path and not the file name that is the file names "Predict_Final.csv" and "Predict_Concat_Final.csv" remains same .

Moreover there is another line of code wher you need to change - "/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/priya_inspiring_india.csv"". Here also instead of "/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/Predict_Final.csv"" , put the address of the directory where you have run the script "Predict_final.py".

    My training dataset is for saying truth or lie statements. So after running the script ,speak some truth or lie statements and after some time,it will be predicted.
Without HeadSet

For those of you who do not have the neuroheadset and wish to see the accuracy of my model, proceed as following -

    Download the file 'result_final_modified.csv" from  my repository.

    Now you have to run the python script named "newaccuracy.py" in my repository .

    You need to make a small change in the above script before running it.

dataset = pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/result_final_modified.csv")

In the above line of code , you need to change the path from "/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/result_final_modified.csv"" to the path where you have downloaded the "result_final_modified.csv" file.

    The above script will split the final dataset into two parts, one for testing and another for training.

    You will get the accuracy score through various algorithms.



   

  

