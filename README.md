# Random Password Generator

This is a simple Random Password Generator application built using Python and Tkinter. It allows users to enter the name of their account and generate a random password, which is then displayed on the screen and saved to a text file.

## Features

- Enter account name
- Generate a secure random password
- Display the generated password
- Save the account name and password to a file
- Refresh input fields
- Exit the application

## Requirements

- Python 3.x
- Tkinter library (comes pre-installed with standard Python distribution)

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/MuhammadRaffey/Simple-Password-Generator
    ```
2. Navigate to the project directory:
    ```bash
    cd Simple-Password-Generator
    ```
3. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

## Usage

1. Run the application:
    ```bash
    python main.py
    ```
2. Enter the name of your account in the input field.
3. Click the "Enter" button to confirm the account name.
4. Click the "Generate password" button to generate a random password.
5. The account name and generated password will be displayed on the screen.
6. The account name and password are also saved to a file named `Passwords.txt` in the same directory.
7. Use the "Refresh" button to clear the input fields and labels.
8. Use the "Exit" button to close the application.


## Code Explanation

The main script `main.py` contains the following:

- `PasswordGeneratorApp`: A Tkinter-based class that defines the GUI and its functionalities.
- `create_widgets()`: Method to create and place all the widgets (buttons, labels, entry fields).
- `remove_placeholder()`: Method to remove placeholder text from the input field after a delay.
- `display_account()`: Method to display the entered account name.
- `generate_password()`: Method to generate a random password and display it.
- `refresh()`: Method to clear the input fields and labels.

## Contributing

Contributions are welcome! Please create a pull request or open an issue to discuss any changes or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html) for providing the necessary information to build the GUI.



