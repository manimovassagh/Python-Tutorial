from PyDictionary import PyDictionary
# result = PyDictionary().meaning('hello')
# print(result)
given_word = input("Hello user, Give me the word please!\n")
result = PyDictionary().translate(given_word,"de")
print(f"The result for the word {given_word} is  {result}")
