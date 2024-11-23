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