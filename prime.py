import random
import math


def check_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    z=int(math.sqrt(num))+2
    for i in range(3,z):
        if(num%i==0):
          return False
    return True

def gen_prime():
    p=0
    q=0
    while True:
        i=random.randint(10000,1000000)
        if check_prime(i):
            p=i
        if p!=0 and q!=0 and p!=q:
            break
        j=random.randint(20000,5000000)
        if check_prime(j):
            q=j
        if p!=0 and q!=0 and p!=q:
            break
    return p,q