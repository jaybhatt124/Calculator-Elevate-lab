import math

# ─── Basic Operations ───────────────────────────────────────────
def add(a, b):        return a + b
def subtract(a, b):   return a - b
def multiply(a, b):   return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

# ─── Basic Extensions ───────────────────────────────────────────
def exponent(a, b):     return a ** b
def modulus(a, b):
    if b == 0:
        return "Error: Modulus by zero!"
    return a % b
def floor_div(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a // b

# ─── Math Module Operations ─────────────────────────────────────
def square_root(a):
    if a < 0:
        return "Error: Cannot take sqrt of negative number!"
    return math.sqrt(a)

def log10(a):
    if a <= 0:
        return "Error: log input must be > 0!"
    return math.log10(a)

def log_natural(a):
    if a <= 0:
        return "Error: log input must be > 0!"
    return math.log(a)

def log_base2(a):
    if a <= 0:
        return "Error: log input must be > 0!"
    return math.log2(a)

def absolute(a):
    return abs(a)

def factorial(a):
    if a < 0:
        return "Error: Factorial not defined for negatives!"
    if not float(a).is_integer():
        return "Error: Factorial only works on whole numbers!"
    return math.factorial(int(a))

def power(a, b):
    return math.pow(a, b)

# ─── Input Helpers ──────────────────────────────────────────────
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  Invalid input. Please enter a number.")

def get_two_numbers():
    a = get_number("  Enter first number  : ")
    b = get_number("  Enter second number : ")
    return a, b

def get_one_number():
    return get_number("  Enter number : ")

# ─── Operations Table ───────────────────────────────────────────
OPERATIONS = {
    "1":  ("Addition",          "{a} + {b}",      add,          2),
    "2":  ("Subtraction",       "{a} - {b}",      subtract,     2),
    "3":  ("Multiplication",    "{a} * {b}",      multiply,     2),
    "4":  ("Division",          "{a} / {b}",      divide,       2),
    "5":  ("Exponentiation",    "{a} ** {b}",     exponent,     2),
    "6":  ("Modulus",           "{a} % {b}",      modulus,      2),
    "7":  ("Floor Division",    "{a} // {b}",     floor_div,    2),
    "8":  ("Square Root",       "sqrt({a})",      square_root,  1),
    "9":  ("Log base 10",       "log10({a})",     log10,        1),
    "10": ("Natural Log (ln)",  "ln({a})",        log_natural,  1),
    "11": ("Log base 2",        "log2({a})",      log_base2,    1),
    "12": ("Absolute Value",    "|{a}|",          absolute,     1),
    "13": ("Factorial",         "{a}!",           factorial,    1),
    "14": ("Power (math.pow)",  "pow({a}, {b})",  power,        2),
}

def print_menu():
    print("\n" + "=" * 40)
    print("         Calculator v2 — CLI App")
    print("=" * 40)
    print("\n  ── Basic Operations ──")
    for key in ["1", "2", "3", "4"]:
        print(f"   {key:>2}. {OPERATIONS[key][0]}")
    print("\n  ── Basic Extensions ──")
    for key in ["5", "6", "7"]:
        print(f"   {key:>2}. {OPERATIONS[key][0]}")
    print("\n  ── Math Module ──")
    for key in ["8", "9", "10", "11", "12", "13", "14"]:
        print(f"   {key:>2}. {OPERATIONS[key][0]}")
    print("\n    0. Exit")
    print("-" * 40)

def format_result(value):
    if isinstance(value, float) and value.is_integer():
        return int(value)
    if isinstance(value, float):
        return round(value, 6)
    return value

# ─── Main Loop ──────────────────────────────────────────────────
def calculator():
    print("\n  Welcome to Calculator v2!")

    while True:
        print_menu()
        choice = input("  Enter choice: ").strip()

        if choice == "0":
            print("\n  Goodbye! Thanks for using Calculator v2.\n")
            break

        if choice not in OPERATIONS:
            print("  Invalid choice. Please try again.")
            continue

        label, template, func, num_inputs = OPERATIONS[choice]
        print(f"\n  [ {label} ]")

        if num_inputs == 2:
            a, b = get_two_numbers()
            result = func(a, b)
            expr = template.format(a=a, b=b)
        else:
            a = get_one_number()
            result = func(a)
            expr = template.format(a=a)

        print("  " + "-" * 36)
        if isinstance(result, str):
            print(f"  {result}")
        else:
            print(f"  {expr} = {format_result(result)}")
        print("  " + "-" * 36)

if __name__ == "__main__":
    calculator()