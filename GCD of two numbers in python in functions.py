#GCD of two numbers using functions in python
def gcd(a,b):
  
  fact_a = []            #empty list for factors of a
  fact_b = []            #empty list for factors of b
  hcf = []                #empty list for the common factors of a and b
   #Finding the factors of a
  for i in range(1,a+1):
    if(a%i==0):
      fact_a.append(i)        #appends the list fact_a with factors of a  

    #Finding the factors of b  
  for i in range(1,b+1):
    if(b%i==0):
      fact_b.append(i)        #appends the list fact_a with factors of a

    #For finding the common factors of a and b
  for i in fact_a:
    for j in fact_b:
      if (i==j):
        hcf.append(i)          #Common factors of a and b are appended to list hcf
  hcf.sort()                   #the list is sorted and arranged in accesding order
  return hcf[-1]               #last element in the list hcf is the "gcd" of a and b
    
a = int(input("Enter first number : "))
b = int(input("Enter second number :"))
x = gcd(a,b)
print("The greatest common divisor of",a,"and",b,"is",x)
