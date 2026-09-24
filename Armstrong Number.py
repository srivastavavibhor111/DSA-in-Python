# Checking if a number is a Armstrong Number or not

# Method 1
n = int(input("Enter a number:"))
num = n
nod = total = 0
print("Method 1")
while (num > 0):
    nod += 1
    num //= 10
num = n
while (num > 0):
    ld = num % 10
    total += ld**nod
    num //= 10
if (n == total):
    print(n, "is a Armstrong Number.")
else:
    print(n, "is not a Armstrong Number.")


# Method 2
print("Method 2")
nod = len(str(n))
while (num > 0):
    ld = num % 10
    total += ld**nod
    num //= 10
if (n == total):
    print(n, "is a Armstrong Number.")
else:
    print(n, "is not a Armstrong Number.")