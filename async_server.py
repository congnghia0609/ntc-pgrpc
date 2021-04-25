"""
@author nghiatc
@since 09/01/2021
"""
import asyncio
import logging
import time
import grpc
from concurrent import futures
from ngrpc import calculator_pb2
from ngrpc import calculator_pb2_grpc
from typing import AsyncIterable


class CalculatorService(calculator_pb2_grpc.CalculatorServiceServicer):
    async def Sum(self, request: calculator_pb2.SumRequest, context) -> calculator_pb2.SumResponse:
        print("Sum called...")
        return calculator_pb2.SumResponse(result=request.num1 + request.num2)

    async def PrimeNumberDecomposition(self, request: calculator_pb2.PNDRequest, context
                                       ) -> AsyncIterable[calculator_pb2.PNDResponse]:
        print("PrimeNumberDecomposition called...")
        k = 2
        n = request.number
        while n > 1:
            if n % k == 0:
                n = n / k
                time.sleep(1)
                # send to client
                print("server response k = %s" % k)
                yield calculator_pb2.PNDResponse(result=k)
            else:
                k = k + 1

    async def Average(self, request_iterator: AsyncIterable[calculator_pb2.AverageRequest], context
                      ) -> calculator_pb2.AverageResponse:
        print("Average called...")
        total = 0.0
        count = 0
        async for req in request_iterator:
            total = total + req.num
            count = count + 1
            print("receive req %s" % req.num)
        return calculator_pb2.AverageResponse(result=total / count)

    async def FindMax(self, request_iterator: AsyncIterable[calculator_pb2.FindMaxRequest], context
                      ) -> AsyncIterable[calculator_pb2.FindMaxResponse]:
        print("FindMax called...")
        max = 0
        async for req in request_iterator:
            num = req.num
            print("recv num %s" % num)
            if num > max:
                max = num
            yield calculator_pb2.FindMaxResponse(max=max)


async def serve() -> None:
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServiceServicer_to_server(CalculatorService(), server)
    server.add_insecure_port('0.0.0.0:5555')
    # start server
    print("Server CalculatorService is running on: 0.0.0.0:5555")
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    asyncio.get_event_loop().run_until_complete(serve())
