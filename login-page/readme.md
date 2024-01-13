# Simple User Authentication System

This simple Python application implements a basic authentication system allowing users to register and log in. It uses a basic example where usernames and passwords are stored in memory using a simple dictionary.

## Usage

To run the program, navigate to the terminal or command prompt and use the command `python your_file_name.py`.

When the program starts, it displays a menu with the following options:

1. **Register**: Sign up by entering a username and password.
2. **Login**: Log in with a registered username and password.
3. **Exit**: Exit the program.

Each option performs the respective operation based on the information entered by the user.

## Security

- Currently, passwords are stored directly as plain text. For a real-world application, additional measures should be taken to securely store and authenticate passwords.
- Basic error checking is implemented on user inputs, but for a real application, more comprehensive error checking and user-friendly messages should be added.

## Development

- You can enhance code readability and maintainability by adding functions or classes.
- Consider using encryption or hashing algorithms for password security.

## Contributing

1. Fork this project (click the "Fork" button in the upper right).
2. Add new features or fix bugs.
3. Submit a pull request with your changes.

## License

This project is licensed under the [MIT License](LICENSE).
