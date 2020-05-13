#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/12 下午6:13
# @Author   : hxc
# @File     : greeter_server.py
# @Software : PyCharm
from concurrent import futures
import logging

import grpc

import sys
print(sys.path)

from protos.hello import hello_pb2_grpc
from service.hello.server import Greeter


def serve():


    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
