# Final Project – Student Cyber Security Management System

---

## 1. Project Title
**Student Cyber Security Management System**

A comprehensive menu-driven Python and C application designed to manage student records and assess their cybersecurity posture during an internship program. This project combines all fundamental programming concepts learned throughout the internship into one integrated mini-application.

---

## 2. Objective
The purpose of this final task is to combine everything learned throughout the internship:
- **Variables** – Store student data and security assessment results
- **Input/Output** – Accept user input and display formatted output
- **Conditional Statements** – Branch logic based on user choices and security criteria
- **Loops** – Iterate through student records, validate input, and display data
- **Functions** – Modularize code into reusable, maintainable functions
- **Arrays/Lists** – Store multiple student records and manage collections of data
- **File Handling** – Persist student records to disk using `students.txt` (save, read, update, delete operations)
- **Problem Solving** – Apply real-world cybersecurity concepts in a practical application

The goal is to build a **mini application** (rather than separate programs) that demonstrates integration of all these concepts in a single, cohesive system.

---

## 3. Features

### Core Modules

#### **Module 1: Add Student**
- Allows users to add a new student record to the system
- Collects: Student Name, Student ID, Branch, and Email Address
- Validates input to prevent duplicate IDs and missing fields
- Automatically saves the record to `students.txt`

#### **Module 2: View Students**
- Displays all student records in a clear, formatted table
- Shows: ID, Name, Branch, Email, Security Score, and Status
- Provides a snapshot of all students in the system

#### **Module 3: Search Student**
- Searches for a student by:
  - Student Name (case-insensitive)
  - Student ID
- Displays the matching record with complete details
- Shows "Record Not Found" if no match is found

#### **Module 4: Delete Student**
- Removes a student record by Student ID
- Shows a confirmation message upon successful deletion
- Updates `students.txt` to reflect the deletion

#### **Module 5: Security Assessment**
- Evaluates a student's cybersecurity practices by asking:
  - Is MFA (Multi-Factor Authentication) Enabled?
  - Password Length?
  - System Updated?
  - Antivirus Installed?
- **Scoring Formula** (out of 100):
  - MFA Enabled: +25 points
  - Password Length ≥12: +25 points (≥8: +15 points)
  - System Updated: +25 points
  - Antivirus Installed: +25 points
- **Security Status Categories**:
  - **Excellent**: 90–100 points
  - **Good Security Practices**: 70–89 points
  - **Moderate**: 40–69 points
  - **Poor**: 0–39 points
- Stores the score and status in the student's record

#### **Module 6: Generate Report**
- Produces a comprehensive security summary showing:
  - Total number of students in the system
  - Individual security scores for each student
  - Average security score across all students
  - List of students with Poor security ratings
  - Helpful insights for the security team

#### **Module 7: File Storage**
- Records are stored in a `students.txt` file using a `|`-delimited format
- The program automatically:
  - **Saves** new and updated records
  - **Reads** existing records at startup
  - **Updates** security assessments
  - **Deletes** student records when requested

### Cyber Security Features (3 of 5 Implemented)

