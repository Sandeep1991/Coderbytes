import re
def LongestWord(sen):

  # code goes here
  # Note: don't forget to properly indent in Python
  words = sen.split()
  print len(words)
  for i in range(0,len(words)-1):
    words[i] = re.sub('[^A-Za-z]+','',words[i])
    sen = max(words, key = len)
  return sen

# keep this function call here
# to see how to enter arguments in Python scroll down
print LongestWord(raw_input())





