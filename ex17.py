from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line, HOW?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")
