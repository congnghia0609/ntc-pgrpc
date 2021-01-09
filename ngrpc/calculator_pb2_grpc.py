# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ngrpc.calculator_pb2 as calculator__pb2


class CalculatorServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Sum = channel.unary_unary(
                '/ngrpc.CalculatorService/Sum',
                request_serializer=calculator__pb2.SumRequest.SerializeToString,
                response_deserializer=calculator__pb2.SumResponse.FromString,
                )
        self.SumWithDeadline = channel.unary_unary(
                '/ngrpc.CalculatorService/SumWithDeadline',
                request_serializer=calculator__pb2.SumRequest.SerializeToString,
                response_deserializer=calculator__pb2.SumResponse.FromString,
                )
        self.PrimeNumberDecomposition = channel.unary_stream(
                '/ngrpc.CalculatorService/PrimeNumberDecomposition',
                request_serializer=calculator__pb2.PNDRequest.SerializeToString,
                response_deserializer=calculator__pb2.PNDResponse.FromString,
                )
        self.Average = channel.stream_unary(
                '/ngrpc.CalculatorService/Average',
                request_serializer=calculator__pb2.AverageRequest.SerializeToString,
                response_deserializer=calculator__pb2.AverageResponse.FromString,
                )
        self.FindMax = channel.stream_stream(
                '/ngrpc.CalculatorService/FindMax',
                request_serializer=calculator__pb2.FindMaxRequest.SerializeToString,
                response_deserializer=calculator__pb2.FindMaxResponse.FromString,
                )
        self.Square = channel.unary_unary(
                '/ngrpc.CalculatorService/Square',
                request_serializer=calculator__pb2.SquareRequest.SerializeToString,
                response_deserializer=calculator__pb2.SquareResponse.FromString,
                )


class CalculatorServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Sum(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SumWithDeadline(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PrimeNumberDecomposition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Average(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FindMax(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Square(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CalculatorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Sum': grpc.unary_unary_rpc_method_handler(
                    servicer.Sum,
                    request_deserializer=calculator__pb2.SumRequest.FromString,
                    response_serializer=calculator__pb2.SumResponse.SerializeToString,
            ),
            'SumWithDeadline': grpc.unary_unary_rpc_method_handler(
                    servicer.SumWithDeadline,
                    request_deserializer=calculator__pb2.SumRequest.FromString,
                    response_serializer=calculator__pb2.SumResponse.SerializeToString,
            ),
            'PrimeNumberDecomposition': grpc.unary_stream_rpc_method_handler(
                    servicer.PrimeNumberDecomposition,
                    request_deserializer=calculator__pb2.PNDRequest.FromString,
                    response_serializer=calculator__pb2.PNDResponse.SerializeToString,
            ),
            'Average': grpc.stream_unary_rpc_method_handler(
                    servicer.Average,
                    request_deserializer=calculator__pb2.AverageRequest.FromString,
                    response_serializer=calculator__pb2.AverageResponse.SerializeToString,
            ),
            'FindMax': grpc.stream_stream_rpc_method_handler(
                    servicer.FindMax,
                    request_deserializer=calculator__pb2.FindMaxRequest.FromString,
                    response_serializer=calculator__pb2.FindMaxResponse.SerializeToString,
            ),
            'Square': grpc.unary_unary_rpc_method_handler(
                    servicer.Square,
                    request_deserializer=calculator__pb2.SquareRequest.FromString,
                    response_serializer=calculator__pb2.SquareResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ngrpc.CalculatorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CalculatorService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Sum(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ngrpc.CalculatorService/Sum',
            calculator__pb2.SumRequest.SerializeToString,
            calculator__pb2.SumResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SumWithDeadline(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ngrpc.CalculatorService/SumWithDeadline',
            calculator__pb2.SumRequest.SerializeToString,
            calculator__pb2.SumResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PrimeNumberDecomposition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/ngrpc.CalculatorService/PrimeNumberDecomposition',
            calculator__pb2.PNDRequest.SerializeToString,
            calculator__pb2.PNDResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Average(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/ngrpc.CalculatorService/Average',
            calculator__pb2.AverageRequest.SerializeToString,
            calculator__pb2.AverageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FindMax(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/ngrpc.CalculatorService/FindMax',
            calculator__pb2.FindMaxRequest.SerializeToString,
            calculator__pb2.FindMaxResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Square(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ngrpc.CalculatorService/Square',
            calculator__pb2.SquareRequest.SerializeToString,
            calculator__pb2.SquareResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
