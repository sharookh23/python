import pandas as pd1
df1 = pd1.DataFrame([[1,2], [3,4]], columns = ['a','b'])
df2 = pd1.DataFrame([[5,6], [7,8]], columns = ['a','b'])
df1 = df1.append(df2)
print(df1)
