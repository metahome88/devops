# a = ["banana", "apple"]

# print("banana" not in a)

# dictionary

student = {"name": ["sam", 'joy', "gold"], "age": [34, 45, 6], "class": ("pri 1", "pri 2", 'pri 3')}
# print(student)

# methods in dictionary
student = {"name": ["sam", 'joy', "gold"], 
           "age": [34, 45, 6], 
           "class": ("pri 1", "pri 2", 'pri 3')
           }

# # index of 1
# print(student.get("class")[0][4])

# # index of pri 2
# print(student.get("class")[1])

# white space
# print(student.get("class")[1][3])

# print(student.get("class")[1][-2])


# step 1: values()
# print(student.values())
# step 2: keys()
# print(student.keys())
# step 3: items()
# print(student.items())
# step 4: get()
# print(student.get("name"))

# step 5: indexing
# print(student.get("name")[0])
# print(student.get("name")[2])
# print(student.get("name")[1][2])

# # pop
# print(student.pop("class"))
# print(student)

# # popitems
# print(student.popitem())
# print(student)

# index and slicing
name = ["programming", 'learning', 'working', 'playing']
# print(name[1][-3:])
# print(name[1][5:])
# print(name[1][5:8])


# set
"""
    a set is a data structure for the collection of data
"""
student = {'sam', 'emmy', 'jack'}
print(type(student))

# method in set
# 1 Add
student.add("rigo")
print(student)


#2 remove
student.remove("rigo")
print(student)

#3 clear
# student.clear()
# print(student)

# 4 pop
student.pop()
print(student)


