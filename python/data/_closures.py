""" A closure is where a function contains a nested function that is able to access
    variables outside of its local scope.
"""

def add_it_up():
    """ Returns a function that will take a single argument, and 
        add the number to a running total, and return the total.
    """
    numbers = []
    # closure

    def add_number(num):
        numbers.append(num)     # numbers is a free variable here
        return sum(numbers)

    return add_number

totals = add_it_up()

print totals(5)
# 5
print totals(6)
# 11
print totals(7)
# 18

""" The numbers variable is created when the add_it_up function is called, and it is
    referenced and appended to whenever totals() is called.
"""