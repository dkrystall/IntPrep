def fibonacciSum(limit):
    fibStart = [1,2]
    limitBroken = False
    total = 0
    currentFib = 1
    while(not limitBroken):
        nextFib = fibStart[-1] + fibStart[-2]
        fibStart.append(nextFib)
        if fibStart[-1] > limit:
            limitBroken = True
    
    fibStart.remove(fibStart[-1])
    for fib in fibStart:
        if fib%2 == 0:
            total += fib
    print(fibStart)
    print("Fibonacci Even Values Total:", total)

fibonacciSum(4000000)
