#!/usr/bin/env python3

import math

def Eratosthenes(n):
    prime = gen_eratosthenes()
    
    if (n < 3):
        print("There are no prime numbers smaller than that!")
    else:
        result = [next(prime) for _ in range(n)]
        return [i for i in result if i < n]
    
def gen_eratosthenes():
    prime = 2
    
    while True:
        yield prime
        x = prime + 1
        i = 2
        x_is_not_prime = True
        while x_is_not_prime:
            while(i < math.sqrt(x)):
                if(x%i == 0):
                    x += 1
                    x_is_not_prime = True
                    break
                else:
                    x_is_not_prime = False
                i += 1
            if(x == 2 or x == 3):
                x_is_not_prime = False
            elif(x == 4):
                x += 1
        prime = x
                