# Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values

my_dict = {chr(i):i for i in range(97, 123)}
print(my_dict)