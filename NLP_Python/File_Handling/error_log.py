try:
    with open("nonexistant.txt","r") as f:
        data = f.read()
except FileNotFoundError as err:
    with open("er.log","a") as log:
        log.write(str(err)+"\n")
        print("⚠️ Error logged.")
        