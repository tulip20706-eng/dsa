import array as arr
arrayName=arr.array("i",[12,35,56,67])
for i in range(0,len(arrayName),2):#time complexity 0(n)
    print(arrayName[1],end=" ")

#write a program to get a pro
    sum=0
    product=1
    for i in range(0,len(arrayName)):
        sum=sum+arrayName[i]
        product=product * arrayName[i]
        print ("sum is:",sum)
        print ("product is:",product)
   
 #write program to count target value in array
    count=0
    target=int(input("enter target vlue"))
    
    

 
