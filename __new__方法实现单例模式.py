class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):  #hasasttr 第一个参数代表对象，第二个参数代表属性名   getasttr  setasstr
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
        return cls._instance

class MyClass(Singleton):
    a = 1

one = MyClass()
two = MyClass()

two.a = 3
print(one.a)
#3
#one和two完全相同,可以用id(), ==, is检测
print(id(one))
#29097904
print(id(two))
#29097904
print(one == two)
#True
print(one is two)
#True

