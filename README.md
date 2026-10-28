# QA Automation test task (Python)

A console program that solves the algorithm part of the test task. Everything
is run from one interactive menu. The answers to the bracket sequence questions
are written below (Part 2).

## Requirements

Python 3.8 or newer. No external libraries are needed.

## How to run

```
python main.py
```

Then choose an option in the menu and enter the values in the console.

## Menu options

| Option | Task | Example input | Output |
|--------|------|---------------|--------|
| 1 | Number > 7 | `10` | `Hello` |
| 1 | Number > 7 | `7` | nothing to print (the condition is strict) |
| 2 | Name check | `John` | `Hello, John` |
| 2 | Name check | `Anna` | `There is no such name` |
| 3 | Multiples of 3 | `1 3 4 6 9 10` | `Multiples of 3: [3, 6, 9]` |

Notes:
- The name comparison is case-sensitive: `john` does not match `John`.
- Invalid input (letters instead of a number, etc.) shows an error message
  and the program keeps running.

## Part 2. Bracket sequence `[((())()(())]]`

### Question 1. Is this sequence correct?

**No.** Two things are wrong:

| Bracket | Opening | Closing | Problem |
|---------|---------|---------|---------|
| `(` `)` | 6 | 5 | one `(` is never closed |
| `[` `]` | 1 | 2 | one extra `]` |

How the stack check finds the error (reading left to right):

1. `[` is opened. Stack: `[`
2. `(((` are opened. Stack: `[ ( ( (`
3. `))` close two of them. Stack: `[ (`
4. `()` opens and closes. Stack: `[ (`
5. `(())` opens and closes. Stack: `[ (`
6. The first `]` arrives, but the top of the stack is `(`.
   `(` cannot be closed by `]`, so the sequence is **not correct**.

### Question 2. What needs to be changed to make it correct?

The smallest fix is to change **one character**. Two ways to do it:

**Option A. Replace the first `]` with `)`**

```
[((())()(())]]   ->   [((())()(()))]
```

The unclosed `(` gets its `)`, and the single remaining `]` closes `[`.

**Option B. Replace the first `(` with `[`**

```
[((())()(())]]   ->   [[(())()(())]]
```

Now there are two `[` for the two `]`, and the round brackets are balanced
(5 opening and 5 closing).

Both results are correct bracket sequences. (Other fixes with more than one
change also exist, for example deleting the first `(` and the last `]`.)
