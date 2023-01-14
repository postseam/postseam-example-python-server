# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from pb.postseam.example.v1 import store_pb2 as pb_dot_postseam_dot_example_dot_v1_dot_store__pb2
from pb.postseam.example.v1 import store_service_pb2 as pb_dot_postseam_dot_example_dot_v1_dot_store__service__pb2


class StoreServiceStub(object):
    """StoreService: Handles all the logic for stores on the platform
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetStore = channel.unary_unary(
                '/pb.postseam.example.v1.StoreService/GetStore',
                request_serializer=pb_dot_postseam_dot_example_dot_v1_dot_store__service__pb2.GetStoreRequest.SerializeToString,
                response_deserializer=pb_dot_postseam_dot_example_dot_v1_dot_store__pb2.Store.FromString,
                )
        self.CreateStore = channel.unary_unary(
                '/pb.postseam.example.v1.StoreService/CreateStore',
                request_serializer=pb_dot_postseam_dot_example_dot_v1_dot_store__service__pb2.CreateStoreRequest.SerializeToString,
                response_deserializer=pb_dot_postseam_dot_example_dot_v1_dot_store__pb2.Store.FromString,
                )


class StoreServiceServicer(object):
    """StoreService: Handles all the logic for stores on the platform
    """

    def GetStore(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateStore(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StoreServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetStore': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStore,
                    request_deserializer=pb_dot_postseam_dot_example_dot_v1_dot_store__service__pb2.GetStoreRequest.FromString,
                    response_serializer=pb_dot_postseam_dot_example_dot_v1_dot_store__pb2.Store.SerializeToString,
            ),
            'CreateStore': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateStore,
                    request_deserializer=pb_dot_postseam_dot_example_dot_v1_dot_store__service__pb2.CreateStoreRequest.FromString,
                    response_serializer=pb_dot_postseam_dot_example_dot_v1_dot_store__pb2.Store.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pb.postseam.example.v1.StoreService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StoreService(object):
    """StoreService: Handles all the logic for stores on the platform
    """

    @staticmethod
    def GetStore(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.postseam.example.v1.StoreService/GetStore',
            pb_dot_postseam_dot_example_dot_v1_dot_store__service__pb2.GetStoreRequest.SerializeToString,
            pb_dot_postseam_dot_example_dot_v1_dot_store__pb2.Store.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateStore(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.postseam.example.v1.StoreService/CreateStore',
            pb_dot_postseam_dot_example_dot_v1_dot_store__service__pb2.CreateStoreRequest.SerializeToString,
            pb_dot_postseam_dot_example_dot_v1_dot_store__pb2.Store.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)