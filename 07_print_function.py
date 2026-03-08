if __name__ == "__main__":
    # Validate input for 'n'(1 <= n <= 150)
    while True:
        try:
            n = int(input("Enter integer n (1-150): ").strip())
            if n < 1 or n > 150:
                print("Invalid input. Please enter an integer between 1 and 150.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 150`.")
            continue

    # Print list of integers from 1 through n as  a string
    my_str = ''.join(str(i) for i in range(1, n+1))
    print(my_str)