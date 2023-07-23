MAX_LINES =3
MAX_BET = 1000
MIN_BET = 1

def validateInput(label, minVal=1, maxVal=10000):
    prefix = "$" if (label != "lines") else ""
    while True:
        value = input(f"Enter the {label} for betting" + f" [{prefix}{minVal} - {prefix}{maxVal}]" + f": {prefix}")
        if value.isdigit():
            value = int(value)
            if minVal <= value <= maxVal:
                print(f"{prefix}{value} accepted as {label}")
                return value
            else:
                print(f"{label} must between {minVal} and {maxVal}")
        else:
            print(f"{value} is not a valid input for {label}")


def deposit():
    '''collects deposits for later use'''
    depositAmount = validateInput("deposit amount", maxVal=MAX_BET)
    return depositAmount


def takebets(accountBalance):
    lines = validateInput("lines", maxVal=3)
    betPerLine = validateInput("bet amount", maxVal=accountBalance)
    betAmount = lines * betPerLine
    return betAmount

def main():
    balance = deposit()
    bet = takebets(balance)
    balance -= bet
    return 0


main()
