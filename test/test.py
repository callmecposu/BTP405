def isPrime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def getPrimeNumbers(n):
    primes = [x for x in range(2,n+1) if isPrime(x)]
    return primes

print(getPrimeNumbers(10))