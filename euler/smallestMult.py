""" 20 = 10,5,2
19
18 = 9,3
17
16 = 8,4
15 = 5,3
14 = 7,2
13
12 = 6,3,2
11  """
def smallest_multi(multi):
    SmallestNumber = multi
    check = 0
    while True:
        for i in range(2,multi+1):
            if SmallestNumber % i > 0:
                break
            check = i
        if check == multi:
            return SmallestNumber
        SmallestNumber += multi

            
print(smallest_multi(20))
