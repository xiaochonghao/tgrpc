#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/12 下午5:41
# @Author   : hxc
# @File     : run_codegen.py
# @Software : PyCharm

import sys
from grpc_tools import protoc

if __name__ == '__main__':
    protoc.main((
        '',
        '-I{}'.format(sys.argv[1]),
        '--python_out={}'.format(sys.argv[1]),
        '--grpc_python_out={}'.format(sys.argv[1]),
        sys.argv[2]
    ))
