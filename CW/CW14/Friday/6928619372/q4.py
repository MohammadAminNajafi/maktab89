import argparse


parser = argparse.ArgumentParser()

parser.add_argument("-n1","--number1",type=int,required=True)
parser.add_argument("-n2","--number2",type=int,required=True)
parser.add_argument("-o","--operation",required=True)

args = parser.parse_args()

if args.operation == "add":
    print(args.number1 + args.number2)
elif args.operation =="substract":
    print(args.number1 - args.number2)
elif args.operation == "multiply":
    print(args.number1 * args.number2)
elif args.operation == "division":
    try:
        print(args.number1 / args.number2)
    except:
        print("zero division error")

