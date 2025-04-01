import matplotlib as plt
from trace_generator import gerar_trace
from tlb import simular_tlb

def main():
    # Parâmetros de teste
    NUM_ACESSOS = 20000
    MAX_PAGINAS = 2000
    P_LOCALIDADE = 0.95
    
    # Gera um traço com certa localidade
    acessos = gerar_trace(num_acessos=NUM_ACESSOS, 
                          max_paginas=MAX_PAGINAS, 
                          p_localidade=P_LOCALIDADE)
    
    # Lista de tamanhos de TLB para testar
    tlb_sizes = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
    
    resultados = []
    for size in tlb_sizes:
        taxa_hit = simular_tlb(acessos, size)
        resultados.append(taxa_hit)
        print(f"TLB Size = {size} | Taxa de Hit = {taxa_hit:.4f}")

    # Plot do resultado
    plt.figure()
    plt.plot(tlb_sizes, resultados, marker='o')
    plt.title("Taxa de Hit vs. Tamanho da TLB")
    plt.xlabel("Tamanho da TLB")
    plt.ylabel("Taxa de Hit")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
