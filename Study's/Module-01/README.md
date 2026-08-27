# Module-01 — Fundamentals

Exercise list for this module: `print()`, variables, and data types. Solve each one in its own file following the naming convention `NN-descriptive-name.py`.

Each exercise below is solvable with what's introduced up to that point. New commands are explained the first time they show up — after that, you're expected to already know them.

---

## Exercises

**01 — hello**
Print `"Hello, world!"` to the console.
> 💡 New command: `print()` — outputs text (or any value) to the console. Anything inside the parentheses gets displayed.

**02 — hello-name**
Store your name in a variable and print a greeting using it, like `"Hello, John!"`.
> 💡 New concept: **variables** — a name that holds a value, created with `name = value`. No need to declare a type; Python infers it.

**03 — multi-print**
Print three different lines of text using three separate `print()` calls.

**04 — string-concat**
Create two string variables (first name, last name) and print them combined into a full name using `+`.
> 💡 New concept: **string concatenation** — joining strings with `+`. Both sides must be strings, or Python raises an error.

**05 — f-string-intro**
Repeat exercise 04, but use an f-string instead of `+`.
> 💡 New syntax: **f-strings** — `f"Hello, {name}"`. Anything inside `{}` is evaluated and inserted into the string. Cleaner than concatenation.

**06 — int-vs-float**
Create one integer variable and one float variable, print both along with their type using `type()`.
> 💡 New command: `type()` — returns the data type of a value (`int`, `float`, `str`, `bool`, etc).

**07 — basic-math**
Create two number variables and print the result of adding, subtracting, multiplying, and dividing them.

**08 — division-types**
Divide two integers using `/` and then using `//`. Print both results and explain the difference in a comment.
> 💡 New operator: `//` — floor division, discards the decimal part. `7 / 2` is `3.5`, `7 // 2` is `3`.

**09 — modulo-intro**
Print the remainder of dividing two numbers.
> 💡 New operator: `%` (modulo) — returns the remainder of a division. `7 % 2` is `1`.

**10 — total-pay**
Given `hours_worked` and `hourly_rate` variables, calculate and print the total pay.

**11 — input-basics**
Ask the user for their name using `input()` and print a greeting with it.
> 💡 New command: `input()` — pauses execution and waits for the user to type something, always returns a `str`.

**12 — input-number**
Ask the user for two numbers (as text) and print their sum. Watch out — `input()` always returns text.
> 💡 New command: `int()` — converts a value into an integer. Needed because `input()` returns a string, not a number. There's also `float()` for decimals.

**13 — celsius-to-fahrenheit**
Ask the user for a Celsius temperature and convert it to Fahrenheit (`F = C * 9/5 + 32`).

**14 — boolean-intro**
Create two boolean variables and print them, along with the result of combining them with `and` and `or`.
> 💡 New type: `bool` — `True` or `False`. `and`/`or` combine boolean expressions.

**15 — comparisons**
Create two number variables and print the result of comparing them with `==`, `!=`, `>`, `<`.

**16 — string-length**
Ask the user for a word and print how many characters it has.
> 💡 New command: `len()` — returns the length of a string, list, or other collection.

**17 — string-upper-lower**
Take a string and print an uppercase and a lowercase version of it.
> 💡 New methods: `.upper()` and `.lower()` — return a modified copy of a string. The original string is unchanged.

**18 — string-slicing**
Given a word, print just the first 3 characters and just the last 3 characters.
> 💡 New syntax: **slicing** — `text[start:end]` extracts part of a string (or list). `text[:3]` means "from the start to index 3". `text[-3:]` means "the last 3 characters".

**19 — string-index**
Print the character at a specific position of a string (e.g. the 4th letter).
> 💡 New concept: **indexing** — `text[0]` is the first character. Python is zero-indexed.

**20 — string-replace**
Take a sentence and replace one word with another, then print the result.
> 💡 New command: `.replace(old, new)` — returns a copy of the string with all occurrences of `old` swapped for `new`.

**21 — string-strip**
Ask the user for input with extra spaces around it (e.g. `"  hello  "`) and print it cleaned up.
> 💡 New command: `.strip()` — removes leading/trailing whitespace (or specified characters) from a string.

**22 — string-split**
Given a full name as one string, split it into first and last name and print them separately.
> 💡 New command: `.split()` — breaks a string into a list of pieces, using whitespace (or a given separator) as the delimiter. Returns a list.

**23 — string-join**
Given a list of words, join them into a single sentence separated by spaces.
> 💡 New command: `" ".join(list)` — the reverse of `.split()`. Joins a list of strings into one string, using the string before `.join` as the separator.

**24 — multiple-assignment**
Assign three variables in a single line (e.g. `a, b, c = 1, 2, 3`) and print them.

**25 — swap-variables**
Given two variables, swap their values without using a third temporary variable.

**26 — round-numbers**
Ask for a float and print it rounded to 2 decimal places.
> 💡 New command: `round(value, digits)` — rounds a number to the given number of decimal places.

**27 — abs-value**
Ask for a number and print its absolute value.
> 💡 New command: `abs()` — returns the absolute (non-negative) value of a number.

**28 — const-naming**
Create three variables that represent constants (e.g. `PI`, `MAX_USERS`) following Python's naming convention for constants, and print them.
> 💡 New convention: Python has no true constants, but by convention names meant to never change are written in `ALL_CAPS`.

**29 — comment-practice**
Take any earlier exercise and add a `#` comment above each line explaining what it does.
> 💡 New syntax: `#` starts a comment — ignored by Python, used to explain code to humans.

**30 — mini-receipt**
Given `item_name`, `item_price`, and `quantity` variables, print a small formatted receipt showing the item, quantity, unit price, and total (price × quantity), using an f-string.

**31 — bmi-calculator**
Ask the user for weight (kg) and height (m), calculate BMI (`weight / height ** 2`), and print the result rounded to 1 decimal place.
> 💡 New operator: `**` — exponentiation. `height ** 2` means height squared.

**32 — variable-type-juggling**
Create a variable holding a number as a string (e.g. `"42"`), convert it to `int`, do math with it, then convert the result back to `str` and print it concatenated with text.
> 💡 New command: `str()` — converts a value into a string. Useful when concatenating numbers with text using `+`.

---

## Notes

- Solve exercises in order — later ones assume you're comfortable with commands introduced earlier.
- If a command isn't explained here, it was introduced in an earlier exercise — scroll up.
- Challenges for this module (extra problems, not part of this core list) live in [`challenges/`](./challenges/).
