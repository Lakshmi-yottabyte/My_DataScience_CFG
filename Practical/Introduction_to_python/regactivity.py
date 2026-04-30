import re
pattern = r"^Song+$"
text=input("Enter random long paragraph text with a word 'Song' in it:")
match =re.findall(pattern,text)
print(match)