"""QA Automation test task (Python).

Part 1: three small algorithms with interactive console input.
Part 2: bracket sequence checker (answers the questions from the task).
"""

BRACKET_PAIRS = {")": "(", "]": "[", "}": "{"}
OPENING = set(BRACKET_PAIRS.values())


# ---------- Part 1: algorithms ----------

def greet_by_number(number):
    """Return "Hello" if number > 7, otherwise None."""
    if number > 7:
        return "Hello"
    return None


def greet_by_name(name):
    """Return a greeting for "John", otherwise an error-like message."""
    if name == "John":
        return "Hello, John"
    return "There is no such name"


def multiples_of_three(numbers):
    """Return only the elements that are divisible by 3."""
    return [n for n in numbers if n % 3 == 0]


# ---------- Part 2: brackets ----------

def is_balanced(sequence):
    """Check that every bracket is closed by the same type, in the right order."""
    stack = []
    for ch in sequence:
        if ch in OPENING:
            stack.append(ch)
        elif ch in BRACKET_PAIRS:
            if not stack or stack.pop() != BRACKET_PAIRS[ch]:
                return False
    return not stack  # stack must be empty at the end


# ---------- Console interface ----------

def run_number():
    raw = input("Enter a number: ").strip()
    try:
        number = float(raw)
    except ValueError:
        print("Error: please enter a valid number.")
        return
    result = greet_by_number(number)
    print(result if result else "Number is not greater than 7, nothing to print.")


def run_name():
    name = input("Enter a name: ").strip()
    print(greet_by_name(name))


def run_array():
    raw = input("Enter numbers separated by spaces (e.g. 1 3 6 8 9): ").split()
    try:
        numbers = [int(x) for x in raw]
    except ValueError:
        print("Error: array must contain only integers.")
        return
    result = multiples_of_three(numbers)
    print("Multiples of 3:", result if result else "none")


def run_brackets():
    default = "[((())()(())]]"
    raw = input(f"Enter a bracket sequence (Enter = {default}): ").strip()
    sequence = raw or default
    if is_balanced(sequence):
        print(f"{sequence} -> correct")
    else:
        print(f"{sequence} -> NOT correct")


MENU = {
    "1": ("Number > 7", run_number),
    "2": ("Name check", run_name),
    "3": ("Multiples of 3 in array", run_array),
    "4": ("Bracket sequence check", run_brackets),
}


def main():
    while True:
        print("\n=== Menu ===")
        for key, (title, _) in MENU.items():
            print(f"{key}. {title}")
        print("0. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "0":
            print("Bye!")
            break
        if choice in MENU:
            MENU[choice][1]()
        else:
            print("Unknown option, try again.")


if __name__ == "__main__":
    main()
