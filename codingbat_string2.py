#---------------------------------------------- q1
#def double_char(str):
#  newStr = ""
#  for i in range(len(str)):
#    newStr = newStr + str[i] + str[i]
  
#  return newStr

#----------------------------------------------- q2
#def count_hi(str):
#  hiStr = "hi"
#  count = 0
  
#  for i in range(len(str) - 1):
#    subStr = str[i] + str[i+1]
    
#    if subStr == hiStr:
#      count = count + 1

#  return count

#----------------------------------------------- q3
#def cat_dog(str):
#  cat_count = 0
#  dog_count = 0
  
#  for i in range(len(str)):
#    subStr = str[i:i+3]
    
#    if subStr == 'cat':
#      cat_count = cat_count + 1
      
#    if subStr == 'dog':
#      dog_count = dog_count + 1 

#  if cat_count == dog_count:
#    return True
#  else:
#    return False

#------------------------------------------------- q4
#def count_code(str):
#  count = 0
  
#  if len(str) < 4:
#    return count
#  else:  
#    for i in range(len(str)):
#      subStr = str[i:i+4]
    
#      if subStr.startswith('co') and subStr.endswith('e'):
#        count = count + 1

#  return count

#---------------------------------------------------- q5
#def end_other(a, b):
  
#  if a.lower().endswith(b.lower()):
#    return True
#  if b.lower().endswith(a.lower()):
#    return True
#  else:
#    return False

#---------------------------------------------------- q6
#def xyz_there(str):
  
#  for i in range(len(str)):
#    if str[i-1] != "." and str[i:i+3] == "xyz":
#      return True
#  else:
#    return False
    
 