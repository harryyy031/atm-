import utils
def deposit():
    amount=int(input("Enter a amount to Deposit"))
    if amount>0:
        utils.balance +=amount
        print(f"{amount} Deposited Successfully")
        utils.statements.append(f"Deposit:  Rs.{amount}")
    else: print("Enter a valid amount Buddy") 
