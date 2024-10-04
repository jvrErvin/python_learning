# Homework: Argument Parsing Practice

## Task

Write a Python script that simulates a basic calculator. The script should accept command-line arguments using `argparse` to perform basic arithmetic operations (addition, subtraction, multiplication, division) on two numbers.

## Requirements

1. **Positional Arguments**:
   - Two numbers: `num1` and `num2` (floats or integers).
   
2. **Optional Argument**:
   - An operation flag `--operation` to specify the arithmetic operation. The available operations should be `add`, `subtract`, `multiply`, or `divide`.
   - If the `--operation` flag is not provided, the script should default to addition.

3. **Error Handling**:
   - If the user tries to divide by zero, the script should handle it and print an appropriate message.
   
4. **Help Text**:
   - Ensure that the `argparse` help text provides clear instructions on how to use the script.

## Example Usage

```bash
# Addition (default operation)
python calculator.py 5 3

# Subtraction
python calculator.py 5 3 --operation subtract

# Multiplication
python calculator.py 5 3 --operation multiply

# Division
python calculator.py 5 3 --operation divide
```

Expected outputs:
```bash
# Addition
Result: 8

# Subtraction
Result: 2

# Multiplication
Result: 15

# Division
Result: 1.6667
```

## Instructions

	1.	Create a Python script called calculator.py.
	2.	Use argparse to parse the two numbers and the --operation flag.
	3.	Implement the basic arithmetic operations based on the user’s input.
	4.	Handle edge cases, such as division by zero.