import utils
def withdraw():
    amount=int(input("Enter a amount to Deposit"))
    if amount<=utils.balance:
        utils.balance -=amount
        print(f" WIthdrawl of {amount} was Successfully")
        utils.statements.append(f"Withdraw: Rs.{amount}")
    else: print("Insufficient Balance Man") 
