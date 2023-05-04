import random

class MooreMachine:
    def __init__(self) -> None:
        self.__states = []

    class state:
        def __init__(self, name, transitions) -> None:
            self.__name = name
            self.__transitions = transitions

    def generate(self):
        randNum = random.randint(0, 3)
        
