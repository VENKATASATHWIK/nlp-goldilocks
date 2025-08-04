try: 
    with open("nonexistent_corpus.txt","r") as f:
        content = f.read()
except FileNotFoundError:
    
    print("❌ Corpus file not found.")