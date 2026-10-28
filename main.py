"""QA Automation test task (Python).

The program has a simple console menu with three options:
  1. Number check    - prints "Hello" if the number is greater than 7
  2. Name check      - greets "John", otherwise says there is no such name
  3. Multiples of 3  - prints the elements of an array that are divisible by 3

The logic of every task lives in its own small function (top part of the file).
The console input/output lives in the functions below them. This keeps the
logic easy to read and easy to reuse.
"""


# ---------------------------------------------------------------------------
# Algorithms
# ---------------------------------------------------------------------------

def greet_by_number(number):
    """Task 1: if the number is greater than 7, return "Hello".

    The condition is strict: for exactly 7 nothing is returned (None).
    """
    if number > 7:
        return "Hello"
    return None


def greet_by_name(name):
    """Task 2: if the name is "John", return "Hello, John".

    For any other name return "There is no such name".
    The comparison is case-sensitive, so "john" does not match.
    """
    if name == "John":
        return "Hello, John"
    return "There is no such name"


def multiples_of_three(numbers):
    """Task 3: return only the elements that are divisible by 3.

    A number is a multiple of 3 when the remainder of dividing it by 3 is 0
    (n % 3 == 0). This also works for 0 and for negative numbers.
    """
    result = []
    for n in numbers:
        if n % 3 == 0:
            result.append(n)
    return result


# ---------------------------------------------------------------------------
# Console interface (reads user input and prints results)
# ---------------------------------------------------------------------------

def run_number():
    raw = input("Enter a number: ").strip()
    try:
        number = float(raw)  # float accepts both 8 and 7.5
    except ValueError:
        print("Error: please enter a valid number.")
        return
    result = greet_by_number(number)
    if result:
        print(result)
    else:
        print("The number is not greater than 7, nothing to print.")


def run_name():
    name = input("Enter a name: ").strip()
    print(greet_by_name(name))


def run_array():
    raw = input("Enter integers separated by spaces (e.g. 1 3 6 8 9): ").split()
    try:
        numbers = [int(x) for x in raw]
    except ValueError:
        print("Error: the array must contain only integers.")
        return
    result = multiples_of_three(numbers)
    if result:
        print("Multiples of 3:", result)
    else:
        print("There are no multiples of 3 in the array.")


# Menu: key -> (title, function that runs the task)
MENU = {
    "1": ("Number > 7", run_number),
    "2": ("Name check", run_name),
    "3": ("Multiples of 3 in an array", run_array),
}


def main():
    """Show the menu again and again until the user chooses 0."""
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
            MENU[choice][1]()  # call the function that belongs to this option
        else:
            print("Unknown option, try again.")


if __name__ == "__main__":
    main()
