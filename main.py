import matplotlib.pyplot as plt 
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
    tlb_sizes = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 1500, 1800, 2048, 2567 , 4096]
    
    resultados = []
    for size in tlb_sizes:
        taxa_hit = simular_tlb(acessos, size)
        resultados.append(taxa_hit)
        print(f"TLB Size = {size} | Taxa de Hit = {taxa_hit:.4f}")

    # Plot do resultado usando posições x personalizadas
    plt.figure(figsize=(10, 6))
    
    # Criar posições personalizadas com espaçamento muito maior entre 2048 e 4096
    posicoes_x = list(range(len(tlb_sizes) - 1))  # Posições normais para os primeiros pontos
    posicoes_x.append(posicoes_x[-1] + 2)  # Adiciona espaçamento quádruplo para o último ponto (4096)
    
    plt.plot(posicoes_x, resultados, marker='o', linewidth=2)
    
    # Definindo os ticks do eixo x como as posições personalizadas, mas mostrando os valores reais
    plt.xticks(posicoes_x, tlb_sizes)
    
    # Formatação do gráfico
    plt.title("Taxa de Hit vs. Tamanho da TLB", fontsize=14)
    plt.xlabel("Tamanho da TLB", fontsize=12)
    plt.ylabel("Taxa de Hit", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()