from sys import argv

script, filename = argv

txt = open(filename)

print(f"We're going to read {filename}.")
result = txt.read()
print(result)
txt.close()
