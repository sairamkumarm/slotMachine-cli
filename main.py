def deposit():
    '''collects deposits for later use'''
    while(True):
        amount = input("Enter a deposit amount: $")
        if amount.isdigit() :
            amount = int(amount)
            return amount
        else:
            print(f"{amount} not valid")
deposit()