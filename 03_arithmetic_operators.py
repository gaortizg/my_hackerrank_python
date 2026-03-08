if __name__ == "__main__":
    # Validate input for 'a' and 'b' (0 < a,b < 10**10)
    while True:
        try:
            a = int(input("Enter integer a: ").strip())
            b = int(input("Enter integer b: ").strip())
            if a <= 0 or b <= 0 or a >= 10**10 or b >= 10**10:
                print("Invalid input. Please enter integers between 1 and 10**10: ")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter integers between 1 and 10**10: ")
            continue

    # Perform arithmetic operations and print results
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")