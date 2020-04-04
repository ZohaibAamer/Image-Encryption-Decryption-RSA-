import prime
import calPublicKey
import calPrivateKey


def power(x,e,m):
    X = x
    E = e
    Y = 1
    while E > 0:
        if E % 2 == 0:
            X = (X * X) % m
            E = E/2
        else:
            Y = (X * Y) % m
            E = E - 1
    return Y
class rsa:
    def __init__(self):
        self.p,self.q=prime.gen_prime() #step 1 get prime numbers
        #step 2 cal n
        self.n=self.p*self.q
        #step 3 cal totient of n
        self.phi=(self.p-1)*(self.q-1)
        #step 4 cal public key e
        self.e=calPublicKey.cal(self.phi,self.n)
        #step 5 cal private key d
        self.d=calPrivateKey.cal(self.e,self.phi)

    def Cipher(self,x):
         return (power(x,self.e,self.n))
    def deCipher(self,x):
        return (power(x,self.d,self.n))