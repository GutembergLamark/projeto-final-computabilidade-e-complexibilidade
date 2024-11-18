# Esse AFD aceita strings binárias que contêm um número ímpar de 1s.

class AFD:
    def __init__(self, states, alphabet, transitions, initial_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.current_state = initial_state
        self.accept_states = accept_states

    def process(self, chain):
        for symbol in chain:
            if symbol in self.transitions[self.current_state]:
                self.current_state = self.transitions[self.current_state][symbol]
            else:
                return False  
        return self.current_state in self.accept_states
    
def AFD_odd_of_1s():
    states = {'q0', 'q1'}
    alphabet = {'0', '1'}
    transitions = {
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q1', '1': 'q0'}
    }
    initial_state = 'q0'
    accept_states = {'q1'}

    return AFD(states, alphabet, transitions, initial_state, accept_states)


afd = AFD_odd_of_1s()
chain = "10101110" 
print("Aceita?" if afd.process(chain) else "Rejeita")

# Estrutura Lógica
# Estados:
#
# q0: Estado de aceitação (número par de 1s).
# q1: Estado com um número ímpar de 1s.
#
# Transições:
#
# q0 --1--> q1
# q1 --1--> q0
#
# A leitura de 0 não altera o estado.
# Alfabeto: {0, 1}.