import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 18})

def plotar_grafico_linhas_com_desvio(titulos, medias, desvios):
    """
    Plota um grafico de linhas com barras de erro representando as medias e desvios padrao.
    """
    plt.figure(figsize=(16, 8))
    plt.errorbar(range(1, len(titulos) + 1), medias, yerr=desvios, fmt='o', ecolor='red', capsize=5)
    plt.title('Tempo de Execução Médio com Desvio Padrão')
    plt.xlabel('Teste')
    plt.ylabel('Tempo Médio (segundos)')
    plt.xticks(range(1, len(titulos) + 1), titulos, rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('graficos/media-com-desvio-padrao.png')
    plt.show()

def plotar_grafico_barras_medias(titulos, medias):
    """
    Plota um grafico de barras representando as medias dos tempos de execucao.
    """
    plt.figure(figsize=(16, 8))
    plt.bar(range(len(titulos)), medias, color='skyblue', alpha=0.7)
    plt.title('Tempo de Execução Médio')
    plt.xlabel('Teste')
    plt.ylabel('Tempo Médio (segundos)')
    plt.xticks(range(len(titulos)), titulos, rotation=45)
    plt.grid(True, axis='y')
    plt.tight_layout()
    plt.savefig('graficos/media.png')
    plt.show()

def plotar_grafico_barras_desvios(titulos, desvios):
    """
    Plota um grafico de barras representando os desvios padrao dos tempos de execucao.
    """
    plt.figure(figsize=(16, 8))
    plt.bar(range(len(titulos)), desvios, color='lightcoral', alpha=0.7)
    plt.title('Desvio Padrão dos Tempos de Execução')
    plt.xlabel('Teste')
    plt.ylabel('Desvio Padrão (segundos)')
    plt.xticks(range(len(titulos)), titulos, rotation=45)
    plt.grid(True, axis='y')
    plt.tight_layout()
    plt.savefig('graficos/desvio-padrao.png')
    plt.show()