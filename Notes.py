#
#
# # print("hello world")
# #
# # # this a new line
# #
# # # Jalen
# #
# # a = 4
# # b = 3
# #
# # print(3 + 5)
# # print(5 - 3)
# # print(3 * 5)
# # print(6 / 2)
# # print(3 ** 2)
# #
# # print
# # print("try to figure out how this work")
# # print(13 % 5)
# #
# # # the"%" sign is a modlus it finds the remainder
# #
# # car_name = "wiebe mobile"
# # car_type = "BMW"
#
#
#
#
#
#
#
#
# def print_hw():
#     print("Hello world")
#     print("Enjoy the day.")
#
# print_hw()
#
#
# def say_hi(name):   # Name is a "parameter
#     print("hello %s" % name)
#     print("coding is great!")
#
# say_hi("Jalen")
#
#
# def print_age(name, age):
#     print("%s is %d years old" % (name, age))
#     age = age + 1 # age = age + 1
#     print("Next year, %s will be %d years old" % (name, age))
#
#
# print_age("Jalen", 15)
#
#
# def algebra_hw(x):
#    return x**3 + 4*x**2 + 7 * x - 4
#
# print(algebra_hw(3))
# print(algebra_hw(4))
# print(algebra_hw(5))
# print(algebra_hw(6))
# print(algebra_hw(7))
#
#
# if statements
#
#
# def grade_calc(percentage):
#     if percentage >= 90:
#         return "A"
#     elif percentage >= 80 and percentage < 90:  # elif
#         return "B"
#     elif percentage >= 70:
#         return "C"
#     elif percentage >= 60:
#         return "D"
#     else:
#         return "F"
#
#     grade_calc(92)
#
#
#     print(grade_calc(59))
#
# '''Write a function called  "happy_bday"
# that "sings" (prints) happy birthday
#
# it must take one parameter called "name"
# '''
#
#
# def happy_bday(name):
#     print("happy birthday to you")
#     print("happy brithday to you")
#     print("happy brithday dear " + name)
#     print("happy brithday to you")
#
# happy_bday("Jalen")
#
# # Loops
#
#
# for num in range(10):
#     print(num + 1)
#
#
#
# random numbers
# import random # this should be on line 1
# print(random.randint(0, 500))
#
# c = '1'
# print(c == 1)
# print(int(c ) ==1)
# print(c == str(1))
#
#
# comparisons
#
# print(1 == 1)  # use a double equal sign
# print(1 != 2)  # 1 is not equal to 2
# print(not False)
#
#
#
# list
# the_count =[1, 2, 3, 4, 5]
# cheeseburger_ingredients = ['cheese', "beef", "sauce", "sesame seed buns", "avocado", "lettace",]
# print(cheeseburger_ingredients[0])
# print(len(cheeseburger_ingredients))
#
# # going through lists
# for item in cheeseburger_ingredients:
#     print(item)

# for hi in the_count:
#     print(hi)
# for num in the_count:
#     print(num * 2)

# length = len(cheeseburger_ingredients)
# range(5)  # a list of the numbers 0 through 4
# range(len(cheeseburger_ingredients)) # Generates a list of all indices

# for num in range(len(cheeseburger_ingredients)):
#     item =  cheeseburger_ingredients[num]
#     print("The item at index %d is %s" % (num, item))

# Recasting into a list
# strOne = "hello world!"
# listOne = list(strOne)
# print(listOne)
# listOne[11] = '.'
# print(listOne)
# print(listOne[-1])


# adding to the list
# cheeseburger_ingredients.append("Fries")

# remove things from a list
# cheeseburger_ingredients.pop(1)
# print(cheeseburger_ingredients)
# cheeseburger_ingredients.remove("cheese")
# print(cheeseburger_ingredients)

# getting the alphabet
# import string
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.punctuation)

# making things lowercase
# strTwo = "ThIs Is A VeRY oDd sEnTeNCe"
# lowercase = strTwo.lower()
# print(lowercase)



# dictionaries - made up if keys: value pair

dictionary = {"name": 'Lance', 'age': 26, 'height': 6 * 12 + 2}

# Accessing things from a dictonary
print(dictionary['name'])
print(dictionary['height'])
print(dictionary['age'])

# add a pair to a dictionary
dictionary["profession"] = "telemarketer"

large_dictionary = {
    'CA':'California',
    'AZ': 'Arizona',
    'NY': 'New York'
}
print(large_dictionary['NY'])

larger_dictionary = {}

largest_dictionary = {
    'CA': {
        'name': 'California'
        'POPULATION : 392500000,
        'border st': [
    'oregon',
    'nevada',
    'arizona'
]
    },
    'AZ': {
        'name': 'arizona',
        'population': 6931000,
        'border st'
    },
    'NY': {},
}

current_node = largest_dictionary['ca']
print(current_node['Border St'][1])