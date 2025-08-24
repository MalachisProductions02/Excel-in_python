import pandas as pd
## In this project we will
## learn how to connect an Excel 
## database to python to solve a common issue for 
## small or big companies.

df = pd.read_excel("uber.xlsx") ## Conect the Excel file to python
print(df) ## Print the data frame
