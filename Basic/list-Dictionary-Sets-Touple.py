## List : list is a data structure in python that is mutable, or changeable, ordered sequence of elements. Each element or value that is inside of a list is called an item. Just as strings are defined as characters between quotes, lists are defined by having values between square brackets [ ].

type([]) #list

lst=[1,2,3,4,5,6,7,8] #list of integers

# print(lst)
# print(lst[2])

lst[4]=50  #modifying the list element, that why we call it mutable


##attributes and methods of list
#lst.append(9)  #to add element at the end of the list

# print(lst[2:5])  #slicing of list

lst.insert(0,0) #to add element at specific position, (index, value).

# print(lst) 

## sum(list) : to find the sum of all the elements in the list
# print(sum(lst))

## operation on list
lst*2  #repeats the list two times 


##SETS: A sets is an unordered collection data type that is iterable, mutable and has no duplicate elements. Python’s set class represents the mathematical notion of a set. This is based on a data structure known as a hash table.


#Define an empty set
# s = set()
# print(type(s))
# print({1,2,3,4,5})  #define a set with elements

# set1 = set({1,9,3,4,8,5,6,4,3}) #repeated element not shown in output
# print(set1)

set1 = {'Hulk', 'Ironman', 'Capt. America', 'Thor'}
set2 = {'Hulk', 'Ironman', 'Capt. America', 'Thor', 'Black Widow'}
# set2={'Superman', 'Batman', 'Aquaman'}

# print(set1)
# print(set2)

(set1.intersection_update(set2))
# print(set1)

set2.difference_update(set1) #the ouptput will be the elements that are in set2 but not in set1 that is 'Black Widow'
# print(set2)

# print(set1.issubset(set2)) #checks if set1 is subset of set2 or not
# print(set2.issuperset(set1)) #checks if set1 is superset of set2 or not

## Dictionary: A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

# dict() dictionary

dic1=dict(name="Aditya", age=21, city="New Delhi")
# print(dic1)

#We can even create dictionary using loop

# my_dic={"Car1":"BMW", "Car2":"Audi", "Car3":"Ferrari"}

# print(my_dic['Car2'])

# for x in my_dic:
#     print(x)  #prints the keys of the dictionary

# for x in my_dic.values(): #prints the values of the dictionary
    # print(x)  

##Adding the items to the dictionary
# my_dic["Car4"]="Lamborghini"
# print(my_dic)


##Nested Dictionary: A nested dictionary is a dictionary that contains another dictionary inside it.

car1_model={"Model":"mercedice", "Year":2020, "Price":"80L"}
car2_model={"Model":"Audi", "Year":2021, "Price":"90L"}
car3_model={"Model":"Ambassador", "Year":2019, "Price":"3Cr"}

cars={"Car1":car1_model, "Car2":car2_model, "Car3":car3_model}

print(cars)
print(cars['Car2']['Model'])  #Accessing the nested dictionary value
print(cars['Car3']['Year']) #Accessing the nested dictionary value

## Touple: A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

#create a tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)