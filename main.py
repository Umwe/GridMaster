import random
import math

# Prints the initial message for the user
def start_message():
    print('Input cell number (e.g. A1) of the different character.')

def section_message(level):
    """Prints the level message."""
    print('Level:', level)

# Displays the question for the user
def view_question(data, number_data, level_configurations, level):
    col, row = level_configurations[level]
    choice_data = random.randint(0, 2)
    mistake_number = random.randint(0, (col * row) - 1)
    print('Debug: mistake_number =', mistake_number)
    question = data[choice_data]
    print(question)

    # Display the grid
    i = 0
    j = 0
    question_str1 = '/|'
    question_str2 = '--'
    while i < col:
        question_str1 += number_data[i] + ''
        question_str2 += '-'
        i += 1
    print(question_str1)
    print(question_str2)

    i = 0
    while i < row:
        question_str = str(i + 1) + '|'
        while j < col:
            if (i * col + j) == mistake_number:
                question_str += question[1]
            else:
                question_str += question[0]
            j += 1
        print(question_str)
        i += 1
        j = 0

    return mistake_number

# Converts user input (e.g., A1) to a numerical representation, Create a dictionary mapping column characters to numbers
def change_input_number(input_str, number_data, col, row):
    str_data = {number_data[i]: i for i in range(len(number_data))}
    str_data.update({number_data[i].lower(): i for i in range(len(number_data))})

    while True:
        input_str_split = list(input_str)

        if len(input_str_split) != 2:
            print('Invalid input. Please enter a valid cell number (e.g. A1)')
            input_str = input('(e.g. A1): ')
            continue

        col_char = input_str_split[0]
        row_char = input_str_split[1]

        if col_char not in str_data:
            print('Invalid column character. Please enter a valid column character.')
            input_str = input('(e.g. A1): ')
            continue

        col_number = str_data[col_char]

        try:
            row_number = int(row_char)
        except ValueError:
            print('Invalid row character. Please enter a valid row number.')
            input_str = input('(e.g. A1): ')
            continue

        if not (1 <= col_number < col) or not (1 <= row_number <= row):
            print(f'Invalid column or row number. Please enter valid values for both.')
            input_str = input('(e.g. A1): ')
            continue

        input_number = (row_number - 1) * col + col_number
        return input_number



# Checks if the user's input matches the correct cell number
def is_correct_number(mistake_number, input_number):
    return mistake_number == input_number

# Displays the result
def view_result(is_correct, mistake_number, number_data, col):
    if is_correct:
        print('Correct!')
    else:
        print('Wrong')
        print('Correct answer is', change_string(mistake_number, number_data, col))

# Converts a numerical representation to a cell number (e.g., A1)
def change_string(number, number_data, col):
    col_number = number % col
    row_number = math.floor(number / col) + 1
    return number_data[col_number] + str(row_number)

# Build level configurations
def build_level_configurations(max_level):
    return {level: (3 + level // 2, 3 + (level - 1) // 2) for level in range(1, max_level + 1)}

# Main function to run the game
def play():
    data = [['O', '0'], ['l', '1'], ['u', 'v']]
    number_data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    max_level = 13
    level_configurations = build_level_configurations(max_level)

    level = 1
    col, row = level_configurations[level]

    start_message()

    while level <= max_level:
        section_message(level)
        mistake_number = view_question(data, number_data, level_configurations, level)
        choice = input('(e.g. A1): ')
        print('Debug: choice =', choice)

        input_number = change_input_number(choice, number_data, col, row)
        if input_number is None:
            continue  # Display field again 

        print('Debug: input_number =', input_number)
        is_correct = is_correct_number(mistake_number, input_number)
        view_result(is_correct, mistake_number, number_data, col)

        if is_correct:
            level += 1
            if level <= max_level:
                col, row = level_configurations[level]
        else:
            if level > 2:
                level -= 2
                col, row = level_configurations[level]
            elif level == 2:
                level -= 1
                col, row = level_configurations[level]

    print('Congratulations! You have passed all 13 levels. Thank you!')

# Start the game
play()
