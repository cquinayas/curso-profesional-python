from urllib.response import addinfo
from pkg_resources import resource_listdir


num = 71
resultado = [x for x in range(2, num) if num % x == 0]
print(resultado)
print(len(resultado)==0)

#Local scope
def my_func():
    y=5
    print(5)
my_func()

#Global scope
x=5
def my_funct():
    print(x)

my_funct()
#nested 
def main():
    a=1
    def nested():
        print(a)
    nested()
main()
#closures
def main2():
    a = 1
    def nested2():
        print(a)
    return nested2
my_func = main2()
my_func()
del(main2)
my_func()
    
