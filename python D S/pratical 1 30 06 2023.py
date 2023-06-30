'''
#case 1

print("Enter To Number")
arr=[ ]

for i in range(5):
    arr.insert(i,int(input()))
    
print("Enter The Number To search")
num=int(input())


for i in range(num):
    
    if(num == arr[i]):
        index=i
        break
    
print("Number Fount At Index No ")
print(index)
'''
'''
#case 2

print("Enter the size : ")
arrsize=int(input())

print("enter "+str(arrsize)+" elements")
arr= [ ]

for i in range(arrsize):
    arr.append(input())

print("enter an element to search")

elem = input()
chk = 0

for i in range(arrsize):
    if   elem == arr[i] :
        index=i
        chk=1
        break
    
if(chk == 1):
    print("element found at index number : "+str(index))
else:
    print("elemnt not found ! ")
'''
'''
#case 3
print ("enter the size ")
arrsize=int(input())

print("enter "+str(arrsize)+" element")
arr= [ ]

for i in range(arrsize):
    arr.append(input())

print("enter an element to search")
elem=input()
k=0
index=[ ]

for i in range(arrsize):
    if (elem==arr[i]):
        index.insert(k,i)
        k+=1
if(k==0):
    print("element does not found !")

else:
    if(k==1):
        print("element found at index no : ",str(index[0]))
    else:
        print("element found at index : ")
        indexLen=len(index)
        for i in range(indexLen):
            print(str(index[i]))
        print("")

'''























