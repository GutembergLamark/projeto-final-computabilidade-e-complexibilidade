# Esse AFN aceita strings que começam com "0" ou terminam com "1".

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
    
def AFN_comeca_0_termina_1():
    estados = {'q0', 'q1', 'q2'}
    alfabeto = {'0', '1'}
    transicoes = {
        'q0': {'0': {'q1'}, '1': {'q2'}},
        'q1': {'0': {'q1'}, '1': {'q2'}},
        'q2': {'0': {'q0'}, '1': {'q2'}} 
    }
    estado_inicial = 'q0'
    estados_aceitacao = {'q1', 'q2'}

    return AFN(estados, alfabeto, transicoes, estado_inicial, estados_aceitacao)

afn = AFN_comeca_0_termina_1()
cadeia = "001001" 
print("Aceita?" if afn.processar(cadeia) else "Rejeita")