def square_it_out(start, end):

    numbers = list(range(start, end + 1))

    squares = [num ** 2 for num in numbers]

    even_squares = [sq for sq in squares if sq % 2 == 0]
    odd_squares = [sq for sq in squares if sq % 2 != 0]

    print(f"Original numbers: {numbers}")
    print(f"Squares: {squares}")
    print(f"Even squares: {even_squares}")
    print(f"Odd squares: {odd_squares}")

square_it_out(1, 10)
