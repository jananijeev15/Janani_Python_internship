# Task 03 - Part E: Username Generator

def generate_usernames(first_name, last_name, birth_year):
    """Generate multiple username suggestions"""
    usernames = []
    
    # Username 1: firstnamelastnamebirthyear
    username1 = (first_name + last_name + str(birth_year)).lower()
    usernames.append(username1)
    
    # Username 2: f.lastname + last 2 digits of year
    username2 = (first_name[0] + "." + last_name + str(birth_year)[-2:]).lower()
    usernames.append(username2)
    
    # Username 3: lastname_firstname
    username3 = (last_name + "_" + first_name).lower()
    usernames.append(username3)
    
    # Username 4: firstname.lastname
    username4 = (first_name + "." + last_name).lower()
    usernames.append(username4)
    
    # Username 5: firstname + last 4 digits of year
    username5 = (first_name + str(birth_year)[-4:]).lower()
    usernames.append(username5)
    
    return usernames

def main():
    print("\n" + "="*50)
    print("USERNAME GENERATOR - CYBER SECURITY UTILITY")
    print("="*50)
    
    while True:
        try:
            first_name = input("\nEnter First Name: ").strip()
            last_name = input("Enter Last Name: ").strip()
            birth_year = input("Enter Birth Year (YYYY): ").strip()
            
            # Validate inputs
            if not first_name or not last_name:
                print("❌ Please enter valid names!")
                continue
            
            try:
                year = int(birth_year)
                if year < 1900 or year > 2024:
                    print("❌ Please enter a valid birth year (1900-2024)!")
                    continue
            except ValueError:
                print("❌ Birth year must be a number!")
                continue
            
            usernames = generate_usernames(first_name, last_name, year)
            
            print("\n" + "="*50)
            print("SUGGESTED USERNAMES:")
            print("="*50)
            for i, username in enumerate(usernames, 1):
                print(f"{i}. {username}")
            print("="*50)
            break
            
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()