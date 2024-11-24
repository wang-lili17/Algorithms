def palindromic_word_in_list(w):
  l_w=[]
  w=w.split()
  for word in w:
    word=word.lower()
    l=len(word)
    half=l//2
    if l%2==0:
      if word[:half]==word[half:][::-1]:
        l_w.append(word)
    else:
      if word[:half]==word[half+1:][::-1]:
        l_w.append(word)
  return l_w

w=input("Enter a sentace: ")
l_w=palindromic_word_in_list(w)

if l_w:
  print(l_w)
  longest=max(l_w,key=len)
  length=len(longest)
  print(longest,length)

else:
  print("No palindromic words in the list")
