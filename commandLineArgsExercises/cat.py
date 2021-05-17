#from sys import argv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="Name of your file")
parser.add_argument("--secondfile", help="Your second file")
parser.add_argument("--thirdfile", help="Your third file")
parser.add_argument("--operation", help="The operation you want to execute")
parser.add_argument("--newfile", help="The file you want to export to")

args = parser.parse_args()
print(args)
#script, filename, operation, newfile = argv
# Read files
with open(args.file) as txt:
# Output file contents to command line w/print
    print(txt.read())

# Allow for output to a new file
if args.operation == '>':
    transfer = open(args.newfile, 'w')
    transfer.write(txt.read())
    transfer.close()
else:
    pass

# Optional Make it able to read multiple files at once
