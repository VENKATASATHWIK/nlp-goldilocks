with open("corpus.txt","r") as f:
    for line in f:
        if line.strip():
            print(line.strip())
            