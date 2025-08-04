with open("annotations.csv","r") as f:
    for line in f:
        word,label = line.strip().split(",")
        print(f"{word} : {label}")
        
        