# Module-01 — Fundamentals

Exercise list for this module: `print()`, variables, data types, arithmetic operators, `input()`, and booleans.

**Not covered yet in this module:** `if`/`else`, `for`/`while`, lists/arrays, string methods (`split`, `replace`, etc). Those come later — every exercise here is solvable with just print, variables, math, and basic type conversion.

Solve each one in its own file following the naming convention:

```
NN-descriptive-name.py
```

Each exercise is solvable with what's introduced up to that point. New commands are explained **the first time they show up** — after that, you're expected to already know them. If a command isn't explained where you're at, scroll up — it was introduced earlier.

Challenges for this module (extra problems, separate from this list) live in [`challenges/`](./challenges/).

---

## 01 — hello

Print `"Hello, world!"` to the console.

```python
print("Hello, world!")
```

> 💡 **New command:** `print()` — outputs text (or any value) to the console. Anything inside the parentheses gets displayed.

---

## 02 — hello-name

Store your name in a variable and print a greeting using it, like `"Hello, John!"`.

> 💡 **New concept:** variables — a name that holds a value, created with `name = value`. No need to declare a type; Python infers it.

---

## 03 — multi-print

Print three different lines of text using three separate `print()` calls.

---

## 04 — string-concat

Create two string variables (first name, last name) and print them combined into a full name using `+`.

> 💡 **New concept:** string concatenation — joining strings with `+`. Both sides must be strings, or Python raises an error.

---

## 05 — f-string-intro

Repeat exercise 04, but use an f-string instead of `+`.

```python
name = "John"
print(f"Hello, {name}!")
```

> 💡 **New syntax:** f-strings — `f"Hello, {name}"`. Anything inside `{}` is evaluated and inserted into the string. Cleaner than concatenation.

---

## 06 — int-vs-float

Create one integer variable and one float variable, print both along with their type using `type()`.

> 💡 **New command:** `type()` — returns the data type of a value (`int`, `float`, `str`, `bool`, etc).

---

## 07 — basic-math

Create two number variables and print the result of adding, subtracting, multiplying, and dividing them.

---

## 08 — division-types

Divide two integers using `/` and then using `//`. Print both results and explain the difference in a comment.

> 💡 **New operator:** `//` — floor division, discards the decimal part. `7 / 2` is `3.5`, `7 // 2` is `3`.

---

## 09 — modulo-intro

Print the remainder of dividing two numbers.

> 💡 **New operator:** `%` (modulo) — returns the remainder of a division. `7 % 2` is `1`.

---

## 10 — total-pay

Given `hours_worked` and `hourly_rate` variables, calculate and print the total pay.

---

## 11 — input-basics

Ask the user for their name using `input()` and print a greeting with it.

> 💡 **New command:** `input()` — pauses execution and waits for the user to type something, always returns a `str`.

---

## 12 — input-number

Ask the user for two numbers (as text) and print their sum. Watch out — `input()` always returns text.

> 💡 **New command:** `int()` — converts a value into an integer. Needed because `input()` returns a string, not a number. There's also `float()` for decimals.

---

## 13 — celsius-to-fahrenheit

Ask the user for a Celsius temperature and convert it to Fahrenheit.

```python
F = C * 9/5 + 32
```

---

## 14 — boolean-intro

Create two boolean variables and print them, along with the result of combining them with `and` and `or`.

> 💡 **New type:** `bool` — `True` or `False`. `and` / `or` combine boolean expressions.

---

## 15 — comparisons

Create two number variables and print the result of comparing them with `==`, `!=`, `>`, `<`.

---

## 16 — rectangle-area

Given `width` and `height` variables, calculate and print the area of a rectangle.

---

## 17 — circle-area

Given a `radius` variable, calculate and print the area of a circle. Use `3.14159` for pi (no imports yet).

```python
area = 3.14159 * radius * radius
```

---

## 18 — average-of-three

Create three number variables and print their average.

---

## 19 — input-float

Ask the user for a product price (as text) and print it converted to a `float`, along with its `type()`.

---

## 20 — temperature-range

Given two temperature variables (`today` and `yesterday`), print whether today is warmer using a comparison (`>`), without an `if` — just print the boolean result directly.

---

## 21 — is-adult

Ask the user for their age (converted to `int`) and print the result of comparing it to `18` using `>=` — just the boolean, no `if` yet.

---

## 22 — string-vs-number

Create a variable holding `"5"` (as text) and another holding `5` (as a number). Print both, then print the result of comparing them with `==`. Explain in a comment why the result is what it is.

---

## 23 — combined-conversion

Ask the user for two numbers as text, convert both to `float`, and print their sum, difference, and product.

---

## 24 — multiple-assignment

Assign three variables in a single line and print them.

```python
a, b, c = 1, 2, 3
```

---

## 25 — simple-interest

Given `principal`, `rate`, and `time` variables, calculate simple interest.

```python
interest = principal * rate * time
```

---

## 26 — round-numbers

Ask for a float and print it rounded to 2 decimal places.

> 💡 **New command:** `round(value, digits)` — rounds a number to the given number of decimal places.

---

## 27 — abs-value

Ask for a number and print its absolute value.

> 💡 **New command:** `abs()` — returns the absolute (non-negative) value of a number.

---

## 28 — const-naming

Create three variables that represent constants (e.g. `PI`, `MAX_USERS`) following Python's naming convention for constants, and print them.

> 💡 **New convention:** Python has no true constants, but by convention names meant to never change are written in `ALL_CAPS`.

---

## 29 — comment-practice

Take any earlier exercise and add a `#` comment above each line explaining what it does.

> 💡 **New syntax:** `#` starts a comment — ignored by Python, used to explain code to humans.

---

## 30 — mini-receipt

Given `item_name`, `item_price`, and `quantity` variables, print a small formatted receipt showing the item, quantity, unit price, and total (price × quantity), using an f-string.

---

## 31 — bmi-calculator

Ask the user for weight (kg) and height (m), calculate BMI, and print the result rounded to 1 decimal place.

```python
bmi = weight / height ** 2
```

> 💡 **New operator:** `**` — exponentiation. `height ** 2` means height squared.

---

## 32 — variable-type-juggling

Create a variable holding a number as a string (e.g. `"42"`), convert it to `int`, do math with it, then convert the result back to `str` and print it concatenated with text.

> 💡 **New command:** `str()` — converts a value into a string. Useful when concatenating numbers with text using `+`.

---

## Notes

- Solve exercises in order — later ones assume you're comfortable with commands introduced earlier.
- No `if`/`else`, `for`/`while`, lists, or string methods here — those get their own module once you've covered them in class or here.
- Challenges for this module (extra problems, not part of this core list) live in [`challenges/`](./challenges/).