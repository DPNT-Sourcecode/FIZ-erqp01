# noinspection PyUnusedLocal
import math

def fizz_buzz(number):
    mult3 = False
    mult5 = False
    result = ''
    res3 = (number % 3 ==0)
    res5 = (number % 5 ==0)
    snumber = str(number)
    in3 = '3' in snumber
    in5 = '5' in snumber
    #delx = (snumber == len(snumber) * snumber[0]) and (number > 10) #check for deluxe
    
    delx = False
    if (res3 and in3):
        delx = True
    if (res5 and in5):
        delx = True

    if (number % 2 ==0 ):   #check even/odd
        fdeluxe = 'deluxe'
    else:
        fdeluxe = 'fake deluxe'
    
    if (res3 or in3):
        mult3 = True
    if (res5 or in5):
        mult5 = True

    if (mult3):
        result = 'fizz'
    if (mult5):
        result = 'buzz'
    if (mult3 and mult5):
        result = 'fizz buzz'
    
    if (delx):
        if (result == ''):
            result = fdeluxe
        else:
            result = result + ' ' + fdeluxe
    
    if (result == ''):
        return(number)
    else:
        return(result)


