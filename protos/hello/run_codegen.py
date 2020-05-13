#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/12 下午5:41
# @Author   : hxc
# @File     : run_codegen.py
# @Software : PyCharm
import os
from grpc_tools import protoc

cur_pos = os.path.dirname(os.path.abspath(__file__))

protoc.main((
    '',
    '-I{}'.format(cur_pos),
    '--python_out={}'.format(cur_pos),
    '--grpc_python_out={}'.format(cur_pos),
    'hello.proto'
))
