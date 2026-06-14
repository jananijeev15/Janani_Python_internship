# Task 03 - Part D: Password Attempt Simulator

def password_attempt_simulator():
    """Simulate password authentication with max 3 attempts"""
    correct_password = "secure123"
    max_attempts = 3
    attempts = 0
    
    print("\n" + "="*45)
    print("PASSWORD AUTHENTICATION SYSTEM")
    print("="*45)
    print(f"You have {max_attempts} attempts to enter the correct password")
    print("(For testing, password is: secure123)")
    print("="*45)
    
    while attempts < max_attempts:
        password = input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter password: ")
        
        if password == correct_password:
            print("\n" + "="*45)
            print("✓ ACCESS GRANTED!")
            print("="*45)
            return True
        else:
            attempts += 1
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"❌ Incorrect password! {remaining} attempt(s) remaining.")
            else:
                print("\n" + "="*45)
                print("❌ ACCOUNT LOCKED!")
                print("Maximum attempts exceeded. Access denied.")
                print("="*45)
                return False
    
    return False

def main():
    password_attempt_simulator()

if __name__ == "__main__":
    main()