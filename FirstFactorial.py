def FirstFactorial(num):

  # code goes here
  # Note: don't forget to properly indent in Python
  if(num==0):
    return 1;
  else:
    #for i in range(1,num):
  	return  num * FirstFactorial(num-1)
 

# keep this function call here
# to see how to enter arguments in Python scroll down
print FirstFactorial(raw_input())           
