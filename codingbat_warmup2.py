#----------------------------------------- q1
#def string_times(str, n):
  
#  newStr = ""
  
#  for i in range(n):
#    newStr = newStr + str
  
#  return newStr

#------------------------------------------ q2
#def front_times(str, n):
  
#  newStr = ""
  
#  for i in range(n):
#    newStr = newStr + str[:3]
    
#  return newStr

#------------------------------------------ q3
#def string_bits(str):
#  newStr = ""
  
#  for i in range(0, len(str), 2):
#    newStr = newStr + str[i]
  
#  return newStr

#---------------------------------------- q4
#def string_splosion(str):
#  newStr = ""
  
#  for i in range(len(str)):
#    newStr = newStr + str[:i+1]
  
#  return newStr

#---------------------------------------- q5
#def last2(str):
#  lastTwo = str[-2:]
#  count = 0
  
#  for i in range(len(str)-2):
#    newStr = str[i] + str[i+1]
    
#    if newStr == lastTwo:
#      count = count + 1
  
#  return count
  
#----------------------------------------- q6
#def array_count9(nums):
#  count = 0
  
#  for i in range(len(nums)):
#    if nums[i] == 9:
#      count = count + 1
      
#  return count

#----------------------------------------- q7
#def array_front9(nums):
  
#  newList = nums[0:4]
  
#  for i in range(len(newList)):
#    if newList[i] == 9:
#      return True
#  else:
#    return False
  
#----------------------------------------- q8  
#def array123(nums):
#  for i in range(len(nums)):
#    if nums[i:i+3] == [1, 2, 3]:
#      return True
#  else:
#    return False

#----------------------------------------- q9
#def string_match(a, b):
#  count = 0
  
#  if len(a) < len(b):
#    shorterStr = a
#  else:
#    shorterStr = b
  
#  for i in range(len(shorterStr) - 1):
#    strA = a[i] + a[i+1]
#    strB = b[i] + b[i+1]
    
#    if strA == strB:
#      count = count + 1
  
#  return count