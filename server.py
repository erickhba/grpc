# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the gRPC route guide server."""

from concurrent import futures
import logging

import grpc
# import grpc_service_pb2_grpc
from protos import grpc_service_pb2_grpc, grpc_service_pb2


class Grpc_ServiceServicer(grpc_service_pb2_grpc.Grpc_ServiceServicer):
    """Provides methods that implement functionality of route guide server."""

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