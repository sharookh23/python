#application of selelcting using loc, iloc, slicing - dataframes
import pandas as pd

zoo = {
      'animal' : ['lion', 'tiger', 'deer'],
      'uniqid' : [1001, 1002, 1003],
      'water_need' : [500, 600, 400] }
df1 = pd.DataFrame(zoo)
ans =input("\n Do you want to print the menu(y = yes/n = no):  ")
while ans == "y" or ans =="Y":
       print('\n DataFrame operations')
       print(" 1. Add the records ")
       print(" 2. display details of all records")
       print(" 3. display animal details using loc : ")
       print(" 4. display animal details using iloc : ")
       print(" 5. display animal details when uniqid is given ") 
       choice = int(input('Enter your choice :  '))
       if choice==1:
                   n=int(input("Enter how many records you want to enter :  "))
                   data1 = ([])
                   for a in range(n):
                              animal1 = input("Enter the name of animal :  ")
                              uniqid1 = int(input("Enter the id of animal:  "))
                              water1 = int(input("Enter the amount of water neeed for the animal:   "))
                              newrow = {'animal' : animal1, 'uniqid' : uniqid1,'water_need' : water1}
                              data1.append(newrow)
                   df2=pd.DataFrame(data1)
                   df2 = df1.append(df2, ignore_index=True)

       elif choice==2:
                   print("ZOO")
                   print(df2)

       elif choice==3:
                  y=input("Enter name of animal for displaying details:  ")
                  print(df2.loc[df2['animal']==y])

       elif choice==4:
                  print(df2.iloc[0:5])

       elif choice==5:
                  y1=int(input("Enter the uniqid for detail display of animal: "))
                  print(df2.loc[df2['uniqid']==y1])

       else:
                  break
else:
      print("\n please quit")
