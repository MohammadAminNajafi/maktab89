import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-n","--fname",required=True)
parser.add_argument("-l","--lname",required=True)
parser.add_argument("-a","--age",default="")
args = parser.parse_args()
print(f"Welcome {args.fname} {args.lname} {args.age}")