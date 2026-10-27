# QA Automation test task (Python)

## Requirements
Python 3.8+ (no external libraries).

## Run the program
```
python main.py
```
Choose an option from the console menu and enter values.


## Part 2: bracket sequence `[((())()(())]]`
1. Is it correct? **No.**
   - Opening `(`: 6, closing `)`: 5 -> one `(` is never closed.
   - Opening `[`: 1, closing `]`: 2 -> one extra `]`.
   - The first `]` arrives while the top of the stack is `(`, so the types do not match.
2. How to fix it: replace the first `]` with `)`:
   `[((())()(())]]` -> `[((())()(()))]` (a single change).
   Alternative: add `)` before the first `]` and delete the last `]`.
