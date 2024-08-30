import json
import sys
import os

def process_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    entries = data.get('entries', [])

    # Counters and sets for unique values
    password_count = 0
    usernames = set()
    passwords = set()
    emails = set()

    # Open files for writing
    with open('userpass.lst', 'w') as userpass_file:
        for entry in entries:
            username = entry.get('username')
            password = entry.get('password')
            email = entry.get('email')

            if password:
                password_count += 1
                userpass_file.write(f'{username}:{password}\n')
                usernames.add(username)
                passwords.add(password)
                emails.add(email)

    # Write unique usernames, passwords, and emails to their respective files
    with open('users.lst', 'w') as users_file:
        for username in sorted(usernames):
            users_file.write(f'{username}\n')

    with open('pass.lst', 'w') as pass_file:
        for password in sorted(passwords):
            pass_file.write(f'{password}\n')

    with open('emails.lst', 'w') as emails_file:
        for email in sorted(emails):
            emails_file.write(f'{email}\n')

    # Output the number of entries containing a password
    print(f'Number of entries containing a password: {password_count}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_json_file>")
        sys.exit(1)

    json_file_path = sys.argv[1]

    if not os.path.exists(json_file_path):
        print(f"File not found: {json_file_path}")
        sys.exit(1)

    process_json_file(json_file_path)
