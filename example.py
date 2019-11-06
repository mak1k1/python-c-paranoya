from ctypes import *
so_file = '/home/mohan/paranoYa/c/example.so'
example = CDLL(so_file)

example.test_empty()
print(example.test_add(5, 6))
