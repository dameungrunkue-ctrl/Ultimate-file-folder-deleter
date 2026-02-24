# Ultimate File Deleter

import os
import sys

# Function to delete files in a directory

def delete_files_in_directory(directory):
    try:
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f'Deleted: {file_path}')
            elif os.path.isdir(file_path):
                print(f'Skipping directory: {file_path}')
    except Exception as e:
        print(f'Error: {e}')

# Main function

def main():
    if len(sys.argv) != 2:
        print('Usage: python ultimate-file-deleter.py <directory_to_clean>')
        sys.exit(1)

    directory = sys.argv[1]
    delete_files_in_directory(directory)

if __name__ == '__main__':
    main()