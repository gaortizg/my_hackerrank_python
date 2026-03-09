#############################################
# Define functions required for the program
#############################################
def get_valid_int(prompt: str) -> int:
    """
    Prompts the user for a positive integer input (1 <= n) and validates it.
    The function will continue to prompt the user until a valid input is received.

    Args:
        prompt (str): The message displayed to the user when asking for input.

    Returns:
        int: A valid positive integer input from the user.
    """
    while True:
        try:
            value = int(input(prompt).strip())
            if value > 0:
                return value
        except ValueError:
            pass
        
        print("Invalid input. Please enter a positive integer.")


def handle_command(action: str, my_list: list[int]) -> None:
    parts = action.split()
    command = parts[0]
    args = list(map(int, parts[1:]))

    commands = {
        "insert": lambda: my_list.insert(*args),
        "print": lambda: print(my_list),
        "remove": lambda: my_list.remove(*args),
        "append": lambda: my_list.append(*args),
        "sort": lambda: my_list.sort(),
        "pop": lambda: my_list.pop(),
        "reverse": lambda: my_list.reverse()
    }

    try:
        commands[command]()
    except (KeyError, TypeError, ValueError):
        print("Invalid command or No. of arguments. Skipping this command and moving on to the next one.")


#############################################
# Run the main program
#############################################
if __name__ == "__main__":
    n = get_valid_int("Enter the number of commands to follow: ")
    my_list: list[int] = []

    for _ in range(n):
        handle_command(input(f"Enter command {(_ + 1)}: ").strip().lower(), my_list)