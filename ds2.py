import pandas as pd1
d1 = {'one' : pd1.Series([1,2,3], index=['a','b','c']), 'two' : pd1.Series([1,2,3,4],index=['a','b','c','d'])}
df1 = pd1.DataFrame(d1)
print(df1)
