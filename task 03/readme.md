# Task 03: Loops, Patterns & Basic Automation

## 📚 Overview

This folder contains 6 Python programs designed to teach fundamental programming concepts including loops, iteration, pattern generation, user input handling, and basic automation. All programs are beginner-friendly with proper error handling.

**Duration:** 30-45 minutes per day  
**Difficulty:** Beginner to Intermediate  
**Language:** Python 3.6+

---

## 📂 Contents

| # | Program | File Name | Purpose |
|---|---------|-----------|---------|
| 1 | Multiplication Table Generator | `Task_03_multiplication_table.py` | Generate multiplication table up to 10 |
| 2 | Number Analysis Tool | `Task_03_number_analysis.py` | Analyze sum, even, and odd numbers |
| 3 | Pattern Printing Challenge | `Task_03_patterns.py` | Print 3 different patterns using loops |
| 4 | Password Attempt Simulator | `Task_03_password_attempt.py` | Simulate password authentication (3 attempts) |
| 5 | Username Generator | `Task_03_username_generator.py` | Generate 5 username suggestions |
| BONUS | Number Guessing Game | `Task_03_number_guessing_game.py` | Interactive guessing game (1-50) |

---

## 🚀 How to Run

### Option 1: Run Individual Program
```bash
# Navigate to Task_03 folder
cd Task_03

# Run any program
python Task_03_multiplication_table.py
```

### Option 2: Run All Programs
```bash
# Linux/Mac
for file in Task_03_*.py; do python "$file"; done

# Windows (PowerShell)
Get-ChildItem Task_03_*.py | ForEach-Object { python $_ }
```

---

## 📋 Program Details

### 1️⃣ Multiplication Table Generator

**File:** `Task_03_multiplication_table.py`

**What it does:**
- Takes a number as input
- Displays multiplication table from 1 to 10

**How to use:**
```
Enter a number: 7

Multiplication Table for 7:
-----------------------------------
7 x  1 = 7
7 x  2 = 14
7 x  3 = 21
...
7 x 10 = 70
```

**Concepts Covered:**
- for loop with range()
- Input validation
- String formatting
- Error handling

**Features:**
- ✓ Input validation (non-zero check)
- ✓ Formatted output
- ✓ Error handling for invalid input

---

### 2️⃣ Number Analysis Tool

**File:** `Task_03_number_analysis.py`

**What it does:**
- Takes a number N as input
- Calculates sum of 1 to N
- Counts even and odd numbers

**How to use:**
```
Enter a number N: 10

===================================
Analysis for numbers 1 to 10:
===================================
Sum = 55
Even Numbers = 5
Odd Numbers = 5
```

**Concepts Covered:**
- for loops
- Conditional statements (if-else)
- Counter logic
- Accumulators

**Algorithm:**
```
For i from 1 to N:
  - Add i to sum
  - Check if i is even (i % 2 == 0)
    - If yes, increment even_count
    - If no, increment odd_count
```

**Features:**
- ✓ Input validation (positive number)
- ✓ Accurate calculations
- ✓ Formatted output

---

### 3️⃣ Pattern Printing Challenge

**File:** `Task_03_patterns.py`

**What it does:**
- Automatically prints 3 different patterns
- No user input required

**Output:**
```
Pattern 1: Increasing Stars
-------------------------
* 
* * 
* * * 
* * * * 
* * * * * 

Pattern 2: Decreasing Stars
-------------------------
* * * * * 
* * * * 
* * * 
* * 
* 

Pattern 3: Number Sequence
-------------------------
1
12
123
1234
12345
```

**Concepts Covered:**
- Nested loops
- String multiplication
- String concatenation
- Loop control

**How it works:**
```python
# Pattern 1: Increasing
for i in range(1, 6):
    print("* " * i)  # String multiplication

# Pattern 2: Decreasing
for i in range(5, 0, -1):
    print("* " * i)

# Pattern 3: Number sequence
for i in range(1, 6):
    row = ""
    for j in range(1, i + 1):
        row += str(j)
    print(row)
```

**Features:**
- ✓ 3 different pattern types
- ✓ Nested loop demonstration
- ✓ String manipulation

---

### 4️⃣ Password Attempt Simulator

**File:** `Task_03_password_attempt.py`

**What it does:**
- Simulates password authentication
- Maximum 3 attempts allowed
- Shows remaining attempts

**Password for testing:** `secure123`

**How to use:**
```
============================================
PASSWORD AUTHENTICATION SYSTEM
============================================
You have 3 attempts to enter the correct password
(For testing, password is: secure123)
============================================

Attempt 1/3 - Enter password: wrong
❌ Incorrect password! 2 attempt(s) remaining.

Attempt 2/3 - Enter password: secure123
============================================
✓ ACCESS GRANTED!
============================================
```

