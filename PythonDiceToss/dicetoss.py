from random import randint
randomedvalue = randint(1,6)
print("----------")
if(randomedvalue == 1):
    print("|        |")
    print("|    *   |")
    print("|        |")
elif(randomedvalue == 2):
    print("|        |")
    print("|  *  *  |")
    print("|        |")
elif(randomedvalue == 3):
    print("|  *     |")
    print("|  *     |")
    print("|  *     |")
elif(randomedvalue == 4):
    print("|  *  *  |")
    print("|        |")
    print("|  *  *  |")
elif(randomedvalue == 5):
    print("|  *  *  |")
    print("|  *  *  |")
    print("|  *     |")
elif(randomedvalue == 6):
    print("|  *  *  |")
    print("|  *  *  |")
    print("|  *  *  |")
else:
    print("|        |")
    print("|        |")
    print("|        |")
print("----------")
