def largest_palindrome(digits):
    largest = 0
    for i in range((10**(digits-1)),(10**digits)):
        for j in range(i,(10**digits)):
            current = i*j
            if (len(str(current))%2 == 0):
                #print(current," we got an even")
                stringify = [str(current)[i:i+(len(str(current)))//2] for i in range(0, len(str(current)), len(str(current))//2)]
                if(stringify[0] == stringify[1][::-1]):
                    if current > largest: largest = current
    print("Ladies and gentlement, we gotem: ",largest)
largest_palindrome(4)