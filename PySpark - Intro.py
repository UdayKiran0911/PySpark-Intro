# Databricks notebook source
# MAGIC %md
# MAGIC ###### Why Python?
# MAGIC - For a structured data SQL does what is expected from it, however when the data is unstructure like An text, image, audio, signal etc, or semi structured like json, xml, sensors etc. SQL wont be able to handle data as expected, and this is where Python comes in.
# MAGIC - Traditional data was being stored in databases driven by a well designed applications hance it is convienent to maintain and process a structred data, however in recent past, social media, customer behaviours patters, oppinions etc. has become significant factors in data analysis and python provides vast libraries to process these types of unstructered or semi structured data.
# MAGIC
# MAGIC ###### Python in Data Engineering
# MAGIC - Storing and Retrival of Data
# MAGIC - Processing Data
# MAGIC - Managing Data
# MAGIC - Analysing Data

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Other Commands (Magic Commands)
# MAGIC - %sh: Shell Script
# MAGIC - %md: Markdown
# MAGIC - %fs: databricks file system
# MAGIC - %python: Python
# MAGIC - %sql: SQL
# MAGIC - %run: To run other notebook

# COMMAND ----------

# MAGIC %sh ls

# COMMAND ----------

# MAGIC %fs ls

# COMMAND ----------

# MAGIC %python
# MAGIC print("hello world")

# COMMAND ----------

# MAGIC %sql
# MAGIC select 1+1

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Python Basics
# MAGIC ###### Python Identifier and Variables
# MAGIC - **Python Indentifier**: Is the name given to indentify - variable, list, tuple, dictonary, function, class, module or objects, Whenever we want to give an entity a name, it is called identifier
# MAGIC   - Often, Indetifier and variable are missunderstood as same but they are not.
# MAGIC - **Python Variables**: Is the name given to a memory location where a value or data is stored, Variable is only a kind of identifier, other kinds of identifiers are function names, class names, structure names, etc. So it can be said that all variables are identifiers whereas, vice versa is not true.
# MAGIC   - As identifier and variable names are user-defined names, it should be taken care that no two identifiers or no two variable names in a program should be the same. It will create a problem of ambiguity in a program.

# COMMAND ----------

# Creating Variables
age = 30
ageFlag = True
name = "World1"
price = 27.35

# COMMAND ----------

# Deleting an object or variable
# in python everything is an object
# using del we can delete an object
a = 10
print(a)
del a
#print(a)

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Python is dynamically typed language
# MAGIC - the variable type is applied based on the data during runtime

# COMMAND ----------

var1 = 30
print("It is now: ", type(var1))
var1 = True
print("It is now: ", type(var1))
var1 = "World2"
print("It is now: ", type(var1))
var1 = 27.25
print("It is now: ", type(var1))

# COMMAND ----------

# Uses upper case names for global variables for easy understanding
# like PATH, USERNAME, PASSWORD

# use "v_" for variables
# use "gv_" for global variables
# use "f_" for functions

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Memory Location of variable

# COMMAND ----------

a = 100
b = 50
c = 100

print("a Loc: ", id(a))
print("b Loc: ", id(b))
print("c Loc: ", id(c), " Same as 'a' location") 
# here python will assign the same location because the value is same as a, instead of creating a new location python re use the previous location beased on the stored value and assign it to the variable
# for Integer values between [-5, 256], python will reuses the memory locations

# COMMAND ----------

d = 257
e = 257
f = 256
g = 256

print("d Loc: ", id(d))
print("e Loc: ", id(e), " Not same as 'd' location")
print("f Loc: ", id(f)) 
print("g Loc: ", id(g), " Same as 'f' location")

# COMMAND ----------

d = -6
e = -6
f = -5
g = -5

print("d Loc: ", id(d))
print("e Loc: ", id(e), " Not same as 'd' location")
print("f Loc: ", id(f)) 
print("g Loc: ", id(g), " Same as 'f' location")

# COMMAND ----------

d = 10.50
e = 10.50

print("d Loc: ", id(d))
print("e Loc: ", id(e), " Not same as 'd' location")

# COMMAND ----------

#we can assign same value to multiple variable as well
a=b=c=d=10
print(a,b,c,d)

# COMMAND ----------

# MAGIC %md
# MAGIC ###### String Formating

# COMMAND ----------

a = 10
b = 20
msg = "This is the price of product"

print(msg+f":a-{a}, ",msg+f":b-{b}")

# COMMAND ----------

