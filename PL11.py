import pandas as pd
s1 = pd.Series([3569,1000,500,67892,345677,78902,56711,68291,25723,236,1189,345,256875])
print("SERIES")
print(s1)
print("*************************************************")
print("Top 3 biggest area in the city are :- ")
print(s1.sort_values().tail(3))
print("Top 3 smallest area in the city are :- ")
print(s1.sort_values().head(3))
