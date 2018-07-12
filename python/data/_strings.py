# Find the first instance of a string in another string

fulltext = "This is the full text that I want to search"

# Find the position of the first letter "e"
print fulltext.find("e")     # prints 10

# Find the position of the first letter "e" after 15 
print fulltext.find("e", 15)     # prints 18

# Find the position of the last letter "e"
print fulltext.rfind("e")     # prints 38
