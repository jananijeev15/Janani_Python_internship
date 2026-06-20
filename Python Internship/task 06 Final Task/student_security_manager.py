"""
Final Task 06: Student Cyber Security Management System
A menu-driven Python application to manage student records and
basic cyber security information. Records are persisted to students.txt.

Cyber Security Features implemented (3 of 5):
  1. Password Strength Checker
  2. Username Generator
  3. Login Validation
"""

import os
import re

FILE_NAME = "students.txt"
DELIMITER = "|"


# ---------------------------------------------------------------------------
# File Handling Helpers
# ---------------------------------------------------------------------------

def load_students():
    """Read all student records from students.txt into a list of dicts."""
    students = []
    if not os.path.exists(FILE_NAME):
        return students

    with open(FILE_NAME, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(DELIMITER)
            if len(parts) == 6:
                students.append({
                    "id": parts[0],
                    "name": parts[1],
                    "branch": parts[2],
                    "email": parts[3],
                    "score": parts[4],
                    "status": parts[5],
                })
    return students


def save_students(students):
    """Overwrite students.txt with the current list of student records."""
    with open(FILE_NAME, "w") as file:
        for s in students:
            line = DELIMITER.join([
                s["id"], s["name"], s["branch"], s["email"],
                s.get("score", "N/A"), s.get("status", "N/A")
            ])
            file.write(line + "\n")


# ---------------------------------------------------------------------------
# Module 1: Add Student
# ---------------------------------------------------------------------------

def add_student(students):
    print("\n--- Add Student ---")
    student_id = input("Enter Student ID: ").strip()

    for s in students:
        if s["id"] == student_id:
            print("Error: A student with this ID already exists.")
            return

    name = input("Enter Student Name: ").strip()
    branch = input("Enter Branch: ").strip()
    email = input("Enter Email Address: ").strip()

    if not student_id or not name or not branch or not email:
        print("Error: All fields are required.")
        return

    students.append({
        "id": student_id,
        "name": name,
        "branch": branch,
        "email": email,
        "score": "N/A",
        "status": "N/A",
    })
    save_students(students)
    print("Student added successfully!")


# ---------------------------------------------------------------------------
# Module 2: View Students
# ---------------------------------------------------------------------------

def view_students(students):
    print("\n--- All Student Records ---")
    if not students:
        print("No student records found.")
        return

    for s in students:
        print("-" * 30)
        print(f"ID: {s['id']}")
        print(f"Name: {s['name']}")
        print(f"Branch: {s['branch']}")
        print(f"Email: {s['email']}")
        print(f"Security Score: {s['score']}")
        print(f"Status: {s['status']}")
    print("-" * 30)


# ---------------------------------------------------------------------------
# Module 3: Search Student
# ---------------------------------------------------------------------------

def search_student(students):
    print("\n--- Search Student ---")
    if not students:
        print("No student records found.")
        return

    print("Search by: 1. Name  2. Student ID")
    choice = input("Enter choice: ").strip()
    query = input("Enter search value: ").strip().lower()

    found = False
    for s in students:
        if (choice == "1" and s["name"].lower() == query) or \
           (choice == "2" and s["id"].lower() == query):
            found = True
            print("\nRecord Found:")
            print(f"ID: {s['id']}, Name: {s['name']}, Branch: {s['branch']}, "
                  f"Email: {s['email']}, Score: {s['score']}, Status: {s['status']}")
            break

    if not found:
        print("Record Not Found.")


# ---------------------------------------------------------------------------
# Module 4: Delete Student
# ---------------------------------------------------------------------------

def delete_student(students):
    print("\n--- Delete Student ---")
    student_id = input("Enter Student ID to delete: ").strip()

    for s in students:
        if s["id"] == student_id:
            students.remove(s)
            save_students(students)
            print(f"Student with ID {student_id} deleted successfully.")
            return

    print("Student ID not found.")


# ---------------------------------------------------------------------------
# Module 5: Security Assessment
# ---------------------------------------------------------------------------

def security_assessment(students):
    print("\n--- Security Assessment ---")
    student_id = input("Enter Student ID for assessment: ").strip()

    target = None
    for s in students:
        if s["id"] == student_id:
            target = s
            break

    if not target:
        print("Student ID not found.")
        return

    mfa = input("Is MFA Enabled? (yes/no): ").strip().lower() == "yes"
    try:
        password_length = int(input("Password Length?: ").strip())
    except ValueError:
        password_length = 0
    system_updated = input("System Updated? (yes/no): ").strip().lower() == "yes"
    antivirus = input("Antivirus Installed? (yes/no): ").strip().lower() == "yes"

    score = 0
    score += 25 if mfa else 0
    score += 25 if password_length >= 12 else (15 if password_length >= 8 else 0)
    score += 25 if system_updated else 0
    score += 25 if antivirus else 0

    if score >= 90:
        status = "Excellent"
    elif score >= 70:
        status = "Good Security Practices"
    elif score >= 40:
        status = "Moderate"
    else:
        status = "Poor"

    target["score"] = str(score)
    target["status"] = status
    save_students(students)

    print(f"\nSecurity Score: {score}/100")
    print(f"Status: {status}")


# ---------------------------------------------------------------------------
# Module 6: Generate Report
# ---------------------------------------------------------------------------

def generate_report(students):
    print("\n--- Security Summary Report ---")
    if not students:
        print("No student records found.")
        return

    total_students = len(students)
    scored_students = [int(s["score"]) for s in students if s["score"] != "N/A"]

    print(f"Total Students: {total_students}")

    print("\nSecurity Scores:")
    for s in students:
        print(f"  {s['name']} (ID: {s['id']}): {s['score']}")

    if scored_students:
        average_score = sum(scored_students) / len(scored_students)
        print(f"\nAverage Security Score: {average_score:.2f}")
    else:
        print("\nAverage Security Score: N/A (no assessments completed yet)")

    poor_students = [s["name"] for s in students if s["status"] == "Poor"]
    print("\nStudents with Poor Security Ratings:")
    if poor_students:
        for name in poor_students:
            print(f"  - {name}")
    else:
        print("  None")


# ---------------------------------------------------------------------------
# Cyber Security Feature 1: Password Strength Checker
# ---------------------------------------------------------------------------

def password_strength_checker():
    print("\n--- Password Strength Checker ---")
    password = input("Enter a password to check: ")

    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    levels = {5: "Very Strong", 4: "Strong", 3: "Moderate", 2: "Weak", 1: "Very Weak", 0: "Very Weak"}
    print(f"Password Strength: {levels[score]} ({score}/5)")

    if feedback:
        print("Suggestions:")
        for tip in feedback:
            print(f"  - {tip}")


# ---------------------------------------------------------------------------
# Cyber Security Feature 2: Username Generator
# ---------------------------------------------------------------------------

def username_generator():
    print("\n--- Username Generator ---")
    first_name = input("Enter first name: ").strip()
    last_name = input("Enter last name: ").strip()
    birth_year = input("Enter birth year (e.g. 2003): ").strip()

    base = (first_name[:3] + last_name[:3]).lower() if first_name and last_name else "user"
    suggestions = [
        f"{base}{birth_year}",
        f"{first_name.lower()}.{last_name.lower()}",
        f"{first_name.lower()}_{last_name.lower()}{birth_year[-2:] if len(birth_year) >= 2 else ''}",
    ]

    print("Suggested Usernames:")
    for s in suggestions:
        print(f"  - {s}")


# ---------------------------------------------------------------------------
# Cyber Security Feature 3: Login Validation
# ---------------------------------------------------------------------------

def login_validation():
    print("\n--- Login Validation ---")
    # Simple demo credentials for validation logic
    correct_username = "admin"
    correct_password = "Admin@123"

    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        username = input("Enter Username: ").strip()
        password = input("Enter Password: ").strip()

        if username == correct_username and password == correct_password:
            print("Login Successful!")
            return
        else:
            attempts += 1
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"Invalid credentials. Attempts remaining: {remaining}")
            else:
                print("Login Failed. Maximum attempts exceeded. Account locked.")


# ---------------------------------------------------------------------------
# Main Menu
# ---------------------------------------------------------------------------

def main():
    students = load_students()

    while True:
        print("\n==========================")
        print(" Student Security Manager")
        print("==========================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Security Assessment")
        print("6. Generate Report")
        print("7. Password Strength Checker")
        print("8. Username Generator")
        print("9. Login Validation")
        print("10. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            security_assessment(students)
        elif choice == "6":
            generate_report(students)
        elif choice == "7":
            password_strength_checker()
        elif choice == "8":
            username_generator()
        elif choice == "9":
            login_validation()
        elif choice == "10":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
