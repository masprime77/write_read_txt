# Write to a text file
with open("example.txt", "w") as f:
    f.write("Hello, world!\n")

# Append to a file
with open("example.txt", "a") as f:
    f.write("Another line.\n")

# Read from a file
with open("example.txt", "r") as f:
    content = f.read()
    print(content)