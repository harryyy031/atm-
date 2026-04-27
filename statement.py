import utils
def statement():
    if len(utils.statements)==0: print("No Statements Yet")
    else:
        print("<------Statements------>")
        for _ in utils.statements:
            print(_)
