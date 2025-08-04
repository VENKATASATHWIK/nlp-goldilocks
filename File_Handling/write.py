raw_texts = ["I love NLP and AI!",
    "This model understands text really well.",
    "Natural language processing is fascinating."]

with open("corpus.txt","w") as f:
    for line in raw_texts:
        f.write(line+"\n")
        
print("raw text data written to corpus.txt")

