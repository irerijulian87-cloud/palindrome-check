#!/usr/bin/env python3
"""
============================================================
 PALINDROME CHECKER  (Python version)
 Features: phrases, menu, history, statistics, colour UI

 Run:  python palindrome.py
============================================================
"""

MAX_HISTORY = 50

# ---------- ANSI colours (work in Termux and most terminals) ----------
RESET, BOLD = "\033[0m", "\033[1m"
RED, GREEN, YELLOW, CYAN = "\033[31m", "\033[32m", "\033[33m", "\033[36m"

history = []          # list of (text, is_palindrome)
total_yes = 0
total_no = 0


# ---------- UI helpers ----------
def clear_screen():
    print("\033[2J\033[H", end="")


def line(char="-", n=44):
    print(char * n)


def banner():
    clear_screen()
    print(CYAN + BOLD, end="")
    line("=")
    print("        PALINDROME CHECKER  v2.0")
    print("   Words, numbers and whole sentences")
    line("=")
    print(RESET, end="")


def pause():
    try:
        input(f"\n{YELLOW}Press ENTER to continue...{RESET}")
    except EOFError:
        pass


# ---------- Core logic ----------
def clean_text(text: str) -> str:
    """Keep only letters/digits, lowercase."""
    return "".join(c.lower() for c in text if c.isalnum())


def is_palindrome(clean: str) -> bool:
    return clean == clean[::-1]


def add_history(text: str, result: bool):
    global total_yes, total_no
    if len(history) == MAX_HISTORY:
        history.pop(0)
    history.append((text, result))
    if result:
        total_yes += 1
    else:
        total_no += 1


# ---------- Menu actions ----------
def do_check():
    banner()
    print(f"\n{BOLD} CHECK A PALINDROME{RESET}")
    line()
    text = input(" Type a word or phrase: ").strip()

    clean = clean_text(text)
    if not clean:
        print(f"\n{RED} Nothing to check. Use letters or numbers.{RESET}")
        pause()
        return

    result = is_palindrome(clean)
    add_history(text, result)

    print(f"\n Original : {text}")
    print(f" Cleaned  : {clean}")
    print(f" Reversed : {clean[::-1]}\n")

    if result:
        print(f"{GREEN}{BOLD} +----------------------------------------+\n"
              f" |   YES! It IS a palindrome.             |\n"
              f" +----------------------------------------+{RESET}")
    else:
        print(f"{RED}{BOLD} +----------------------------------------+\n"
              f" |   NO. It is NOT a palindrome.          |\n"
              f" +----------------------------------------+{RESET}")
    pause()


def do_history():
    banner()
    print(f"\n{BOLD} HISTORY (last {MAX_HISTORY} checks){RESET}")
    line()
    if not history:
        print(" No checks yet.")
    else:
        for i, (text, result) in enumerate(history, 1):
            shown = text if len(text) <= 26 else text[:25] + "~"
            tag = f"{GREEN}PALINDROME{RESET}" if result else f"{RED}NOT{RESET}"
            print(f" {i:2d}. {shown:<26} {tag}")
    pause()


def do_stats():
    total = total_yes + total_no
    banner()
    print(f"\n{BOLD} STATISTICS{RESET}")
    line()
    print(f" Total checked   : {total}")
    print(f" Palindromes     : {GREEN}{total_yes}{RESET}")
    print(f" Not palindromes : {RED}{total_no}{RESET}")
    if total:
        print(f" Palindrome rate : {100 * total_yes / total:.1f}%")
    pause()


def do_help():
    banner()
    print(f"\n{BOLD} HELP{RESET}")
    line()
    print(" A palindrome reads the same forwards and\n"
          " backwards. Spaces, punctuation and capital\n"
          " letters are ignored.\n\n"
          " Try these:\n"
          "   racecar\n"
          "   Level\n"
          "   12321\n"
          "   A man, a plan, a canal: Panama\n"
          "   Was it a car or a cat I saw?\n"
          "   hello   (not a palindrome)")
    pause()


def show_menu():
    print(f"\n{BOLD} MAIN MENU{RESET}")
    line()
    print("  [1] Check a word or phrase")
    print("  [2] View history")
    print("  [3] View statistics")
    print("  [4] Help / examples")
    print("  [5] Exit")
    line()


# ---------- Main ----------
def main():
    actions = {"1": do_check, "2": do_history, "3": do_stats, "4": do_help}

    while True:
        banner()
        show_menu()
        try:
            choice = input(" Choose an option (1-5): ").strip()
        except (EOFError, KeyboardInterrupt):
            break

        if choice == "5":
            break
        if choice in actions:
            try:
                actions[choice]()
            except (EOFError, KeyboardInterrupt):
                break
        else:
            print(f"\n{RED} Invalid option. Choose 1-5.{RESET}")
            pause()

    print(f"\n{CYAN} Thank you for using Palindrome Checker. Goodbye!{RESET}\n")


if __name__ == "__main__":
    main()
