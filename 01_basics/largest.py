largest = 0
i = 0
while i < 5 :
    num= int(input("enter a no:"))
    i+=1
    if i==1:
        largest = num
    else:
        num>largest
        largest = num
print("largest no:",largest)