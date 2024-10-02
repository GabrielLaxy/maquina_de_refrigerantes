# alfabeto finito de entradas
I = ['b','m25', 'm50', 'm100']

#estado inicial
S0 = 0

#tabela de estados
T = [
    [('s0', 'n'), ('s1', 'n'), ('s2', 'n'), ('s4', 'n')],    # s0
    [('s1', 'n'), ('s1', 'n'), ('s2', 'n'), ('s4', 'n')],    # s1
    [('s2', 'n'), ('s1', 'n'), ('s2', 'n'), ('s4', 'n')],    # s2
    [('s3', 'n'), ('s5', 'n'), ('s6', 'n'), ('s8', 'n')],    # s3
    [('s4', 'n'), ('s5', 'n'), ('s6', 'n'), ('s8', 'n')],    # s4
    [('s5', 'n'), ('s5', 'n'), ('s6', 'n'), ('s8', 't25')],  # s5
    [('s6', 'n'), ('s7', 'n'), ('s7', 't50'), ('s8', 't50')],# s6
    [('s7', 'n'), ('s7', 'n'), ('s7', 't50'), ('s8', 't100')],# s7
    [('s8', 'r'), ('s8', 't25'), ('s8', 't50'), ('s8', 't100')] # s8
]

def processa_entrada(*alfabeto):
    mapa_entradas = {
        'b': 0,
        'm25': 1,
        'm50': 2,
        'm100': 3,
    }
    
    # processar cada entrada
    for entrada in alfabeto:
        if entrada not in mapa_entradas:
            raise ValueError(f"Entrada inválida: {entrada}")
