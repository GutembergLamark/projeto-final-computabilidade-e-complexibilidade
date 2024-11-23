# Descriptografa strings

class TuringMachine:
    def __init__(self, tape_input, transitions, initial_state, accept_state, reject_state):
        self.tape = list(tape_input)  
        self.head_position = 0  
        self.current_state = initial_state  
        self.transitions = transitions  
        self.accept_state = accept_state  
        self.reject_state = reject_state  
    
    def execute_step(self):
        """Executa um único passo da Máquina de Turing."""
        current_symbol = self.tape[self.head_position]
        
        transition_key = (self.current_state, current_symbol)
        if transition_key in self.transitions:
            next_state, write_symbol, move_direction = self.transitions[transition_key]
            
            self.tape[self.head_position] = write_symbol
            
            if move_direction == "R":
                self.head_position += 1
            elif move_direction == "L":
                self.head_position -= 1
            
            self.current_state = next_state
        else:
            
            self.current_state = self.reject_state
    
    def run(self):
        """Executa a Máquina de Turing até alcançar aceitação ou rejeição."""
        while self.current_state not in {self.accept_state, self.reject_state}:
            self.execute_step()
            
        return "".join(self.tape), self.current_state
    
def create_cesar_cipher_transitions(shift):
    """Cria transições para descriptografar uma cifra de César com um deslocamento fixo."""
    transitions = {}
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    
    for i, letter in enumerate(alphabet):
        decrypted_index = (i - shift) % len(alphabet)
        decrypted_letter = alphabet[decrypted_index]
        transitions[("q0", letter)] = ("q0", decrypted_letter, "R")  

    
    transitions[("q0", " ")] = ("q0", " ", "R")

    
    transitions[("q0", "_")] = ("q_accept", "_", "R")  

    return transitions



encrypted_text = "KHOOR ZRUOG"  
tape_with_padding = encrypted_text + "_"  
shift = 3  

transitions = create_cesar_cipher_transitions(shift)
initial_state = "q0"
accept_state = "q_accept"
reject_state = "q_reject"

# Executa a Máquina de Turing
turing_machine = TuringMachine(
    tape_input=tape_with_padding,
    transitions=transitions,
    initial_state=initial_state,
    accept_state=accept_state,
    reject_state=reject_state,
)
final_tape, final_state = turing_machine.run()

if final_state == accept_state:
    decrypted_text = final_tape.strip()
    print(f"Texto descriptografado: {decrypted_text}")
    print(f"Estado final: {final_state}")
else:
    print("Erro na descriptografia.")
    print(f"Estado final: {final_state}")