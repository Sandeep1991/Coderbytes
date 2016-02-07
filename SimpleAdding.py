def SimpleAdding(num): 

  # code goes here 
  # Note: don't forget to properly indent in Python
  sum = 0
  for i in range(num+1):
    sum += i
  num = sum
  return num    
    
# keep this function call here  
print SimpleAdding(raw_input())   
