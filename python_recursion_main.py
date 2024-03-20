#1. Write a program that take a positive number as an argument and pritns the numbers from n to zero.

def count_down(n):
    #base case
    if n == 0:
        return

        #recursive case
    print(n)
    count_down(n - 1)

    count_down(7)

    #2. Write a function that prins the natural numbers from 1 to n.

    def natural_numbers(n, i=1):
        #base case
        if i > n:
            return
        
        #recursive case
        print(i)
        natural_numbers(n, i + 1)
    
    natural_numbers(3)

#3. Write a function that returns the nth elements in the Fibonacci Sequence.

def fibonacci(n):
    #base case
    if n == 1:
        return 0
    elif n == 2:
        return 1
    
    #recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

#print(fibonnaci(8))

#4. Write a function that calculates the value of 'a' to the power of 'b'.

def exponents(a,b):
    #4 * 4 * 4
    #base case
    if b == 1:
        return a
    
    #recursive case
    return a * exponents(a, b - 1)

#print(exponents(2,3))

#5. Write a function that checks whether a string is a palindrome or not. The program should take in a string and return True if the string is a palindrome and False if it is not.

def palindrome(str):
    #base case
    if len(str) <= 1:
        return True
    
    #recursive case
    if str[0] == str[-1]:
        return False

    return palindrome(str[1:-1])
    
#print(palindrome('33883'))

def manyParams(**kwargs):
  string_params = []
  numerical_params = []
  other_params = []

  for val in kwargs.values():
    if isinstance(val, str):
      string_params.append(val)
    elif isinstance(val, bool):
      other_params.append(val)
    elif isinstance(val, int):
      numerical_params.append(val)
    else:
      other_params.append(val)

 
  return string_params, numerical_params, other_params