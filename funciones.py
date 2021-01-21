import random

def generator():

    upper = 'abcdefghijklmnopqrstuvwxyz'
    lower = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '@#$%^&*_-'

    tout = upper + lower + numbers + symbols
    len = 16 
    password = "" .join(random.sample(tout,len))

    return password
