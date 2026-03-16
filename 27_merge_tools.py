#############################################
# Define functions required for the program
#############################################
def merge_the_tools(word: str, k: int) -> None:
    """
    Implementation of Merge the Tools challenge
    https://www.hackerrank.com/challenges/merge-the-tools/problem

    Parameters:
    ----------
        word: str
            String to be used
        k: int
            Length of each substring
    
    Returns: None
        Print each subsequence on a new line. There will be len(word)/k of them 
    """
    for i in range(0, len(word), k):
        substring = word[i:i+k]

        seen: set = set()
        result: list = []

        for c in substring:
            if c not in seen:
                seen.add(c)
                result.append(c)

        print("".join(result))

#############################################
# Run the main program
#############################################
if __name__ == "__main__":
    # Validate string length
    while True:
        try:
            S = input("Enter String: ").strip()
            if  not (1 <= len(S) <= 10**4) or any (c.isspace() for c in S):
                raise ValueError
            
            k = int(input("Enter length of substring: ").strip())
            if  k < 1 or len(S) % k != 0:
                raise ValueError
        
            break
        except ValueError:
            print("Invalid input. Please enter a string with no spaces and length [1, 10**4], and a valid integer k that divides the string length.")
    
    # Run merge_the_tools routine
    merge_the_tools(S, k)