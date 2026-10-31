# weakspot

**A command-line password strength auditor written in Python.**

#### Video Demo: https://youtu.be/t1_P492o4OQ

#### Description:

`weakspot` analyzes a password and tells you why it might be weak. Instead of relying only on length or "must contain a symbol" rules, it combines three checks that reflect how attackers actually crack passwords: how large the brute force search space is (entropy), whether the password appears in a list of real-world commonly used passwords, and whether it contains predictable number sequences.

The goal is to give a fast, offline, and explainable verdict: not just "weak", but the specific reasons behind it.

---

## Features

- **Entropy estimation**: calculates how hard the password is to brute force, in bits. Passwords below 60 bits are flagged.
- **Common password detection**: checks the password against the NCSC list of the 100,000 most used passwords.
- **Sequential number detection**: flags runs of 3 or more consecutive digits in ascending or descending order, such as `123` or `987`.
- **Combined verdict**: reports every issue found in a single message.
- **Fully offline**: the password never leaves the machine.

## Installation

```bash
git clone https://github.com/malikarsya/weakspot.git
cd weakspot
pip install -r requirements.txt
```

## Usage

```bash
python project.py <password>
```

Examples:

```bash
$ python project.py password123
Password is common, <60 bit, and has sequential numbers

$ python project.py "my password"
Spaces are not allowed.

$ python project.py
Format is project.py [password]
```

If the password passes all three checks, the program prints `Password is Safe`.

## Project Structure

| File | Purpose |
|------|---------|
| `project.py` | Main program. Contains `main()` and the three check functions. |
| `test_project.py` | Unit tests for the check functions, run with `pytest`. |
| `100k-most-used-passwords-NCSC.txt` | Wordlist of the 100,000 most common passwords, published by the UK National Cyber Security Centre. |
| `requirements.txt` | Python dependencies. |

### Core Functions

- `calculate_entropy(pass_list)`: estimates the password's entropy in bits using `length × log2(pool)`, where the pool is the combined size of the character sets the password uses: lowercase (26), uppercase (26), digits (10), and punctuation (32).
- `is_common(password)`: returns `True` if the password appears in the NCSC common password list.
- `has_sequential_number(pass_list)`: returns `True` if the password contains 3 or more consecutive digits in ascending or descending order.

## Design Decisions

**Booleans over messages.** The check functions return values (`True`/`False` or a number) instead of formatted strings. This keeps the logic separate from the output, so `main()` decides what to print and each function can be tested on its own.

**60 bit threshold.** Entropy below 60 bits is treated as weak, since that range is within reach of offline brute force attacks on modern hardware.

**Sequence length of 3.** Two consecutive digits appear too often by chance to be meaningful, but three or more (like `123`) is a strong signal of a human-chosen pattern.

**Spaces are rejected.** Passwords are passed as a single command-line argument, so spaces are not allowed to avoid ambiguous input.

**Offline by design.** A password auditor that sends passwords over the network defeats its own purpose. All analysis happens locally.

## Testing

```bash
pytest test_project.py
```

## Limitations and Future Work

- Entropy estimation assumes every character is chosen randomly, so it can overestimate the strength of human-chosen passwords (for example, a dictionary word with a capital letter).
- The wordlist is read from disk on every check. Loading it once into a set would make lookups faster.
- Passing a password as a command-line argument can leave it in shell history. A hidden prompt mode using `getpass` is a planned improvement.
- Planned: keyboard pattern detection (like `qwerty`), substring matching against the wordlist, and optional breach checking via the Have I Been Pwned k-anonymity API.

## Acknowledgements

- Wordlist: NCSC 100k most used passwords
- Built as the final project for [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/).

## Author

Malik Madani