c_count = 40
tgt_count = 30
reject = 10

# variable based
print(f'Source count:{c_count}, target count:{tgt_count}, rejected count:{reject}')
# referenced based
print('Source count:{a}, target count:{b}, rejected count:{c}'.format(a=c_count, b=tgt_count, c=reject))
# index based
print('Source count:{0}, target count:{1}, rejected count:{2}'.format(c_count, tgt_count, reject))
print('Source count:{}, target count:{}, rejected count:{}'.format(c_count, tgt_count, reject))

# COMMAND ----------

# MAGIC %md
# MAGIC ###### format stings with types
# MAGIC - %s - stings
# MAGIC - %d - digits
# MAGIC - %f - floats
# MAGIC - %c - characters
# MAGIC - %i - binary
# MAGIC - %o - octal
# MAGIC - %x - hecadecimal with lower case letters after 9
# MAGIC - %X - hecadecimal with upper case letters after 9
# MAGIC - %e - exponent notation

# COMMAND ----------

loc = "hyderabad"
temp = 31.5
quant = 16
isHotToday = True

print("Bought %d apples, at %s and is it hot today?: %i, because the temperature is around %f degree celsius"%(quant, loc, isHotToday, temp))

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Type Casting

# COMMAND ----------

a = "10"
print(type(a))
print(type(int(a)))

# COMMAND ----------

b = 10
c = 20
print(str(b)+str(c))

# COMMAND ----------

#Escape characters
str_s = 'hello  this isn\'t good'
print(str_s)

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Integers

# COMMAND ----------

