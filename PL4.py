#selection & deletion of rows-dataframes
import pandas as pd
zoo = {
      'animal' : ['lion','tiger', 'deer'],
      'uniqid' : [1001,1002,1003],
      'water need' : [500,600,400]
      }
df1 = pd.DataFrame(zoo)
ans =input("\n Do you want to print the menu(y = yes/n = no):  ")
while ans == "y" or ans =="Y":
       print('\n DataFrame operations')
       print(" 1. Add the  records ")
       print(" 2. display details of all records")
       print(" 3. delete record when uniquid is given ")
       choice = int(input('Enter your choice :  '))

       if choice == 1:
             n=int(input("Enter howmany records you want to enter :  "))
             data1 = ([])
             for a in range(n):
                   animal1 = input("Enter the name of animal :  ")
                   uniqid1 = int(input("Enter the id of animal:  "))
                   water1 = int(input("Enter the amount of water neeed for the animal:   "))
                   newrow = {'animal' : animal1, 'uniqid' : uniqid1,'water need' : water1}
                   data1.append(newrow)
             df2=pd.DataFrame(data1)
             df2 = df1.append(df2, ignore_index=True)

       elif choice == 2:
                   print("ZOO")
                   print(df2)

       elif choice == 3 :
                   df2.set_index('uniqid',inplace=True)
                   y = int(input("Enter the uniqid to delete :  "))
                   df2.drop( labels=y, axis = 0,inplace=True)
                   print("\n record deleted")
                   print("ZOO AFTER DELETION")
                   print("\n Records after deletion are : \n",df2)

       elif choice == 4 :
                  exit()
       else:
                   break

else:
      print("\n please quit")
                         
                         
             
