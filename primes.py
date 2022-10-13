
def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("Input value must be positive.")
    list = []
    num = 2
    while len(list) < number_of_primes:
        if is_prime(num):
            list.append(num)
        num += 1

    return list


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
