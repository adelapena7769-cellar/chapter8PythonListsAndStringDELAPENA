fname = input("Enter file name: ")

fhand = open(fname)

count = 0

for line in fhand:
    if line.startswith("From "):
        words = line.split()
        print(words[1])
        count += 1