# Lesson 5: File Handling
# 1. Exploring Python's OS Module

import os

def list_directory_contents(path):
    try:
        if os.path.exists(path):
            print(f"Contents of directory '{path}':")
            for item in os.listdir(path):
                print(item)
        else:
            print(f"Directory '{path}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
user_directory = "/Users/kurtistoledo/github/Assignments-File-Handling"
list_directory_contents(user_directory)

def report_file_sizes(directory):
    try:
        if os.path.exists(directory):
            print(f"File sizes in directory '{directory}':")
            for item in os.listdir(directory):
                item_path = os.path.join(directory, item)
                if os.path.isfile(item_path):
                    size_bytes = os.path.getsize(item_path)
                    print(f"{item}: {size_bytes} bytes")
        else:
            print(f"Directory '{directory}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
report_file_sizes(user_directory)

def count_file_extensions(directory):
    try:
        if os.path.exists(directory):
            extension_count = {}
            for item in os.listdir(directory):
                item_path = os.path.join(directory, item)
                if os.path.isfile(item_path):
                    _, extension = os.path.splitext(item)
                    extension = extension.lower()  # Normalize to lowercase
                    extension_count[extension] = extension_count.get(extension, 0) + 1

            print("File extension counts:")
            for ext, count in extension_count.items():
                print(f"{ext}: {count}")
        else:
            print(f"Directory '{directory}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
count_file_extensions(user_directory)

