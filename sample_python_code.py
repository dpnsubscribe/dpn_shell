# Assign True or False as appropriate on the lines below!

# Set this to True if 17 < 328 or to False if it is not.

bool_one = (17<328)
# We did this one for you!

print bool_one

# Set this to True if 100 == (2 * 50) or to False otherwise.
bool_two = (100 == (2*50))

print bool_two


# Set this to True if 19 <= 19 or to False if it is not.
bool_three = (19<=19)

print bool_three


# Set this to True if -22 >= -18 or to False if it is not.
bool_four = (-22>=-18)
print bool_four


# Set this to True if 99 != (98 + 1) or to False otherwise.
bool_five = (99!=(98+1))
print bool_five


print 'Welcome to the Pig Latin Translator!'

# Start coding here!

original = raw_input("Enter a word:")

if len(original) >0 and original.isalpha():
    
    print original

else:
    print "empty or not alpha"