n = int(input("Enter a number: "))
f = 1
if n < 0:
   print("Sorry, factorial does not exist for negative numbers")
else:
   for i in range(1,n + 1):
       f = f*i
   print("The factorial of",n,"is",f)
