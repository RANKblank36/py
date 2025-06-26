test_dict = {'codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'coding': 1}

print("Test Dictionary:")
for key, value in test_dict.items():
    print(f"{key}: {value}")

word = input("\nEnter the word you want to check the frequency of: ")

if word in test_dict:
    print(f"The frequency of '{word}' is {test_dict[word]}")
else:
    print(f"'{word}' is not found in the dictionary.")
