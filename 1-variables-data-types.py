# VARIABLES
# Variable = container that stores information 
my_num = 5

#print(my_num)



# INTEGERS & FLOATS
# Integer is any number that's positive or negative 
# Ex: 5, 0, -5, -10 

# Float is any number with a decimal
# Ex: 5.0, 0.0, 2.9, -10.0 
print(5 / 2)
print(5 // 2)
print(5 // 4)
print(5 % 5)

# STRINGS
# Strings HAVE TO BE WRAPPED AROUND QUOTES
my_first_name = 'Dylan'
my_last_name = 'Song'
print(my_first_name + ' ' + my_last_name)

# Type Casting
my_age = 19
print(my_first_name + ' is ' + str(my_age))


# BOOLEANS
# True
# False
my_bool = True
this_bool = False

print('--------------------------')

# PRACTICE PROBLEM
'''
Given two variables "name" and "height_inches", print out a statement in this form:
{name} is {X} feet and {X} inches tall. 
'''
name = 'Dylan'
height_inches = 67 
print(name + ' is ' + str(67 // 12) + ' feet ' + str(67 % 12) + ' inches tall.')
