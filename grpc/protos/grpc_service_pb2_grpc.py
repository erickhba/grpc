# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from grpc.protos import grpc_service_pb2 as grpc_dot_protos_dot_grpc__service__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in grpc/protos/grpc_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class Grpc_ServiceStub(object):
    """Interface exported by the server.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetVoid = channel.unary_unary(
                '/grpc_service.Grpc_Service/GetVoid',
                request_serializer=grpc_dot_protos_dot_grpc__service__pb2.Void.SerializeToString,
                response_deserializer=grpc_dot_protos_dot_grpc__service__pb2.Void.FromString,
                _registered_method=True)
        self.GetLong = channel.unary_unary(
                '/grpc_service.Grpc_Service/GetLong',
                request_serializer=grpc_dot_protos_dot_grpc__service__pb2.Long.SerializeToString,
                response_deserializer=grpc_dot_protos_dot_grpc__service__pb2.Long.FromString,
                _registered_method=True)
        self.GetLongBatch = channel.unary_unary(
                '/grpc_service.Grpc_Service/GetLongBatch',
                request_serializer=grpc_dot_protos_dot_grpc__service__pb2.LongBatch.SerializeToString,
                response_deserializer=grpc_dot_protos_dot_grpc__service__pb2.Long.FromString,
                _registered_method=True)
        self.GetString = channel.unary_unary(
                '/grpc_service.Grpc_Service/GetString',
                request_serializer=grpc_dot_protos_dot_grpc__service__pb2.String.SerializeToString,
                response_deserializer=grpc_dot_protos_dot_grpc__service__pb2.String.FromString,
                _registered_method=True)
        self.GetJson = channel.unary_unary(
                '/grpc_service.Grpc_Service/GetJson',
                request_serializer=grpc_dot_protos_dot_grpc__service__pb2.Json.SerializeToString,
                response_deserializer=grpc_dot_protos_dot_grpc__service__pb2.String.FromString,
                _registered_method=True)


class Grpc_ServiceServicer(object):
    """Interface exported by the server.
    """

    def GetVoid(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLong(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLongBatch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetString(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetJson(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_Grpc_ServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetVoid': grpc.unary_unary_rpc_method_handler(
                    servicer.GetVoid,
                    request_deserializer=grpc_dot_protos_dot_grpc__service__pb2.Void.FromString,
                    response_serializer=grpc_dot_protos_dot_grpc__service__pb2.Void.SerializeToString,
            ),
            'GetLong': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLong,
                    request_deserializer=grpc_dot_protos_dot_grpc__service__pb2.Long.FromString,
                    response_serializer=grpc_dot_protos_dot_grpc__service__pb2.Long.SerializeToString,
            ),
            'GetLongBatch': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLongBatch,
                    request_deserializer=grpc_dot_protos_dot_grpc__service__pb2.LongBatch.FromString,
                    response_serializer=grpc_dot_protos_dot_grpc__service__pb2.Long.SerializeToString,
            ),
            'GetString': grpc.unary_unary_rpc_method_handler(
                    servicer.GetString,
                    request_deserializer=grpc_dot_protos_dot_grpc__service__pb2.String.FromString,
                    response_serializer=grpc_dot_protos_dot_grpc__service__pb2.String.SerializeToString,
            ),
            'GetJson': grpc.unary_unary_rpc_method_handler(
                    servicer.GetJson,
                    request_deserializer=grpc_dot_protos_dot_grpc__service__pb2.Json.FromString,
                    response_serializer=grpc_dot_protos_dot_grpc__service__pb2.String.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc_service.Grpc_Service', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('grpc_service.Grpc_Service', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Grpc_Service(object):
    """Interface exported by the server.
    """

    @staticmethod
    def GetVoid(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/grpc_service.Grpc_Service/GetVoid',
            grpc_dot_protos_dot_grpc__service__pb2.Void.SerializeToString,
            grpc_dot_protos_dot_grpc__service__pb2.Void.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetLong(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/grpc_service.Grpc_Service/GetLong',
            grpc_dot_protos_dot_grpc__service__pb2.Long.SerializeToString,
            grpc_dot_protos_dot_grpc__service__pb2.Long.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetLongBatch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/grpc_service.Grpc_Service/GetLongBatch',
            grpc_dot_protos_dot_grpc__service__pb2.LongBatch.SerializeToString,
            grpc_dot_protos_dot_grpc__service__pb2.Long.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetString(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/grpc_service.Grpc_Service/GetString',
            grpc_dot_protos_dot_grpc__service__pb2.String.SerializeToString,
            grpc_dot_protos_dot_grpc__service__pb2.String.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetJson(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/grpc_service.Grpc_Service/GetJson',
            grpc_dot_protos_dot_grpc__service__pb2.Json.SerializeToString,
            grpc_dot_protos_dot_grpc__service__pb2.String.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
