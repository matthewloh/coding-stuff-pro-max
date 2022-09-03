#data types
int
float
complex
str
bool
list
tuple
set
dict

#Variables need to be like this
_some_stuff = "wtf"
#has to start with underscore, lowercase or uppercase, not numbers or symbols

#Strings
#[start:stop:stepover]
#immutability (strings cannot be changed, you cant reassign a part of a string, and it'll take an entirely new memory value)
quote = "to be or not to be"

quote2 = (quote.replace("be" , "hey"))
print(quote2)
print(quote)
#Booleans

#Password checker 
username = input("Please insert your username") #username

pw = input("Please insert your password") #password

pwl = len((pw.strip())) #password length

asterisks = ('*' * int(pwl)) # "*" number of elements in pwl
print(f"Hey {username}, your password {asterisks} is {pwl} characters long") #("Hey {username},  password {pw} is {pwl} long)

if pwl > 10:
    print("Wtf are you doing that's a long ass password")
else:
    print ("Your password is less than 10 characters long")

#Data Structures are a way to organize information and data into a folder. There are different types of data structure
#suitable for each stuff. It can contain all kinds of shtuff of the data types.

#Lists use the [] syntax. Tuples use ()syntax. Lists are mutable
#List methods include .extend, .append, .insert to add. To remove there are .pop, .remove and .clear
#More list methods include using keywords to find number of values or object in a list, 
# they are .count and x in basket and so on
# Some python commands or methods will produce new list, but some don't, functions like sorted do.
#another list method is .copy   
# .sort and .reverse 

# list unpacking print a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
# print(a, b, c, other, d)
# None is a type
# Dictionary is a data structure, an unordered key value pair, you can assign any type of data to a string, 
# dictionary can become a
# elements of a list, making list methods work on it, ay caramba
# Dictionary
# bruh = {'a':1, "b":2}
# bruh_list = [ {'a': [1, 2, 3, 4], 'b': "True", 'c': "banana"}, {'a': [5, 6, 7, 8], 'b': True, 'c': "orange"}, 
# {'a': [9, 10, 11, 12], 'b': "False", 'c': "bornana"} ]
# print(bruh_list[1]["c"][::-1])
# print(type((bruh_list[1]["b"])))
# print(type(bruh_list))
# A dictionary is not sorted, a list has order, it is sorted. When order matters, use a list. Dictionaries
# have a pair of values, it holds a lot more possible information. There are many other different data structures too
# 
# To be a dictionary key, that is, the thing that something is assigned to, it has to be immutable.
# A list is mutable, so it can't be a key value. When there are two identical types with same value, the thing will ge
# get over written. 
# { "123" : [1,2,3], "123" : [4,5,6]} print(dictionary["123"] will give us [4,5,6])
# There are a few kinds of dict methods that we can print like "fruit" in dictionary.values() or "hello" in 
# dictionary.keys(). There is also dictionary.items() that prints out the dictionary in tuples. 
# Then there is also dictionary.clear() and then dictionary2 = dictionary.copy()
# Dictionary also has .pop method. .pop method will remove the key, and return the value at the same time. 
# After pop, the key you pop will be removed from that dictionary's memory .popitem is soemthing new in 3.10,
# where it will remove a 
# To grab a dictionary, you need to grab it by the assigned key
# Idk man, there is also .update where you update a dictionary elemnent {"age": 123}, originally {"age:34"}, will
# give you "age: 123". If they key doesn't exist in the first place, it'll add in. 
# 
# 
# Tuples are like lists but immutable, a good use of a tuple is latitude longitude. Tuples are less flexible but 
# more performant. They behave somewhat like lists.
# .
# Operations on tuples - slicing, indexing, 
#  variable assignment works like in list so >>>x,y,z, *other = (1, 2, 3, 4, 5) will behave like you expect
# Main two methods are counting and indexing
# 
# Last main data type - set
# Sets are simply unordered collections of unique objects
# Sets cannot produce a duplicate, set.add(unique object) can, set.add(nonunique object) won't change.
# operations on sets will only use the overall set with  unique objects. 
# .copy 
# .clear are shared between sets and lists 
# Set-unique methods
# .difference(), .discard(), .difference_update(), .intersection() or &, .isdisjoint(), .issubset(), .issuperset(), 
# .union() can also use (set 1  | set 2 )
# # new_set = your_set.discard(6)
# print(your_set.discard(6))
# print(your_set)
# print(my_set.difference_update(your_set))
# print(my_set)
# print(my_set.intersection(your_set))
# print(my_set.isdisjoint(your_set))
# print(my_set | (your_set))
# print(my_set.issubset(your_set))
# print(your_set.issuperset(your_set))
# can use .update
#