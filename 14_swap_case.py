#############################################
# Run the main program
#############################################
if __name__ == "__main__":
    while True:
        try:
            s = input("Enter a string: ")
            if len(s) > 0 and len(s) <= 1000:
                print(s.swapcase())  
                break
        except ValueError:
            pass
        print("Invalid input. Please enter a string with 1 to 1000 characters.")
      