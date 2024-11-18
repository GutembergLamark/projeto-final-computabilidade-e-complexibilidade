# Esse AFD aceita strings binárias que terminam em "01". 
# Para isso, o autômato precisa verificar se os dois últimos símbolos da cadeia formam "01".

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
    
def AFD_ends_in_01():
    states = {'q0', 'q1', 'q2'}
    alphabet = {'0', '1'}
    transicoes = {
        'q0': {'0': 'q1', '1': 'q0'},
        'q1': {'0': 'q1', '1': 'q2'},
        'q2': {'0': 'q1', '1': 'q0'}
    }
    initial_state = 'q0'
    accept_states = {'q2'}

    return AFD(states, alphabet, transicoes, initial_state, accept_states)


afd = AFD_ends_in_01()
chain = "11011001" 
print("Aceita?" if afd.process(chain) else "Rejeita")

# Estrutura Lógica
#
# Estados:
#
# q0: Estado inicial.
# q1: Estado onde o último símbolo lido foi 0.
# q2: Estado de aceitação (últimos dois símbolos foram "01").
#
# Transições:
#
# q0 --0--> q1
# q1 --1--> q2
#
# Todos os outros caminhos retornam a q0 ou mantêm o estado.
# Alfabeto: {0, 1}.