labels = ["1", "2", "X", "3"]
for label in labels:
    try:
        print(int(label))
    except ValueError:
        print(f"cannot convert {label} to integer")
        