import random as r

def zues(input1):
    test = 'rps'
    return test[input1]

def printWinner(a,b):
    if (player==comp):
        print("DRAW")
    #For Rock Case
    elif(player=='r' and comp=='p'):
        print("Computer Wins")
    elif(player=='r' and comp=='s'):
        print("Player Wins")
    #For Paper Case
    elif(player=='p' and comp=='r'):
        print("Player Wins")
    elif(player=='p' and comp=='s'):
        print("Computer Wins")
    #For Scissors Case
    elif(player=='s' and comp=='r'):
        print("Computer Wins")
    elif(player=='s' and comp=='p'):
        print("Player Wins")
    return

def toAsciiChar(a):
    if(a=='p'):
        return "|"
    if(a=='r'):
        return "O"
    if(a=='s'):
        return "8<"

player = input("Rock(r) , Paper (p) or Scissors (s) ")
player.lower()
comp = r.randint(0,2)  #comp means computer
comp = zues(comp)
print(toAsciiChar(player)," VS ",toAsciiChar(comp))
printWinner(player,comp)
