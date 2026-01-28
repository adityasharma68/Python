## List : list is a data structure in python that is mutable, or changeable, ordered sequence of elements. Each element or value that is inside of a list is called an item. Just as strings are defined as characters between quotes, lists are defined by having values between square brackets [ ].

type([]) #list

lst=[1,2,3,4,5,6,7,8] #list of integers

print(lst)
print(lst[2])

lst[4]=50  #modifying the list element, that why we call it mutable


##attributes and methods of list
#lst.append(9)  #to add element at the end of the list

print(lst[2:5])  #slicing of list

lst.insert(0,0) #to add element at specific position, (index, value).

print(lst) 

## sum(list) : to find the sum of all the elements in the list
print(sum(lst))

## operation on list
lst*2  #repeats the list two times 


##SETS: A sets is an unordered collection data type that is iterable, mutable and has no duplicate elements. Python’s set class represents the mathematical notion of a set. This is based on a data structure known as a hash table.