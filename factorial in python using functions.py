#Factoial program using functions
def factorial(n):
  fact = 1
  for i in range (n,0,-1):
    fact = fact * i
  print("Factoial of",n,'is :',fact)

n = int(input("Enter n value : "))
factorial(n)
