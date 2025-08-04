try:
    print("start text cleaning : ")
    raise Exception("cleaning failed !")
except Exception as e:
     print(f"❌ {e}")
finally:
    print("cleaning block ended!")