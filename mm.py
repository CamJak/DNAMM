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
                
    def getOutput(self, input):
        
        # Start with an empty output and the first state
        output = ""
        currentState = self.states[0]

        # For each DNA in the input, get the next state and add the output
        for DNA in input:

            # Check if the input is valid
            if DNA not in ["A", "T", "C", "G"]:
                return "Invalid input"
            
            # Otherwise, get the next state and add the output
            else:
                currentState = self.states[currentState.transitions[DNA]]
                output += currentState.output

        return output
    
    def getReverseOutput(self, input):

        # Start with an empty output and the first state
        output = ""
        previousState = self.states[0]

        # For each DNA in the input, get the next state and add the output
        for DNA in input:
            # Check if the input is valid
            if DNA not in ["A", "T", "C", "G"]:
                return "Invalid input"
            
            # Otherwise, get the next state and add the output
            currentOutput = DNA
            if DNA == "A":
                currentState = self.states[0]
            elif DNA == "T":
                currentState = self.states[1]
            elif DNA == "C":
                currentState = self.states[2]
            elif DNA == "G":
                currentState = self.states[3]

            for key, value in previousState.transitions.items():
                if value == currentState.name:
                    output += key
                    break
            
            previousState = currentState
                    
        return output
    
    def getCols(self):
        col1 = ""
        col2 = ""
        col3 = ""
        col4 = ""
        for state in self.states:
            col1 += str(state.transitions["G"])
            col2 += str(state.transitions["A"])
            col3 += str(state.transitions["C"])
            col4 += str(state.transitions["T"])

        return [col1, col2, col3, col4]
    
    def encodeCols(self, cols):
        encodedCols = ""
        for i in range(len(cols)):
            for integer in cols[i]:
                encodedCols += format(int(integer), '02b')

        return encodedCols

def main():
    
    mm = MooreMachine()
    mm.generate()

    # Showing the states generated by the machine
    for state in mm.states:
        print(f"State: {state.name}, Output: {state.output}, Transitions: {state.transitions}")

    print()

    # Testing the getOutput function]
    input = "GACGACTGTCAGTAGCAGT"
    output = mm.getOutput(input)
    print(f"Input: {input}, Output: {output}")

    cols = mm.getCols()
    print(f"Cols: {cols}")
    print()
    encodedCols = mm.encodeCols(cols)
    print(encodedCols)

    output1 = mm.getReverseOutput(output)
    print(f"Input: {input}, Output: {output1}")
    print(input == output1)

if __name__ == "__main__":
    main()



