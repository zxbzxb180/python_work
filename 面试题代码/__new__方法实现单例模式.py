class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_isinstance'):
            cls._isinstance = super().__new__(cls)
        return cls._isinstance


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

