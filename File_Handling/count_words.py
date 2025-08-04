with open("corpus.txt","r") as f:
    content = f.read()
    total_words = len(content.split())
    

print(f"🧮 Total words in corpus: {total_words}")
    