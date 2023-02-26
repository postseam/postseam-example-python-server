# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from pb.postseam.example.v1 import product_pb2 as pb_dot_postseam_dot_example_dot_v1_dot_product__pb2
from pb.postseam.example.v1 import product_service_pb2 as pb_dot_postseam_dot_example_dot_v1_dot_product__service__pb2


class ProductServiceStub(object):
    """ProductService: Handles all the logic for products on the platform
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetProduct = channel.unary_unary(
                '/pb.postseam.example.v1.ProductService/GetProduct',
                request_serializer=pb_dot_postseam_dot_example_dot_v1_dot_product__service__pb2.GetProductRequest.SerializeToString,
                response_deserializer=pb_dot_postseam_dot_example_dot_v1_dot_product__pb2.Product.FromString,
                )
        self.CreateProduct = channel.unary_unary(
                '/pb.postseam.example.v1.ProductService/CreateProduct',
                request_serializer=pb_dot_postseam_dot_example_dot_v1_dot_product__service__pb2.CreateProductRequest.SerializeToString,
                response_deserializer=pb_dot_postseam_dot_example_dot_v1_dot_product__pb2.Product.FromString,
                )
        self.ListProducts = channel.unary_unary(
                '/pb.postseam.example.v1.ProductService/ListProducts',
                request_serializer=pb_dot_postseam_dot_example_dot_v1_dot_product__service__pb2.ListProductsRequest.SerializeToString,
                response_deserializer=pb_dot_postseam_dot_example_dot_v1_dot_product__service__pb2.ListProductsResponse.FromString,
                )


class ProductServiceServicer(object):
    """ProductService: Handles all the logic for products on the platform
    """

    def GetProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListProducts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProductServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProduct,
                    request_deserializer=pb_dot_postseam_dot_example_dot_v1_dot_product__service__pb2.GetProductRequest.FromString,
                    response_serializer=pb_dot_postseam_dot_example_dot_v1_dot_product__pb2.Product.SerializeToString,
            ),
            'CreateProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateProduct,
                    request_deserializer=pb_dot_postseam_dot_example_dot_v1_dot_product__service__pb2.CreateProductRequest.FromString,
                    response_serializer=pb_dot_postseam_dot_example_dot_v1_dot_product__pb2.Product.SerializeToString,
            ),
            'ListProducts': grpc.unary_unary_rpc_method_handler(
                    servicer.ListProducts,
                    request_deserializer=pb_dot_postseam_dot_example_dot_v1_dot_product__service__pb2.ListProductsRequest.FromString,
                    response_serializer=pb_dot_postseam_dot_example_dot_v1_dot_product__service__pb2.ListProductsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pb.postseam.example.v1.ProductService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProductService(object):
    """ProductService: Handles all the logic for products on the platform
    """

    @staticmethod
    def GetProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.postseam.example.v1.ProductService/GetProduct',
            pb_dot_postseam_dot_example_dot_v1_dot_product__service__pb2.GetProductRequest.SerializeToString,
            pb_dot_postseam_dot_example_dot_v1_dot_product__pb2.Product.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.postseam.example.v1.ProductService/CreateProduct',
            pb_dot_postseam_dot_example_dot_v1_dot_product__service__pb2.CreateProductRequest.SerializeToString,
            pb_dot_postseam_dot_example_dot_v1_dot_product__pb2.Product.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListProducts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.postseam.example.v1.ProductService/ListProducts',
            pb_dot_postseam_dot_example_dot_v1_dot_product__service__pb2.ListProductsRequest.SerializeToString,
            pb_dot_postseam_dot_example_dot_v1_dot_product__service__pb2.ListProductsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)