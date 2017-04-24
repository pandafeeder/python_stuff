#this is for python3 which implicitly inherit from object

def singleton(cls):
    class SingleTonWrapper(cls):
        def __new__(cls, *args, **kwargs):
            instance = getattr(cls, "__instance__", None)
            if not instance:
                instance = object.__new__(cls)
                cls.__instance__ = instance
            return instance
    return SingleTonWrapper



@singleton
class Myclass:
    def show_addr(self):
        print(hex(id(self)))

c1, c2 = Myclass(), Myclass()

if c1 is c2:
    print("same")
else:
    raise Exception("Not same obj!")

c1.show_addr()
c2.show_addr()
