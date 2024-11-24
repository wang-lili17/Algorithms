def palindromic_word(word):
  word=word.lower()
  l=len(word)
  half=l//2
  if l%2==0:
    return word[:half]==word[half:][::-1]
  else:
    return word[:half]==word[half+1:][::-1]

word=input("iput a word: ")
if palindromic_word(word):
  print("The word is palindromic ")
else:
  print("The word is not a palindromic ")
