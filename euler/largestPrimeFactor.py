

def largesPrimeFactor(mysteryNumber):
    primeFactors = []
    for number in range(1, int((mysteryNumber/2+1))):
        if mysteryNumber % number == 0:
            for i in range(2, number):
                if(number % i == 0):
                    print("factor ", number, " is not prime")
                    break
            else:
                primeFactors.append(number)
                print(number, "is prime")
                print(primeFactors)
    primeFactors[-1]

#print(largesPrimeFactor(600851475143))


def largestPrimeFactor(mysteryNumber):
    print("Mystery Number is:", mysteryNumber)
    if mysteryNumber%2 is 0:    
        for i in range(2, int(mysteryNumber/2)):
            if mysteryNumber == i:
                continue
            if not mysteryNumber % i:
                return largestPrimeFactor(mysteryNumber / i)
        return mysteryNumber

    if mysteryNumber%2 is not 0:
        for i in range(2, int(mysteryNumber/2+1)):
            if mysteryNumber == i:
                print(i, mysteryNumber)
                continue
            if not mysteryNumber % i:
                print(i, mysteryNumber)
                return largestPrimeFactor(mysteryNumber / i)
        return mysteryNumber
        
print(largestPrimeFactor(600851475143))