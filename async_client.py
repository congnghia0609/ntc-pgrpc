"""
@author nghiatc
@since 09/01/2021
"""
import asyncio
import logging
import time
from typing import Iterable

import grpc
from ngrpc import calculator_pb2
from ngrpc import calculator_pb2_grpc


async def call_sum() -> None:
    print("Call sum api")
    channel = grpc.aio.insecure_channel('localhost:5555')
    stub = calculator_pb2_grpc.CalculatorServiceStub(channel)
    resp = await stub.Sum(calculator_pb2.SumRequest(num1=7, num2=6))
    print("sum api response: ", resp.result)


async def call_pnd():
    print("call pnd api")
    channel = grpc.aio.insecure_channel('localhost:5555')
    stub = calculator_pb2_grpc.CalculatorServiceStub(channel)
    resp = stub.PrimeNumberDecomposition(calculator_pb2.PNDRequest(number=120))
    async for r in resp:
        print("prime number: %s" % r.result)


def avg_iterator(n) -> Iterable[calculator_pb2.AverageRequest]:
    for i in range(0, n):
        time.sleep(1)
        yield calculator_pb2.AverageRequest(num=5*(i+1))


async def call_average() -> None:
    print("call average api")
    channel = grpc.aio.insecure_channel('localhost:5555')
    stub = calculator_pb2_grpc.CalculatorServiceStub(channel)
    req_iterator = avg_iterator(5)
    resp = await stub.Average(req_iterator)
    print("Average response %s" % resp.result)


def find_max_iterator() -> Iterable[calculator_pb2.FindMaxRequest]:
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


async def call_find_max() -> None:
    print("call find max")
    channel = grpc.aio.insecure_channel('localhost:5555')
    stub = calculator_pb2_grpc.CalculatorServiceStub(channel)
    req_iterator = find_max_iterator()
    responses = stub.FindMax(req_iterator)
    async for resp in responses:
        print("Max response: %s" % resp.max)


if __name__ == '__main__':
    logging.basicConfig()
    # asyncio.get_event_loop().run_until_complete(call_sum())
    # asyncio.get_event_loop().run_until_complete(call_pnd())
    # asyncio.get_event_loop().run_until_complete(call_average())
    asyncio.get_event_loop().run_until_complete(call_find_max())
