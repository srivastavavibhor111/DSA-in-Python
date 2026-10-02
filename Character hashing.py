# Character Hashing

# Method 1: Brute Force
print("Method 1: Brute Force")
s = "azyxyyzaaaa"
q = [ "d", "a", "y", "x"]
for i in q:
    count = 0
    for j in s:
        if j == i:
            count += 1
    print("Frequency of", i, "is:", count)

# Method 2: Using List Hashing
print()
print("# Method 2: Using List Hashing")
s = "azyxyyzaaaa"
q = [ "d", "a", "y", "x"]
hash_list = [0]*27
for i in s:
    ascii_value = ord(i)
    index = ascii_value - 97
    hash_list[index] += 1
for i in q:
    ascii_value = ord(i)
    index = ascii_value - 97
    print("Frequency of", i,"is:", hash_list[index])

# Method: 3 Using Dictionary Hashing
print()
print("# Method: 3 Using Dictionary Hashing")
s = "azyxyyzaaaa"
q = [ "d", "a", "y", "x"]
hash_dict = {}
for i in s:
    hash_dict[i] = hash_dict.get(i, 0) + 1

for i in q:
    if i not in hash_dict:
        print("Frequency of", i,"is: 0")
    else:
        print("Frequency of", i, "is:",hash_dict[i])
