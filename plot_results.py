import sys
import matplotlib.pyplot as plt

def main():
    # Lê os dados da entrada padrão (stdin)
    lines = sys.stdin.readlines()

    # Processa os dados
    tlb_sizes = []
    resultados = []
    
    # Adiciona os dados lidos à lista
    for line in lines:
        size, hit_rate = line.strip().split(',')
        tlb_sizes.append(int(size))
        resultados.append(float(hit_rate))
    
    # Printando os resultados para melhor acompanhamento
    print("Resultados da simulação:")
    for i in range(len(tlb_sizes)):
        print(f"TLB Size = {tlb_sizes[i]} | Taxa de Hit = {resultados[i]:.4f}")
    
    plt.figure(figsize=(10, 6))
    
    posicoes_x = list(range(len(tlb_sizes) - 1))  
    posicoes_x.append(posicoes_x[-1] + 2)  
    
    plt.plot(posicoes_x, resultados, marker='o', linewidth=2)
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