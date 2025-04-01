# tlb.py

from collections import OrderedDict

class TLB:
    """
    Implementa uma TLB simples com política LRU (Least Recently Used).
    Usa OrderedDict para controlar a ordem de uso.
    """
    def __init__(self, size):
        self.size = size
        self.cache = OrderedDict()

    def consulta(self, pagina_virtual):
        """
        Verifica se a página virtual está na TLB.
         - Se sim, move a entrada para o final (mais recente) e retorna True (hit).
         - Se não, retorna False (miss).
        """
        if pagina_virtual in self.cache:
            # HIT: move para o final (LRU)
            self.cache.move_to_end(pagina_virtual)
            return True
        return False

    def adicionar_entrada(self, pagina_virtual, pagina_fisica):
        """
        Adiciona ou atualiza a entrada na TLB.
        - Se a TLB está cheia, remove a entrada menos recentemente usada.
        - Em seguida, insere a nova entrada e a marca como mais recente.
        """
        if pagina_virtual in self.cache:
            # Atualiza e move para o final
            self.cache.move_to_end(pagina_virtual)
        else:
            # Caso não exista, verificar se está cheia
            if len(self.cache) >= self.size:
                self.cache.popitem(last=False)  # Remove LRU
            self.cache[pagina_virtual] = pagina_fisica


def simular_tlb(trace, tlb_size):
    """
    Simula a execução de um traço de acessos para um TLB de tamanho 'tlb_size'.
    Retorna a taxa de hits (proporção de acessos que deram hit na TLB).

    Nesta versão simplificada, a 'tabela de páginas' é apenas:
       pagina_virtual -> pagina_fisica = pagina_virtual (mapeamento 1-para-1).
    """
    tlb = TLB(tlb_size)
    hits = 0
    total_acessos = len(trace)

    for pagina_virtual in trace:
        # Verifica se já está na TLB
        if tlb.consulta(pagina_virtual):
            # Hit
            hits += 1
        else:
            # Miss - busca na 'tabela de páginas' (simulação trivial)
            pagina_fisica = pagina_virtual
            tlb.adicionar_entrada(pagina_virtual, pagina_fisica)

    return hits / total_acessos
