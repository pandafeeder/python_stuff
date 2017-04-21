"""
abstrcted class can't be instanciated directly,
sub class(s) has to implentent all abstructedmethod
and abstrctedproperty in oreder to be able to be instanciated
"""

from abc import ABCMeta, abstractmethod, abstractproperty

class IdealRobotModel(metaclass=ABCMeta):
    def __init__(self, name, lines):
        self._name = name
        self._lines = lines
    
    @abstractmethod
    def talk(self): pass

    material = abstractproperty()


class Terminator(IdealRobotModel):
    
    def __init__(self, name, lines):
        IdealRobotModel.__init__(self, name, lines)

    def talk(self):
        print(self._lines)

    material = property(lambda s: s._material, lambda s, v: setattr(s, "_material", v))


if __name__ == "__main__":

    try:
        robot = IdealRobotModel()
    except TypeError as ex:
        print(ex)
    
    t1 = Terminator("Arnold Schwarzenegger", "I'll be back")
    t1.material = 'steel'

    t1.talk()
    print("t1 is made of %s" % t1.material)
