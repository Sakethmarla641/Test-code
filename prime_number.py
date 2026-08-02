def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def primes_up_to(limit):
    for num in range(2, limit + 1):
        if is_prime(num):
            yield num


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate prime numbers up to a limit.")
    parser.add_argument("limit", type=int, nargs="?", default=100, help="Maximum number to check for primes.")
    args = parser.parse_args()

    for prime in primes_up_to(args.limit):
        print(prime)
