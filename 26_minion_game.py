#############################################
# Define functions required for the program
#############################################
def minion_game(word: str) -> None:
    """
    Implementation of the Minion Game
    https://www.hackerrank.com/challenges/the-minion-game/problem

    Parameters:
    ----------
        word: str
            String to be used in the game
    
    Returns: None
        Prints the winner's name and score, separated by a space on one line,
        or Draw if there is no winner
    """
    vowels: str = "AEIOU"
    kevin_score: int = sum(len(word) - i for i, c in enumerate(word) if c in vowels)
    stuart_score: int = sum(len(word) - i for i, c in enumerate(word) if c not in vowels)
    
    print("Kevin", kevin_score) if kevin_score > stuart_score else print("Stuart", stuart_score) if stuart_score > kevin_score else print("Draw")


#############################################
# Run the main program
#############################################
if __name__ == "__main__":
    # Validate string length
    while True:
        try:
            S = input("Enter String: ").strip()
            if  1 <= len(S) <= 10e6 and S.isalpha() and S.isupper():
                break
        except ValueError:
            pass
        print("Invalid input. Please only enter one string with uppercase letters, no spaces, and length between [1, 10**6].")
    
    # Minion Game routine
    minion_game(S)