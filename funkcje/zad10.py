#przydatne funkcje dotyczące lambdy i funkcji filtered


def double(x):
    return x * 2

x = 10
x = double(x)
print(x)

x = 10
f = lambda x: x * 2
print(f(x))

def power(x, y):
    return x ** y

x = 5 
y = 3
print(power(x, y))

f = lambda x, y: x ** y
print(f(x, y))

list_numers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_odd(x):
    return x % 2 != 0

print(is_odd(7),is_odd(8))

filteded_list = filter(is_odd, list_numers)
print(list(filteded_list))

filteded_list = filter(lambda x: x % 2 != 0, list_numers)
print(list(filteded_list))

print(list(filter(lambda x: x % 2 != 0, list_numers)))

def generate_multiply_function(n):
    return lambda x: x * n


multiply_by_2 = generate_multiply_function(2)
multiply_by_3 = generate_multiply_function(3)


print(multiply_by_2(13), multiply_by_3(8))