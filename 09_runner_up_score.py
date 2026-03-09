def get_valid_int(prompt: str) -> int:
    """
    Prompts the user for a positive integer input (2 <= n <= 10) and validates it. The function will continue to prompt the user until a valid input is received.

    Args:
        prompt (str): The message displayed to the user when asking for input.

    Returns:
        int: A valid positive integer input from the user.
    """
    while True:
        try:
            value = int(input(prompt).strip())
            if value < 2 or value > 10:
                print("Invalid input. Please enter a positive integer between 2 and 10.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter an integer between 2 and 10.")

def get_valid_scores(prompt: str, n: int) -> list:
    """
    Prompts the user for a list of positive integers and validates each one. The function will continue to prompt the user until all inputs are valid.

    Args:
        prompt (str): The message displayed to the user when asking for input.
        n (int): The number of scores to expect.

    Returns:
        list: A list of valid positive integers input from the user.
    """
    while True:
        try:
            scores = list(map(int, input(prompt).strip().split()))
            if len(scores) != n:
                print(f"Invalid input. Please enter exactly {n} scores.")
                continue
            if any(score < -100 or score > 100 for score in scores):
                print("Invalid input. Please enter scores between -100 and 100.")
                continue
            return scores
        except ValueError:
            print("Invalid input. Please enter integers only.")

if __name__ == "__main__":
    n = get_valid_int("Enter the number of scores n: ")
    sorted_unique_scores = sorted(set(get_valid_scores(f"Enter {n} scores for list A (space-separated): ", n)), reverse=True)

    if len(sorted_unique_scores) < 2:
        print("Not enough unique scores to determine the second highest.")
    else:
        print(f"Runner-up score: {sorted_unique_scores[1]}")
    
    