import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here")
parser.add_argument("square", help="Display a square of a given number")
args = parser.parse_args()
print(args.square**2)
