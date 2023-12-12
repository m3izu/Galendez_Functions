def find_smallest_factor(n):
    if n < 2:
        print("Invalid input. Enter a number greater than 2.")
        return

    for i in range(2, n):
        if n % i == 0:
            print(f"The smallest factor other than 1 for {n} is {i}.")
            return

    print(f"The smallest factor other than 1 for {n} is {n}.")


def is_prime(num):
    # Function to check if a number is prime
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def display_primes(start, end):
    # Function to display all prime numbers within a given range
    if start < 0:
        print("Enter a non-negative number.")
        return

    if end <= start:
        print("Enter a number greater than", start)
        return

    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")


if __name__ == "__main__":
    # Main program
    while True:
        print("Choose an option:")
        print("1. Find the smallest factor of a number.")
        print("2. Find prime numbers within a range.")
        print("0. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 0:
            print("Program terminated.")
            break
        elif choice == 1:
            user_input = int(input("Enter an integer >= 2: "))
            find_smallest_factor(user_input)
        elif choice == 2:
            start = int(input("Enter the start number: "))
            end = int(input("Enter the end number: "))
            display_primes(start, end)
        else:
            print("Invalid choice. Please enter 0, 1, or 2.")
