from sub import *
from add import *
from mult import *
from div import *
a=int(input ("Enter the number"))
b=int(input ("Enter the number"))
choice = int(input("ENTER A CHOICE \n 1. Addition \n 2. Subtration \n 3. Division \n 4 Multiplication"))
if choice == 1:
    print(addFunc(a,b))
elif choice == 2:
    print(subFunc(a,b))
elif choice == 3:
    print(divFunc(a,b))
elif choice == 4:
    print(multFunc(a,b))
else:
    print("OOPSss!!! something is wrong here...")


