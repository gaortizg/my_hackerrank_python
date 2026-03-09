#############################################
# Run the main program
#############################################
if __name__ == "__main__":
    # Validate logo t input
    while True:
        try:
            t = int(input("Enter the t of the logo: "))
            if t < 0 or t >= 50 or t % 2 == 0:
                print("Please enter an odd integer between 0 and 49.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    

    c = 'H'

    # Top Cone
    for i in range(t):
        print((c*i).rjust(t-1) + c + (c*i).ljust(t-1))

    # Top Pillars
    for i in range(t+1):
        print((c*t).center(t*2) + (c*t).center(t*4))

    # Middle Belt
    for i in range((t+1)//2):
        print((c*t*5).center(t*6))

    # Bottom Pillars
    for i in range(t+1):
        print((c*t).center(t*2) + (c*t).center(t*4))

    # Bottom Cone
    for i in range(t):
        print(((c*(t-i-1)).rjust(t) + c + (c*(t-i-1)).ljust(t)).rjust(t*5))