print("Addition: ",2+3)
print("Substraction: ",2-3)
print("Multiplication: ",2*3)
print("Division (Result is float): ",17/7)
print("Double Division (Result is Integer): ",17//7)
print("Exponent: ",2**3)
print("Modulus (Reminder): ",17%7)

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Python Indexes
# MAGIC - left --> right = [0, n]
# MAGIC - right --> left = [-1, -n]
# MAGIC - index max val = [n-1]

# COMMAND ----------

loc = "Bangalore"
print(len(loc))
print(loc[2:8])
print(loc[-7:-2])
print(loc[::-1]) # complete reverse

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Python Datatype
# MAGIC - Numeric : int, float, complex
# MAGIC - String: str: <code>is a kind of sequence, we can retrive substring based on indexes</code>
# MAGIC - Sequence: list, tuple, range
# MAGIC - Binary: bytes, bytearray, memoryview : <code>dealing with audios, videos images, encoded data</code>
# MAGIC - Mapping: dict
# MAGIC - Boolean: bool
# MAGIC - Set: set, frozenset
# MAGIC - Data Structures (Collections): list, tuple, range, dict, set, frozenset

# COMMAND ----------

# Range
# range() function is used to generate sequance of numbers over time
# syntax range(star, stop, step)

print(list(range(10)))
print(type(range(10)))

# COMMAND ----------

print(list(range(0, 5)))

# COMMAND ----------

# prints all even numbers
print(list(range(0,20, 2)))

# COMMAND ----------

# prints all odd numbers
print(list(range(1,20, 2)))

# COMMAND ----------

# MAGIC %md
# MAGIC ###### list, tuple, dict, sets

# COMMAND ----------

lst = [1,2,3,4,"hello",True, 23.5, 54.1]
print(lst)
print(type(lst))
print(lst[2:5])
lst.append(6)
print(lst)
lst.extend([11,12,"world"]) # extends the existing list
print(lst)
lst.append([14,15,"this is string", False]) # append adds new item as another item in existing list
print(lst)
print(lst[::-1]) # reverses the list
print(lst.index(2))
lst.insert(4, 5) # insert based on index
print(lst)
lst2 = [1,6,3,8,2,0,4,6,9,6,3,2,7]
lst2.sort()
print(lst2)
lst2.sort(reverse=True)
print(lst2)
lst2 = [1,6,3,8,2,0,4,6,9,6,3,2,7]
lst2.reverse()
print(lst2)

lst2.remove(8) # remove element by value
print(lst2)
lst2.pop(3) # remove element by index , also pop returns the value that is being removed
print(lst2)
lst2.pop() # remove the last element
print(lst2)

del lst2[5]
print(lst2)

lst2.clear() # it removes all the values and clears the memory as well
print(lst2)

# COMMAND ----------

# Defualt copy
print("\nDefualt copy")
lista = [1,2,3,4,5,[7,8,9,10]]
listb = lista.copy()
print("original list and memory location:",lista, id(lista))
print("original sublist list and memory location:",lista[5], id(lista[5]))
print("copied list and memory location:",listb, id(listb))
print("copied sublist and memory location:",listb[5], id(listb[5]))

print("\nAfter listb update")
listb.append(12) 
listb[5].append(11)
listb[3] = 300
print(lista, id(lista))
print(listb, id(listb))

# while the memory locations of the orginal lista and listb are different, any changes in list b will not reflect at element level
# howvever the location of sub list on both lista and list b are same, any changes in sublist of list b will reflect in sublist of lista as well

# COMMAND ----------

import copy

# COMMAND ----------

# Deep copy
print("\nDeep copy")
lista = [1,2,3,4,5,[7,8,9,10]]
listb = copy.deepcopy(lista)
print("original list and memory location:",lista, id(lista))
print("original sublist list and memory location:",lista[5], id(lista[5]))
print("copied list and memory location:",listb, id(listb))
print("copied sublist and memory location:",listb[5], id(listb[5]))

print("\nAfter listb update")
listb.append(12) 
listb[5].append(11)
listb[3] = 300
print(lista, id(lista))
print(listb, id(listb))

# location of lista and listb are different
# also location of sublist of lista and sublist of listb is also different
# changes in anyway on listb will not refelect in lista

# COMMAND ----------

# shallow copy
print("\nShallow copy")
lista = [1,2,3,4,5,[7,8,9,10]]
listb = copy.copy(lista)
print("original list and memory location:",lista, id(lista))
print("original sublist list and memory location:",lista[5], id(lista[5]))
print("copied list and memory location:",listb, id(listb))
print("copied sublist and memory location:",listb[5], id(listb[5]))

print("\nAfter listb update")
listb.append(12) 
listb[5].append(11)
listb[3] = 300
print(lista, id(lista))
print(listb, id(listb))

# copy and shallow copy are the same

# COMMAND ----------

tup = (1,2,3,4,5)
print(tup[1:3])
# tup[2]=7, # will raise error, because tuple are immutable
print(len(tup))
print(tup.index(2)) # fetch index having value

tup2 = (7,8,9)
print(tup+tup2)

# COMMAND ----------

a = {} # default as 'dict'
print(a, type(a))
a = {1,2,3,4,5,5} # only takes unique values, drops duplicates automatically
print(a, type(a))
a = {"one":1, 'two':2, 'three':3}
print(a, type(a))

# COMMAND ----------

a = set(list(range(10)))
print(a)
b = set(list(range(3,12,1)))
print(b)
c = set(list(range(3,7,1)))
print(c)

print("\nSet Operations")
print(a.union(b)) # merge all values and drops duplicates
print(a.intersection(b)) # fetach only the common values
print(a.difference(b)) # fetch elements of a that are not in b
print(b.difference(a)) # fetch elements of a that are not in b
print(c.issubset(a))
print(b.issubset(a))

# add, remove, search values in set
b.remove(8) # if item is not found remove will raise exception
b.discard(10) # if item is not found, discard doen't raise exception
print(b)
b.add(13)
print(b)
#print(b[2]) # will raise error because there is no index in sets, hence are ordered
print(2 in b)
print(2 in a)



# COMMAND ----------

a = {"one":1,"two":2,"three":3,"four":4}
print(type(a))
print(a["three"])
print(a.keys())
print(a.values())
a["two"]=22
print(a)
a.update({"five":5})
print(a)
print(22 in a) # defualt it will search in keys
print("three" in a)
print(22 in a.values())
# print(a[1]) # will raise error because there is index (by keys) in dictionary, but is undered are ordered
# print(a.index("three"))  # will raise error because there is index (by keys) in dictionary, but is undered are ordered
print(a.items())

a = {"one":1,"two":2,"three":3,"four":4, "three":3,"four":44}
print(a) # doesn't allow duplicates, and will keeps the right most key value in the case of duplicates and drop others

# COMMAND ----------

a  = frozenset({'apple','1',True,5})
print(a, type(a))
#a[2] = False #will rase error, because frozensets are immutable
#print(a[1]) # can't access frozenset values same as sets
print([x for x in a])
#print(a.contains('apple'))
print('apple' in a)

# COMMAND ----------

# MAGIC %md
# MAGIC ###### bool, bytes, bytearray, memoryview, complex

# COMMAND ----------

a=False
b=1
print(a, type(a))
print(b, type(bool(a)))


# COMMAND ----------

x = b'hello'
print(x, type(x))
print(x[2])
# x[2]="w" # immutable

y = "world"
print(bytes(y, 'utf-8'))

z = 50
print(bytes(z))

# COMMAND ----------

x = bytearray(144)
print(x, type(x))
print(x[2])
x[2]=5 # muteable
print(x)

# COMMAND ----------

mv = memoryview(bytes(55))
print(mv, "\n", bytes(mv),"\n", list(mv))

# COMMAND ----------

mv = memoryview(bytes("0123abcABC", 'utf-8'))
print(mv, "\n", bytes(mv),"\n", list(mv))

mv = memoryview(bytearray("python", 'utf-8'))
print(mv, "\n", bytes(mv),"\n", list(mv))
mv[0]=122
print(bytes(mv)) # replaced with ascii value of p with z

# COMMAND ----------

comp_x = 10+5j
print(comp_x, type(comp_x))
print(comp_x.conjugate())
print(comp_x.real, comp_x.imag)
print(comp_x.conjugate().real, comp_x.conjugate().imag)

print(comp_x+comp_x.conjugate())
print(comp_x-comp_x.conjugate())

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Date and Time

# COMMAND ----------

import datetime
x = datetime.datetime.now()
print(x, type(x))

print(x.day, x.year, x.month)
print(x.strftime("%A"), x.strftime("%a"))
print(x.strftime("%B"), x.strftime("%b"), x.strftime("%m"))
print(x.strftime("%H"), x.strftime("%M"), x.strftime("%S"), x.strftime("%p"))
print(x.strftime("%I"))

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Conditional Statements and loops

# COMMAND ----------

# MAGIC %md
# MAGIC ###### if-elif-else

# COMMAND ----------

a = 55
b = 66
if a == b:
    print("Equal")
else:
    print("Unqual")

# COMMAND ----------

a = 55
b = 66
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")

# COMMAND ----------

a = 55
b = 55
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")

# COMMAND ----------

# short hand if
a = 15
b = 45
if a > b: print("a greater then b")

# short hand if else
a = 30
b = 55
print("a greater then b") if a > b else print('a is less then b') # <true stmt> if <cond> else <false stmt>

# short hand if elif else
a = 30
b = 30
print("a greater then b") if a > b else print('a is less then b') if a < b else print("a is equal to b")
# <true stmt> if <cond> else 
#     <true stmt> if <cond> else 
#        <false stmt>

# COMMAND ----------

# MAGIC %md
# MAGIC ###### for loop

# COMMAND ----------

for a in range(5):
    print(a)

# COMMAND ----------

for a in "hello world":
    print(a)

# COMMAND ----------

fruits = ["apple",'banana','cherry','orange','lemon']
for fruit in fruits:
    if fruit == 'cherry':
        break # complete loop is terminated
    print(fruit)

# COMMAND ----------

fruits = ["apple",'banana','cherry','orange','lemon']
for fruit in fruits:
    if fruit == 'cherry':
        continue # skip rest, continue to next interation
    print(fruit)

# COMMAND ----------

fruits = ["apple",'banana','cherry','orange','lemon']
for fruit in fruits:
    if fruit == 'cherry':
        pass # placeholder for future statements
    print(fruit)

# COMMAND ----------

# MAGIC %md
# MAGIC ###### while loop

# COMMAND ----------

# careful with while
i = 0
while i < 10:
    print(i) 
    i+=1

# COMMAND ----------

# MAGIC %md
# MAGIC ###### functions
# MAGIC - positional arguments
# MAGIC - keyword arguments
# MAGIC - default arguments
# MAGIC - variable length arugments (*args)
# MAGIC - key-value pair arguments (**kwargs)
# MAGIC - pass by value, pass by reference
# MAGIC - lambda function

# COMMAND ----------

# creating functions
def func_sum(a,b):
    return a+b

func_sum(3,4)

# COMMAND ----------

# positional arguments
# by defualt parameters are read left to right
def name_age(name, age):
    print("Name is:", name)
    print("Age is:",age)
    
name_age('uday', 36)
name_age(36, 'uday')

# COMMAND ----------

# keyword arguments
# arguments are passed using key-value pair, so order is not important
def name_age(name, age):
    print("Name is:", name)
    print("Age is:",age)
    
name_age(name='uday', age=36)
name_age(age=36, name='uday')

# COMMAND ----------

# default arguments
# if argument is not specified default value be consiidered
# defualt arguments must follow non-default arguments
def name_age(age, name='uday'):
    print("Name is:", name)
    print("Age is:",age)
 
name_age(age=36)
name_age(36, name='kiran')

# COMMAND ----------

# variable length arguments
def value_sum(*args):
    return sum(args)

print(value_sum(1,2,3,4,5,6))
print(value_sum(1,2,3))
print(value_sum(100, 200))

# COMMAND ----------

# variable length arguments key value pairs
def kv_data(**kwargs):
    for k, v in kwargs.items():
        print(k, v)
print(kv_data(name='uday',lastname='kiran',age='36'))
# none appears because the functions is trying to return something, and as there is no return statement it returns none.

# COMMAND ----------

# pass by value, pass by reference

# PASS BY VALUE
def show_rslt(param1):
    param1=param1+200
    print(id(param1))
    return param1

param1=30
print(param1, id(param1))
print(show_rslt(param1))
print(param1, id(param1))

# COMMAND ----------

# pass by value, pass by reference

# PASS BY Reference
def show_rslt(param1):
    param1.append('b')
    print(id(param1))
    return param1

param1=["a"]
print(param1, id(param1))
print(show_rslt(param1))
print(param1, id(param1))

# COMMAND ----------

#lambda function
lam_fun = lambda a: a+10
print(lam_fun(20))

lam_fun = lambda a, b: a+b
print(lam_fun(30,50))

lam_fun = lambda a, b: a if a>=b else b
print(lam_fun(30,60))
print(lam_fun(50,25))

lam_fun = lambda a, b: a if a>b else b if a<b else "both equal"
print(lam_fun(25,30))
print(lam_fun(40,20))
print(lam_fun(50,50))

lam_fun = lambda a: [x for x in range(a)]
print(lam_fun(15))

lam_fun = lambda a, b: [x+b for x in range(a)]
print(lam_fun(10, 5))

lam_fun = lambda a: [x for x in range(a) if x%2==0]
print(lam_fun(44))

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Exception(Error) Handling

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Try - Except - Else - Final blocks

# COMMAND ----------

# Data Level Exceptions
try:
    a = 10
    b = '12'
    print(a/b)
    print('exception raised, continuing')
except Exception as e:
    print("Found Exception: ",e)
    
try:
    a = 10
    b = 0
    print(a/b)
    print('exception raised, continuing')
except ZeroDivisionError as e:
    print("Found ZDE Exception: ",e)
except Exception as e:
    print("Found Exception: ",e)

# COMMAND ----------

# Data Level Exceptions
try:
    a = 10
    b = '12'
    print(a/b)
    print('exception raised, continuing')
except Exception as e:
    print("Found Exception: ",e)
else:
    print("All Well")

# COMMAND ----------

# Data Level Exceptions
try:
    a = 10
    b = 0
    print(a/b)
    print('exception raised, continuing')
except Exception as e:
    print("Found Exception: ",e)
else:
    print("All Well")
finally:
    print("Execute Anyway")

# COMMAND ----------

# Data Level Exceptions
try:
    raise NameError("Raise Division by zero error") 
except NameError as d:
    print("Error Found: ",d)
finally:
    print("Execute Anyway")

# COMMAND ----------

# MAGIC %md
# MAGIC ###### File Handling
# MAGIC - 'r': read - Default, error if file do not exists
# MAGIC - 'a': append - append data to file at EOF, creates file if not exists
# MAGIC - 'w': write - overwrite to file be recreating, creates file if not exists
# MAGIC - 'x': creates file, error if file exists

# COMMAND ----------

# MAGIC %fs ls dbfs:/

# COMMAND ----------

# MAGIC %fs ls file:/

# COMMAND ----------

with open('file://usr//abc.txt', 'a') as textfile:
    textfile.write("""Hello\nWorld""")

# COMMAND ----------

# MAGIC %fs ls '/user/'

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Common Operators
# MAGIC <table>
# MAGIC   <thead>
# MAGIC     <th>Operator</th>
# MAGIC     <th>Description</th>
# MAGIC     <th>Returns</th>
# MAGIC   </thead>
# MAGIC   <tbody>
# MAGIC     <tr><td>==,!=,&gt;,&lt;,&gt;=,&lt;=</td>
# MAGIC       <td>Comparision Operators: used for comparing two objects or values</td>
# MAGIC       <td>Boolean(True, False)</td>
# MAGIC     </tr>
# MAGIC     <tr><td>and, or, not</td>
# MAGIC       <td>logical operators: used for validating two statements</td>
# MAGIC       <td>Boolean(True, False)</td></tr>
# MAGIC     <tr><td>enumerate</td>
# MAGIC       <td>adds a counter to iterable object</td>
# MAGIC       <td>counter, value</td></tr>
# MAGIC     <tr><td>zip()</td>
# MAGIC       <td>paring two equal length sequence objects</td>
# MAGIC       <td>paried values</td></tr>
# MAGIC     <tr><td>sum(), min(), max(), mean()</td>
# MAGIC       <td>aggregate functions</td>
# MAGIC       <td>values</td></tr>
# MAGIC     <tr><td>isinstance</td>
# MAGIC       <td>to find the type of the object</td>
# MAGIC       <td>Boolean(True, False)</td></tr>
# MAGIC     <tr><td>reversed(list)</td>
# MAGIC       <td>reverses the iterable object</td>
# MAGIC       <td>Reversed Object</td></tr>
# MAGIC   </tbody>
# MAGIC </table>

# COMMAND ----------

lst = [1,2,3,4,5]
tup = (6,7,8,9,10)
print('\nEnumerate function')
for idx, val in enumerate(lst):
    print(idx, val)
    
print('\nZip function')
for lsval, tuval in zip(lst, tup):
    print(lsval, tuval)

# COMMAND ----------

lst2 = [1,2,3,4,5,6,7,8,9]
print(sum(lst2))
print(min(lst2))
print(max(lst2))

# COMMAND ----------

print(isinstance(5, int))
print(isinstance(7.6, float))
print(isinstance("Hello", str))

# COMMAND ----------

print(list(reversed([1,4,5,2,3,6])))
print(list(reversed((8,12,13,9,10,11))))

# COMMAND ----------

# MAGIC %md
# MAGIC ###### globals and locals
# MAGIC will give all the variables and functions, objects in global and local sessions

# COMMAND ----------

globals()

# COMMAND ----------

locals()

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Random
# MAGIC - shuffle : shuffle the randomly in the sequence
# MAGIC - randit: generate a random sequence of numbers with in a range

# COMMAND ----------

import random

lst1 = [1,2,3,4,5,6,7]
random.shuffle(lst1)
print(lst1)

print(random.randint(5,10))

# COMMAND ----------

# MAGIC %md
# MAGIC ###### split
# MAGIC - it will split a string based on a seperator
# MAGIC ###### upper, lower
# MAGIC - case conversion
# MAGIC ###### replace
# MAGIC - replace a string with another string
# MAGIC ###### strip
# MAGIC - removes whitespaces leading and trailing ends of the string
# MAGIC ###### capitalize
# MAGIC - first character of a string is capitalized

# COMMAND ----------

print("Hello World".split(" "))
print("Hello World".upper())
print("Hello World".lower())
print("Hello World".replace('World',"Everyone"))
print(" Hello World ".strip()) # lstrip() for leading space, rstrip() for trailing end space
print("hello everyone, how are you".capitalize())

# COMMAND ----------

# MAGIC %md
# MAGIC ###### filter and reduce

# COMMAND ----------

def geteven(num):
    if num%2==0:
        return num
    
print(list(filter(geteven, [1,2,3,4,5,6,7,8])))

print(list(filter(lambda x: x%2==0, [1,2,3,4,5,6,7,8,9,10,11,12])))

# COMMAND ----------

from functools import reduce

list1 = [1,2,3,4,5,6,7,8,9,10]
print(reduce(lambda a,b: a+b, list1))

# COMMAND ----------

# MAGIC %md
# MAGIC ###### list comprehension

# COMMAND ----------

lst2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

print([x**2 for x in lst2])

print([x for x in lst2 if x%2==0])

print([x if x%2==0 else x**2 for x in lst2])

# COMMAND ----------

# MAGIC %md
# MAGIC ###### assert
# MAGIC - if the condition is true, assert wont return anything
# MAGIC - if the condition is false, it would return the string after (,)
# MAGIC - used during unit test

# COMMAND ----------

a=10
b=5

assert(a==b), "Both a and b are not equal"
# if the condition is true, assert wont return anything
# if the condition is false, it would return the string after (,)

# COMMAND ----------

a=10
b=10

assert(a==b), "Both a and b are equal"
# if the condition is true, assert wont return anything
# if the condition is false, it would return the string after (,)
