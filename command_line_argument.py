import argparse
import sys

def calc(args):
    if args.a == 45 and args.b == 5 and args.o == "mul":
        return 'The result is ', int(555)
    elif args.a == 56 and args.b == 9 and args.o == "add":
        return 'The result is', int(77)
    elif args.a == 56 and args.b == 6 and args.o == "div":
        return 'The result is:', int(4)
    elif args.o == "add":
        return 'The sum of the numbers is ', args.a + args.b
    elif args.o == "sub":
        return 'The differece of both the numbers is ', args.a - args.b
    elif args.o == "mul":
        return 'The product of the number is', args.a * args.b
    elif args.o == "div":
        return 'The result is ', args.a / args.b

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--a',type=float,default=0.0,help="Enter first number.")
    parser.add_argument('b',type=float,default=0.0,help="Enter second number.")
    parser.add_argument('o',type=str,default=0.0,help="Enter the operator.")
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))

# The following command has to be run on command line utility
# python rough.py --a 45 5 mul