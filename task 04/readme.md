# Task 04: Functions, File Handling & Student Management System

## 📚 Overview

This folder contains 6 Python programs designed to teach modular programming, file handling, data management, and building complete applications. Programs include a calculator, student management system, marks analyzer, and utility tools.

**Duration:** 30-45 minutes per day  
**Difficulty:** Beginner to Intermediate  
**Language:** Python 3.6+

---

## 📂 Contents

| # | Program | File Name | Purpose |
|---|---------|-----------|---------|
| 1 | Calculator with Functions | `Task_04_calculator_functions.py` | Menu-driven calculator (4 operations) |
| 2 | Student Information Manager | `Task_04_student_manager.py` | Add and display student records |
| 3 | Marks Analysis System | `Task_04_marks_analyzer.py` | Calculate grades for 5 subjects |
| 4 | File Handling Challenge | `Task_04_file_handling.py` | Save/read student data from files |
| 5 | Password Vault Simulator | `Task_04_password_vault.py` | Store website credentials securely |
| BONUS | Activity Log Generator | `Task_04_activity_log_generator.py` | Log program activities with timestamp |

---

## 🚀 How to Run

### Option 1: Run Individual Program
```bash
# Navigate to Task_04 folder
cd Task_04

# Run any program
python Task_04_calculator_functions.py
```

### Option 2: Run All Programs
```bash
# Linux/Mac
for file in Task_04_*.py; do python "$file"; done

# Windows (PowerShell)
Get-ChildItem Task_04_*.py | ForEach-Object { python $_ }
```

---

## 📋 Program Details

### 1️⃣ Calculator with Functions

**File:** `Task_04_calculator_functions.py`

**What it does:**
- Menu-driven calculator
- Performs 4 basic operations
- Uses separate functions for each operation

**How to use:**
```
========================================
CALCULATOR MENU
========================================
1. Addition
2. Subtraction
3. Multiplication
4. Division
========================================
Enter Choice (1-4): 1
Enter First Number: 10
Enter Second Number: 20

========================================
Addition Result:
10.0 + 20.0 = 30.0
========================================

Do you want another calculation? (yes/no): yes
```

**Concepts Covered:**
- Function definition and calling
- Parameters and return values
- Menu-driven programming
- Error handling
- Input validation

**Code Structure:**
```python
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def calculator():
    # Menu logic here

def main():
    # Loop for multiple calculations
```

**Features:**
- ✓ 4 operations (Add, Subtract, Multiply, Divide)
- ✓ Division by zero protection
- ✓ Input validation
- ✓ Repeat calculation option
- ✓ Error handling

**Operations Supported:**
| Operation | Symbol | Example |
|-----------|--------|---------|
| Addition | + | 10 + 20 = 30 |
| Subtraction | - | 20 - 10 = 10 |
| Multiplication | × | 10 × 5 = 50 |
| Division | ÷ | 20 ÷ 4 = 5 |

---

### 2️⃣ Student Information Manager

**File:** `Task_04_student_manager.py`

**What it does:**
- Add multiple student records
- Store student information (name, roll no, branch, semester)
- Display all students in formatted way

**How to use:**
```
=============================================
STUDENT INFORMATION MANAGER
=============================================

=============================================
MENU
=============================================
1. Add Student
2. Display All Students
3. Exit
=============================================
Enter your choice: 1

---------------------------------------------
ADD NEW STUDENT
---------------------------------------------
Enter Student Name: Soham Patel
Enter Roll Number: 101
Enter Branch: CSE
Enter Semester: 5
✓ Student added successfully!

Menu again...
Enter your choice: 2

=============================================
ALL STUDENTS (1 total)
=============================================

--- Student 1 ---
Name: Soham Patel
Roll No: 101
Branch: CSE
Semester: 5

=============================================
```

**Concepts Covered:**
- Functions for modularity
- Dictionaries for data storage
- Lists for managing multiple records
- Menu-driven interface
- Input validation

**Data Structure:**
```python
student = {
    "name": "Soham Patel",
    "roll_number": "101",
    "branch": "CSE",
    "semester": "5"
}

students = [student1, student2, ...]  # List of students
```

