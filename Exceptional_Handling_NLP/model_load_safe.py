try:
    print("loading model: ")
    raise FileNotFoundError("Model file missiing")
except FileNotFoundError as e:
   print(f"⚠️ {e}")
finally:
    print("🔄 Model loading attempted.")