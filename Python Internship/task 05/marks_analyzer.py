"""
Task 05 - Part A: Student Marks Analyzer
Accepts marks of 5 students and displays Highest, Lowest, and Average marks.
"""

def main():
    marks = []
    print("Enter marks of 5 students:")
    for i in range(5):
        while True:
            try:
                mark = float(input(f"Enter marks of student {i + 1}: "))
                marks.append(mark)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    highest = max(marks)
    lowest = min(marks)
    average = sum(marks) / len(marks)

    print("\n--- Marks Analysis Report ---")
    print(f"Highest Marks: {highest}")
    print(f"Lowest Marks: {lowest}")
    print(f"Average Marks: {average:.2f}")


if __name__ == "__main__":
    main()
