from concurrent import futures
import logging
from custom_class import FakeDataAPI
import grpc
from grpc.protos import grpc_service_pb2, grpc_service_pb2_grpc
import json


class Grpc_ServiceServicer(grpc_service_pb2_grpc.Grpc_ServiceServicer):
    def GetVoid(self, request, context):
        return grpc_service_pb2.Void()        

    def GetLong(self, request, context):
        resp = request.n * 2
        return grpc_service_pb2.Long(n = resp) 
    
    def GetLongBatch(self, request, context):
        resp = request.n1 + request.n2 + request.n3 -request.n4 -request.n5 +request.n6 -request.n7 +request.n8
        return grpc_service_pb2.Long(n = resp) 
    
    def GetString(self, request, context):
        resp = request.n
        return grpc_service_pb2.String(n = resp)
    
    def GetJson(self, request, context):
        resp = request.n
        return grpc_service_pb2.Json(s = resp)
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_service_pb2_grpc.add_Grpc_ServiceServicer_to_server(
        Grpc_ServiceServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()