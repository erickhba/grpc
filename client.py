import grpc
import time
import string
import random

from protos import grpc_service_pb2, grpc_service_pb2_grpc


def run():
    N = 10
    #192.168.0.5
    with grpc.insecure_channel('localhost:50051') as channel:
        
        stub = grpc_service_pb2_grpc.Grpc_ServiceStub(channel)        
        total = []

        # Get Void
        for i in range(N): 
            start_time = time.time()
            response = stub.GetVoid(grpc_service_pb2.Void())
            total.append(time.time() - start_time)
            print("--- %s seconds ---" % total[i])

        print(f"\nGetVoid - Execucoes: {N}; Média: {sum(total)/N}\n")
        total.clear()
        
        #Get Long 
        for i in range(N): 
            start_time = time.time()
            response = stub.GetLong(grpc_service_pb2.Long(n = 1231))
            total.append(time.time() - start_time)
            print("--- %s seconds ---" % total[i])

        print(f"\nGetLong - Execucoes: {N}; Média: {sum(total)/N}\n")
        total.clear()

        #Get long batch
        for i in range(N): 
            start_time = time.time()
            response = stub.GetLongBatch(grpc_service_pb2.LongBatch(n1 =1231231, n2= 123312444, n3= 1124656, n4=894587649, n5=90283881232, n6=1231239494949, n7=218380010000, n8=99328 ))
            total.append(time.time() - start_time)
            print("--- %s seconds ---" % total[i])

        print(f"\nGetLongBatch - Execucoes: {N}; Média: {sum(total)/N}\n")
        total.clear()



        #Get String

        # generating random strings
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4104304))
        
        for i in range(N): 
            start_time = time.time()
            response = stub.GetString(grpc_service_pb2.String(n = res))
            total.append(time.time() - start_time)
            print("--- %s seconds ---" % total[i])

        print(f"\nGetString - Execucoes: {N}; Média: {sum(total)/N}\n")
        total.clear()


        #Get long batch
        for i in range(N): 
            start_time = time.time()
            response = stub.GetJson(grpc_service_pb2.Json())
            total.append(time.time() - start_time)
            print("--- %s seconds ---" % total[i])

        print(f"\nGetJson - Execucoes: {N}; Média: {sum(total)/N}\n")
        total.clear()



if __name__ == '__main__':
    run()