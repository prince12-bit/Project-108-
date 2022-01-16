import csv 
import plotly.express as pe
import pandas as pa 

data = pa.read_csv("data.csv")

mean = data.groupby(["student_id" , "level"] , as_index = False )["attempt"].mean()

fig = pe.scatter(mean , x = "student_id", y = "level" , size="attempt" ,  color = "attempt")


fig.show()


