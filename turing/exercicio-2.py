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
    
input_tape = "10101"
transitions = {
    ("q0", "1"): ("q1", " ", "R"),
    ("q0", "0"): ("q2", " ", "R"),
    ("q0", " "): ("q_accept", " ", "R"),

    ("q1", "1"): ("q1", "1", "R"),
    ("q1", "0"): ("q1", "0", "R"),
    ("q1", " "): ("q3", " ", "L"),

    ("q2", "1"): ("q2", "1", "R"),
    ("q2", "0"): ("q2", "0", "R"),
    ("q2", " "): ("q3", " ", "L"),

    ("q3", "1"): ("q0", " ", "R"),
    ("q3", "0"): ("q0", " ", "R"),
    ("q3", " "): ("q_accept", " ", "R"),
}

initial_state = "q0"
accept_state = "q_accept"
reject_state = "q_reject"

# Execução
tape_with_padding = input_tape + " " * 10
turing_machine = TuringMachine(
    tape_input=tape_with_padding,
    transitions=transitions,
    initial_state=initial_state,
    accept_state=accept_state,
    reject_state=reject_state
)
final_tape, final_state = turing_machine.run()
print("Resultado final na fita:", final_tape.strip())
print("Estado final:", final_state)