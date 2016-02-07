def LetterChanges(str):

  # code goes here
  lst = list(str)
  print lst
  dict = {'z':'A','a':'b','b':'c','c':'d','d':'E','e':'f',
          'f':'g','g':'h','h':'I','i':'j','j':'k','k':'l',
          'l':'m','m':'n','n':'O','o':'p','p':'q','q':'r',
          'r':'s','s':'t','t':'U','u':'v','v':'w','w':'x',
          'x':'y','y':'z'};
  # Note: don't forget to properly indent in Python
  str =''
  for itr in lst:
    if ord(itr)>=97 and ord(itr)<=122:
      str += dict[itr]
    else: str += itr
  return str

# keep this function call here
print LetterChanges(raw_input())
