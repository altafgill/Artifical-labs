# Question 8: Print Numbers 0 to 6, Skipping 3 and 6

for num in range(7):
    if num == 3 or num == 6:
        continue
    print(num, end=" ")