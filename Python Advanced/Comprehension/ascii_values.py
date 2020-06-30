# Write program that receives a list of characters and creates a dictionary with each character as a key and its ASCII
# value as a value. Try solving that problem using comprehensions.

chars = ['a', 'b', 'c', 'a']
print({x : ord(x) for x in chars})

valies = {'a', 'o', 'u', 'e', 'i'}
text = 'ILovePython'

result = {ch for ch in text if ch.lower() not in valies}
print(result)
