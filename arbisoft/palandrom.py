import sys


def is_palindrome(word):
    # Convert the word to lowercase to make the check case-insensitive
    word = word.lower()
    return word == word[::-1]


def check_palindrome_from_file(file_path):
    with open(file_path, 'r') as file:
        word = file.readline().strip()
        return "TRUE" if is_palindrome(word) else "FALSE"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a file path as an argument")
    else:
        file_path = sys.argv[1]
        result = check_palindrome_from_file(file_path)
        print(result)

# Usage: python script_name.py input_file.txt


def is_palindrome(word):
    # Convert the word to lowercase to make the check case-insensitive
    word = word.lower()
    return word == word[::-1]


def check_palindrome_from_file(file_path):
    with open(file_path, 'r') as file:
        word = file.readline().strip()
        return "TRUE" if is_palindrome(word) else "FALSE"


# Replace 'input_file.txt' with the actual file path
result = check_palindrome_from_file('input_file.txt')
print(result)
