# Esse AFD aceita strings binárias que contêm pelo menos dois 0s em qualquer posição.

class AFD:
    def __init__(self, states, alphabet, transitions, initial_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.current_state = initial_state
        self.accept_states = accept_states

    def process(self, chain):
        for symbol in chain:
            if(symbol not in self.alphabet): return False
            if symbol in self.transitions[self.current_state]:
                self.current_state = self.transitions[self.current_state][symbol]
            else:
                return False  
        return self.current_state in self.accept_states
    
def AFD_two_zeros():
    states = {'q0', 'q1', 'q2'}
    alphabet = {'0', '1'}
    transitions = {
        'q0': {'0': 'q1', '1': 'q0'},
        'q1': {'0': 'q2', '1': 'q1'},
        'q2': {'0': 'q2', '1': 'q2'}
    }
    initial_state = 'q0'
    accept_states = {'q2'}

    return AFD(states, alphabet, transitions, initial_state, accept_states)

afd = AFD_two_zeros()
chain = "101101" 
print("Aceita?" if afd.process(chain) else "Rejeita")

# Estrutura Lógica
#
# Estados:
#
# q0: Estado inicial (zero 0s vistos).
# q1: Um 0 visto.
# q2: Estado de aceitação (dois ou mais 0s vistos).
#
# Transições:
#
# q0 --0--> q1
# q1 --0--> q2
#
# Em q2, qualquer entrada mantém o estado.
# Alfabeto: {0, 1}.