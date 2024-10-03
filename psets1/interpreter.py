expression = input("Expression: ")

try:
    result = eval(expression)
    print(float(result))
except Exception as e:
    print("Error in expression:", e)

