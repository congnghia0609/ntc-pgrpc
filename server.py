"""
@author nghiatc
@since 09/01/2021
"""
import logging
from concurrent import futures

import grpc

from ngrpc import calculator_pb2
from ngrpc import calculator_pb2_grpc


class CalculatorService(calculator_pb2_grpc.CalculatorServiceServicer):
    def Sum(self, request, context):
        print("Sum called...")
        return calculator_pb2.SumResponse(result=request.num1+request.num2)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServiceServicer_to_server(CalculatorService(), server)
    server.add_insecure_port('0.0.0.0:5555')
    # start server
    print("Server CalculatorService is running on: 0.0.0.0:5555")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
