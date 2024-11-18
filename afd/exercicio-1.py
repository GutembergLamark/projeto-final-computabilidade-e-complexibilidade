#Enunciado:
# Um AFD comum é reconhecer strings em uma linguagem binária (usando apenas 0 e 1). 
# Vamos definir um exemplo onde o autômato aceita apenas strings com um número par de 0s.

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

def AFD_pair_of_zeros():
    states = {'q0', 'q1'}
    alphabet = {'0', '1'}
    transitions = {
        'q0': {'0': 'q1', '1': 'q0'},
        'q1': {'0': 'q0', '1': 'q1'}
    }
    initial_state = 'q0'
    accept_states = {'q0'}

    afd = AFD(states, alphabet, transitions, initial_state, accept_states)
    return afd


afd = AFD_pair_of_zeros()
chain = "100110000111"  
print("Aceita?" if afd.process(chain) else "Rejeita")

# Estrutura Lógica do AFD
#
# Para a linguagem descrita (número par de 0s), o autômato possui:
# 
# Estados:
# q0: Estado inicial e de aceitação (par de 0s).
# q1: Estado que representa um número ímpar de 0s.
# Transições:
# De q0 para q1 ao ler 0 e de q1 para q0 ao ler outro 0.
# Em ambos os estados, a leitura de 1 mantém o estado atual (não afeta o número de 0s).
# Alfabeto: {0, 1}.