# Task 03 - Part A: Multiplication Table Generator

def multiplication_table(number):
    """Generate multiplication table for a given number"""
    print(f"\nMultiplication Table for {number}:")
    print("-" * 35)
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i:2d} = {result}")
    print("-" * 35)

def main():
    while True:
        try:
            number = int(input("\nEnter a number: "))
            if number == 0:
                print("Please enter a non-zero number!")
                continue
            multiplication_table(number)
            break
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()