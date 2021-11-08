list = [] # creating an empty list

n = int(input("Enter number of elements : ")) 

for i in range(0, n): # iterating till the range
    element= int(input())
    list.append(element) # adding the element   
print(list)

matrices = []
# find highest height of the peak-----------------------------
highestPeak = 0
temp = 0
totalWidth = 0
currentWidth = 0
for ind,dist in enumerate(list):
    if (ind % 2) == 0:
        temp = temp+dist
    else:
        temp = temp-dist
    if(temp>highestPeak):
        highestPeak = temp
        
    totalWidth = totalWidth + dist

currentHeight = highestPeak

# To add values in matrix 
for ind,j in enumerate(list):
    for k in range(j):
        #print(j,"K")
        if(ind%2 ==0):
            matrices.append([currentWidth,currentHeight,"UP"])
            currentHeight = currentHeight-1
        else:
            currentHeight = currentHeight+1
            matrices.append([currentWidth,currentHeight,"DOWN"])
        #print("Current Width Before :",currentWidth)  
        currentWidth = currentWidth+1  
        #print("Current Width After :",currentWidth)
        
    #print("Width : ",totalWidth)    
#print(matrices)

# To get highest Position
def findHighestPos(): 
    for x in matrices:
        if x[1]==1:
            return x[0]
            
#-------------Head-----------------#
for head in range(totalWidth+1):
    if head==findHighestPos():
        print("O",end="")
    else:
        print(" ",end = "")


print ("")

#-------------Hand-----------------#
for hand in range(totalWidth+1):
    if hand+1==findHighestPos():
        print("/",end = "")
    elif hand-1==findHighestPos():
        print("\\",end = "")
    elif hand==findHighestPos():
        print("|",end = "")
    else:
        print(" ",end = "")
        
print ("")

#-------------Leg-----------------#

for leg in range(totalWidth+1):
    if leg+1==findHighestPos():
        print("<",end = "")
    elif leg-1==findHighestPos():
        print(">",end = "")
    elif leg==findHighestPos():
        print(" ",end ="")
    else:
        print(" ",end ="")
#-------------------

for x in range(int(totalWidth)): #10
    for y in range(totalWidth+1): #56
        if [y,x,"UP"] in matrices:
            print("/",end = "")
        elif [y,x,"DOWN"] in matrices:
            print("\\",end = "")
        else:
            print(" ",end = "")
    print(" ")
'''print("length of the list = ", len(list)) 
print("totalwidth  = ",totalWidth)  '''
#print(findHighestPos())
