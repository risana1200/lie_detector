
# coding: utf-8

# In[99]:


import pandas as pd
import csv


# In[121]:


in1 = pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/arpit_truth.csv")
in2 = pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/arpit_lie.csv")
in3 = pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/nobha_truth.csv")
in4 = pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/nobha_lie.csv")
in5 = pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/nisha_truth.csv")
in6 = pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/nisha_lie.csv")
in7 = pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/priya_truth.csv")
in8 = pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/priya_lie.csv")
in9 = pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/shubhi_truth.csv")
in10 = pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/shubhi_lie.csv")
in11= pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/rakhi_truth.csv")
in12 = pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/rakhi_lie.csv")
in13= pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/nirma_truth.csv")
in14 = pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/nirma_lie.csv")
in15 = pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/komal_truth.csv")
in16 = pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/komal_lie.csv")
in17 = pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/kaajal_truth.csv")
in18 = pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/kaajal_lie.csv")
in19 = pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/disha_truth.csv")
in20 = pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/disha_lie.csv")
in21= pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/kushagra_truth.csv")
in22 = pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/kushagra_lie.csv")
in23= pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/himani_truth.csv")
in24 = pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/himani_lie.csv")
in25 = pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/malvika_truth.csv")
in26= pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/malvika_lie.csv")
in27= pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/risana_truth.csv")
in28= pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/risana_lie.csv")
in29= pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/jayti_truth.csv")
in30= pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/jayti_lie.csv")



# In[122]:"""


in1 = in1.drop(in1.index[489:500])
in1=in1.drop(in1.index[500:525])
in1.to_csv("result_final_RRR.csv")

in2 = in2.drop(in2.index[0:80])
in2=in2.drop(in2.index[560:579])
in2.to_csv("arpit_lie_R.csv")

in3 = in3.drop(in3.index[0:80])
in3=in3.drop(in3.index[560:579])
in3.to_csv("nobha_truth_R.csv")

in4 = in4.drop(in4.index[0:80])
in4=in4.drop(in4.index[560:579])
in4.to_csv("nobha_lie_R.csv")

in5 = in5.drop(in5.index[0:80])
in5=in5.drop(in5.index[560:579])
in5.to_csv("nisha_truth_R.csv")

in6 = in6.drop(in6.index[0:80])
in6=in6.drop(in6.index[560:579])
in6.to_csv("nisha_lie_R.csv")

in7 = in7.drop(in7.index[0:80])
in7=in7.drop(in7.index[560:579])
in7.to_csv("priya_truth_R.csv")

in8 = in8.drop(in8.index[0:80])
in8=in8.drop(in8.index[560:579])
in8.to_csv("priya_lie_R.csv")

in9 = in9.drop(in9.index[0:80])
in9=in9.drop(in9.index[560:579])
in9.to_csv("shubhi_truth_R.csv")

in10 = in10.drop(in10.index[0:80])
in10=in10.drop(in10.index[560:579])
in10.to_csv("shubhi_lie_R.csv")

in11= in11.drop(in11.index[0:80])
in11=in11.drop(in11.index[560:579])
in11.to_csv("rakhi_truth_R.csv")

in12 = in12.drop(in12.index[0:80])
in12=in12.drop(in12.index[560:579])
in12.to_csv("rakhi_lie_R.csv")

in13 = in13.drop(in13.index[0:80])
in13=in13.drop(in13.index[560:579])
in13.to_csv("nirma_truth_R.csv")

in14= in14.drop(in14.index[0:80])
in14=in14.drop(in14.index[560:579])
in14.to_csv("nirma_lie_R.csv")

in15 = in15.drop(in15.index[0:80])
in15=in15.drop(in15.index[560:579])
in15.to_csv("komal_truth_R.csv")

in16 = in16.drop(in16.index[0:80])
in16=in16.drop(in16.index[560:579])
in16.to_csv("komal_lie_R.csv")

in17 = in17.drop(in17.index[0:80])
in17=in17.drop(in17.index[560:579])
in17.to_csv("kaajal_truth_R.csv")

in18 = in18.drop(in18.index[0:80])
in18=in18.drop(in18.index[560:579])
in18.to_csv("kaajal_lie_R.csv")

in19 = in19.drop(in19.index[0:80])
in19=in19.drop(in19.index[560:579])
in19.to_csv("disha_truth_R.csv")

in20 = in20.drop(in20.index[0:80])
in20=in20.drop(in20.index[560:579])
in20.to_csv("disha_lie_R.csv")

in21 = in21.drop(in21.index[0:80])
in21=in21.drop(in21.index[560:579])
in21.to_csv("kushagra_truth_R.csv")

in22= in22.drop(in22.index[0:80])
in22=in22.drop(in22.index[560:579])
in22.to_csv("kushagra_lie_R.csv")

in23= in23.drop(in23.index[0:80])
in23=in23.drop(in23.index[560:579])
in23.to_csv("himani_truth_R.csv")

in24 = in24.drop(in24.index[0:80])
in24=in24.drop(in24.index[560:579])
in24.to_csv("himani_lie_R.csv")

in25 = in25.drop(in25.index[0:80])
in25=in25.drop(in25.index[560:579])
in25.to_csv("malvika_truth_R.csv")

in26 = in26.drop(in26.index[0:80])
in26=in26.drop(in26.index[560:579])
in26.to_csv("malvika_lie_R.csv")

in27 = in27.drop(in27.index[0:80])
in27=in27.drop(in27.index[560:579])
in27.to_csv("risana_truth_R.csv")

in28 = in28.drop(in28.index[0:80])
in28=in28.drop(in28.index[560:579])
in28.to_csv("risana_lie_R.csv")

in29 = in29.drop(in29.index[0:80])
in29=in29.drop(in29.index[560:579])
in29.to_csv("jayti_truth_R.csv")

in30 = in30.drop(in30.index[0:80])
in30=in30.drop(in30.index[560:579])
in30.to_csv("jayti_lie_R.csv")