**Features:**
- ✓ Add multiple students
- ✓ Display all students
- ✓ Formatted output
- ✓ Input validation
- ✓ Menu-driven interface

**Functions Used:**
- `get_student_info()` - Collects student data
- `display_student()` - Displays single student
- `student_manager()` - Main menu

---

### 3️⃣ Marks Analysis System

**File:** `Task_04_marks_analyzer.py`

**What it does:**
- Accept marks for 5 subjects (Math, English, Science, History, Computer)
- Calculate total and percentage
- Assign grade based on performance
- Display detailed results

**How to use:**
```
=============================================
MARKS ANALYSIS SYSTEM
=============================================

=============================================
ENTER MARKS FOR 5 SUBJECTS
=============================================
Enter marks for Math (0-100): 85
Enter marks for English (0-100): 78
Enter marks for Science (0-100): 92
Enter marks for History (0-100): 88
Enter marks for Computer (0-100): 95

=============================================
RESULTS
=============================================
Math        :  85.00
English     :  78.00
Science     :  92.00
History     :  88.00
Computer    :  95.00
=============================================
Total Marks    : 438/500
Percentage     : 87.60%
Grade          : B
=============================================

Grade Criteria:
---------------------------------------------
90-100% -> Grade A
80-89%  -> Grade B
70-79%  -> Grade C
60-69%  -> Grade D
<60%    -> Grade F
---------------------------------------------
```

**Concepts Covered:**
- Input validation (0-100 range)
- Mathematical calculations
- Conditional logic for grading
- List handling
- Formatted output
- Data analysis

**Grading Scale:**
| Percentage | Grade |
|-----------|-------|
| 90-100% | A |
| 80-89% | B |
| 70-79% | C |
| 60-69% | D |
| <60% | F |

**Calculations:**
```python
# Total = Sum of 5 marks
Total = Math + English + Science + History + Computer

# Percentage = (Total / 500) × 100
Percentage = (Total / 500) * 100

# Grade based on percentage
if Percentage >= 90: Grade = "A"
elif Percentage >= 80: Grade = "B"
...
```

**Features:**
- ✓ 5 subject marks input
- ✓ Marks validation (0-100)
- ✓ Total calculation
- ✓ Percentage calculation
- ✓ Automatic grading
- ✓ Grade criteria display
- ✓ Formatted results table
- ✓ Repeat analysis option

**Functions Used:**
- `get_marks()` - Collect marks from user
- `calculate_total()` - Sum all marks
- `calculate_percentage()` - Calculate percentage
- `calculate_grade()` - Assign grade
- `display_grade_criteria()` - Show grading scale

---

### 4️⃣ File Handling Challenge

**File:** `Task_04_file_handling.py`

**What it does:**
- Save student records to file (student_data.txt)
- Read records from file
- Display all records
- Clear all records with confirmation

**How to use:**
```
=============================================
FILE HANDLING MENU
=============================================
1. Add Student Record
2. Read All Records
3. Clear All Records
4. Exit
=============================================
Enter your choice: 1

=============================================
ADD STUDENT RECORD
=============================================
Enter Student Name: Soham
Enter Roll Number: 101
Enter Branch: CSE
Enter Marks: 85
✓ Student Record Saved Successfully

Menu again...
Enter your choice: 2

=============================================
Reading File...
=============================================
Name: Soham
Roll No: 101
Branch: CSE
Marks: 85
---------------------------------------------
=============================================
```

**File Created:**
`student_data.txt`

**File Format:**
```
Name: Soham
Roll No: 101
Branch: CSE
Marks: 85
---------------------------------------------
Name: Priya
Roll No: 102
Branch: IT
Marks: 90
---------------------------------------------
```

**Concepts Covered:**
- File I/O operations
- File modes (read, write, append)
- Exception handling for file operations
- File existence checking
- Data persistence

**File Operations:**
```python
# Writing/Appending to file
with open("student_data.txt", 'a') as file:
    file.write(data)

# Reading from file
with open("student_data.txt", 'r') as file:
    content = file.read()

# Clearing file
with open("student_data.txt", 'w') as file:
    pass
```

