# Projeto: Análise do Desempenho da TLB em Sistemas com Localidade de Memória

## Descrição

Este projeto tem como objetivo estudar o impacto do tamanho da Translation Lookaside Buffer (TLB) no desempenho de sistemas de paginação. Por meio da simulação de acessos à memória, com padrões que reproduzem localidade temporal e espacial, foi possível observar o comportamento da taxa de hits (*hit ratio*) para diferentes configurações de TLB.

Através deste experimento, demonstramos que, após um determinado ponto, aumentar o tamanho da TLB deixa de trazer ganhos significativos de desempenho.

## Estrutura do Projeto

- `trace_generator.py`: Responsável pela geração do traço de acessos à memória com localidade configurável.
- `tlb.py`: Implementação da TLB utilizando a política de substituição LRU (Least Recently Used).
- `tlb_simulator.py`: Executa a simulação, variando o tamanho da TLB, e gera os resultados colocando-os na entrada padrão.
- `plot_results.py`: Pega o resultado da entrada padrão gerado pelo `tlb_simulator` e plota o gráfico.

## Como Executar

1. Clone este repositório:
   ```bash
   git clone git@github.com:RonalddMatias/SO-project.git
   cd SO-project

2. Instale as dependências necessárias (se ainda não tiver o matplotlib):
   ```bash
   pip3 install matplotlib

3. Execute o arquivos principais:
   ```bash
   python3 tlb_simulator.py | python3 plot_results.py

4. O programa irá:

- Gerar um traço de acessos à memória.
- Simular diferentes tamanhos de TLB.
- Exibir um gráfico "Taxa de Hit vs. Tamanho da TLB".

## Personalização:

Se desejar gerar diferentes traços ou testar diferentes configurações, é possível alterar os parâmetros no arquivo `tlb_simulator.py`, como:

- Número de acessos (*NUM_ACESSOS*)
- Número máximo de páginas (*MAX_PAGINAS*)
- Probabilidade de localidade (*p_localidade*)
- Lista de tamanhos de TLB (*tlb_sizes*)

Importante ressaltar que ja deixei setado os parâmetros para o plot apresentado no relatório.

## Autor

- Ronaldd Feliph Matias Costa
