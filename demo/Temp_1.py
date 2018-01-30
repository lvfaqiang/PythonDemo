class She:

    def __init__(self, value=26.0):
        self.value = value

    def __set__(self, instance, value):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value


class Hua:
    def __get__(self, instance, owner):
        return instance.s * 1.8 + 32

    def __set__(self, instance, value):
        instance.s = (float(value) - 32) / 1.8


class Temp:
    s = She()
    h = Hua()
