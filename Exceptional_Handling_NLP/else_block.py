try:
    with open("corpus.txt","r") as f:
        content = f.read()
except FileNotFoundError:
    print("file is missing")
else:
    print("file loaded successfully!!!")