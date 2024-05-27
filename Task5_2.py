# Lesson 5: File Handling
# 2. Regex-Powered Text Data Processing

import re

def extract_emails(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            # Define a regular expression pattern for extracting emails
            email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}\b'
            # Find all email addresses in the text using the pattern
            email_addresses = re.findall(email_pattern, content)
            # Remove duplicates by converting to a set and then back to a list
            unique_emails = list(set(email_addresses))
            return unique_emails
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
contacts_file = "contacts.txt"
extracted_emails = extract_emails(contacts_file)
if extracted_emails:
    print("Extracted email addresses:")
    for email in extracted_emails:
        print(email)
