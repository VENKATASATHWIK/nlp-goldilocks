new_data = [ "Data augmentation improves model accuracy.",
    "Transformers changed NLP forever."
]

with open("corpus.txt","a") as f:
    for sentence in new_data:
        f.write(sentence + "\n")
        
print("new sentences appended")
