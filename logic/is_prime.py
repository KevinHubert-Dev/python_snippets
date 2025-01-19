# %%
def primes_below(number):
    """
    Calculate the number of prime numbers below a given number.

    This function iterates through all numbers from 2 up to (but not including) the specified number,
    checks if each number is prime, and counts how many prime numbers are found.

    Args:
        number (int): The upper limit (exclusive) to check for prime numbers.

    Returns:
        int: The count of prime numbers below the specified number.

    Example:
        >>> primes_below(10)
        4
        # Primes below 10 are 2, 3, 5, and 7
    """
    primes = []
    for num in range(2, number):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
        if is_prime:
            primes.append(num)
    return len(primes)

# %%

if __name__ == "__main__":
    number = 100
    print(f"Number of primes below {number}: {primes_below(number)}")

# %%

# 1.) Chat with AI about the speed of the code
# 2.) Provide more infos to AI to improve the code 
# 3.) Let us use AI to call the code via the server.py script
# 4.) Let us generate tests in test_is_prime.py
# 4.1.) Ask AI how to execute the tests