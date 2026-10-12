# for loop: iterating by index

words = ["geeks", "for", "geeks"]

for index in range(len(words)):
    print(words[index])


# Loop control statement: continue
# It skips the rest of the current iteration.

print("\nPrint all letters except \"e\" and \"s\"")
for letter in "geeksforgeeks":
    if letter == 'e' or letter == 's':
        continue
    print('Current letter : ', letter)


# Loop control statement: break
# It exits the loop immediately.

print("\nBreak the loop as soon as it sees \"e\" or \"s\"")

for letter in "geeksforgeeks":
    if letter == 'e' or letter == 's':
        break
    print('Current letter : ', letter)
