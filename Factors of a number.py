from math import sqrt

# Method 1: Brute Force
print("Using Method 1: Brute Force")
result = []
num = int(input("Enter the number to find the factors:"))
for i in range(1, num+1):
    if (num % i == 0):
        result.append(i)
print("Factors are:", result)
print()

# Method 2: Better Solution
print("Using Method 2: Better Approach")
result = []
num = int(input("Enter the number to find the factors:"))
for i in range(1, (num//2)+1):
    if (num % i == 0):
        result.append(i)
result.append(num)
print("Factors are:", result)
print()

# Method 3: Optimal Solution
print("Using Method 3: Optimal Solution")
result = []
num = int(input("Enter the number to find the factors:"))
for i in range(1, int(sqrt(num))+1):
    if (num % i == 0):
        result.append(i)
        if (num // i != i):
            result.append(num//i)
print("Factors are:", result)