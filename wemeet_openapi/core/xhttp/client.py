from urllib.parse import urlparse

import requests
from abc import ABC, abstractmethod
from typing import *

from requests_toolbelt import MultipartEncoder

from wemeet_openapi.core.xhttp.authenticator import Authenticator
from wemeet_openapi.core.xhttp.request import ApiRequest
from wemeet_openapi.core.xhttp.response import ApiResponse
from wemeet_openapi.core.xhttp.serializer import Serializer


# AbstractClient 封装 REST 标准客户端接口
class AbstractClient(ABC):

    @abstractmethod
    def get(self, req: ApiRequest) -> ApiResponse:
        pass

    @abstractmethod
    def post(self, req: ApiRequest) -> ApiResponse:
        pass

    @abstractmethod
    def put(self, req: ApiRequest) -> ApiResponse:
        pass

    @abstractmethod
    def delete(self, req: ApiRequest) -> ApiResponse:
        pass


# Client 封装 REST 标准客户端默认实现
class Client(AbstractClient):

    def __init__(self, host: str, protocol: str = "http",
                 session: Optional[requests.Session] = requests.Session(),
                 serializer: Optional[Serializer] = None):
        self.__host: str = host
        self.__protocol: str = protocol
        self.__serializer: Optional[Serializer] = serializer
        # 设置请求 session
        self.__session: Optional[requests.Session] = session

        if self.__host == "":
            raise Exception("http client's host can't be empty")
        try:
            res = urlparse(f"{self.__protocol}://{self.__host}")
            if not all([res.scheme, res.netloc]):
                raise Exception("http client's protocol or host is illegal")
        except ValueError:
            raise Exception("http client's protocol or host is illegal")

    def post(self, req: ApiRequest) -> ApiResponse:
        if req is None:
            raise Exception("http client do request error, 'req' is None")
        return self._do_request(req=req, method="POST")

    def put(self, req: ApiRequest) -> ApiResponse:
        if req is None:
            raise Exception("http client do request error, 'req' is None")
        return self._do_request(req=req, method="PUT")

    def delete(self, req: ApiRequest) -> ApiResponse:
        if req is None:
            raise Exception("http client do request error, 'req' is None")
        return self._do_request(req=req, method="DELETE")

    def get(self, req: ApiRequest,
            serializer: Optional[Serializer] = None,
            authenticators: Optional[List[Authenticator]] = None) -> ApiResponse:
        if req is None:
            raise Exception("http client do request error, 'req' is None")
        return self._do_request(req=req, method="GET")

    def _do_request(self, req: ApiRequest, method: str) -> ApiResponse:

        # 获取序列化器，以当前请求配置的为准
        serializer = req.serializer()
        if serializer is None:
            serializer = self.__serializer

        # 序列化请求体
        data: Optional[bytes] = b''
        if req.body is not None:
            if isinstance(req.body, MultipartEncoder):
                data = req.body
            elif serializer is not None:
                data = serializer.serialize(req.body)
            elif isinstance(req.body, (str, bytes)):
                data = req.body.encode("utf-8")

        # 生成 url
        u = req.generate_url(f"{self.__protocol}://{self.__host}")
        # 构造 requests http 请求
        http_req = requests.Request(method=method, url=u, params=req.query_params, data=data).prepare()

        # 设置请求头
        for k, v in req.header().items():
            http_req.headers[k] = v

        # 增加鉴权头
        authenticators = req.authenticators()
        if authenticators is not None:
            for authenticator in authenticators:
                authenticator.auth_header(http_req=http_req)
        # 获取 requests session
        if self.__session is None:
            self.__session = requests.Session()

        # 执行发送请求
        http_resp = self.__session.send(http_req)
        http_resp_header: Dict[str, str] = {}
        for k, v in http_resp.headers.items():
            http_resp_header[k] = v
        # 读取响应
        resp_body = http_resp.content
        # 关闭连接
        http_resp.close()

        # 封装响应返回
        return ApiResponse(status_code=http_resp.status_code,
                           raw_body=resp_body,
                           header=http_resp_header,
                           serializer=serializer)
