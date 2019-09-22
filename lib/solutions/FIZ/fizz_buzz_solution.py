# noinspection PyUnusedLocal
import math

def fizz_buzz(number):
    mult3 = False
    mult5 = False
    res3 = math.modf(number/3.0)
    res5 = math.modf(number/5.0)
    in3 = '3' in number
    in5 = '5' in number
    if (res3[0]==0.0 or in3):
        mult3 = True
    if (res5[0]==0.0 or in5):
        mult5 = True
    if (mult3 and mult5):
        return('fizz buzz')
    if (mult3):
        return('fizz')
    if (mult5):
        return('buzz')

    return(number)

r1 = fizz_buzz(3)
r2 = fizz_buzz(31)
r3 = fizz_buzz(5)

