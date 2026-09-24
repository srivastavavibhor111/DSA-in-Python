# Reversing a number using while loop

n = int(input("Enter a number to reverse:"))
num = n
reverse = 0
while (num > 0):
    ld = num % 10
    print(ld, end=" ")
    reverse = reverse*10 + ld
    num //= 10
print()
print("Reversed number is:", reverse)