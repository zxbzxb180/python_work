def a(func):
    def test():
        func()
        print(2)
        #return func() 也可以对func进行调用
    return test

@a
def b():
    print(1)

b()
