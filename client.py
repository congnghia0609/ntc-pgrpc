"""
@author nghiatc
@since 09/01/2021
"""
import logging
import time

import grpc
from ngrpc import calculator_pb2
from ngrpc import calculator_pb2_grpc


def call_sum():
    print("Call sum api")
    # with grpc.insecure_channel('localhost:5555') as channel:
    #     stub = calculator_pb2_grpc.CalculatorServiceStub(channel)
    #     resp = stub.Sum(calculator_pb2.SumRequest(num1=7, num2=6))
    channel = grpc.insecure_channel('localhost:3333')
    stub = calculator_pb2_grpc.CalculatorServiceStub(channel)
    resp = stub.Sum(calculator_pb2.SumRequest(num1=7, num2=6))
    print("sum api response: ", resp.result)


def call_pnd():
    print("call pnd api")
    channel = grpc.insecure_channel('localhost:5555')
    stub = calculator_pb2_grpc.CalculatorServiceStub(channel)
    resp = stub.PrimeNumberDecomposition(calculator_pb2.PNDRequest(number=120))
    for r in resp:
        print("prime number: %s" % r.result)


def avg_iterator(n):
    # list_req = [
    #     calculator_pb2.AverageRequest(num=5),
    #     calculator_pb2.AverageRequest(num=10),
    #     calculator_pb2.AverageRequest(num=15),
    #     calculator_pb2.AverageRequest(num=20),
    #     calculator_pb2.AverageRequest(num=25)
    # ]
    for i in range(0, n):
        time.sleep(1)
        yield calculator_pb2.AverageRequest(num=5*(i+1))


def call_average():
    print("call average api")
    channel = grpc.insecure_channel('localhost:5555')
    stub = calculator_pb2_grpc.CalculatorServiceStub(channel)
    req_iterator = avg_iterator(5)
    resp = stub.Average(req_iterator)
    print("Average response %s" % resp.result)


def find_max_iterator():
    list_req = [
        calculator_pb2.FindMaxRequest(num=5),
        calculator_pb2.FindMaxRequest(num=10),
        calculator_pb2.FindMaxRequest(num=1),
        calculator_pb2.FindMaxRequest(num=6),
        calculator_pb2.FindMaxRequest(num=9)
    ]
    for req in list_req:
        time.sleep(1)
        yield req


def call_find_max():
    print("call find max")
    channel = grpc.insecure_channel('localhost:5555')
    stub = calculator_pb2_grpc.CalculatorServiceStub(channel)
    req_iterator = find_max_iterator()
    responses = stub.FindMax(req_iterator)
    for resp in responses:
        print("Max response: %s" % resp.max)


if __name__ == '__main__':
    logging.basicConfig()
    # call_sum()
    # call_pnd()
    # call_average()
    call_find_max()
