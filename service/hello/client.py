#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/12 下午6:14
# @Author   : hxc
# @File     : greeter_client.py
# @Software : PyCharm
from __future__ import print_function
import logging

import grpc

from protos.hello import hello_pb2, hello_pb2_grpc


def run():
    with grpc.insecure_channel('49.233.188.224:50051') as channel:
        stub = hello_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(hello_pb2.HelloRequest(name='hxc'))

    print("Greeter client received:" + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
