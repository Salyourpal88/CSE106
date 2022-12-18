from turtle import title
import pandas as pd 
import matplotlib.pyplot as plt

#Problem 1
temp1 = pd.read_csv("weather_data.txt")
temp2 = temp1.loc[:,["date", "actual_max_temp", "actual_min_temp"]]
temp2.plot(x = "date", title = "Weather Data")
plt.legend()#????
plt.show()

#Problem 2
#temp1 = temp1.loc[:, "actual_precipitation"]
#temp1.plot(x = "date", title = "Weather Data")
#temp1["actual_precipitation", "date"].plot(kind = 'hist', x = "actual_precipitation", y = "date")
temp1["actual_precipitation"].plot(kind = 'hist')
plt.show()