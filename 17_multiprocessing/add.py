import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--a", type=int, required=True)
    parser.add_argument("--b", type=int, required=True)
    parser.add_argument("--c", type=int, required=False, default=10000000)
    return parser.parse_args()
    
    
def add(a, b, c):
    return a + b + c

if __name__ == "__main__":
    args = parse_args()
    sum = add(args.a, args.b, args.c)
    print(sum)
