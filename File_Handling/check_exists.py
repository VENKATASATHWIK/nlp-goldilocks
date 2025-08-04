import os
file_path = "corpus.txt"
if os.path.exists(file_path):
    with open(file_path,"r") as f:
        print(f.read())
else:
    print("❌ corpus.txt does not exist.")