**File Modes:**
| Mode | Purpose | Behavior |
|------|---------|----------|
| 'r' | Read | Opens file (error if not exists) |
| 'w' | Write | Creates/overwrites file |
| 'a' | Append | Adds to end of file |

**Features:**
- ✓ Save records to file
- ✓ Read all records
- ✓ Display formatted records
- ✓ Clear all data with confirmation
- ✓ File existence checking
- ✓ Error handling for I/O operations
- ✓ Data persistence

**Functions Used:**
- `save_student_data()` - Write to file
- `read_student_data()` - Read from file
- `clear_file_data()` - Clear all data
- `file_handler_menu()` - Main menu

---

### 5️⃣ Password Vault Simulator

**File:** `Task_04_password_vault.py`

**What it does:**
- Store website credentials (website, username, password)
- View all saved credentials
- Clear vault with confirmation
- File-based storage

**How to use:**
```
==================================================
PASSWORD VAULT SIMULATOR - CYBER SECURITY UTILITY
==================================================
⚠️  Note: This is a learning project. No encryption is applied.
==================================================

==================================================
PASSWORD VAULT MENU
==================================================
1. Add Password
2. View All Passwords
3. Clear Vault
4. Exit
==================================================
Enter your choice: 1

=============================================
ADD PASSWORD TO VAULT
=============================================
Enter Website Name: Gmail
Enter Username: user@gmail.com
Enter Password: Test@123
✓ Password saved successfully!

Menu again...
Enter your choice: 2

=============================================
PASSWORD VAULT
=============================================
Website: Gmail
Username: user@gmail.com
Password: Test@123
---------------------------------------------
Website: GitHub
Username: myusername
Password: MySecurePass123
---------------------------------------------
=============================================
```

**File Created:**
`password_vault.txt`

**File Format:**
```
Website: Gmail
Username: user@gmail.com
Password: Test@123
---------------------------------------------
Website: GitHub
Username: myusername
Password: MySecurePass123
---------------------------------------------
```

**Concepts Covered:**
- File handling (append and read)
- Data structure organization
- Menu-driven interface
- Input validation
- Security awareness (educational)

**Features:**
- ✓ Add credentials
- ✓ View all credentials
- ✓ Persistent storage
- ✓ Clear vault with confirmation
- ✓ Input validation
- ✓ Error handling

**⚠️ Security Notes:**
- This is educational only
- No encryption applied
- Real applications should use:
  - **Encryption:** cryptography module
  - **Hashing:** bcrypt, argon2
  - **Secure Storage:** Database with encryption
  - **Environment Variables:** For sensitive data

**Functions Used:**
- `add_password()` - Store credentials
- `display_passwords()` - Show all credentials
- `clear_vault()` - Clear all data
- `password_vault_menu()` - Main menu

---

### 🎮 BONUS: Activity Log Generator

**File:** `Task_04_activity_log_generator.py`

**What it does:**
- Log program activities with timestamp
- Record date, time, program name, and activity
- View activity history
- Clear logs with confirmation

**How to use:**
```
==================================================
LOG FILE GENERATOR - CYBER SECURITY UTILITY
==================================================

==================================================
LOGGING MENU
==================================================
1. Log Calculator Usage
2. Log Student Manager Usage
3. Log Marks Analyzer Usage
4. Log File Handler Usage
5. Log Password Vault Usage
6. Log Custom Activity
7. View Activity Log
8. Clear Log
9. Exit
==================================================
Enter your choice: 1

✓ Activity logged!

Menu again...
Enter your choice: 7

==================================================
ACTIVITY LOG
==================================================
Date: 2024-06-14
Time: 14:30:45
Program: Task_04_Program
Activity: Calculator Program - User performed arithmetic calculations
--------------------------------------------------
Date: 2024-06-14
Time: 14:31:20
Program: Task_04_Program
Activity: Student Manager - User added/viewed student records
--------------------------------------------------
==================================================
```

