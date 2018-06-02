""" A list the same object type (char, int, float, etc) can be
put into an array which is much more efficient than using a list

When creating an array, you must specify the data type that will 
be entered into it.

The available types are (ref https://docs.python.org/2/library/array.html):

Type code 	C Type 			Python Type 		Minimum size in bytes
'c' 		char 			character 			1
'b' 		signed char 	int 				1
'B' 		unsigned char 	int 				1
'u' 		Py_UNICODE 		Unicode character 	2 (* note)
'h' 		signed short 	int 				2
'H' 		unsigned short 	int 				2
'i' 		signed int 		int 				2
'I' 		unsigned int 	long 				2
'l' 		signed long 	int 				4
'L' 		unsigned long 	long 				4
'f' 		float 			float 				4
'd' 		double 			float 				8

Note: The 'u' typecode corresponds to Python’s unicode character. 
On narrow Unicode builds this is 2-bytes, on wide builds this is 4-bytes. 
"""


"""
Creating an array to hold signed int values (-128 - 127)


>>> b = array('b')
>>> b
array('b')
>>> b.append(12)
>>> b
array('b', [12])
>>> b.append(122)
>>> b.append(128)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OverflowError: signed char is greater than maximum
>>> b.append(-123)
>>> b
array('b', [12, 122, -123])

"""