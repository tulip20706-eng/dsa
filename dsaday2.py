import array as arr
arrayName = arr.array("i",[23,87,90])

#1.add
#a)apend (value)-> add the values in last ,t/c - 0(1),0(n)
#b) insert(index,value)-> insert the value at index, t/c-0(1),0(n)
#2.delete
#1.remove()
#2.pop() or pop(index)

arrayName.remove(87)
print(arrayName)

arrayName.pop(1)
print(arrayName)
arrayName[0]=40
print(arrayName)

for i in range(0,len(arrayName)):
    print(arrayName[1],end="")