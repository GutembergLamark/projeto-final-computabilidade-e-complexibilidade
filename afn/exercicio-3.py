# Esse AFN aceita strings que contêm o padrão "10" ou "01" em qualquer posição.

class AFN:
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_aceitacao):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_aceitacao = estados_aceitacao

    def processar(self, cadeia):
        return self._processar_recursivo(cadeia, {self.estado_inicial})

    def _processar_recursivo(self, cadeia, estados_atuais):
        if not cadeia:  
            return any(estado in self.estados_aceitacao for estado in estados_atuais)

        simbolo = cadeia[0]
        proximos_estados = set()
        for estado in estados_atuais:
            if estado in self.transicoes and simbolo in self.transicoes[estado]:
                proximos_estados.update(self.transicoes[estado][simbolo])
        
        return self._processar_recursivo(cadeia[1:], proximos_estados)
    
def AFN_comeca_e_termina_mesmo_simbolo():
    estados = {'q0', 'q1', 'q2', 'q3', 'q4'}
    alfabeto = {'0', '1'}
    transicoes = {
        'q0': {'0': {'q1'}, '1': {'q3'}},   
        'q1': {'0': {'q1'}, '1': {'q2'}},   
        'q2': {'0': {'q1'}, '1': {'q2'}},   
        'q3': {'1': {'q3'}, '0': {'q4'}},   
        'q4': {'1': {'q3'}, '0': {'q4'}}    
    }
    estado_inicial = 'q0'
    estados_aceitacao = {'q1', 'q3'}        

    return AFN(estados, alfabeto, transicoes, estado_inicial, estados_aceitacao)

afn = AFN_comeca_e_termina_mesmo_simbolo()
cadeias = ["0010", "1101", "000", "111", "01", "1010111101"]
for cadeia in cadeias:
    print(f"Cadeia: {cadeia} -> {'Aceita' if afn.processar(cadeia) else 'Rejeita'}")