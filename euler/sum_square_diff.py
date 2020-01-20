def difference_sum_of_squares(limit):
    sum_of_square = 0
    square_of_sums = 0

    for i in range(1,limit+1):
        square_of_sums += i
        sum_of_square += i*i
        print(i)
        print(i*i)
    square_of_sums = square_of_sums*square_of_sums
    return (square_of_sums - sum_of_square)
print(difference_sum_of_squares(100))