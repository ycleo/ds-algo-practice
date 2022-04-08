# index: 0, 1, 2, 3, 4, 5, 6...
# value: 0, 1, 1, 2, 3, 5, 8...

# recursive way
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#         f(6)
#   f(4)        f(5)
# f(2) f(3)   f(3) f(4)
#.......

# time: O(n ^ 2)  --> the number of node in the recursion tree
# space: O(n)     --> the depth of the recursion tree

# iterative way
def fibonacci(n):
    if n <= 1:
        return n
    else:
        a = 0
        b = 1
        while n >= 2:
            c = a + b
            a, b = b, c
            n -= 1
        return b

# time: O(n) --> linear time
# space: O(1)