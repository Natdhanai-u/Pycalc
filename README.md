# Pycalc

Pycalc is a command-line calculator developed in Python. It supports basic arithmetic operations and handles invalid user input.
## Features

- Addition 
- Subtraction 
- Multiplication
- Division 
- Input validation and error handling 

## Requirements 

- Python 3 
- Git (for cloning the repository)

## Getting Started 

Choose **one** of the following methods to clone the repository.

### Option 1: Clone with HTTPS

HTTPS is a straightforward option for most users. 

~~~bash
git clone https://github.com/Natdhanai-u/Pycalc.git
cd Pycalc
~~~

### Option 2: Clone with SSH 

Use SSH if you have added an SSH key to your GitHub account. 

```bash
git clone git@github.com:Natdhanai-u/Pycalc.git
cd Pycalc
```

For setup instructions, see the [GitHub SSH documentation](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

### Option 3: Clone with GitHub CLI

Install [GitHub CLI](https://cli.github.com/) first. Sign in if needed:

```bash
gh auth login
```
Clone the repository and enter the project directory:

```bash
gh repo clone Natdhanai-u/Pycalc
cd Pycalc
```

### Run the calculator 

From the project root, run: 

```bash
python src/main.py
```

If your system uses `python3`, run:

```bash
python3 src/main.py
```

## Usage

When you start Pycalc, the program prompts you to select an arithmetic operation.

Available operations:

- `add`
- `subtract`
- `multiply`
- `divide`

After selecting an operation, enter the first and second numbers when prompted. The calculator then displays the result. 

## Example 

```text
Welcome to the calculator
>>>>>>>>>>>>>>>>>>>>>>>>>
Choose: add, subtract, multiply, divide
=> add

Enter the first number: 
=> 10

Enter the second number: 
=> 5 

>> Result: 15.0
```

The example above demonstrates an addition operation. Actual terminal output may vary slightly depending on the program's implementation. 

## Error Handling 

Pycalc includes basic error handling to improve reliability.

- **Invalid Operation:** Displays an error message when the selected operation is not supported. 
- **Invalid Number:** Prompts the user again when the input cannot be converted to a number. 
- **Division by Zero:** Prevents division by zero and displays an appropriate error message. 

## Project Structure 

The project is organized into separate files to keep the calculator's interface and arithmetic logic independent.

```text
Pycalc/
├── src/
│   ├── main.py
│   └── function.py
├── .gitignore
├── LICENSE
└── README.md
```

## Future Improvements 

Potential improvements for the future version include:

- Support multiple calculations in one session.
- Add automated tests using `unittest` or `pytest`.
- Improve the command line interface. 
- Add more mathematical operations. 

## License 

This project is licensed under the MIT License. 
See the [LICENSE](LICENSE) file for details. 
