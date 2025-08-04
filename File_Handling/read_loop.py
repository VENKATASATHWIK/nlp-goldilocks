# read_loop.py
with open("corpus.txt","r") as f:
    while(line:= f.readline()):
        print(line.strip())
        