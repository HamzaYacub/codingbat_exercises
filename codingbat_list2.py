#------------------------------------------- q1
#def count_evens(nums):
#  count = 0
  
#  for i in nums:
#    if i % 2 == 0:
#      count = count + 1
    
#  return count

#-------------------------------------------- q2
#def big_diff(nums):
#  max_value = max(nums)
#  min_value = min(nums)
  
#  diff = max_value - min_value
  
#  return diff

#-------------------------------------------- q3
#def centered_average(nums):
   
#  return (sum(nums) - max(nums) - min(nums)) / (len(nums) - 2)

#-------------------------------------------- q4
#sumOf = 0
#  l = len(nums)
#  i = 0
  
#  while i < l:
#    if nums[i] == 13:
#      i = i + 2
#      continue
    
#    sumOf = sumOf + nums[i]
#    i = i + 1
  
#  return sumOf

#-------------------------------------------- q5
#def sum67(nums):
#  sumOf = 0
#  check = True
  
#  for i in nums:
#    if i == 6:
#      check = False
    
#    if check:
#      sumOf = sumOf + i
#      continue
      
#    if i == 7:
#      check = True

#  return sumOf

#--------------------------------------------- q6
#def has22(nums):
#  for i in range(len(nums) - 1):
#    if nums[i] == 2 and nums[i + 1] == 2:
#      return True
#  else:
#    return False