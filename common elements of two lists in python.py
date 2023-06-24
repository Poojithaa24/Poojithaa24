#Writ a python program for printing common elements of the two lists
l1 = [1,2,3,4,5]
l2 = [4,5,6,7]
common = []          #Empty list 
#Finding common elements in two lists
for i in l1:
  for j in l2:
    if(i == j):
      common.append(j)        #common elements are appended to list 'common'
print("Common elements:",common)
