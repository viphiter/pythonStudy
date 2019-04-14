
class Person(object):
    def __init__(self,name,age):
        print('自动构造对象',self)
        self.name = name
        self.age = age

    def show(self):
        print(f'姓名为：{self.name},年龄为：{self.age}')

    def __del__(self):
        print('对象销毁',self)


p = Person('苏大强','64')

p.show()

del p