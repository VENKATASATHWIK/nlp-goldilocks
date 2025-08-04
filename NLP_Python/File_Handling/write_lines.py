tokenized = [
    "I love NLP .",
    "Transformers are powerful .",
    "Text preprocessing matters ."
]

with open("cleaned_corpus.txt","w") as f:
    f.writelines([line + "\n" for line in tokenized])
    
print("Tokenized corpus writen!!")
