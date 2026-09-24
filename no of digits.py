# Counting the number of digits in a number 

from math import log10

# Method 1
n = int(input("Enter a number:"))
num = n
nod = 0
print("Method 1")
while (num > 0):
    nod += 1
    num //= 10
print("No. of digits in", n, "is:", nod)

# Method 2
print("Method 2")
count = int(log10(n) + 1)
print("No. of digits in", n, "is:", count)
