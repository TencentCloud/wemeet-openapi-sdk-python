from abc import ABC, abstractmethod
from typing import *


# Serializer 抽象序列化器
class Serializer(ABC):
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def content_type(self) -> str:
        pass

    @abstractmethod
    def serialize(self, v: Any) -> Optional[bytes]:
        pass

    @abstractmethod
    def deserialize(self, data: Optional[bytes], v_t: Type[Any]) -> Any:
        pass
