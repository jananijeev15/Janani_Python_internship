"""
Task 05 - Part D: Cyber Security Log Analyzer
Stores login attempts and displays totals for success/failure.
"""

def main():
    login_attempts = ["Success", "Failed", "Failed", "Success", "Failed", "Success"]

    total_attempts = len(login_attempts)
    successful_logins = login_attempts.count("Success")
    failed_logins = login_attempts.count("Failed")

    print("--- Login Attempt Log ---")
    print(login_attempts)

    print("\n--- Report ---")
    print(f"Total Attempts: {total_attempts}")
    print(f"Successful Logins: {successful_logins}")
    print(f"Failed Logins: {failed_logins}")

    print("\nWhy monitoring failed logins matters:")
    print("Repeated failed login attempts can indicate a brute-force attack,")
    print("credential stuffing, or an unauthorized user trying to guess a password.")
    print("Tracking failed logins helps detect intrusions early, trigger account")
    print("lockouts, and alert security teams before an attacker gains access.")


if __name__ == "__main__":
    main()
