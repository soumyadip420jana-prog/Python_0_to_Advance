name=input("Enter your name: ");

print(f"Good morning,{name}")

letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''

print(letter.replace("<|Name|>","Soumyadip").replace("<|Date|>","18AUG"))