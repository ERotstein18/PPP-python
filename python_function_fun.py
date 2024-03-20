
#1.arb_args - Takes in any number of arguments and prints them one at a time.
def arb_args(*args):
    for arg in args:
        print(arg)

def arb_args(*args):
    for i in args:
        print(i)

arb_args(1, False, "string")

#2.inner_func - Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. The result of both nested functions should then be added together and printed.


def inner_func(a, b):
    def multiplt():
        return a * b
    def divide():
        return a / b
    print(multiplt(a, b) + divide(a, b))

#3.lunch_lady - Takes in two strings: a student's name and their lunch preference. The function should print both strings. If a lunch preference is not given, "Mystery Meat" should be printed instead.

def lunch_lady(student_name, lunch="Mystery Meat"):
    print(f"{student_name}'s lunch is: {lunch}")

lunch_lady("Alice")
lunch_lady("Bob", "Spicy Hotdog")

#4.sum_n_product - Accepts two integers and returns both the sum and the product.
def sum_n_product(a, b):
    sum = a + b
    product = a * b
    return sum, product
    print(sum_n_product(a,b))