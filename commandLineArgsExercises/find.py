import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename")

args = parser.parse_args()

# find a pattern for a file and match it (-name)

# Get the name of the file (first test)
print(args.filename)

# find all of a certain type (-type)
