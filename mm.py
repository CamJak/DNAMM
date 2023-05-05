import random
class MooreMachine:
    def __init__(self) -> None:
        self.states = []

    class state:
        def __init__(self, name, output, transitions = {}) -> None:
            self.name = name
            self.output = output
            self.transitions = transitions

    def generate(self):
        output = ["A", "T", "C", "G"]
        inputs = ["G", "A", "C", "T"]

        regenerate = True
        while regenerate:
            input_G = [0, 1, 2, 3]
            input_A = [0, 1, 2, 3]
            input_C = [0, 1, 2, 3]
            input_T = [0, 1, 2, 3]
            self.states = []
            for i in range(4):
                self.states.append(self.state(i, output[i], {}))
                usedNums = [0, 1, 2, 3]
                for j in range(4):
                    randNum = random.randint(0, 3)
                    if j == 0:
                        regenerate = False
                        while randNum not in input_G or randNum not in usedNums:
                            for num in input_G:
                                if num not in usedNums:
                                    regenerate = True
                                else:
                                    regenerate = False
                                    break
                            if regenerate:
                                break
                            randNum = random.randint(0, 3)
                            regenerate = False
                        if randNum in usedNums and randNum in input_G:
                            input_G.remove(randNum)
                            usedNums.remove(randNum)
                    elif j == 1:
                        regenerate = False
                        while randNum not in input_A or randNum not in usedNums:
                            for num in input_A:
                                if num not in usedNums:
                                    regenerate = True
                                else:
                                    regenerate = False
                                    break
                            if regenerate:
                                break
                            randNum = random.randint(0, 3)
                            regenerate = False
                        
                        if randNum in usedNums and randNum in input_A:
                            input_A.remove(randNum)
                            usedNums.remove(randNum)
                    elif j == 2:
                        regenerate = False
                        while randNum not in input_C or randNum not in usedNums:
                            for num in input_C:
                                if num not in usedNums:
                                    regenerate = True
                                else:
                                    regenerate = False
                                    break
                            if regenerate:
                                break
                            randNum = random.randint(0, 3)
                            regenerate = False
                        if randNum in usedNums and randNum in input_C:
                            input_C.remove(randNum)
                            usedNums.remove(randNum)
                    elif j == 3:
                        regenerate = False
                        while randNum not in input_T or randNum not in usedNums:
                            for num in input_T:
                                if num not in usedNums:
                                    regenerate = True
                                else:
                                    regenerate = False
                                    break
                            if regenerate:
                                break
                            randNum = random.randint(0, 3)
                            regenerate = False
                        if randNum in usedNums and randNum in input_T:
                            input_T.remove(randNum)
                            usedNums.remove(randNum)
                        if regenerate:
                            break
                    if regenerate:
                        break
                    if not regenerate:
                        self.states[i].transitions.update({inputs[j]: randNum})
                
        
def main():
    mm = MooreMachine()
    mm.generate()
    for state in mm.states:
        print(f"State: {state.name}, Output: {state.output}, Transitions: {state.transitions}")

main()
