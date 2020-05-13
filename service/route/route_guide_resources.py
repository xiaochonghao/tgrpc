#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/13 下午7:41
# @Author   : hxc
# @File     : route_guide_resources.py
# @Software : PyCharm

import json
import os
from protos.route import route_guide_pb2


def read_route_guide_database():
    feature_list = []
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    with open("{}/route_guide_db.json".format(cur_dir)) as route_guide_db_file:
        for item in json.load(route_guide_db_file):
            point = route_guide_pb2.Point(latitude=item["location"]["latitude"],
                                          longitude=item["location"]["longitude"])
            feature = route_guide_pb2.Feature(name=item["name"], location=point)
            feature_list.append(feature)

    return feature_list
