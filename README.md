# GridMaster

GridMaster is a cell game designed to challenge your puzzle-solving skills in a grid-based environment. The game consists of 13 levels, each with a different grid size. Your objective is to correctly identify a specific cell in each level that contains a mistake.

## Game Overview

- The game consists of 13 levels, and you progress through each level by correctly identifying the cell with the mistake.
- The grid dimensions change with each level, providing increasing levels of difficulty.

## Game Mechanics

- The game generates a question based on a random choice of data.
- A mistake is introduced in the grid by replacing a character in one of the cells.
- Your task is to input the correct cell coordinates (e.g., A1) to identify the mistake.

## Code Components

- `start_message()`: Prints the initial message for the user.
- `section_message(level)`: Prints the current level message.
- `view_question(data, number_data, level_configurations, level)`: Displays the question, grid, and mistake. Returns the mistake cell number.
- `change_input_number(input_str, number_data, col, row)`: Converts user input (e.g., A1) to a numerical representation.
- `is_correct_number(mistake_number, input_number)`: Checks if the user's input matches the correct cell number.
- `view_result(is_correct, mistake_number, number_data, col)`: Displays the result of the user's input.
- `change_string(number, number_data, col)`: Converts a numerical representation to a cell number (e.g., A1).
- `build_level_configurations(max_level)`: Builds level configurations (grid dimensions) for each level.
- `play()`: The main function to run the game, containing the game loop.

## Getting Started

1. Clone the repository: `git clone https://github.com/Umwe/GridMaster.git`
2. Navigate to the project directory: `cd GridMaster`
3. Run the game: `python main.py`

## Contributing

Contributions to GridMaster are welcome! If you have any ideas for improvements or new features, feel free to submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

GridMaster was inspired by the love for puzzles and grid-based games. We would like to thank the contributors and the open-source community for their support and valuable feedback.
