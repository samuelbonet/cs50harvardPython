variable_name = input("Enter the variable name in camelCase: ")

snake_case_name = ""  

for char in variable_name:
    if char.isupper() and snake_case_name:  
        snake_case_name += "_" + char.lower() 
    else:
        snake_case_name += char.lower()

print("Snake case:", snake_case_name)
