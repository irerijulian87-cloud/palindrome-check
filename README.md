# Palindrome Checker (C and Python)

Two versions of the same program: a **palindrome checker** written in **C** and in **Python**.

> A palindrome reads the same forwards and backwards: `racecar`, `Level`, `12321`.

---

## At a Glance

| | C version | Python version |
|---|---|---|
| File | `palindrome.c` | `palindrome.py` |
| Input | One word at a time | Words, numbers, and full sentences |
| Ignores capitals | Yes | Yes |
| Ignores spaces and punctuation | No (single words only) | Yes |
| Interface | Simple prompt loop | Colour menu |
| Extras | Quit command | History, statistics, help screen |
| Exit | Type `quit` or press Ctrl+D | Menu option `5` |

---

## How to Run

**C**

```bash
gcc palindrome.c -o palindrome
./palindrome
```

**Python** (Python 3.6+)

```bash
python palindrome.py
```

---

## How It Works

Both programs use the same idea:

1. Take the text the user typed.
2. Normalise it (make it lowercase).
3. Compare it against its own reverse.
4. Report whether it matches.

### C: two-pointer comparison

Compare the first character with the last, the second with the second-to-last, and so on, stopping at the middle. One mismatch means it is not a palindrome.

```c
for (i = 0; i < length / 2; i++) {
    if (tolower((unsigned char)word[i]) !=
        tolower((unsigned char)word[length - 1 - i])) {
        isPalindrome = 0;
        break;
    }
}
```

```
r a c e c a r
↑           ↑   r = r ✓
  ↑       ↑     a = a ✓
    ↑   ↑       c = c ✓
      ↑         middle, done
```

### Python: clean, then reverse

Strip everything except letters and digits, then compare the string to its reverse using a slice.

```python
def clean_text(text: str) -> str:
    return "".join(c.lower() for c in text if c.isalnum())

def is_palindrome(clean: str) -> bool:
    return clean == clean[::-1]
```

`"A man, a plan, a canal: Panama"` becomes `"amanaplanacanalpanama"`, which equals its reverse.

---

## Example Runs

**C**

```
Enter a word (or 'quit' to exit): Level
Level is a palindrome.

Enter a word (or 'quit' to exit): hello
hello is not a palindrome.

Enter a word (or 'quit' to exit): quit
Goodbye!
```

**Python**

```
 Type a word or phrase: Was it a car or a cat I saw?

 Original : Was it a car or a cat I saw?
 Cleaned  : wasitacaroracatisaw
 Reversed : wasitacaroracatisaw

 YES! It IS a palindrome.
```

### Good test inputs

| Input | Result |
|---|---|
| `racecar` | Palindrome |
| `Level` | Palindrome (case ignored) |
| `12321` | Palindrome |
| `A man, a plan, a canal: Panama` | Palindrome (Python only) |
| `hello` | Not a palindrome |

---

## Key Features

### C version
- **Loop:** checks word after word until the user quits
- **Flag reset:** `isPalindrome` is reset each pass so one result doesn't affect the next
- **Safe input:** `scanf("%99s", ...)` limits input to fit the 100-character buffer
- **EOF handling:** the loop ends cleanly if input is closed

### Python version
- **Phrases and numbers:** punctuation and spaces are ignored
- **Menu system:** check, history, statistics, help, exit
- **History:** remembers the last 50 checks
- **Statistics:** total checked, palindromes, non-palindromes, and palindrome rate
- **Input handling:** empty input is rejected, and Ctrl+C / Ctrl+D exit cleanly

---

## What We Learned

- The same algorithm can be expressed very differently: manual index comparison in C, a one-line slice in Python.
- C gives control over memory and characters (buffers, `strlen`, `tolower`) but needs care with input sizes.
- Python lets us focus on features (cleaning text, history, statistics) because the language handles the low-level work.

---

## Limitations and Possible Improvements

- The C version only handles single words. Supporting phrases would need `fgets` plus a cleaning step like Python's `clean_text`.
- History and statistics are not saved between runs.

---

## Repository Structure

```
.
├── palindrome.c     # C version
├── palindrome.py    # Python version
└── README.md
```
