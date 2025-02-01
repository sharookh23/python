import pandas as pd
student1 = {'test1' : [5,6,8,3,10] , 'test2' : [7,8,9,6,15] }
student2 = {'test1' : [3,3,6,6,8] , 'test2' : [5,8,9,10,5] }
ds1 = pd.DataFrame (student1)
ds2 = pd.DataFrame (student2)
print(ds1)
print(ds2)
print("\n subtraction")
print(ds1.sub(ds2))
print("\n addition")
print(ds1.add(ds2))
print("\n multiplication")
print(ds1.mul(ds2))
print("\n division")
print(ds1.div(ds2))
