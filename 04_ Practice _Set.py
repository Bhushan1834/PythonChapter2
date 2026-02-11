# Display user-entered name followed by Good Afternoon
name = input("Enter your name:")
print(f"Good Afternoon, {name} ")

# Fill the letter template with name and date
letter = '''Dear <|zname|>,
Yoy are selected!
<|Date|>'''
print(letter.replace("<|Nmae|>", "Bhushan").replace("<|Date|>", "24 september 2050"))

# Detect double space in a string
name = "Bhushan is a good  boy and  "
print(name.find("  "))

# Replace double space with single space
name = "Bhushan is a good  boy and  "
print(name.replace("  "," ")) # String are immutable which means that yoc cannot change them by runnning function on them

# Format letter using escape sequence characters
letter = "Dear Bhushan,\n\tThis python course is nice.\nThanks!"
print(letter)
