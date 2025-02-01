# series arithmetic, slicing, indexing & vector operations
# series of dictionary
import pandas as pd
d1 = {'a' :10, 'b' :2, 'c' :3, 'd' :4}
d2 = {'a' :11, 'b' :22, 'c' :33, 'd' :44}
d3 = {"Anita" :11, "Beeena" :22, 'cini' :33, "Deepak" :44}
s1 = pd.Series(d1)
s2 = pd.Series(d2)
s3 = pd.Series(d3)
ans = input("\n Do you want to print the menu(y=yes/n=no) :  ")
while ans =='y' or ans == 'Y' :

                  print("\n 1. series mathematical operations")
                  print(" 2. vector operations")
                  print(" 3. slicing")
                  print(" 4. default indexing")
                  print(" 5. labelled indexing")

                  choice = int(input("\n Enter your choice : "))

                  if choice ==1:
                        addition = s1+s2
                        print("\n Addition of s1 & s2 is \n",addition)
                        multi = s1*s2
                        print("\n  multiplication of s1 & s2 is \n",multi)
                        division = s1/s2
                        print("\n division of s1 & s2 is \n",division)
                        addition2 = s1+s3
                        print("\n Addition of s1 & s3 is \n",addition2)

                  elif choice == 2:
                        a = s1+2
                        print("\n s1 + 2 is \n",a)
                        b = s2*3
                        print("\n s2*3 is \n", b)
                        c = s1**3
                        print("|n s1**3 is \n", c)
                        print('\n s3>30 is \n',s3>30)

                  elif choice == 3 :
                        print("\n first two element of s1 \n ",s1.head(2))
                        print("\n last two elements of s1 \n",s1.tail(2))
                        print("|n middle two item of s2 \n",s2[1],s2[2])

                  elif choice == 4:

                        print("\n Display Beena's mark using default indexing ",s3[1])
                  elif choice == 5:

                        print("\n Display Beena's mark using labelled indexing ")

                        s4 = pd.Series(s3.values, index = ['a', 'b', 'c', 'd'])
                        print(s4['b'])
                  else:
                        break
else:
      print("\n please quit")
