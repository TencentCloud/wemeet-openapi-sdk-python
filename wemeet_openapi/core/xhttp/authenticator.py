import requests
from abc import ABC, abstractmethod


# Authenticator 抽象鉴权器
class Authenticator(ABC):

    @abstractmethod
    def auth_header(self, http_req: requests.PreparedRequest) -> None:
        pass
