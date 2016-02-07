def LetterCapitalize(str):

  # code goes here
  # Note: don't forget to properly indent in Python
  lst = list(str)
  for i in range(len(lst)):
      if(i==0 or lst[i-1]==' '):
          lst[i] = chr(ord(lst[i])-32)
  str = ''.join(lst)
  return str

# keep this function call here
print LetterCapitalize(raw_input())           
