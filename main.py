data = []

with open("data.txt", "r") as f:
    lines = f.readlines()

# strip() removes the unnecessary '\n' and spaces.
# the code also removes the comment.
lines = [line.strip() for line in lines if line.strip() and not line.startswith("#")]

headers = lines[0].split()

for line in lines[1:]:
    parts = line.split()

    date = ' '.join(parts[0:4])
    duration = parts[4:6]
    tipo = parts[6]
    comment = parts[7].strip('"')
    status = ' '.join(parts[8])

    entry = {
        "date": date,
        "duration": duration,
        "tipo": tipo,
        "comment": comment,
        "status": status
    }

    data.append(entry)

for entry in data:
    print(entry)
