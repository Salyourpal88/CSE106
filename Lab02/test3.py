import pandas as pd

#Problem 1
print("Record Precipitation:")
temp1 = pd.read_csv("weather_data.txt")
print(temp1[temp1.record_precipitation > 5], "date")
print('\n')

#Problem 2 
print("Average max tempeture in July 2014:")
print(temp1.loc[0:30, "actual_max_temp"])
print('\n')

#Problem 3
print("Record Max tempeture of Max Tempetures:")
print(temp1.loc[temp1.actual_max_temp.max(), "date"])
print('\n')

#Problem 4
print("Amount of Rain in October 2014:")
temp2 = temp1.loc[92:122, "actual_precipitation"]
temp2 = temp2.sum()
print(temp2)
print('\n')

#Problem 5
print("Condition:")
condition = (temp1.actual_min_temp < 60) & (temp1.actual_max_temp > 90) 
print(temp1.loc[condition, "date"])