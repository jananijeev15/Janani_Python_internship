# Task 03 - Part C: Pattern Printing Challenge

def pattern_1():
    """Print increasing star pattern"""
    print("\nPattern 1: Increasing Stars")
    print("-" * 25)
    for i in range(1, 6):
        print("* " * i)

def pattern_2():
    """Print decreasing star pattern"""
    print("\nPattern 2: Decreasing Stars")
    print("-" * 25)
    for i in range(5, 0, -1):
        print("* " * i)

def pattern_3():
    """Print number sequence pattern"""
    print("\nPattern 3: Number Sequence")
    print("-" * 25)
    for i in range(1, 6):
        row = ""
        for j in range(1, i + 1):
            row += str(j)
        print(row)

def main():
    print("\n" + "="*35)
    print("PATTERN PRINTING CHALLENGE")
    print("="*35)
    
    pattern_1()
    pattern_2()
    pattern_3()
    
    print("\n" + "="*35)
    print("All patterns printed successfully!")
    print("="*35)

if __name__ == "__main__":
    main()