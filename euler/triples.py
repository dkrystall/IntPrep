def findTriples(total):
    searching = True
    while searching:

        for a in range(1,total):
            if a is total-1:
                print("Number not found")
                searching = False
            for b in range(a,total):
                if not searching:
                    break
                for c in range(b, total):
                    aSquared = a*a
                    bSquared = b*b
                    cSquared = c*c
                    #print("a is:", a," b is:",b," c is", c)
                    if (aSquared+bSquared == cSquared):
                            print(a,b,c)
                            print((a*a),"+",(b*b),"=",(c*c))
                            if a+b+c == total:
                                print(a,"+",b,"+",c,"=",total)
                                print("Answer found!")
                                print("Product of a,b,c is: ",a*b*c)
                                searching = False
                                if not searching:
                                    break

findTriples(1000)
