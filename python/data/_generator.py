""" Generators are iterables that calculate the returned items as they are requested
instead of beforehand"""

def do_it(x):
	print "doing something to return '{}'".format(x)
	return x

""" When using list comprehension, the calculation is done when the list is created"""

l = [do_it(n) for n in xrange(10)]
# doing something to return '0'
# doing something to return '1'
# doing something to return '2'
# doing something to return '3'
# doing something to return '4'
# doing something to return '5'
# doing something to return '6'
# doing something to return '7'
# doing something to return '8'
# doing something to return '9'

print l
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print "Ready to iterate"
# Ready to iterate

for number in l:
	print number
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

""" Use () around the expression instead of [] to create a generator"""
g = (do_it(n) for n in xrange(10))

print g
# <generator object <genexpr> at 0x7f13bb72b730>

print "Ready to iterate"
# Ready to iterate

for number in g:
	print number

# doing something to return '0'
# 0
# doing something to return '1'
# 1
# doing something to return '2'
# 2
# doing something to return '3'
# 3
# doing something to return '4'
# 4
# doing something to return '5'
# 5
# doing something to return '6'
# 6
# doing something to return '7'
# 7
# doing something to return '8'
# 8
# doing something to return '9'
