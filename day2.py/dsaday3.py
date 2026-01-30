import array as arr
#to find maximum value in the array
arr = [12,7,8,9,0]
max_val = arr[0]
for i in range(1,len(arr)):
    if arr[i]>max_val:
        max_val = arr[i]
print(max_val)

#to find 2nd maximum value in the array
import math 
arr = [12,7,8,9,0]
firstmax = -math.inf
secondmax= -math.inf 
for curvalue in arr:
    if curvalue > firstmax:
        secondmax = firstmax
        firstmax = curvalue

    elif curvalue >secondmax:
         secondmax = curvalue
print(secondmax)

#dictionary 
class solution:
    def twosum(self,nums:list[int],target:int)->list[int]:
        dict={}
        for i in range (0,len(nums)):
            need = target - nums[i]
            if need in dict:
                return [dict[need],i]
            dict[nums[i]]=i