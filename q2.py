x = []
# Taking user input for the length of array.
n = int(input("Enter the num of entries:"))
# Taking user input for the array.
for i in range(0,(n)):
    x.append(int(input("{0}th number:".format(i))))

print(x)

count = 0
temp = 0
tempn = 0
final = [0]     #If there are more than 1 such element.
#Traversing through the array using two pointer variables inorder to count maximum frequency of the most occuring element.
for i in x:
    for j in x:
        if(i==j):
            temp +=1
            tempn = j
    if(count<temp):
        count = temp
        final = [tempn]
    if(count==temp and tempn not in final):
        final.append(tempn)
    temp = 0

#Printing the final result.
print("Maximum frequency value is:",count," With element:",final)
