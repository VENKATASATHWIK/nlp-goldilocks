with open("corpus.txt","r") as f:
    for line in reversed(f.readlines()):
        print(line.strip())
        