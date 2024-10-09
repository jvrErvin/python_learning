import argparse

def parse_arguments() -> argparse.Namespace:
    """
    Parse the numbers and the operation to solve basic mathematical problems

    Returns:
    argparse.Namespace: Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("num1", type=int or float, required=True, help="The first number you want to do the operation with")
    parser.add_argument("num2", type=int or float, required=True, help="The second number you want to do the operation with")
    parser.add_argument("--operation", required=False, default="addition", choices=["addition", "subtract", "multiply", "divide"], help="The type of mathematic operation you want to do")
    return parser.parse_args()


def addition(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2


if __name__ == "__main__":
    args = parse_arguments()
    if args.operation == "addition":
        print(f"The two number's sum is {addition(args.num1, args.num2)}")
    elif args.operation == "subtract":
        print(f"The two number's differecne is {subtract(args.num1, args.num2)}")
    elif args.operation == "multiply":
        print(f"The two number's product is {multiply(args.num1, args.num2)}")
    elif args.operation == "divide":
        if round(args.num2) != 0:
            print(f"The two numbers's quotient is {divide(args.num1, args.num2)}")
        else:
            print("The division with zero is not interpretable")
    else:
        pass #can't happen

 # on num1 TypeError: 'required' is an invalid argument for positionals    