**Concepts Covered:**
- while loops
- Conditional statements
- Counter variables
- String comparison

**Features:**
- ✓ 3-attempt limit
- ✓ Attempt counter
- ✓ Remaining attempts display
- ✓ Account lock after failures

**Security Note:**
This is for educational purposes only. Real applications use:
- Password hashing (bcrypt, argon2)
- Salt generation
- Rate limiting
- Logging failed attempts

---

### 5️⃣ Username Generator

**File:** `Task_03_username_generator.py`

**What it does:**
- Takes first name, last name, and birth year
- Generates 5 different username suggestions

**How to use:**
```
==================================================
USERNAME GENERATOR - CYBER SECURITY UTILITY
==================================================

Enter First Name: Soham
Enter Last Name: Patel
Enter Birth Year (YYYY): 2004

==================================================
SUGGESTED USERNAMES:
==================================================
1. sohampatel2004
2. s.patel04
3. patel_soham
4. soham.patel
5. soham2004
==================================================
```

**Username Patterns Generated:**
1. `firstnamelastnamebirthyear` - Full concatenation
2. `f.lastname + last2digits` - Initial format
3. `lastname_firstname` - Underscore separated
4. `firstname.lastname` - Dot separated
5. `firstname + birthyear` - Name with year

**Concepts Covered:**
- String manipulation
- String methods (lower(), slicing)
- List handling
- Input validation

**String Operations:**
```python
# String slicing
first_char = name[0]      # First character
last_two_digits = year[-2:] # Last 2 characters

# String methods
username = (name).lower()  # Convert to lowercase

# String concatenation
full_username = first + "." + last + digits
```

**Features:**
- ✓ Input validation
- ✓ Birth year validation (1900-2024)
- ✓ 5 unique username formats
- ✓ Case conversion

---

### 🎮 BONUS: Number Guessing Game

**File:** `Task_03_number_guessing_game.py`

**What it does:**
- Computer thinks of a random number (1-50)
- User tries to guess it
- Computer gives high/low hints
- Counts total attempts

**How to use:**
```
==================================================
NUMBER GUESSING GAME
==================================================
I have thought of a secret number between 1 and 50.
Try to guess it!
==================================================

Enter your guess: 25
📈 Too low! Try a higher number.

Enter your guess: 40
📉 Too high! Try a lower number.

Enter your guess: 35
✓ CORRECT! You guessed it in 3 attempt(s)!
==================================================

Do you want to play again? (yes/no): yes
```

**Concepts Covered:**
- random module
- while loops
- Conditional statements
- User input handling
- Attempt counting

**How it works:**
```python
import random

secret = random.randint(1, 50)  # Generate random number
attempts = 0

while True:
    guess = int(input("Guess: "))
    attempts += 1
    
    if guess == secret:
        print(f"Correct in {attempts} attempts!")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
```

**Features:**
- ✓ Random number generation
- ✓ High/Low hints
- ✓ Attempt counter
- ✓ Replay option
- ✓ Input validation

---

## 🔧 Requirements

- Python 3.6 or higher
- No external libraries required
- All programs use only Python standard library

**Check Python version:**
```bash
python --version
```

---

## 📝 Running Each Program

### Program 1: Multiplication Table
```bash
python Task_03_multiplication_table.py
# Input: Any positive number
# Output: Multiplication table
```

### Program 2: Number Analysis
```bash
python Task_03_number_analysis.py
# Input: Positive number (e.g., 10)
# Output: Sum, Even count, Odd count
```

### Program 3: Patterns
```bash
python Task_03_patterns.py
# No input required
# Output: 3 patterns automatically
```

### Program 4: Password Simulator
```bash
python Task_03_password_attempt.py
# Input: Password (correct one is: secure123)
# Output: Access granted or denied
```

### Program 5: Username Generator
```bash
python Task_03_username_generator.py
# Input: First name, Last name, Birth year
# Output: 5 username suggestions
```

### Program 6: Guessing Game
```bash
python Task_03_number_guessing_game.py
# Input: Your guesses (1-50)
# Output: Hints and final result
```

---

## 💡 Learning Objectives

By completing this task, you will learn:

✓ **Loop Fundamentals**
- for loops with range()
- while loops
- Loop control and counters
- Nested loops

✓ **Conditional Logic**
- if-elif-else statements
- Comparison operators (==, <, >, <=, >=, !=)
- Logical operators (and, or, not)

✓ **String Manipulation**
- String concatenation
- String methods (lower(), strip())
- String slicing
- String formatting

