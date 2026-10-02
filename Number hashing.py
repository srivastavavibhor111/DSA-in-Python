# Applying concept of Hashing 
# Print frequency of value entered by user

# Method 1: Brute Force
print("Method 1: Using Brute Force")
n = [5, 3, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]
num = int(input("Enter the value whose frequency has to find:"))
for i in m:
    count = 0
    for j in n:
        if i == j:
            count += 1
    if i == num:
        print("Frequency of", num, "is:", count)
        break
else:
    print("Frequency of", num, "is: 0")


# Method 2: Using List Hashing
print()
print("Method 1: Using List Hashing")
n = [5, 3, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]
num = int(input("Enter the value whose frequency has to find:"))
hash_list = [0]*11
for i in n:
    hash_list[i] += 1
print(hash_list)
for i in m:
    if i > 10 or i < 1:
        print("Frequency of", num, " is 0")
    else:
        print("Frquency of", i, "is ", hash_list[i])
if num > 10 or num < 1:
    print("Frequency of", num, " is 0")
else:
    print("Frequency of", num, "is ", hash_list[num])


# Method 3: Using Dictionary Hashing
print()
print("Method 3: Using Dictionary Hashing")
n = [5, 3, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]
num = int(input("Enter the value whose frequency has to find:"))
hash_dict = {}
for i in n:
    hash_dict[i] = hash_dict.get(i, 0) + 1

for i in m:
    if i > 10 or i < 1:
        print("Frequency of", num, " is 0")
    elif i not in hash_dict:
        print("Frquency of", i, "is 0")
    else:
        print("Frequency of", i,"is", hash_dict[i])
if num > 10 or num < 1:
    print("Frequency of", num, " is 0")
elif num not in hash_dict:
    print("Frequency of", num, " is 0")
else:
    print("Frequency of", num, "is ", hash_dict[num])



