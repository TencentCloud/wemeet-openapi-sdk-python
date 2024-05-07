from typing import Optional, Dict, Any

from wemeet_openapi.core.constants import JSON_SERIALIZER
from wemeet_openapi.core.xhttp.response import ApiResponse


class ClientException(Exception):
    """
    ClientException 客户端异常

    :param e: 原生异常
    """

    def __init__(self, e: Exception):
        self.e: Exception = e

    def __str__(self) -> str:
        return f"[wemeet client error] {self.e.__str__()}"


class ServiceException(Exception):
    class ErrorInfo(object):
        error_code: int
        new_error_code: int
        message: str

        def __init__(self, error_info: Dict[str, Any]):
            self.error_code: int = error_info["error_code"]
            self.new_error_code: int = error_info["new_error_code"]
            self.message: str = error_info["message"]

    error_info: Optional[ErrorInfo] = None
    api_resp: Optional[ApiResponse] = None

    def __init__(self,
                 api_resp: Optional[ApiResponse] = None):
        self.api_resp = api_resp
        try:
            self.error_info = JSON_SERIALIZER.deserialize(data=api_resp.raw_body,
                                                          v_t=ServiceException.ErrorInfo)
        except Exception:
            pass

    def __str__(self) -> str:
        msg = f"http status code: {self.api_resp.status_code} "
        if self.error_info is not None:
            msg += f"error code: {self.error_info.error_code}, new error code: {self.error_info.new_error_code}, " \
                   f"message: {self.error_info.message} "
        else:
            msg += f"response body: {self.api_resp.raw_body}"

        return f"[wemeet service error] {msg}"