✓ **Input/Output**
- input() function
- print() with formatting
- Error messages

✓ **Data Types**
- Integers and floats
- Strings
- Lists (basic)
- Booleans

✓ **Best Practices**
- Input validation
- Error handling
- Code organization
- Comments and documentation

---

## 🧪 Testing Guide

### Test Case 1: Multiplication Table
```
Input: 5
Expected Output:
5 x  1 = 5
5 x  2 = 10
...
5 x 10 = 50
```

### Test Case 2: Number Analysis
```
Input: 5
Expected Output:
Sum = 15
Even Numbers = 2 (2, 4)
Odd Numbers = 3 (1, 3, 5)
```

### Test Case 3: Password Attempt
```
Attempt 1: wrong → "Incorrect, 2 attempts remaining"
Attempt 2: wrong → "Incorrect, 1 attempt remaining"
Attempt 3: secure123 → "Access granted!"
```

### Test Case 4: Username Generator
```
Input: John, Doe, 2000
Outputs should include:
- johndoe2000
- j.doe00
- doe_john
- john.doe
- john2000
```

---

## ⚠️ Common Errors & Solutions

### ValueError: invalid literal for int()
**Problem:** User enters non-numeric input  
**Solution:** Program catches this with try-except

### IndexError: string index out of range
**Problem:** Accessing invalid string index  
**Solution:** Always check string length before indexing

### ZeroDivisionError
**Problem:** Division by zero  
**Solution:** Check denominator before dividing (not in this task)

### Infinite Loop
**Problem:** Loop condition never becomes false  
**Solution:** Always update loop variable

---

## 📊 Sample Execution Flow

```
Program starts
   ↓
Display menu/instructions
   ↓
Get user input
   ↓
Validate input
   ↓
Process data (calculations, logic)
   ↓
Display formatted output
   ↓
Ask for repetition or exit
   ↓
Program ends
```

---

## 🎯 Practice Challenges

### Easy Challenges:
1. Modify multiplication table to use custom range (not just 1-10)
2. Add more patterns to Pattern Printing program
3. Display number pattern as a formatted table

### Medium Challenges:
1. Extend Username Generator to create 10+ suggestions
2. Add difficulty levels to Guessing Game
3. Create a combined program with menu for all tasks

### Hard Challenges:
1. Add password strength checker
2. Create a mini-authentication system
3. Build a game with scoring system

---

## 📚 Key Programming Concepts Explained

### For Loops
```python
# Syntax
for variable in range(start, end, step):
    # code block
    
# Examples
for i in range(1, 11):        # 1 to 10
for i in range(0, 10, 2):     # 0, 2, 4, 6, 8
for i in range(5, 0, -1):     # 5 down to 1
```

### While Loops
```python
# Syntax
while condition:
    # code block
    # must update condition
    
# Example
attempts = 0
while attempts < 3:
    password = input("Enter: ")
    attempts += 1
```

### String Slicing
```python
text = "Hello"
text[0]      # 'H' (first character)
text[-1]     # 'o' (last character)
text[1:4]    # 'ell' (characters 1-3)
text[-2:]    # 'lo' (last 2 characters)
```

---

## 📞 Debugging Tips

1. **Use print() statements** to track variable values
2. **Test with simple inputs first** before complex ones
3. **Check loop conditions** carefully
4. **Validate input** before processing
5. **Read error messages** carefully - they help!

---

## 🏆 Completion Checklist

- [ ] All 6 programs run without errors
- [ ] Input validation works correctly
- [ ] Output is properly formatted
- [ ] No crashes or infinite loops
- [ ] Code is readable and commented
- [ ] Tested with multiple inputs
- [ ] Bonus (Guessing Game) completed
- [ ] Ready to push to GitHub

---

## 📝 Code Quality Standards

✓ **Readability**
- Clear variable names
- Proper indentation (4 spaces)
- Comments where needed

✓ **Functionality**
- All features working
- Error handling present
- Input validation done

✓ **Documentation**
- Docstrings for functions
- Comments for complex logic
- Usage examples provided

---

## 🔗 Related Topics to Study

- Python loops and iterations
- String manipulation techniques
- Pattern generation algorithms
- Random number generation
- User input validation
- Basic authentication concepts

---

## 📖 Additional Resources

### Official Documentation
- [Python range() function](https://docs.python.org/3/library/stdtypes.html#range)
- [String methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [random module](https://docs.python.org/3/library/random.html)

### Learning Platforms
- W3Schools Python Tutorial
- Real Python Articles
- GeeksforGeeks Python Guide


**Author:** Janani  
**Version:** 1.0 - Corrected and Verified  
**Status:** ✅ Ready for Submission  
**Date:** June  12 2024