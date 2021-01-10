"""
@author nghiatc
@since 09/01/2021
"""
import logging
import time
import grpc
from concurrent import futures
from ngrpc import calculator_pb2
from ngrpc import calculator_pb2_grpc


class CalculatorService(calculator_pb2_grpc.CalculatorServiceServicer):
    def Sum(self, request, context):
        print("Sum called...")
        return calculator_pb2.SumResponse(result=request.num1+request.num2)

    def PrimeNumberDecomposition(self, request, context):
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

    def Average(self, request_iterator, context):
        print("Average called...")
        total = 0.0
        count = 0
        for req in request_iterator:
            total = total + req.num
            count = count + 1
            print("receive req %s" % req.num)
        return calculator_pb2.AverageResponse(result=total / count)

    def FindMax(self, request_iterator, context):
        print("FindMax called...")
        max = 0
        for req in request_iterator:
            num = req.num
            print("recv num %s" % num)
            if num > max:
                max = num
            yield calculator_pb2.FindMaxResponse(max=max)


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
