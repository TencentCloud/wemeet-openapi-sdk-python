from typing import *

from wemeet_openapi.core.xhttp.serializer import Serializer


class ApiResponse(object):
    def __init__(
            self,
            status_code: Optional[int] = None,
            raw_body: Optional[bytes] = None,
            header: Dict[str, str] = None,
            serializer: Optional[Serializer] = None
    ):
        self.status_code: Optional[int] = status_code
        self.raw_body: Optional[bytes] = raw_body
        if header is None:
            header = {}
        self.header: Dict[str, str] = header

        self.__serializor: Optional[Serializer] = serializer

    def serializer(self) -> Optional[Serializer]:
        return self.__serializor

    def translate(self, dst_t: Any, serializor: Optional[Serializer] = None) -> Any:

        copy_resp = ApiResponse(raw_body=self.raw_body)
        if serializor is not None:
            copy_resp.__serializor = serializor
        else:
            copy_resp.__serializor = self.__serializor

        if dst_t is None:
            raise Exception("response body translate error, 'dst_t' is None")

        if copy_resp.__serializor is None:
            raise Exception("response body translate error, serializer is None")
        try:
            return copy_resp.__serializor.deserialize(copy_resp.raw_body, v_t=dst_t)
        except Exception as e:
            raise Exception(f"response body translate error, "
                            f"type '{dst_t}' can't be translated by "
                            f"'{copy_resp.__serializor.name()}' serializer") from e
