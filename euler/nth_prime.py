primes = [0] #so nth prime can skip 0 index

#find primes up to n, ie: n = 100, primes within the range 1-100
def sieve_of_erathosthenes(n):
    is_prime = list(bytearray(n)) 
    for i in range(0,n):
        is_prime[i] = True
    j = 2
    while j*j < n:
        if is_prime[j] == True:
            k = j*j
            while k < n:
                is_prime[k] = False
                k += j
        j += 1
    l = 2
    while l < n:
        if(is_prime[l] == True):
            primes.append(l)
        l+=1

sieve_of_erathosthenes(1000000)

#returns the nth prime, ie 6 = 13
def find_nth_prime(n):
    return primes[n]

print(find_nth_prime(6))