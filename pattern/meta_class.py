import os

class StaticClassMeta(type):
    """not allowed to be instanciated"""
    def __new__(cls, name, bases, attr):
        t = type.__new__(cls, name, bases, attr)
        def e(cls): 
            raise RuntimeError('Static class cannot be instanciated')
        t.__new__ = e
        return t

class StaticClass(object, metaclass=StaticClassMeta):
    @classmethod
    def pwd(cls):
        print(os.getcwd())
    
StaticClass.pwd()

try:
    s = StaticClass()
except Exception as ex:
    print(ex)


class SealedClass(type):
    """not allowed to be inherited"""
    _types = set()
    def __init__(cls, name, bases, attr):
        if cls._types & set(bases):
            raise RuntimeError("sealed class cannot be inherited")
        cls._types.add(cls)

class A(metaclass=SealedClass): 
    def __init__(self):
        print('instanciating A...')

a = A()

try:
    class B(A): pass
except Exception as ex:
    print(ex)
