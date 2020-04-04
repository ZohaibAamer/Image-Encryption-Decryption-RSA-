import prime

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def cal(k,n):
    for i in range (2,k+1):
        if(gcd(i,k)==1):
           if(prime.check_prime(i) and n%i != 0):
                return i