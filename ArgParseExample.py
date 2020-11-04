import argparse

parser =argparse.ArgumentParser()
parser.add_argument("a")
parser.add_argument("b")
args=parser.parse_args()
print(int(args.a)+int(args.b))