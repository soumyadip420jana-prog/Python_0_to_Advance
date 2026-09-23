name="Soumyadip"

print(len(name))
print(name.capitalize())
print(name.endswith("rry"))
print(name.startswith("ha"))

print(name.upper())
print(name.lower())
print(len(name))
print(name.count("o"))
print(name.find("d"))

s = "Hello123"

print(s.isalpha())    # False
print(s.isdigit())    # False
print(s.isalnum())    # True
print(s.islower())    # False
print(s.isupper())    # False


name = "Harry is a good  boy and  "

print(name.find("  "))
print(name.replace("  ", " "))

print(name) # Strings are immutable which means that you cannot change them by running functions on them