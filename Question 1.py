# multiply = 1
# s = range(1,11)
#
# for i in range(5):
#     for j in range(10):
#         if s[j] == 10:
#             print(s[j]*multiply, '/n')
#             multiply = multiply + 1
#         else:
#             print((s[j]*multiply),end=' ')

fibonacci_cache = {}

def fib(n):
    if n in fibonacci_cache:
        value = fibonacci_cache[n]
    elif n == 1 or n == 2:
        value = 1
    else:
        value = fib(n - 1) + fib(n - 2)
    fibonacci_cache[n] = value
    return fibonacci_cache

value = 0
n=0
while n <=2000:
    value = fibonacci_cache
    n += 1

print(fibonacci_cache)


