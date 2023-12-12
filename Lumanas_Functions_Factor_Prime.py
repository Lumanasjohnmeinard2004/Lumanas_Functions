def smallest_factor(n):
    "Find the smallest factor of n."""
    if n < 2:
        return None  # No smallest factor for numbers less than 2
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    return n  # n is a prime number

def prime_numbers_in_range(start, end):
    "Find and print prime numbers in the specified range."
    primes = []
    for num in range(start, end + 1):
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


while True:
    print("Menu:")
    print("1. Find the smallest factor of n")
    print("2. Find prime numbers in a range")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 0:
        print("Program terminated.")
        break
    elif choice == 1:
        n = int(input("Enter a number (n): "))
        result = smallest_factor(n)
        print(f"The smallest factor of {n} is: {result}")
    elif choice == 2:
        start = int(input("Enter the starting number: "))
        end = int(input("Enter the ending number: "))
        result = prime_numbers_in_range(start, end)
        print(f"Prime numbers between {start} and {end}: {result}")
    else:
        print("Invalid choice. Please enter 0, 1, or 2.")
