import sys
from trace_generator import gerar_trace
from tlb import simular_tlb

def main():
    NUM_ACESSOS = 20000
    MAX_PAGINAS = 2000
    P_LOCALIDADE = 0.95
    
    acessos = gerar_trace(num_acessos=NUM_ACESSOS, 
                          max_paginas=MAX_PAGINAS, 
                          p_localidade=P_LOCALIDADE)
    
    tlb_sizes = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 1500, 1800, 2048, 2567, 4096]

    # Executa simulações e imprime resultados na saida padrão
    for size in tlb_sizes:
        taxa_hit = simular_tlb(acessos, size)
        print(f"{size},{taxa_hit:.6f}")

if __name__ == "__main__":
    main()