# Create a Frequency Map
# Store frequency of each distinct number in a dictionary

# Method 1: Brute Force
print("Method 1: Brute Force")
nums = [5, 6, 7, 7, 1, 9, 1, 1, 1, 5, 1, 1]
freq_dict = {}
for i in nums:
    if i in freq_dict:
        freq_dict[i] += 1
    else:
        freq_dict[i] = 1

print(freq_dict) 


# Method 2: Using get() method of dictionary
print("Method 2: Using get() method")
nums = [5, 6, 7, 7, 1, 9, 1, 1, 1, 5, 1, 1]
freq_dict = {}
for i in nums:
    freq_dict[i] = freq_dict.get(i, 0) + 1
print(freq_dict)