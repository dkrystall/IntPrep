#Question 9
# pythagorean triple a<b<c, total is equal to a+b+c
def findTriples(total):
    for a in range(1,total):
        if a == total-1:
            print("Number not found")
            searching = False
        for b in range(a,total):
            c=total-(a+b)
            if(c > b):
                aSquared, bSquared, cSquared  = a*a, b*b, c*c
                if (aSquared+bSquared == cSquared):
                        if a+b+c == total:
                            print(a,"+",b,"+",c,"=",total)
                            print("Answer found!")
                            print("Product of a,b,c is: ",a*b*c)
                            return a*b*c
findTriples(1000)