marks = int(input("Enter marks: "))

if marks >= 90 and marks <= 100:
    grade = 'A'
elif marks >= 80 and marks <= 89:
    grade = 'B'
elif marks >= 70 and marks <= 79:
    grade = 'C'
elif marks >= 60 and marks <= 69:
    grade = 'D'
else:
    grade = 'F'

print(f"Grade: {grade}")