"""
Task 05 - Part E: Blacklisted IP Checker
Checks whether a user-entered IP address exists in a blacklist.
"""

def main():
    blacklisted_ips = ["192.168.1.10", "10.0.0.5", "172.16.1.100", "192.168.0.50"]

    print("Blacklisted IPs:", blacklisted_ips)
    ip_address = input("Enter an IP Address to check: ").strip()

    if ip_address in blacklisted_ips:
        print("IP Found in Blacklist")
    else:
        print("IP Not Found")


if __name__ == "__main__":
    main()