**File Created:**
`activity_log.txt`

**File Format:**
```
Date: 2024-06-14
Time: 14:30:45
Program: Task_04_Program
Activity: Calculator Program - User performed arithmetic calculations
--------------------------------------------------
Date: 2024-06-14
Time: 14:31:20
Program: Task_04_Program
Activity: Student Manager - User added/viewed student records
--------------------------------------------------
```

**Concepts Covered:**
- datetime module
- Timestamp logging
- File operations
- Pre-defined and custom activities
- Logging systems
- Security monitoring

**datetime Format Codes:**
| Code | Meaning | Example |
|------|---------|---------|
| %Y | Year | 2024 |
| %m | Month | 06 |
| %d | Day | 14 |
| %H | Hour | 14 |
| %M | Minute | 30 |
| %S | Second | 45 |

**Features:**
- ✓ Auto date/time logging
- ✓ Pre-defined activity types
- ✓ Custom activity logging
- ✓ View activity history
- ✓ Clear logs with confirmation
- ✓ Program start/exit logging
- ✓ Formatted timestamp output

**Functions Used:**
- `log_activity()` - Record activity
- `display_log()` - Show activity history
- `clear_log()` - Clear all logs
- `log_menu()` - Main menu

---

## 🔧 Requirements

- Python 3.6 or higher
- No external libraries required
- Uses only Python standard library (datetime, os)

**Check Python version:**
```bash
python --version
```

---

## 📝 Running Each Program

### Program 1: Calculator
```bash
python Task_04_calculator_functions.py
# Choose operation (1-4)
# Enter two numbers
# Get result
```

### Program 2: Student Manager
```bash
python Task_04_student_manager.py
# Add students or view all
# Menu-driven interface
```

### Program 3: Marks Analyzer
```bash
python Task_04_marks_analyzer.py
# Enter marks for 5 subjects
# Get total, percentage, grade
```

### Program 4: File Handler
```bash
python Task_04_file_handling.py
# Save, read, or clear student data
# Creates student_data.txt
```

### Program 5: Password Vault
```bash
python Task_04_password_vault.py
# Add, view, or clear credentials
# Creates password_vault.txt
```

### Program 6: Activity Logger
```bash
python Task_04_activity_log_generator.py
# Log activities and view history
# Creates activity_log.txt
```

---

## 💡 Learning Objectives

By completing this task, you will learn:

✓ **Functions & Modularity**
- Function definition and calling
- Parameters and return values
- Scope and namespaces
- Code reusability

✓ **File Handling**
- File I/O operations (read, write, append)
- File modes and paths
- Exception handling for files
- File existence checking

✓ **Data Structures**
- Dictionaries for structured data
- Lists for collections
- Data organization
- Data persistence

✓ **Menu Systems**
- Menu-driven programming
- User input handling
- Choice validation
- Loop control

✓ **Exception Handling**
- Try-except blocks
- Specific exception handling
- Error messages
- Graceful degradation

✓ **Date & Time**
- datetime module
- Timestamp generation
- Time formatting
- Logging with timestamps

✓ **Best Practices**
- Input validation
- Error handling
- Code organization
- User-friendly interfaces

---

## 🧪 Testing Guide

### Test Case 1: Calculator - Division by Zero
```
Choice: 4 (Division)
First Number: 10
Second Number: 0
Expected: Error message "Division by zero!"
```

### Test Case 2: Marks Analyzer - Invalid Marks
```
Enter marks for Math: 150
Expected: Error message "Marks must be between 0 and 100!"
```

### Test Case 3: File Handler - Create File
```
Choice: 1 (Add Record)
Fill all fields
Expected: student_data.txt created with record
```

### Test Case 4: Student Manager - Empty Field
```
Enter Student Name: (leave blank)
Expected: Error message "All fields are required!"
```

### Test Case 5: Password Vault - Clear Vault
```
Choice: 3 (Clear Vault)
Confirm: no
Expected: "Operation cancelled"
```

---

## ⚠️ Common Errors & Solutions

### FileNotFoundError
**Problem:** File doesn't exist when reading  
**Solution:** Create file by saving data first

