import pandas as pd
dict1 = {'Rice' :50, 'Wheat' :20}
series1 = pd.Series(dict1)
series2 = pd.Series({'barley' :40, 'maize' :50, 'corn' :3, 'sugar' :45, 'onion' :4})
series3 = series1.append(series2)
series4 = pd.Series(series3)
ans = input("\n Do you want to print the menu(y=yes/n=no): ")
while ans == "y" or ans == "Y" :
      print("\n series operation")
      print(" 1.initialize the records ")
      print(" 2. Add 5 more records & display the series")
      print(" 3.delete the record")
      print(" 4.display records lesss than 5 kg: ")
      choice = int(input("enter your choice:  "))
      
      if choice == 1 :
            print("SMALL BAZAR")
            print(series1)
      elif choice == 2 :
            print("SMALL BAZAR")
            print(series4)
      elif choice == 3 :
            y = input ("Enter the item for deletion: ")
            result=series4.drop(labels=[y])
            print("\n item deleted")
            print("SMALL BAZAR AFTER DELETION")
            print("\n Record after deletion are: ", result , sep='\n')
      elif choice == 4 :
            series6 = pd.Series(series4)
            print("SMALL BAZAR")
            print(series6[series6<5])
      else:
            break
else :
      print("\n please quit")
      
