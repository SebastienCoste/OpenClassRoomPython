# -*-coding:Latin-1 -*
import random as r
import math as m


def getEarnings(bet, valueBet, realValue):
    if valueBet == realValue:
        return bet * 3
    if valueBet%2 == realValue%2:
        return m.ceil(bet / 2)
    return 0

if __name__ == "__main__":
    hasToChoose = True;
    while hasToChoose:
        numberStr = input("number of the bet ? 0-49\n")
        try:
            number = int(numberStr)
            assert number >= 0 and number <50
        except ValueError:
            print ("input is not a number")
        except AssertionError:
            print ("Choose a number between 0 and 49")
        else: hasToChoose = False;  
        
    hasToChoose = True;
    while hasToChoose:        
        amountStr = input("amount bet?\n")
        try:
            amount = int(amountStr)
            assert amount > 0
        except ValueError:
            print ("input is not a number")
        except AssertionError:
            print ("Bet something more than 0")
        else: hasToChoose = False;  
    
    grabed = r.randrange(50)
    print("Number picked up:", grabed);
    earnings = getEarnings(amount, number, grabed)
    if earnings > 0:
        print ("you earned:", earnings)
    else:
        print("you lost")




