entities = [
    ["Word", "Entity"],
    ["NLP", "TECH"],
    ["Google", "ORG"],
    ["India", "LOC"]
]

with open("annotations.csv","w") as f:
    for row in entities:
        f.write(",".join(row)+"\n")
        
print("✅ Annotations saved.")
    
    