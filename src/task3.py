def check_number(num):
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"

def first_ten_primes():
    primes = []
    num = 2
    while len(primes) < 10:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
        num += 1
    return primes

def sum_1_to_100():
    return sum(range(1, 101))
