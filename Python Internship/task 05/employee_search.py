"""
Task 05 - Part B: Employee Record Search
Stores a list of employee names and searches for a given name.
"""

def main():
    employees = ["John", "Alice", "David", "Sophia", "Michael"]

    print("Employee Records:", employees)
    search_name = input("Enter the name to search: ").strip()

    found = False
    for name in employees:
        if name.lower() == search_name.lower():
            found = True
            break

    if found:
        print("Record Found")
    else:
        print("Record Not Found")


if __name__ == "__main__":
    main()
