# trace_generator.py
import random

def gerar_trace(num_acessos=10000, max_paginas=1000, p_localidade=0.95):
    """
    Gera um traço de acessos com localidade:
        num_acessos -> número de acessos no traço
        max_paginas -> número de páginas no sistema
        p_localidade -> probabilidade de acessar uma página próxima da última acessada
    """
    trace = []
    # Escolhe a primeira página aleatoriamente
    pagina_atual = random.randint(0, max_paginas - 1)
    trace.append(pagina_atual)
    
    for _ in range(num_acessos - 1):
        if random.random() < p_localidade:
            # Acesso próximo (localidade espacial)
            deslocamento = random.randint(-2, 2)  # Pode ajustar
            prox_pagina = pagina_atual + deslocamento
            # Garante que fique dentro do range
            prox_pagina = max(0, min(prox_pagina, max_paginas - 1))
            pagina_atual = prox_pagina
        else:
            # Acesso completamente aleatório
            pagina_atual = random.randint(0, max_paginas - 1)
        trace.append(pagina_atual)

    return trace
