if __name__ == "__main__":
    # Validate input for 'a' and 'b' (0 < a,b < 10**10)
    while True:
        try:
            a = int(input("Enter integer a: ").strip())
            b = int(input("Enter integer b: ").strip())
            if b == 0:
                print("Invalid input. b cannot be zero. Please enter a non-zero integer for b.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter integers only.")
            continue

    # Perform division operations and print results
    print(f"a // b = {a // b}")
    print(f"a / b = {a / b}")