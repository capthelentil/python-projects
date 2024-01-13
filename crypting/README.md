# Caesar Cipher Encryption and Decryption

This Python program encrypts and decrypts text using the Caesar Cipher method. The Caesar Cipher is a simple encryption algorithm that shifts each letter in the text by a certain amount.

## How to Use

1. **Encrypting Text:**
    - When you run the program, it will prompt you to enter a text and a shift amount.
    - After entering the text and shift amount, the program will display the encrypted text.

2. **Decrypting Encrypted Text:**
    - When you run the program again, it will ask you to enter the encrypted text and the shift amount.
    - Entering the required information will result in the display of the decrypted text.

## How It Works

The program utilizes the Caesar Cipher algorithm for both encryption and decryption. Here's a brief overview of the algorithm:

- **Encryption:**
    1. For each character in the input text:
    2. Check if the character is an alphabetic character.
    3. Determine whether the character is uppercase or lowercase.
    4. Shift the character by the specified amount in the alphabet.
    5. Append the shifted character to the encrypted text.
    6. If the character is not alphabetic, append it as is.

- **Decryption:**
    1. For each character in the encrypted text:
    2. Check if the character is an alphabetic character.
    3. Determine whether the character is uppercase or lowercase.
    4. Shift the character backward by the specified amount in the alphabet.
    5. Append the shifted character to the decrypted text.
    6. If the character is not alphabetic, append it as is.

## Python Version Used

This program is written in Python 3.x.

## How to Run

If Python is not installed, you can download and install it from [python.org](https://www.python.org/downloads/). Then, in the terminal or command prompt, follow these steps:

1. Navigate to the project directory:

    ```bash
    cd /path/to/your/project
    ```

2. Run the program:

    ```bash
    python caesar_cipher.py
    ```

3. Enter the requested information from the user and observe the result.

## License

This project is licensed under the [MIT License](LICENSE).
