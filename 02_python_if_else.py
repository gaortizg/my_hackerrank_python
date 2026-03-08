if __name__ == "__main__":
    # Validate input for n (it has to be an integer between [1,100])
    while True:
        try:
            n = int(input("Enter integer between 1 and 100: ").strip())
            if n < 1 or n > 100:
                print("Invalid input. Please enter an integer between 1 and 100: ")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 100: ")
            continue
    
    # Check conditions of challenge and print result
    if (n % 2 == 1) or (n in range(6,21)):
        print("Weird")
    else:
        print("Not Weird")
