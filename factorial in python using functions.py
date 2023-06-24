#Factoial program using functions
def factorial(n):
  fact = 1
  for i in range (n,0,-1):             #decrementing the value from n to 1
    fact = fact * i                     #evaluating factorial
  print("Factoial of",n,'is :',fact)

n = int(input("Enter n value : "))
factorial(n)
