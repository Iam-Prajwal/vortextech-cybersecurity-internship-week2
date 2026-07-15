# Password Strength Checker — Project Report

**Vortex Tech Cyber Security Internship — Week 2**

---

## Introduction

Weak passwords remain one of the most common entry points for account compromise, credential stuffing, and brute-force attacks. Despite widespread awareness, users continue to rely on short, predictable, or reused passwords because there is often no immediate feedback telling them *why* a password is weak or *how* to improve it. This project addresses that gap by building a lightweight, rule-based Password Strength Checker in Python that evaluates a password against several security criteria and returns both a strength rating and personalized, actionable feedback.

This tool was built as the Week 2 deliverable of the Cyber Security Internship, with the goal of applying secure coding principles, modular program design, and an understanding of password security fundamentals in a small, self-contained project suitable for a portfolio.

## Objective

The objective of this project is to:

- Build a command-line Python tool that evaluates password strength based on industry-recognized criteria (length, character variety, and blacklist matching).
- Produce clear strength categories (Very Weak, Weak, Medium, Strong, Very Strong) rather than a single pass/fail result.
- Provide personalized, human-readable feedback that helps a user understand exactly what to change.
- Demonstrate clean, modular, PEP 8-compliant Python code that separates logic (checking rules) from presentation (displaying results).
- Document and test the tool with a representative range of sample passwords.

## How the Password Checker Works

The checker takes a single password as input and runs it through six independent checks:

1. **Minimum length** — is the password at least 8 characters long?
2. **Bonus length** — is the password 12 characters or longer (rewarded as an extra strength signal)?
3. **Uppercase letters** — does it contain at least one uppercase character?
4. **Lowercase letters** — does it contain at least one lowercase character?
5. **Digits** — does it contain at least one numeric digit?
6. **Special characters** — does it contain at least one symbol (e.g. `!`, `@`, `#`)?

In parallel, the password is checked (case-insensitively) against a blacklist of commonly leaked or guessed passwords such as `password`, `123456`, and `qwerty`. A blacklist match overrides every other check — even a password that technically satisfies length and complexity rules is treated as **Very Weak** if it is a known, commonly guessed value, because attackers will always try these first regardless of how "complex" they appear.

Each satisfied check (excluding the blacklist check) contributes one point to a numeric score out of 6. That score is then mapped to a final strength label, and any unmet checks are translated into specific, friendly feedback messages so the user knows exactly what to fix.

## Algorithm

```
INPUT: password (string)

1. Run individual checks:
   min_length      = length(password) >= 8
   bonus_length    = length(password) >= 12
   has_uppercase   = any character is uppercase
   has_lowercase   = any character is lowercase
   has_digit       = any character is a digit
   has_special     = any character is a punctuation symbol
   is_blacklisted  = lowercase(password) is in the blacklist set

2. Calculate score:
   IF is_blacklisted:
       score = 0
   ELSE:
       score = sum of all TRUE checks above (excluding is_blacklisted),
               out of a maximum of 6

3. Map score to strength label:
   score == 0        -> "Very Weak"
   score in [1, 2]    -> "Weak"
   score in [3, 4]    -> "Medium"
   score == 5        -> "Strong"
   score == 6        -> "Very Strong"

4. Generate feedback:
   FOR each failed check, append a corresponding suggestion
   IF no checks failed, append a positive confirmation message

OUTPUT: strength label, numeric score, feedback list
```

This scoring approach was chosen over a simple pass/fail system because it gives users incremental, meaningful signal — moving from "Weak" to "Medium" by adding just one missing element (like a digit or symbol) is far more motivating and instructive than a flat rejection.

## Python Concepts Used

| Concept | Where It's Used |
|---|---|
| **Functions & modular design** | Each check (length, uppercase, digit, etc.) is its own pure function, making the code easy to test and reuse |
| **Sets** | The blacklist and special-character list are stored as `set` objects for fast, constant-time membership checks |
| **String methods** | `str.isupper()`, `str.islower()`, `str.isdigit()`, and `str.lower()` are used throughout for character analysis |
| **`string` module** | `string.punctuation` supplies the full set of standard special characters instead of hardcoding them manually |
| **Dictionaries** | Check results are stored and passed around as a dictionary (`checks`), keeping related data grouped together |
| **List comprehension / `any()`** | Used with generator expressions (e.g. `any(char.isupper() for char in password)`) for concise, readable checks |
| **Conditional logic (`if`/`elif`/`else`)** | Drives the score-to-strength mapping and feedback generation |
| **String formatting (f-strings)** | Used for clean, readable terminal output |
| **Separation of concerns** | Logic (`evaluate_password`), scoring (`score_to_strength`), and display (`display_result`) are kept in distinct functions rather than one large script |

## Screenshots Placeholder

> **![alt text](image.png)**

## Example Outputs

The full set of 8 tested passwords and their real, program-generated output is documented separately in [`sample_outputs.md`](./sample_outputs.md). A condensed summary:

| Password (masked) | Strength Rating | Score |
|---|---|---|
| `1*****` | Very Weak | 0/6 |
| `q*****` | Very Weak | 0/6 |
| `a******` | Weak | 1/6 |
| `a*******` | Weak | 2/6 |
| `a********` | Medium | 3/6 |
| `A********` | Medium | 4/6 |
| `A*********` | Strong | 5/6 |
| `A***********` | Very Strong | 6/6 |

## Discussion

Building this tool reinforced a few practical lessons about password security beyond just the coding exercise itself:

- **Length matters more than people assume.** Two of the "Weak" examples above (`abcdefg`, `abcdefgh`) use only lowercase letters, yet purely increasing character variety without increasing length still caps out at "Medium" — reinforcing that length and character diversity work together, not as substitutes for each other.
- **Blacklisting is a critical, often-overlooked layer.** Complexity rules alone (uppercase, digits, symbols) can be satisfied by predictable patterns like `Password123!`, which still shows up in leaked credential lists. A blacklist check catches this class of "technically complex but practically weak" password that pure rule-based scoring would otherwise miss.
- **Feedback quality affects real-world adoption.** A tool that simply says "weak" is far less useful than one that says *why*. This is consistent with usability research on password meters, which shows that actionable, specific feedback measurably improves the passwords users choose.
- **Limitations of a rule-based approach.** This checker does not detect patterns like keyboard walks (`qwertyuiop`), repeated characters (`aaaaaaaa`), or personal information (birthdates, names). A production-grade checker would ideally incorporate entropy-based scoring (such as the `zxcvbn` library) alongside blacklist and complexity checks for a more realistic strength estimate.

## Conclusion

This project successfully implements a modular, readable Python password strength checker that evaluates passwords across length, character diversity, and blacklist criteria, and returns both a clear strength rating and personalized feedback. Testing across 8 representative passwords confirmed that the scoring logic behaves consistently and produces intuitive results across all five strength categories. Beyond the code itself, this exercise reinforced core password security principles — particularly that complexity rules alone are insufficient without accounting for commonly guessed passwords — which directly informs how authentication systems should be designed in real-world applications.
