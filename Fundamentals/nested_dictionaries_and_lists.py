
# x = [ [5,2,3], [10,8,9] ]
# z = [ {'x': 10, 'y': 20} ]

# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]

# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }

# """Change the value 10 in x to 15."""
# x[1][0] = 15
# print("1: ", x[1])

# """Change the last_name of the first student from 'Jordan' to 'Bryant'"""
# students[1]["last_name"] = 'Bryant'
# print("2: ", students[1])

# """In the sports_directory, change 'Messi' to 'Andres'"""
# sports_directory['soccer'][0] = "Andres"
# print("3: ", sports_directory['soccer'])


# """ Get Values From a List of Dictionaries """

# def iterateDictionary2(arg, dict):
#     for item in range(len(dict)):
#         print(dict[item][arg])

# iterateDictionary2('first_name', students)


"""
Iterate through a dictionary with list values - Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:
"""

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dictionary):
    for key in dictionary:
        print(str(len(dictionary[key])) + " " + key)
        for item in range(len(dictionary[key])):
            print(dictionary[key][item])

printInfo(dojo)