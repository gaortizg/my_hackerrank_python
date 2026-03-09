#############################################
# Define functions required for the program
#############################################
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

def get_valid_score(prompt: str) -> list[float]:
    """
    Prompts the user for a list of three positive float inputs (0.0 <= score <= 100.0) and validates it.
    The function will continue to prompt the user until a valid input is received.

    Args:
        prompt (str): The message displayed to the user when asking for input.

    Returns:
        list[float]: A list of three valid positive float inputs from the user.
    """
    while True:
        try:
            scores = list(map(float, input(prompt).strip().split()))

            # Validate only three scores are entered, all are floats, and all are between 0.0 and 100.0
            if len(scores) != 3:
                print("Invalid input. Please enter exactly 3 scores.")
                return get_valid_score(prompt)
            elif any(score < 0.0 or score > 100.0 for score in scores):
                print("Invalid input. Please enter positive floats between 0.0 and 100.0.")
                return get_valid_score(prompt)
            else:
                return scores
        except ValueError:
            print("Invalid input. Please enter valid float numbers.")
            continue    

#############################################
# Run the main program
#############################################
if __name__ == "__main__":
    n = get_valid_int("Enter the number of students: ")

    # Initialize students' marks dictionary and store information about students and their scores as key:value pairs
    student_marks: dict[str, list[float]] = {}
    for _ in range(n):
        name = input(f"Enter student name {(_ + 1)}: ").strip()
        scores = get_valid_score(f"Enter the scores of {name} (3 scores separated by space): ")
        student_marks[name] = scores

    # Ask for student name and check whether it exists.
    #   - If it exists, calculate the average score and print it.
    #   - If it doesn't exist, ask for a different name.
    while True:
        query_name = input("Enter the name of the student to calculate average score: ").strip()
        if query_name in student_marks:
            average_score = sum(student_marks[query_name]) / len(student_marks[query_name])
            print(f"Average score for {query_name}: {average_score:.2f}")
            break
        else:
            print(f"Student '{query_name}' not found.")
