import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd

df = pd.read_csv("School2.csv")
data = df["Math_score"].tolist()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    set_of_means= random_set_of_mean(100)
    mean_list.append(set_of_means)

mean = statistics.mean(mean_list)
std_deviation = statistics.stdev(mean_list)
print("Mean of Sampling Distribution:" , mean)
print("Standard Deviation" , std_deviation)

first_stdev_start , first_stdev_end = mean-std_deviation , mean+std_deviation
second_stdev_start , second_stdev_end = mean-(2*std_deviation) , mean+(2*std_deviation)
third_stdev_start , third_stdev_end = mean-(3*std_deviation) , mean+(3*std_deviation)

df1 = pd.read_csv("School_1_Sample.csv")
data1 = df1["Math_score"].tolist()
mean_Sample1 = statistics.mean(data1)
print("Mean of Sample 1:" , mean_Sample1)
fig = ff.create_distplot([mean_list] , ["student marks"] , show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean] , y=[0,0.17] , mode="lines" , name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_Sample1, mean_Sample1] , y=[0,0.17] , mode="lines" , name="MEAN OF STUDENTS"))
fig.add_trace(go.Scatter(x=[first_stdev_end  , first_stdev_end] , y=[0,0.17] , mode="lines" , name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_stdev_end , second_stdev_end] , y=[0,0.17] , mode="lines" , name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_stdev_end  , third_stdev_end] , y=[0,0.17] , mode="lines" , name="STANDARD DEVIATION 3 END"))
fig.show()

df2 = pd.read_csv("School_2_Sample.csv")
data2 = df2["Math_score"].tolist()
mean_Sample2 = statistics.mean(data2)
print("Mean of Sample 2:" , mean_Sample2)
fig = ff.create_distplot([mean_list] , ["student marks"] , show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean] , y=[0,0.17] , mode="lines" , name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_Sample2, mean_Sample2] , y=[0,0.17] , mode="lines" , name="MEAN OF STUDENTS"))
fig.add_trace(go.Scatter(x=[first_stdev_end  , first_stdev_end] , y=[0,0.17] , mode="lines" , name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_stdev_end , second_stdev_end] , y=[0,0.17] , mode="lines" , name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_stdev_end  , third_stdev_end] , y=[0,0.17] , mode="lines" , name="STANDARD DEVIATION 3 END"))
fig.show()

df3 = pd.read_csv("School_3_Sample.csv")
data3 = df3["Math_score"].tolist()
mean_Sample3 = statistics.mean(data3)
print("Mean of Sample 3:" , mean_Sample3)
fig = ff.create_distplot([mean_list] , ["student marks"] , show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean] , y=[0,0.17] , mode="lines" , name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_Sample3, mean_Sample3] , y=[0,0.17] , mode="lines" , name="MEAN OF STUDENTS"))
fig.add_trace(go.Scatter(x=[first_stdev_end  , first_stdev_end] , y=[0,0.17] , mode="lines" , name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_stdev_end , second_stdev_end] , y=[0,0.17] , mode="lines" , name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_stdev_end  , third_stdev_end] , y=[0,0.17] , mode="lines" , name="STANDARD DEVIATION 3 END"))
fig.show()

z_score = (mean-mean_Sample2)/std_deviation
print("Z Score:" , z_score)