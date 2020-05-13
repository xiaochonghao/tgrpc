# tgrpc
实现python server&amp;client两端的grpc demo

---

## 开发步骤
1. 编写`.proto`文件.
2. 利用脚本`run_codegen.py`生成`python`代码.
    ```bash
    # 下面的命令会利用protos/route/route_guide.proto文件，在protos/route/下生成grpc的python代码
    python protos/run_codegen.py protos/route/ protos/route/route_guide.proto
    ```
3. 继承`*_pb2_grpc.py`下的`*Servicer`类，结合`*_pb2.py`下的`Message`类，实现`Service`类.
4. 在`run_server.py`中初始化`server`对象，配置组合凭证，即包括通道凭证、调用(`Metadata`)凭证.
5. 将实现的`Service`类注册到`server`对象，在一个通道配置运行多个`Service`
6. 启动`server`对象