# noinspection PyUnusedLocal
import math

def fizz_buzz(number):
    mult3 = False
    mult5 = False
    a = math.modf(number/3.0)
    b = math.modf(number/5.0)
    if (a[0]==0.0):
        mult3 = True
    if (b[0]==0.0):
        mult5 = True
    if (mult3 and mult5):
        return('fizz buzz')
    if (mult3):
        return('fizz')
    if (mult5):
        return('buzz')

    return(number)




