import random

MAX_LINES =3
MAX_BET = 1000
MIN_BET = 1
SHUFFLE_COLUMN = ['A', 'B', 'B', 'C', 'C', 'C', 'D', 'D', 'D', 'D']
WINNINGS = {
    "AAA": 3,
    "BBB": 2.5,
    "CCC": 2,
    "DDD": 1.5,
    "AA": 1.25,
    "BB": 1,
    "CC": 0.75,
    "DD": 0.5,
}

def validateInput(label, minVal=1, maxVal=10000, extra=""):
    prefix = "$" if (label != "lines") else ""
    while True:
        value = input(f"Enter the {label} for betting" + f" [{prefix}{minVal} - {prefix}{maxVal}]" + f"{extra}: {prefix}")
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
    '''Takes bets including number of lines to bet on and the amount bet on each of those lines'''
    lines = validateInput("lines", maxVal=3)
    maxBetPerLine = round((accountBalance/lines),2)
    betPerLine = validateInput("bet amount", maxVal=maxBetPerLine, extra="(per line | whole dollars only)")
    betAmount = lines * betPerLine
    accountBalance -= betAmount
    print(
        f'''
           Betting Invoice
        ---------------------
        Bet amount:     ${betPerLine}
        Lines selected: {lines}
        _____________________
        Total bet:      ${betAmount}
        Account Balance:${accountBalance}
        ''')
    return lines, betAmount, accountBalance

def printslots(matrix):
    flatmatrix = [elem for row in matrix for elem in row]
    a, b, c, d, e, f, g, h, i = flatmatrix
    print(f'''
╭───────────╮
│   SLOTS   │
│ ╭─╮╭─╮╭─╮ │
│ │{a}││{b}││{c}│ │
│ │{d}││{e}││{f}│ │
│ │{g}││{h}││{i}│ │
│ ╰─╯╰─╯╰─╯ │
╰───────────╯
''')

def shuffleSample(column):
    for i in range(random.randint(1, 10)):
        random.shuffle(column)
    col1 = random.sample(column * 3, 3)
    col2 = random.sample(column * 3, 3)
    col3 = random.sample(column * 3, 3)
    initMatrix = [col1, col2, col3]
    initMatrix = [list(row) for row in zip(*initMatrix)]
    return initMatrix

def run_slots():
    initColumn = SHUFFLE_COLUMN
    endMatrix = shuffleSample(initColumn)
    return endMatrix

def getResults(slots):
    print(slots)
    for i in range(2):
        for j in range(2):
            if slots[i][j] != slots[i][j+1]:
                slots[i][j] = '0'
    print(slots)
    newSlots = ["".join(row) for row in slots]
    # sortedSlots = ["".join(sorted(s)) for s in newSlots]
    # print(newSlots)
    winningSlots = []




def main():
    #balance = deposit()
    # lines, bet, balance = takebets(balance)
    slots = run_slots()
    printslots(slots)
    getResults(slots)



main()
