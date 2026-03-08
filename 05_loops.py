if __name__ == "__main__":
    # Validate input for 'n'(1 <= n <= 20)
    while True:
        try:
            n = int(input("Enter integer n (1-20): ").strip())
            if n < 1 or n > 20:
                print("Invalid input. Please enter an integer between 1 and 20.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 20.")
            continue

    # Print squares of integers from 0 to n-1
    for i in range(n):
        print(i**2)