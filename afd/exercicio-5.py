# Esse AFD aceita strings binárias onde tanto o número de 1s quanto o número de 0s é par.

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
    
def AFD_parity_zeros_ones():
    states = {'q00', 'q01', 'q10', 'q11'}
    alphabet = {'0', '1'}
    transitions = {
        'q00': {'0': 'q10', '1': 'q01'},
        'q01': {'0': 'q11', '1': 'q00'},
        'q10': {'0': 'q00', '1': 'q11'},
        'q11': {'0': 'q01', '1': 'q10'}
    }
    initial_state = 'q00'
    accept_states = {'q00'}

    return AFD(states, alphabet, transitions, initial_state, accept_states)

afd = AFD_parity_zeros_ones()
chain = "01001101"
print("Aceita?" if afd.process(chain) else "Rejeita")

# Estrutura Lógica
#
# Estados:
#
# q00: Número par de 0s e 1s.
# q01: Par de 0s e ímpar de 1s.
# q10: Ímpar de 0s e par de 1s.
# q11: Ímpar de 0s e ímpar de 1s.
#
# Transições:
#
# Cada estado alterna com base no símbolo lido.
# Alfabeto: {0, 1}.