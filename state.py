import pandas as pd
ser1 = pd.Series([34567, 890, 450, 67892, 34677, 789020, 256711, 678291, 637632, 25723,2367, 11786, 345, 256517])
print("top 3 biggest areas are:")
print (ser1.sort_values().tail (3))
print ("3 smalllest areas are :")
print(ser1.sort_values().head(3))
