a=int(input())
list = ['Hello\n']
def foo(x):
     print x * a
def my_map_simple(fun, list):
     for item in list:
         fun(item)
my_map_simple(foo, list)
