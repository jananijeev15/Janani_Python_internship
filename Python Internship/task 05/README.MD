# Programming Task 05 – Arrays, Lists & Data Processing

## Project Title
Arrays, Lists & Data Processing – Python and C Programming Internship Task 05

## Objective
The purpose of this task is to understand how data is stored, processed, searched, and analyzed using Arrays (C) and Lists (Python). These concepts are heavily used in software development, automation, and cybersecurity tools.

## Features
- **Student Marks Analyzer** – Accepts marks of 5 students and displays the highest, lowest, and average marks.
- **Employee Record Search** – Stores a list of employee names and searches for a given name using linear search, displaying "Record Found" or "Record Not Found."
- **Number Statistics Tool** – Accepts 10 numbers and displays the largest, smallest, sum, average, and counts of even/odd numbers.
- **Cyber Security Log Analyzer** – Stores a list of login attempts (Success/Failed) and reports total, successful, and failed login counts.
- **Blacklisted IP Checker** – Stores a list of blacklisted IP addresses and checks whether a user-entered IP is present.
- **Bonus: Contact Management System** – Menu-driven program to add, view, search, and delete contacts using a list.

## Technologies Used
- Python 3
- C Programming (GCC)
- Lists (Python) / Arrays (C)
- Loops, conditionals, functions
- Linear search

## Program Flow
1. Each program prompts the user for input (marks, names, numbers, IP address, etc.) using `input()`.
2. Data is stored in a Python list (or C array).
3. The program processes the data using loops and built-in functions (`max()`, `min()`, `sum()`, etc., or manual loops in C).
4. Results are displayed to the user in a clearly formatted output.
5. Where required (e.g., search/checker tools), the program compares user input against stored data and reports a match or no-match result.

## Challenges Faced
- Handling invalid user input (e.g., non-numeric values) using validation and `try/except` blocks.
- Designing a clean, readable output format consistent with the example outputs.
- Translating Python list operations into equivalent array logic in C (e.g., manual max/min/sum instead of built-in functions).
- Implementing case-insensitive search for names so that searches work regardless of input casing.

## Learning Outcomes
- Strengthened understanding of how Python lists and C arrays store and process collections of data.
- Practiced linear search, a foundational searching algorithm used in many real-world applications.
- Learned to calculate basic statistics (max, min, sum, average) from a dataset using loops.
- Understood why monitoring failed login attempts is important for detecting brute-force attacks and unauthorized access in cybersecurity systems.
- Gained experience building small, focused, menu-driven utility programs that mirror real cybersecurity monitoring tools (e.g., blacklist checkers).

## Folder Structure
```
Programming_Task_05_YourName/
├── Python Files/
│   ├── marks_analyzer.py
│   ├── employee_search.py
│   ├── statistics_tool.py
│   ├── log_analyzer.py
│   └── blacklist_checker.py
├── C Files/
│   ├── marks_analyzer.c
│   ├── employee_search.c
│   ├── statistics_tool.c
│   ├── log_analyzer.c
│   └── blacklist_checker.c
├── Bonus/
│   └── contact_manager_bonus.py
├── Screenshots/
├── README.md
```

## How to Run

### Python
```
python3 marks_analyzer.py
python3 employee_search.py
python3 statistics_tool.py
python3 log_analyzer.py
python3 blacklist_checker.py
python3 contact_manager_bonus.py
```

### C
```
gcc marks_analyzer.c -o marks_analyzer
./marks_analyzer
```
(Repeat the same compile-and-run pattern for the other `.c` files.)