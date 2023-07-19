# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ya_pb2 as ya__pb2


class YaProductsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.YaShowProducts = channel.unary_unary(
                '/YaProducts/YaShowProducts',
                request_serializer=ya__pb2.YaProductInfoRequest.SerializeToString,
                response_deserializer=ya__pb2.YaProductInfoResponse.FromString,
                )


class YaProductsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def YaShowProducts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_YaProductsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'YaShowProducts': grpc.unary_unary_rpc_method_handler(
                    servicer.YaShowProducts,
                    request_deserializer=ya__pb2.YaProductInfoRequest.FromString,
                    response_serializer=ya__pb2.YaProductInfoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'YaProducts', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class YaProducts(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def YaShowProducts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/YaProducts/YaShowProducts',
            ya__pb2.YaProductInfoRequest.SerializeToString,
            ya__pb2.YaProductInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class YaSearchStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.YaSearchProduct = channel.unary_unary(
                '/YaSearch/YaSearchProduct',
                request_serializer=ya__pb2.YaSearchRequest.SerializeToString,
                response_deserializer=ya__pb2.YaSearchResponse.FromString,
                )


class YaSearchServicer(object):
    """Missing associated documentation comment in .proto file."""

    def YaSearchProduct(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_YaSearchServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'YaSearchProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.YaSearchProduct,
                    request_deserializer=ya__pb2.YaSearchRequest.FromString,
                    response_serializer=ya__pb2.YaSearchResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'YaSearch', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class YaSearch(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def YaSearchProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/YaSearch/YaSearchProduct',
            ya__pb2.YaSearchRequest.SerializeToString,
            ya__pb2.YaSearchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
