from math import *
import q1
import q2
import q4

def fibo(n):
    try:
        if n < 0:
            raise ValueError
        elif n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return fibo(n - 1) + fibo(n - 2)
    except Exception as e:
        q1.fib_log(e)

def isprime(n):
    try:
        assert isinstance(n,int)
        assert n >0
        testlist = [2] + list(range(3, floor(sqrt(n)) + 1, 2))
        for testnumber in testlist:
            if n % testnumber == 0:
                return False
        return True
    except :
        q2.prime_log()

def sum(a,b):
    try:
        assert isinstance(a,int) and isinstance(b,int)
        return a+b
    except:

        q4.log_stream()



sum("a",5)
# fibo("a")
# fibo(-3)
# isprime("a")
# isprime(-6)