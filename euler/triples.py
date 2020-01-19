#Question 9
def findTriples(total):
    searching = True
    while searching:
        for a in range(1,total):
            if not searching:
                break
            if a == total-1:
                print("Number not found")
                searching = False
            for b in range(a,total):
                if not searching:
                    break
                c=total-(a+b)
                if(c > b):
                    aSquared, bSquared, cSquared  = a*a, b*b, c*c
                    if (aSquared+bSquared == cSquared):
                            if a+b+c == total:
                                print(a,"+",b,"+",c,"=",total)
                                print("Answer found!")
                                print("Product of a,b,c is: ",a*b*c)
                                searching = False
                                if not searching:
                                    break
findTriples(1000)