"""
Task 05 - Part C: Number Statistics Tool
Accepts 10 numbers and displays largest, smallest, sum, average,
count of even numbers and count of odd numbers.
"""

def main():
    numbers = []
    print("Enter 10 numbers:")
    for i in range(10):
        while True:
            try:
                num = int(input(f"Enter number {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    largest = max(numbers)
    smallest = min(numbers)
    total = sum(numbers)
    average = total / len(numbers)
    even_count = len([n for n in numbers if n % 2 == 0])
    odd_count = len([n for n in numbers if n % 2 != 0])

    print("\n--- Number Statistics ---")
    print(f"Largest Number: {largest}")
    print(f"Smallest Number: {smallest}")
    print(f"Sum: {total}")
    print(f"Average: {average:.2f}")
    print(f"Even Numbers: {even_count}")
    print(f"Odd Numbers: {odd_count}")


if __name__ == "__main__":
    main()
