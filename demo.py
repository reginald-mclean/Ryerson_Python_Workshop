# Assumptions I have made:
# You have Python (version >= 3.6) installed. Python 2.x can be very different
# You have some sort of development environment installed
# This IDE is called PyCharm, it is free. There are others as well

# Today: Data types, data structures, different operations, loops, if statements, functions
# maybe some objects, and advanced Python tools
# Next time: Using these tools for data analysis



# Data Types
#  Int, Float
a = 1348572349
b = 1.5
c = 5.5

#  String
c = "Reggie"

#  Bool
d = True
e = False

#  Lists
# f = []
# print(f)
# f.append('a')
# print(f)
# f.append('b')
# print(f)
# f.insert(0, 'c')
# print(f)
# print(f[0])
# print(f[1])
# print(f[2])
# print(len(f))

g = [10, 11, 12, 13, 14]
g.append(15)
# print(g[4])
# print(g[-1])

# print(g[-5])

# h = "This$is$the$text$from$the$user"
# l = h.split('$')
# print(l)


#c = "This.is.the.Python.Tutorial"
#h = c.split('.')
#print(h)




a = 1234
a = 234.234234
a = 'This is a string'
a = True




#  = [1, '2', 3.0, '4', True]
# count = g[0] + g[1]
# print(g)


#  Operations
a = 10
b = 3
i = a + b
# print(i)
j = a - b
# print(j)
l = a * b
# print(l)
m = 3/2
# print(type(m))  # 3.333333333
m = 3//2
# print(type(m))  # 3



n = 2.1 ** 3.7
# print(n)





n = 12 % 3
# print(n)


c = (a + b)
d = c ** b
o = d + 100
# print(o)


a = 5
b = 3

o = (b * b) / a
# print(o)


a = False
b = False


# if a == True and b == True:
#     print("A or B was true")

# if a is 5 or b is 10:
#    print("A or B was true")


# True True = True
# True False = False
# False True = False
# False False = False
'''
a = 5
d = True
if a == 5.9:
    print("This was true!")
if d is True:
    print(d)'''
'''a = 1
if a*6 == 30:
    print("Yeah ok")
elif a == 1000:
    print([1, 2, 3])
else:
    print("Probably this")'''

# count = 100
# max_iterations = 0
# while count > max_iterations:
#    print("The statement is True")
#    count -= 1 # count = count + 1

l = [i for i in range(100, 110)]

import random
random.shuffle(l)
# print(l)
# l.sort()
# print(l)
# print(sorted(l))

'''
print(l)

my_dictionary = {}
my_dictionary['Reggie'] = 100
my_dictionary[2348234] = 12
my_dictionary[12.12] = 912
print(my_dictionary)
print(my_dictionary['Reggie'])

for i in my_dictionary:
    print(i)
    print(my_dictionary[i])


'''

def AddTwoVariables(a, b):
    c = a + b
    return c


result = AddTwoVariables(5, 10)
print(result)

# reginald.mclean@ryerson.ca








'''
def my_function(x):
    x += 1
    # do something to x
    return x
#print(my_function(3))

#  While loop
s = 5
while s > 0:
    #print(s)
    s = s - 1
#print("The loop is complete")

#  For loop
#for i in range(20, -1, -2):
#    print(i)
g = [1, '2', 8, '4', 5.4]
#for idx in range(len(g)):
#    print(g[idx])
#print(g[-2:])
h = ['Reggie', 'Mackenzie', 'Gus', 'Matthew', 'Samantha']
j = [100, 98, 97, 96, 99]
#print(h)
#h.sort()
#h = sorted(h, reverse=True)
#print(h)
my_dictionary = {}
my_dictionary["Reggie"] = 100
my_dictionary["Maggie"] = 99
my_dictionary["Mahek"] = 99
#print(my_dictionary)
keys = list(my_dictionary.keys())
for i in keys:
    print(my_dictionary[i])


#  Conditional Statements
#  If/elif/else
if a == 5:
    print("This was true!")
if d:
    print(d)

if a*6 == 5:
    print("Yeah ok")
elif a == 1000:
    print("Hmmm")
else:
    print("Probably this")
#  While loop
s = 5
while s > 0:
    print(s)
    s -= 1
#  For loop
for i in range(5):
    print(i)

#  Dictionaries
my_dictionary = {}
my_dictionary['Reggie'] = 100
my_dictionary[5] = 1

#  2D Arrays
t = [[1, 2, 3], [9, 10, 11], [14, 9, 5]]
print(t)

#  Sorting
g.sort()
sorted(g)


class Car:
    def __init__(self):
        self.brand = "Honda"
        self.model = "Civic"
        self.year = 2016

    def print(self):
        print(self.brand + " " + self.model + " " + str(self.year))


my_car = Car()
my_car.print()


#  Classes/Objects



#  Functions
#  Return values

# Advanced Python
#  List Comprehensions
#  Multiple Function Arguments
#  Sets
#  Map, Filter, Reduce'''
