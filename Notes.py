# print("hello world")
#
# # this a new line
#
# # Jalen
#
# a = 4
# b = 3
#
# print(3 + 5)
# print(5 - 3)
# print(3 * 5)
# print(6 / 2)
# print(3 ** 2)
#
# print
# print("try to figure out how this work")
# print(13 % 5)
#
# # the"%" sign is a modlus it finds the remainder
#
# car_name = "wiebe mobile"
# car_type = "BMW"








def print_hw():
    print("Hello world")
    print("Enjoy the day.")

print_hw()


def say_hi(name):   # Name is a "parameter
    print("hello %s" % name)
    print("coding is great!")

say_hi("Jalen")


def print_age(name, age):
    print("%s is %d years old" % (name, age))
    age = age + 1 # age = age + 1
    print("Next year, %s will be %d years old" % (name, age))


print_age("Jalen", 15)


def algebra_hw(x):
   return x**3 + 4*x**2 + 7 * x - 4

print(algebra_hw(3))
print(algebra_hw(4))
print(algebra_hw(5))
print(algebra_hw(6))
print(algebra_hw(7))


# if statements


def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80 and percentage < 90:  # elif
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

    grade_calc(92)


    print(grade_calc(59))

'''Write a function called  "happy_bday"
that "sings" (prints) happy birthday

it must take one parameter called "name"
'''


def happy_bday(name):
    print("happy birthday to you")
    print("happy brithday to you")
    print("happy brithday dear " + name)
    print("happy brithday to you")

happy_bday("Jalen")

# Loops


for num in range(10):
    print(num + 1)




# random numbers
import random # this should be on line 1
print(random.randint(0, 1000))
