phrase= input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip()

if phrase in ["42", "Forty Two"]:
    print("Yes")
elif phrase=="forty-two":
    print("Yes")
else:
    print("No")

