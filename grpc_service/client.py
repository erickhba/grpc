import grpc
import time
import string
import random
from custom_class import FakeDataAPI
from plotar_grafico import plotar_grafico_barras_desvios, plotar_grafico_barras_medias, plotar_grafico_linhas_com_desvio

import numpy as np
import sys
sys.path.insert(0, 'C:\\Users\\User\\Documents\\Faculdade\\sistemas_distribuidos\\grpc\\')

from grpc_service.protos import grpc_service_pb2, grpc_service_pb2_grpc


class ClientGRPC:
    def __init__(self, host="localhost", port=50051):
        self.host = host
        self.port = port
        self.conn = None
        self.root = None
        self.titulos = []
        self.medias = []
        self.desvios = []
   
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

    def run(self):
        N = 10
        verbose_log = False
        #192.168.0.5
        with grpc.insecure_channel('localhost:50051') as channel:
            
            stub = grpc_service_pb2_grpc.Grpc_ServiceStub(channel)        
            total = []

            # Get Void
            for i in range(11): 
                start_time = time.perf_counter()
                response = stub.GetVoid(grpc_service_pb2.Void())
                total.append(time.perf_counter() - start_time)
                print("--- %s seconds ---" % total[i]) if verbose_log == True else ()
            
            total.pop(0)
            # Calcula a media e o desvio padrao dos tempos de execucao
            media = np.mean(total)
            desvio_padrao = np.std(total) 
            print(f"\nGetVoid - Execucoes: {N}; Média: {media}; Std: {desvio_padrao}\n")
            self.registrar_resultados('GetVoid', media, desvio_padrao)
            total.clear()
            
            #Get Long 
            for i in range(N): 
                start_time = time.perf_counter()
                response = stub.GetLong(grpc_service_pb2.Long(n = 1231))
                total.append(time.perf_counter() - start_time)
                print("--- %s seconds ---" % total[i]) if verbose_log == True else ()

            # Calcula a media e o desvio padrao dos tempos de execucao
            media = np.mean(total)
            desvio_padrao = np.std(total) 
            print(f"\nGetLong - Execucoes: {N}; Média: {media}; Std: {desvio_padrao}\n")
            self.registrar_resultados('GetLong', media, desvio_padrao)

            total.clear()

            #Get long batch
            for i in range(N): 
                start_time = time.perf_counter()
                response = stub.GetLongBatch(grpc_service_pb2.LongBatch(n1 =1231231, n2= 123312444, n3= 1124656, n4=894587649, n5=90283881232, n6=1231239494949, n7=218380010000, n8=99328 ))
                total.append(time.perf_counter() - start_time)
                print("--- %s seconds ---" % total[i]) if verbose_log == True else ()


            # Calcula a media e o desvio padrao dos tempos de execucao
            media = np.mean(total)
            desvio_padrao = np.std(total) 
            print(f"\nGetLongBatch - Execucoes: {N}; Média: {media}; Std: {desvio_padrao}\n")
            self.registrar_resultados('GetLongBatch', media, desvio_padrao)
            total.clear()



            #Get String with multiple sizes
            for tamanho in [2**i for i in range(11)]:

                # generating random strings
                res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=tamanho))
                
                for i in range(N): 
                    start_time = time.perf_counter()
                    response = stub.GetString(grpc_service_pb2.String(n = res))
                    total.append(time.perf_counter() - start_time)
                    print("--- %s seconds ---" % total[i]) if verbose_log == True else ()

                # Calcula a media e o desvio padrao dos tempos de execucao
                media = np.mean(total)
                desvio_padrao = np.std(total) 
                print(f"\nGetString size: {tamanho} - Execucoes: {N}; Média: {media}; Std: {desvio_padrao}\n")
                self.registrar_resultados(f'GetString {tamanho}', media, desvio_padrao)
                total.clear()


            #Get long batch
            data = FakeDataAPI.get_comments()   
            for i in range(N): 
                start_time = time.perf_counter()
                response = stub.GetJson(grpc_service_pb2.Json(s = data))
                total.append(time.perf_counter() - start_time)
                print("--- %s seconds ---" % total[i]) if verbose_log == True else ()

            # Calcula a media e o desvio padrao dos tempos de execucao
            media = np.mean(total)
            desvio_padrao = np.std(total) 
            print(f"\nGetJson - Execucoes: {N}; Média: {media}; Std: {desvio_padrao}\n")
            self.registrar_resultados('GetJson', media, desvio_padrao)
            total.clear()

        plotar_grafico_barras_desvios(self.titulos, self.desvios)
        plotar_grafico_linhas_com_desvio(self.titulos, self.medias, self.desvios)
        plotar_grafico_barras_medias(self.titulos, self.medias)

if __name__ == "__main__":
    client = ClientGRPC()
    client.run()
