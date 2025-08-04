with open("corpus.txt","r") as src:
    data = src.read()
    
with open("corpus_backup.txt","w") as backup:
    backup.write(data)

print("✅ Backup created as corpus_backup.txt")