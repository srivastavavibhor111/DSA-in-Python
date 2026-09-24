# Checking if a number is Palindrome or not

# Method 1
n = int(input("Enter a number:"))
print("Method 1")
num = n
reverse = 0
while (num > 0):
    ld = num % 10
    reverse = reverse*10 + ld
    num //= 10
if (reverse == n):
    print(n, "is a Palindrome Number.")
else:
    print(n, "is not a Palindrome Number.")


# Method 2
print("Method 2")
s = str(n)
reverse_str = s[::-1]
if (reverse_str == s):
    print(n, "is a Palindrome Number.")
else:
    print(n, "is not a Palindrome Number.")

