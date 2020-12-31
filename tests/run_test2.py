# -*- coding: utf-8 -*-
"""
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
"""

import json
import threading
# import unittest

# import time


import sys
import os
import time

sys.path.append(os.path.abspath("./"))
sys.path.append(os.path.abspath("./dubbo/"))
# sys.path.append(os.path.abspath("./task_log"))
# sys.path.append(os.path.abspath("./posm"))
# sys.path.append(os.path.abspath("./pricer"))
# sys.path.append(os.path.abspath("./quote"))
# sys.path.append(os.path.abspath("./risk_calculator"))
# print(sys.path)

from dubbo.client import DubboClient, ZkRegister
from dubbo.codec.encoder import Object
from dubbo.common.loggers import init_log


def pretty_print(value):
    print (json.dumps(value, ensure_ascii=False, indent=4, sort_keys=True))


def run(_dubbo):
    for j in range(1000):
        _dubbo.call('echo18')

def test_run_default():
    zk = ZkRegister('127.0.0.1:2181')
    dubbo_cli = DubboClient('org.apache.dubbo.samples.api.GreetingsService', dubbo_version='2.0.2', zk_register=zk, group="1234")

# spu_query_request = Object('com.qianmi.pc.item.api.spu.request.SpuQueryRequest')
# spu_query_request['chainMasterId'] = 'A000000'
# spu_query_request['channel'] = channel
# spu_query_request['pageSize'] = 2000

    # goods_query_request = Object('org.apache.dubbo.samples.User', values={
    #     'name': 'A859315',
    #     'age': 2
    # })
    goods_query_request = Object('org.apache.dubbo.samples.User')
    goods_query_request['name'] = 'A000000222'
    # goods_query_request['channel'] = channel
    goods_query_request['age'] = 2000

    # result = dubbo_cli.call('sayHiOjb2', args=[goods_query_request])
    # # dubbo_cli.call

    # goods_query_request['name'] = 'A00000022255555555555555'

    # # time.sleep(3)  # after 300 seconds, the service will be stopped

    # # print("1111111111111111111111111111111111111111111")
    # result = dubbo_cli.call('sayHiOjb', args=[goods_query_request])
    # # pretty_print(result)
    # goods_query_request['name'] = 'A00000022266666666666666666'
    # result = dubbo_cli.call('sayHiOjb2', args=[goods_query_request])
    # goods_query_request['name'] = 'A000000222677777777777777777'
    # result = dubbo_cli.call('sayHiOjb2', args=[goods_query_request])
    # pretty_print(result)

    for i in range(100):
        goods_query_request['name'] = 'A000000222'+str(i)
        try:
            dubbo_cli.call('sayHiOjb2', args=[goods_query_request])
        except Exception as identifier:
            print(identifier)
            pass

def run2(_dubbo, goods_query_request):
    for j in range(1000):
        _dubbo.call('sayHiOjb2', args=[goods_query_request])

def test_run():
    zk = ZkRegister('127.0.0.1:2181')
    dubbo_cli = DubboClient('org.apache.dubbo.samples.api.GreetingsService', dubbo_version='2.0.2', zk_register=zk, group="23456")
                 #DubboClient('me.hourui.echo.provider.Echo', dubbo_version='2.0.2', zk_register=zk)
    for i in range(4):
        goods_query_request = Object('org.apache.dubbo.samples.User')
        goods_query_request['name'] = 'A000000222'+str(i)
        # goods_query_request['channel'] = channel
        goods_query_request['age'] = 2000
        thread = threading.Thread(target=run2, args=(dubbo_cli, goods_query_request))
        thread.start()

if __name__ == "__main__":
    init_log()  # 初始化日志配置，调用端需要自己配置日志属性
    test_run_default()
    # test_run()