#### **Option 1: Password Strength Checker** ✓ (Implemented)
- Evaluates password quality on a scale of 1–5
- Checks for:
  - Minimum length (8+ characters)
  - Uppercase letters (A–Z)
  - Lowercase letters (a–z)
  - Numbers (0–9)
  - Special characters (!@#$%^&*()etc.)
- Provides actionable feedback to improve weak passwords
- Rates as: Very Strong, Strong, Moderate, Weak, Very Weak

#### **Option 2: Username Generator** ✓ (Implemented)
- Generates multiple username suggestions based on:
  - First name
  - Last name
  - Birth year
- Produces 3 unique username variations for user selection

#### **Option 3: Login Validation** ✓ (Implemented)
- Implements a simple authentication system
- Features:
  - Username and password verification
  - Maximum attempt limit (3 attempts)
  - Account lockout after failed attempts
  - Demonstrates basic login security principles

#### **Not Implemented (Optional)**
- Option 4: Security Awareness Quiz
- Option 5: Blacklist IP Checker

---

## 4. Technologies Used

### Programming Languages
- **Python 3** – Primary implementation language for the application
- **C Programming** – Alternative implementation (optional)

### Libraries & Modules
- **os** – File system operations (check file existence)
- **re** – Regular expressions (password strength validation)

### Data Structures
- **Lists** – In-memory storage of student records
- **Dictionaries** – Structured representation of individual student data
- **Plain Text Files** – Persistent storage using `|`-delimited format

### Concepts & Techniques
- **File I/O** – Read/write operations to `students.txt`
- **Data Validation** – Input checking and error handling
- **Menu-Driven Architecture** – Loop-based user interface
- **Modular Design** – Separate functions for each feature
- **Exception Handling** – `try/except` blocks for robust error management

---

## 5. Program Flow

### Startup Phase
```
1. Program launches
2. Load existing student records from students.txt (if file exists)
3. Store records in memory as a list of dictionaries
```

### Main Menu Loop
```
4. Display menu with 10 options:
   1. Add Student
   2. View Students
   3. Search Student
   4. Delete Student
   5. Security Assessment
   6. Generate Report
   7. Password Strength Checker
   8. Username Generator
   9. Login Validation
   10. Exit

5. Prompt user for choice
```

### Processing Flow
```
6. Based on user choice, execute corresponding module:

   Choice 1 (Add Student):
      a. Collect student ID, name, branch, email
      b. Validate that ID is unique
      c. Create new student record
      d. Add to in-memory list
      e. Save updated list to students.txt
      f. Confirm success

   Choice 2 (View Students):
      a. Check if any records exist
      b. Iterate through each student record
      c. Format and display all student details

   Choice 3 (Search Student):
      a. Ask user for search criteria (name or ID)
      b. Get search query from user
      c. Loop through records to find match (case-insensitive)
      d. Display matching record or "not found" message

   Choice 4 (Delete Student):
      a. Ask for student ID to delete
      b. Find matching record in list
      c. Remove from list
      d. Save updated list to students.txt
      e. Confirm deletion

   Choice 5 (Security Assessment):
      a. Ask for student ID
      b. Collect security answers (MFA, password length, updates, antivirus)
      c. Calculate security score using weighted formula
      d. Determine status category
      e. Update student record with score and status
      f. Save to students.txt

   Choice 6 (Generate Report):
      a. Read all student records
      b. Calculate total count
      c. Compute average security score
      d. Identify poor-rated students
      e. Display formatted summary report

   Choices 7–9 (Security Tools):
      a. Run respective cybersecurity utility
      b. Provide feedback to user
      c. Return to main menu

   Choice 10 (Exit):
      a. Terminate program gracefully
```

### Data Persistence
```
7. After every operation that modifies student data:
   - Update in-memory list
   - Overwrite students.txt with current state
   - Ensure no data loss between sessions
```

### Termination
```
8. User selects Exit
9. All data already saved to students.txt
10. Program closes
```

---

## 6. Challenges Faced

### Data Persistence Challenge
- **Problem**: Had to design a simple yet effective file format to store structured student records in plain text while maintaining data integrity across sessions.
- **Solution**: Chose a `|`-delimited format (e.g., `101|Soham Patel|CSE|soham@example.com|85|Good`) that is easy to parse and human-readable.

### Synchronization Challenge
- **Problem**: Keeping the in-memory list and the `students.txt` file in sync after every modification (add, delete, assess) to prevent data loss or inconsistencies.
- **Solution**: Implemented a `save_students()` function that overwrites the entire file after every operation, ensuring consistency.

### Input Validation Challenge
- **Problem**: Handling invalid inputs (non-numeric marks, empty fields, improper data types) without crashing the program.
- **Solution**: Used `try/except` blocks for numeric conversions and explicit checks for empty/required fields.

### Security Scoring Challenge
- **Problem**: Creating a fair, meaningful scoring formula that produces realistic Excellent/Good/Moderate/Poor categories without over-weighting individual factors.
- **Solution**: Assigned proportional weights (25 points each for MFA, password, updates, antivirus) and set category thresholds based on security best practices (90+ = Excellent, 70+ = Good, 40+ = Moderate, <40 = Poor).

### Integration Challenge
- **Problem**: Combining six+ distinct modules (add, view, search, delete, assess, report) and three cybersecurity tools into one cohesive application without making the code unwieldy or repetitive.
- **Solution**: Used a modular design with separate functions for each feature, a central main loop for menu handling, and shared file I/O helpers to avoid duplication.

### User Experience Challenge
- **Problem**: Designing an intuitive menu-driven interface that is easy to navigate while remaining beginner-friendly.
- **Solution**: Clear menu formatting with numbered options, descriptive prompts, and success/error messages that guide users through each operation.

### Case-Sensitivity Challenge
- **Problem**: Searches and comparisons failing when users enter input with different casing (e.g., "JOHN" vs "john").
- **Solution**: Converted all search queries and student names to lowercase before comparison using `.lower()` method.

---

## 7. Learning Outcomes

### Core Programming Concepts
✓ **Variables & Data Types** – Successfully used strings, integers, floats, and lists to represent student data  
✓ **Input/Output** – Implemented user prompts and formatted output for readability  
✓ **Conditional Logic** – Applied if/elif/else statements for menu navigation and security scoring  
✓ **Loops** – Used while loops for the main menu and for loops to iterate through student records  
✓ **Functions** – Modularized code into reusable functions for each feature  
✓ **Lists & Dictionaries** – Managed collections of student records efficiently  
✓ **File Handling** – Mastered reading, writing, and updating persistent data storage  

### Real-World Application Skills
✓ Gained practical experience building a **complete, functional application** instead of isolated coding exercises  
✓ Learned to **integrate multiple features** into a single cohesive system  
✓ Understood how **data persistence** works in real applications (save/load from disk)  
✓ Practiced **problem decomposition** by breaking a large project into manageable modules  
✓ Experienced the importance of **error handling** and input validation in user-facing applications  

### Cybersecurity Knowledge
✓ Learned practical cybersecurity concepts:
  - Multi-Factor Authentication (MFA) and its importance
  - Password strength principles (length, character diversity)
  - System patching and updates as a security baseline
  - Antivirus software role in endpoint protection
  
✓ Implemented three cybersecurity tools from scratch:
  - Password strength evaluation (regular expressions, scoring)
  - Username generation (string manipulation)
  - Login validation with rate limiting (basic authentication)

### Professional Development
✓ Experienced **iterative development** – building features incrementally and testing each module  
✓ Practiced **code documentation** – adding comments and creating a comprehensive README  
✓ Learned **user-centric design** – creating menus and messages that are clear and helpful  
✓ Developed **debugging skills** – identifying and fixing issues during development  
✓ Strengthened **problem-solving mindset** – approaching complex tasks systematically  

### Project Management
✓ Successfully managed a **multi-module project** with interdependent components  
✓ Maintained **code organization** using folders and clear naming conventions  
✓ Created **documentation** explaining features, flow, and usage  
✓ Gained confidence for **future projects** combining multiple internship learnings  

---

## Folder Structure
```
Final_Project_YourName/
├── Python Version/
│   └── student_security_manager.py
├── C Version/
│   └── student_security_manager.c (optional)
├── Documentation/
│   ├── Project_Report.pdf
│   └── Screenshots/
│       ├── main_menu.png
│       ├── add_student.png
│       ├── view_students.png
│       ├── security_assessment.png
│       └── generate_report.png
├── students.txt (auto-created on first run)
└── README.md
```

---

## GitHub Repository Structure
```
CyberSecurity_Internship/
├── Task_01/
│   └── [Task 01 files]
├── Task_02/
│   └── [Task 02 files]
├── Task_03/
│   └── [Task 03 files]
├── Task_04/
│   └── [Task 04 files]
├── Task_05/
│   ├── Python Files/
│   │   ├── marks_analyzer.py
│   │   ├── employee_search.py
│   │   ├── statistics_tool.py
│   │   ├── log_analyzer.py
│   │   └── blacklist_checker.py
│   ├── C Files/
│   │   ├── marks_analyzer.c
│   │   ├── employee_search.c
│   │   ├── statistics_tool.c
│   │   ├── log_analyzer.c
│   │   └── blacklist_checker.c
│   ├── Bonus/
│   │   └── contact_manager_bonus.py
│   └── README.md
└── Final_Project/
    ├── Python Version/
    │   └── student_security_manager.py
    ├── C Version/
    │   └── student_security_manager.c
    ├── Documentation/
    │   ├── Project_Report.pdf
    │   └── Screenshots/
    ├── README.md
    └── students.txt
```

---

## How to Run

### Prerequisites
- Python 3.6+ installed on your system
- (Optional) GCC compiler for C version

### Python Version
```bash
cd Final_Project/Python\ Version/
python3 student_security_manager.py
```

### C Version (Optional)
```bash
cd Final_Project/C\ Version/
gcc student_security_manager.c -o student_security_manager
./student_security_manager
```

---

## Usage Example

```
==========================
 Student Security Manager
==========================
1. Add Student
2. View Students
3. Search Student
4. Delete Student
5. Security Assessment
6. Generate Report
7. Password Strength Checker
8. Username Generator
9. Login Validation
10. Exit

Enter your choice: 1

--- Add Student ---
Enter Student ID: 101
Enter Student Name: Soham Patel
Enter Branch: CSE
Enter Email Address: soham@example.com
Student added successfully!

[... menu returns ...]

Enter your choice: 5

--- Security Assessment ---
Enter Student ID for assessment: 101
Is MFA Enabled? (yes/no): yes
Password Length?: 12
System Updated? (yes/no): yes
Antivirus Installed? (yes/no): yes

Security Score: 100/100
Status: Excellent
```

---

## Submission Checklist
- [ ] All Python source code is present and working
- [ ] All C source code is present (optional but recommended)
- [ ] `students.txt` is created on first run
- [ ] All modules (Add, View, Search, Delete, Assess, Report) are functional
- [ ] All three cybersecurity features are implemented
- [ ] Code is well-commented and readable
- [ ] README.md is comprehensive and complete
- [ ] Screenshots showing program execution are included
- [ ] Project is uploaded to GitHub before the deadline
- [ ] GitHub repository link is submitted through the Sunday Submission Form

---

## Notes
This project is **not about creating a perfect application**. It is about demonstrating your **growth throughout the internship** and applying the concepts you have learned in a **practical way**. Focus on:
- **Clean code** – Readable variable names, proper indentation, logical organization
- **Proper documentation** – Comments explaining complex logic, comprehensive README
- **Understanding your implementation** – You should be able to explain every part of your code
- A **well-structured project with clear logic** is more valuable than a complex project that you cannot explain.

## Folder Structure
```
Final_Project_YourName/
├── Python Version/
│   └── student_security_manager.py
├── C Version/
│   └── student_security_manager.c
├── Documentation/
│   ├── Project_Report.pdf
│   └── Screenshots/
├── students.txt
├── README.md
```

## GitHub Repository Structure
```
CyberSecurity_Internship/
├── Task_01
├── Task_02
├── Task_03
├── Task_04
├── Task_05
└── Final_Project
```

## How to Run

### Python
```
python3 student_security_manager.py
```
The program will automatically create `students.txt` in the same directory the first time a student is added.

### C
```
gcc student_security_manager.c -o student_security_manager
./student_security_manager
```
