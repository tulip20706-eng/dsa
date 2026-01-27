#Q1
#list =[1,2,3,4,5]
#list.reverse()
#print(list)

#list=[7,8,9,0]
#list.reverse()
#print(list)

#Q2
#list= [35,40,67,89,23]
#above_75 = 0
#below_45 = 0
#for marks in list:
  #  if (marks>75):
     # below_45= below_45+1
#print (above_75,
     #  below_45,sep=" ")

## while loop 
#l1= [35,40,67,89,23]
#      below_45,sep=" ")

##Q3
#l1 = [-8,2,7,-5,9,-4,6]
#p_sitive=0
#n_egative=0
#for i in l1:
#    if i>0:
 #       p_sitive = p_sitive+1
  #   elif i<0:
    #    n_egative= n_egative+1
#print(p_sitive,n_egative,sep=" ")


#count the no.of digit
##n = int(input("enter number"))
#count=0
#while n>0:
 #   n=n //10
  #  count+=1
#print (count)

#reverse the num
#n = int(input("enter number"))
#rev = 0
#while n>0:
 #   digit = n%10
  #  rev = rev*10+digit
   # n = n//10
   # print(rev)


#neg rev
#n= int(input("enter number"))
#rev = 0
#sign = 1

#if n < 0:
 #   sign= -1
  #  n= n * -1
   # while n>0:
    #    digit = n %10
     #   rev = rev *10+digit
      #  n = n//10
       # print(rev*sign)
    

## 

#class Solution:
 #   def isPalindrome(self, x int)-> bool:
  #  if x < 0 :
   #     return false

    #    n=x
     #   rev = 0
      #  while x>0
       # digit = x %10
        #rev = rev * 10 + digit
    #    x = x//10
     #   if n== rev:
      #      return true
       # else:
        #  retuen false



import array as arr
arrName= arr.array('i',[10,20,30,40,50])
#operation 
#1add
#a) append()- adds an element at the end of the array
arrName.append(60)
print("after append:",arrName)
arrName.insert(2,25)
print("after insert:",arrName)