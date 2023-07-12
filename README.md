# Password Checker

This Python program checks the security of passwords by comparing them against a database of known compromised passwords using the Have I Been Pwned API.

## How to Use

1. Ensure that you have Python 3 installed on your machine.

2. Install the required libraries by running the following command:
```
pip install requests hashlib
```

3. Clone this repository or download the source code file.

4. Open the terminal or command prompt and navigate to the project directory.

5. Run the `password_checker.py` file using the Python interpreter.

6. Enter the passwords you want to check as command-line arguments, separated by spaces.

7. The program will query the Have I Been Pwned API and check if the passwords have been compromised.

8. It will print a message indicating the number of times each password has been found in compromised databases. If a password has not been found, it will display a "Carry on!" message.

## How it Works

The program uses the SHA-1 hashing algorithm from the `hashlib` library to securely hash the passwords. It then sends the first five characters of the hashed password to the Have I Been Pwned API to receive a list of hashes that match the queried characters.

The `get_password_leaks_count` function compares the queried hash suffix with the received hashes to determine if the password has been compromised. If a match is found, it returns the count of how many times the password has been leaked. If no match is found, it returns 0.

The `pwned_api_check` function checks if a password exists in the API response by calling the other functions and returns the count of password leaks.

The `main` function accepts command-line arguments (passwords) and calls `pwned_api_check` for each password. It then prints the results accordingly.

## Example Output

Here's an example of the program's output:

```
$ python password_checker.py password123 MySecretPassword 12345678
password123 was found 98765 times... you should probably change your password
MySecretPassword was NOT found. Carry on!!
12345678 was found 54321 times... you should probably change your password
```

The output indicates the number of times each password has been found in compromised databases. If a password has not been found, it displays a "Carry on!" message.

## Contributions

Contributions to this project are welcome. If you find any issues or have suggestions for improvement, please feel free to submit a pull request.
