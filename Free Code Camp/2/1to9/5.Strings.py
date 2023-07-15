# Strings : ordered, immutable, text representation
# %, .format(), f-Strings

my_String = 'I\'m a programmer'
my_String2 = """
    Multiline strings
    """
name = "Tom"
char = my_String[-1]
subString = my_String[6:16]

# for i in my_String:
#     print(i)

if 'e' in my_String:
    print('True')
else:
    print('False')

print(type(char))
print(subString)

my_String3 = 'How,are,you,doing?'
my_List3 = my_String3.split(',')
newString3 = ''.join(my_List3)
print(my_List3)
print(newString3)

my_List4 = ['a'] * 6 # this will create a six 'A's list

var = 'Tom'
my_String5 = "The variable is %s" %var
print(my_String5)

var6 = 3.142
var6_1 = 'Jake'
my_String6 = 'The variables are {:.2f} and {}.'.format(var6, var6_1)
print(my_String6)

var7 = 8.1922
var7_1 = 9.293
my_String7 = f'The variables are {var7} and {var7_1}.'
print(my_String7)