# Task 03 - Part B: Number Analysis Tool

def number_analysis(n):
    """Analyze numbers from 1 to N"""
    if n <= 0:
        return None, None, None
    
    total_sum = 0
    even_count = 0
    odd_count = 0
    
    for i in range(1, n + 1):
        total_sum += i
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    return total_sum, even_count, odd_count

def main():
    while True:
        try:
            n = int(input("\nEnter a number N: "))
            
            if n <= 0:
                print("❌ Please enter a positive number!")
                continue
            
            total_sum, even_count, odd_count = number_analysis(n)
            
            print("\n" + "="*35)
            print(f"Analysis for numbers 1 to {n}:")
            print("="*35)
            print(f"Sum = {total_sum}")
            print(f"Even Numbers = {even_count}")
            print(f"Odd Numbers = {odd_count}")
            print("="*35)
            break
            
        except ValueError:
            print("❌ Please enter a valid number!")

if __name__ == "__main__":
    main()