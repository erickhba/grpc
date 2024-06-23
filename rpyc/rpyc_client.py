import time
import rpyc
import numpy as np
from tipo_complexo import TipoComplexo
from plotar_grafico import plotar_grafico_barras_desvios, plotar_grafico_barras_medias, plotar_grafico_linhas_com_desvio

class ClientRPyC:
    def __init__(self, host="localhost", port=18861):
        self.host = host
        self.port = port
        self.conn = None
        self.root = None
        self.titulos = []
        self.medias = []
        self.desvios = []
    
    def conectar(self):
        """ Conecta ao servidor RPyC """
        self.conn = rpyc.connect(self.host, self.port)
        self.root = self.conn.root
    
    def desconectar(self):
        """ Fecha a conexao com o servidor RPyC """
        if self.conn:
            self.conn.close()
    
    def medir_tempo_execucao(self, funcao, *args, num_execucoes=10):
        """
        Mede o tempo de execucao de uma funcao e calcula a media
        e o desvio padrao dos tempos de execucao.

        Parametros:
        - funcao: funcao a ser executada.
        - *args: argumentos da funcao.
        - num_execucoes: numero de vezes que a funcao sera executada para medir o tempo (padrao: 10).
        """
        tempos = []
        
        # Realiza num_execucoes vezes a execucao da funcao para medir o tempo de cada execucao
        for i in range(num_execucoes):
            start_time = time.perf_counter()
            funcao(*args)
            tempo_execucao = time.perf_counter() - start_time
            tempos.append(tempo_execucao)
            print(f"--- {tempo_execucao} segundos ---")
            
        # Calcula a media e o desvio padrao dos tempos de execucao
        media = np.mean(tempos)
        desvio_padrao = np.std(tempos) 
        print(f"\nExecucoes: {num_execucoes}; Media: {media} segundos; Desvio padrao: {desvio_padrao} segundos\n")
        
        return tempos, media, desvio_padrao
    
    def registrar_resultados(self, titulo, media, desvio):
        """
        Registra os resultados (titulo, media e desvio padrao) nos atributos da classe.

        Parametros:
        - titulo: titulo a ser adicionado a lista de titulos.
        - media: media a ser adicionada a lista de medias.
        - desvio: desvio padrao a ser adicionado a lista de desvios.
        """
        self.titulos.append(titulo)
        self.medias.append(media)
        self.desvios.append(desvio)
    
    def executar_testes(self, num_execucoes=10):
        try:
            self.conectar()

            # Teste 1: operacao void
            print("Teste 1: operacao void")
            tempos_void, media_void, desvio_void = self.medir_tempo_execucao(self.root.exposed_void_operation, num_execucoes=num_execucoes)
            self.registrar_resultados("Teste 1: void", media_void, desvio_void)

            # Teste 2: operacao long
            print("Teste 2: operacao long")
            tempos_long, media_long, desvio_long = self.medir_tempo_execucao(self.root.exposed_long_operation, 12345678901234567890, num_execucoes=num_execucoes)
            self.registrar_resultados("Teste 2: long", media_long, desvio_long)

            # Teste 3: oito operacoes long
            print("Teste 3: oito operacoes long")
            tempos_batch, media_batch, desvio_batch = self.medir_tempo_execucao(self.root.exposed_long_batch_operation, 
                                                          12345678901234567890, 
                                                          23456789012345678902, 
                                                          34567890123456789012, 
                                                          45678901234567890123,
                                                          56789012345678901234, 
                                                          67890123456789012345, 
                                                          78901234567890123456, 
                                                          89012345678901234567, 
                                                          num_execucoes=num_execucoes)
            self.registrar_resultados("Teste 3: batch long", media_batch, desvio_batch)

            # Teste 4: operacao de string com tamanhos variados
            print("Teste 4: operacao de string com tamanhos variados")
            for tamanho in [2**i for i in range(11)]:
                string_arg = ("X" * tamanho)
                print(f"Tamanho da string: {tamanho}")
                tempos_string, media_string, desvio_string = self.medir_tempo_execucao(self.root.exposed_string_operation, string_arg, num_execucoes=num_execucoes)
                self.registrar_resultados(f"Teste 4: string {tamanho}", media_string, desvio_string)

            # Teste 5: operacao com tipo complexo
            print("Teste 5: operacao com tipo complexo")
            complex_obj = TipoComplexo()
            tempos_complex, media_complex, desvio_complex = self.medir_tempo_execucao(self.root.exposed_complex_operation, complex_obj, num_execucoes=num_execucoes)
            self.registrar_resultados("Teste 5: complexo", media_complex, desvio_complex)
            
            # Teste 6: operacao com JSON
            print("Teste 6: operacao com JSON")
            json_data = {
                "int": 123,
                "string": "123",
                "list": [1, 2, 3],
                "objeto": {
                    "chave_1": 1,
                    "chave_2": 2,
                    "chave_3": 3
                }
            }
            tempos_json, media_json, desvio_json = self.medir_tempo_execucao(self.root.exposed_json_operation, json_data, num_execucoes=num_execucoes)
            self.registrar_resultados("Teste 6: JSON", media_json, desvio_json)

            # Plotar grafico de linhas com desvio padrao
            plotar_grafico_linhas_com_desvio(self.titulos, self.medias, self.desvios)
            plotar_grafico_barras_medias(self.titulos, self.medias)
            plotar_grafico_barras_desvios(self.titulos, self.desvios)

        finally:
            self.desconectar()

if __name__ == "__main__":
    client = ClientRPyC()
    client.executar_testes()
