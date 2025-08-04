with open("corpus.txt","r") as f:
    for i, line in enumerate(f.readlines(),1):
        print(f"sentence {i}: {line.strip()}")