try:
    with open("dataset.txt","r") as f:
        print(int(f.read()))
except FileNotFoundError:
    print("file missing")
except ValueError:
    print("data format is not numerical")
    