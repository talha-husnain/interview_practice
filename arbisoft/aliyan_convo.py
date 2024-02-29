# def encode_word(word):
#     # 6x5 matrix of the alphabet
#     alphabet = [list("ABCDE"), list("FGHIJ"), list("KLMNO"), list(
#         "PQRST"), list("UVWXY"), ["Z", '', '', '', '']]
#     instructions = ""
#     current_position = (0, 0)

#     for letter in word:
#         # Find the position of the letter in the matrix
#         position = [(index, row.index(letter))
#                     for index, row in enumerate(alphabet) if letter in row][0]

#         # Vertical movement
#         vertical_movement = position[0] - current_position[0]
#         if vertical_movement > 0:
#             instructions += 'd' * vertical_movement
#         elif vertical_movement < 0:
#             instructions += 'u' * abs(vertical_movement)

#         # Horizontal movement
#         horizontal_movement = position[1] - current_position[1]
#         if horizontal_movement > 0:
#             instructions += 'r' * horizontal_movement
#         elif horizontal_movement < 0:
#             instructions += 'l' * abs(horizontal_movement)

#         # Select the letter
#         instructions += '#'

#         # Update current position
#         current_position = position

#     return instructions


# # Test the function
# print(encode_word("UP"))
# print(encode_word("UPYOUGO"))


import sys


def find_position_of_letter(letter, alphabet):
    for index, row in enumerate(alphabet):
        if letter in row:
            return index, row.index(letter)
    return None  # Just as a precaution, but this case shouldn't occur


def encode_word(word):
    # 6x5 matrix of the alphabet
    alphabet = [list("ABCDE"), list("FGHIJ"), list("KLMNO"), list(
        "PQRST"), list("UVWXY"), ["Z", '', '', '', '']]
    instructions = ""
    current_position = (0, 0)

    for letter in word:
        # Find the position of the letter in the matrix
        position = find_position_of_letter(letter, alphabet)

        # Vertical movement
        vertical_movement = position[0] - current_position[0]
        if vertical_movement > 0:
            instructions += 'd' * vertical_movement
        elif vertical_movement < 0:
            instructions += 'u' * abs(vertical_movement)

        # Horizontal movement
        horizontal_movement = position[1] - current_position[1]
        if horizontal_movement > 0:
            instructions += 'r' * horizontal_movement
        elif horizontal_movement < 0:
            instructions += 'l' * abs(horizontal_movement)

        # Select the letter
        instructions += '#'

        # Update current position
        current_position = position

    return instructions


# Test the function
print(encode_word("UP"))
print(encode_word("UPYOUGO"))


def find_position_of_letter(letter, alphabet):
    for index, row in enumerate(alphabet):
        if letter in row:
            return index, row.index(letter)
    return None


def encode_word(word, alphabet):
    instructions = ""
    current_position = (0, 0)
    for letter in word:
        position = find_position_of_letter(letter, alphabet)
        vertical_movement = position[0] - current_position[0]
        if vertical_movement > 0:
            instructions += 'd' * vertical_movement
        elif vertical_movement < 0:
            instructions += 'u' * abs(vertical_movement)
        horizontal_movement = position[1] - current_position[1]
        if horizontal_movement > 0:
            instructions += 'r' * horizontal_movement
        elif horizontal_movement < 0:
            instructions += 'l' * abs(horizontal_movement)
        instructions += '#'
        current_position = position
    return instructions


def process_file(file_path):
    alphabet = [list("ABCDE"), list("FGHIJ"), list("KLMNO"), list(
        "PQRST"), list("UVWXY"), ["Z", '', '', '', '']]
    with open(file_path, 'r') as file:
        words = file.readlines()
    for word in words:
        word = word.strip().upper()  # Ensure the word is uppercase
        encoded_instructions = encode_word(word, alphabet)
        print(f"{word}: {encoded_instructions}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a file path as an argument")
        sys.exit(1)  # Exit the script if no argument is provided
    file_path = sys.argv[1]
    process_file(file_path)


# abdurrafay.rehan@aiesec.net
# Pass: 123123456456
