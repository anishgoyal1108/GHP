def count_trailing_zeroes(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count

def find_factorial_with_40_zeroes():
    n = 1
    while True:
        zeroes = count_trailing_zeroes(n)
        if zeroes == 40:
            print("n =", n)
        elif zeroes > 40:
            break
        n += 1

find_factorial_with_40_zeroes()