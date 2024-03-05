# GridMaster
Cell Game for solving puzzles in a grid-based environment


# Game Overview:

The game consists of 13 levels, and the user progresses through each level by correctly identifying a cell in a grid.
The grid dimensions change with each level.

# Game Mechanics:

The game generates a question based on a random choice of data.
A mistake is introduced in the grid by replacing a character in one of the cells.
The user must input the correct cell coordinates (e.g., A1) to identify the mistake.
# Code Components:

start_message(): Prints the initial message for the user.
section_message(level): Prints the current level message.
view_question(data, number_data, level_configurations, level): Displays the question, grid, and mistake. Returns the mistake cell number.
change_input_number(input_str, number_data, col, row): Converts user input (e.g., A1) to a numerical representation.
is_correct_number(mistake_number, input_number): Checks if the user's input matches the correct cell number.
view_result(is_correct, mistake_number, number_data, col): Displays the result of the user's input.
change_string(number, number_data, col): Converts a numerical representation to a cell number (e.g., A1).
build_level_configurations(max_level): Builds level configurations (grid dimensions) for each level.
play(): The main function to run the game, containing the game loop.
Improvements/Changes:
