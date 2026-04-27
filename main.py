from utils import *
from dis_balance import *
from withdraw import *
from deposit import *
from statement import *
import os
while True:
        print("\n1. Display Balance")
        print("\n2. Deposit Money")
        print("\n3. Withdraw Money")
        print("\n4. Show Statements")
        print("\n5. Exit")
        choice = input("Enter your choice: ")
        if choice.isdigit():
            choice = int(choice)
            if   choice ==1: dis_balance()
            elif choice ==2: deposit()
            elif choice ==3: withdraw()
            elif choice ==4: statement()
            elif choice ==5: 
                print("Thank you") 
                exit()
            else:  print("Enter a Valid Number Man")
                