"""
@author nghiatc
@since 09/01/2021
"""
import logging

import grpc
from ngrpc import calculator_pb2
from ngrpc import calculator_pb2_grpc


def call_sum():
    print("Call sum api")
    with grpc.insecure_channel('localhost:5555') as channel:
        stub = calculator_pb2_grpc.CalculatorServiceStub(channel)
        resp = stub.Sum(calculator_pb2.SumRequest(num1=7, num2=6))
    print("sum api response: ", resp.result)


if __name__ == '__main__':
    logging.basicConfig()
    call_sum()
