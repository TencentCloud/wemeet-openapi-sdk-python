from typing import *

from wemeet_openapi.core.xhttp.authenticator import Authenticator
from wemeet_openapi.core.xhttp.serializer import Serializer


class ApiRequest(object):

    def __init__(
            self,
            api_uri: str,
            body: Optional[Any] = None,
            header: Dict[str, str] = None,
            serializer: Optional[Serializer] = None,
            authenticators: List[Authenticator] = None):

        self.api_uri: str = api_uri
        self.path_params: Dict[str, str] = {}
        self.query_params: List[Tuple[str, str]] = []
        self.body: Optional[Any] = body

        # 配置请求头
        if header is not None:
            self.__header: Dict[str, str] = header
        else:
            self.__header: Dict[str, str] = {}

        # 配置序列化器
        self.__serializer: Optional[Serializer] = serializer
        # 配置鉴权器
        if authenticators is not None:
            self.__authenticators: List[Authenticator] = authenticators
        else:
            self.__authenticators: List[Authenticator] = []

    def serializer(self) -> Optional[Serializer]:
        return self.__serializer

    def authenticators(self) -> List[Authenticator]:
        return self.__authenticators

    def header(self) -> Dict[str, str]:
        return self.__header

    def generate_url(self, base_url: str) -> str:
        raw_uri = self.api_uri
        if not raw_uri.startswith("http"):
            raw_uri = f"{base_url}{raw_uri}"
        # path
        for key in self.path_params:
            raw_uri = raw_uri.replace("{" + key + "}", self.path_params[key])

        # query
        return raw_uri
