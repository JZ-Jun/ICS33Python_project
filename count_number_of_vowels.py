# Write a Python Program to Count the Number of Vowels in a String.
str = "qaweps"  # the str it gave us
i = 0
for each in str:
    if each in "aeiouAEIOU":
        i += 1
print(i)
