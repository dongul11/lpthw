import sys #Import argument from system

# script, filename = argv # unpack arguments to variables
script = sys.argv[0]
filename = sys.argv[1] # another way to do it :)

txt = open(filename) # open file using open() command

print (f"Here's your file {filename}:") # ask input
print (txt.read()) # read and print the txt file
txt.close()

print ("Type the filename again:")
file_again = input("> ") # ask input

txt_again = open(file_again) # reopen file

print (txt_again.read()) # read and print the txt again
txt_again.close
