#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/12 下午6:13
# @Author   : hxc
# @File     : greeter_server.py
# @Software : PyCharm
from protos.hello import hello_pb2, hello_pb2_grpc


class Greeter(hello_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        return hello_pb2.HelloReply(message='Hello, %s!~' % request.name)
