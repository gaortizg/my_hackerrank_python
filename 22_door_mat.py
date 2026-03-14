#############################################
# Run the main program
#############################################
if __name__ == "__main__":
    # Validate dimensions of door mat (N, M)
    while True:
        try:
            N, M = map(int, input("Enter the height (N) and width (M) of the door mat: ").strip().split())
            if N < 5 or N > 101 or N % 2 == 0:
                print("Please enter an odd integer for the heigth N between 5 and 101.")
                continue

            if M < 15 or M > 303 or M / N != 3:
                print("Please enter a valid widht M (M = 3 * N).")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # routine to print door mat

    # ========================
    # Short version with list comrpehension
    # ========================
    print(
        "\n".join(
            ("WELCOME" if i == N // 2 else (".|." * (2 * (i if i < N // 2 else N - i - 1)+1))).center(M, "-")
             for i in range(N)
        )
    )

    # ========================
    # Long version with for loops
    # ========================
    # for i in range(1, N, 2):
    #     print((".|." * i).center(M, "-"))
    
    # print("WELCOME".center(M, "-"))

    # for i in range(N - 2, -1, -2):
    #     print((".|." * i).center(M, "-"))