data = []

with open("data.txt", "r") as f:
    lines = f.readlines()

print(lines)

# strip() removes the unnecessary '\n' and spaces.
# the code also removes the comment.
lines = [line.strip() for line in lines if line.strip() and not line.startswith("#")]

print(lines)