### ValueError: invalid literal for float()
**Problem:** User enters non-numeric marks  
**Solution:** Program validates and asks again

### IOError
**Problem:** Cannot write to file (permissions)  
**Solution:** Check file permissions and disk space

### IndexError
**Problem:** Accessing invalid list index  
**Solution:** Always check list length first

### Empty File Error
**Problem:** Reading from empty file  
**Solution:** Check if file exists and has content

---

## 📊 Files Generated

| File Name | Purpose | Created By |
|-----------|---------|-----------|
| student_data.txt | Student records | File Handling |
| password_vault.txt | Credentials | Password Vault |
| activity_log.txt | Activity history | Activity Logger |

---

## 📂 Folder Structure

```
Task_04/
├── Task_04_calculator_functions.py
├── Task_04_student_manager.py
├── Task_04_marks_analyzer.py
├── Task_04_file_handling.py
├── Task_04_password_vault.py
├── Task_04_activity_log_generator.py
└── README.md (this file)
```

---

## 🎯 Practice Challenges

### Easy Challenges:
1. Add more operations to calculator (power, square root)
2. Add search functionality to student manager
3. Display average marks in marks analyzer

### Medium Challenges:
1. Export student data to CSV file
2. Add password strength checker
3. Create backup of vault

### Hard Challenges:
1. Add database support instead of text files
2. Implement basic encryption for passwords
3. Create statistics dashboard
4. Build a GUI version using tkinter

---

## 📚 Key Programming Concepts

### Functions
```python
def function_name(parameters):
    """Docstring explaining function"""
    # code
    return result

result = function_name(arguments)
```

### File Handling
```python
# Write/Append
with open("file.txt", 'a') as f:
    f.write("data")

# Read
with open("file.txt", 'r') as f:
    content = f.read()
```

### Dictionaries
```python
student = {
    "name": "John",
    "age": 20
}
student["name"]  # Access value
```

### Lists
```python
students = []
students.append(student)  # Add
for s in students:        # Loop
    print(s)
```

---

## 🔗 Related Topics to Study

- Object-oriented programming (Classes)
- Database operations (SQLite)
- Web frameworks (Flask, Django)
- API development
- Data encryption
- User authentication

---

## 📖 Additional Resources

### Official Documentation
- [Python Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [File I/O](https://docs.python.org/3/tutorial/inputoutput.html)
- [datetime module](https://docs.python.org/3/library/datetime.html)
- [os module](https://docs.python.org/3/library/os.html)

### Learning Platforms
- W3Schools Python Tutorial
- Real Python Articles
- GeeksforGeeks Python Guide

---

## 📝 Code Quality Standards

✓ **Readability**
- Clear variable names
- Proper indentation (4 spaces)
- Comments for complex logic

✓ **Functionality**
- All features working
- Error handling present
- Input validation

✓ **Documentation**
- Function docstrings
- Usage examples
- Clear comments

✓ **Testing**
- Multiple test cases
- Edge case handling
- Error conditions

---

## ✅ Completion Checklist

- [ ] All 6 programs run without errors
- [ ] Input validation works correctly
- [ ] File operations function properly
- [ ] Menu navigation works smoothly
- [ ] Output is properly formatted
- [ ] No crashes or infinite loops
- [ ] Code is readable with comments
- [ ] Tested with multiple inputs
- [ ] Bonus program completed
- [ ] Ready to push to GitHub

---


## 📞 Debugging Tips

1. **Print variable values** to track execution
2. **Test with simple inputs** before complex ones
3. **Check file paths** for file operations
4. **Validate all inputs** before processing
5. **Read error messages** carefully
6. **Use try-except** for error handling

---

## ⚠️ Important Reminders

- All files are created in the program's directory
- No external libraries required
- Always validate user input
- Handle exceptions gracefully
- Test thoroughly before submitting
- Comment your code
- Follow PEP 8 style guide

---

**Author:** Janani
**Version:** 1.0 - Corrected and Verified  
**Status:** ✅ Ready for Submission  
**Date:** June 2024