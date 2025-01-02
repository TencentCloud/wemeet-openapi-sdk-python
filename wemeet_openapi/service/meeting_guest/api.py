# coding: utf-8

"""
    腾讯会议OpenAPI

    SAAS版RESTFUL风格API

    API version: v1.0.4

    Do not edit the class manually.
"""  # noqa: E501


from typing import Dict, List, Optional, Callable, BinaryIO

from wemeet_openapi.core import Config, DEFAULT_AUTHENTICATOR, DEFAULT_SERIALIZER
from wemeet_openapi.core.xhttp import ApiRequest, ApiResponse
from wemeet_openapi.core.authenticator import Authenticator
from wemeet_openapi.core.serializer import Serializer
from wemeet_openapi.core.exception import ServiceException, ClientException
from wemeet_openapi.service.meeting_guest.model import *

from requests_toolbelt import MultipartEncoder


class ApiV1GuestsMeetingIdGetRequest(object):
    """查询会议嘉宾列表（通过会议 ID 查询）

    通过会议 ID 查询会议嘉宾列表，只有会议创建人才有权限查询，支持 OAuth2.0 鉴权访问。  > 注意 > 只有商业版、企业版或教育版用户可以使用会议嘉宾功能，个人版尚无此功能。
    
    :param meeting_id: (required)
    :type meeting_id: str

    :param userid: 用户的 ID（企业内部请使用企业唯一用户标识，OAuth2.0 鉴权用户请使用 openId）。 (required)
    :type userid: str

    :param instanceid: 用户的终端设备类型： 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序。9：voip、sip 设备 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch MacOS 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch iOS (required)
    :type instanceid: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        userid: Optional[str] = None,
        instanceid: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.meeting_id = meeting_id
        self.userid = userid
        self.instanceid = instanceid
        self.body = body

class ApiV1GuestsMeetingIdGetResponse(ApiResponse):
    data: Optional[V1GuestsMeetingIdGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1GuestsMeetingIdGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1GuestsMeetingIdPutRequest(object):
    """修改会议嘉宾列表（通过会议 ID 修改）

    通过会议 ID 修改会议嘉宾列表，只有会议创建人才有权限修改，支持 OAuth2.0 鉴权访问。  *  > 注意 > 只有商业版、企业版或教育版用户可以使用会议嘉宾功能，个人版尚无此功能。
    
    :param meeting_id: (required)
    :type meeting_id: str

    :param body:
    :type body: V1GuestsMeetingIdPutRequest
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        body: Optional[V1GuestsMeetingIdPutRequest] = None
    ):
        self.meeting_id = meeting_id
        self.body = body

class ApiV1GuestsMeetingIdPutResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class MeetingGuestApi:
    def __init__(self, config: Config):
        self.__config = config

    def v1_guests_meeting_id_get(
        self,
        request: ApiV1GuestsMeetingIdGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1GuestsMeetingIdGetResponse:
        """v1_guests_meeting_id_get 查询会议嘉宾列表（通过会议 ID 查询）[/v1/guests/{meeting_id} - GET]

            通过会议 ID 查询会议嘉宾列表，只有会议创建人才有权限查询，支持 OAuth2.0 鉴权访问。  > 注意 > 只有商业版、企业版或教育版用户可以使用会议嘉宾功能，个人版尚无此功能。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/guests/{meeting_id}",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'meeting_id' is set
            if request.meeting_id is None:
                raise Exception("meeting_id is required and must be specified")
            # verify the required parameter 'userid' is set
            if request.userid is None:
                raise Exception("userid is required and must be specified")
            # verify the required parameter 'instanceid' is set
            if request.instanceid is None:
                raise Exception("instanceid is required and must be specified")
            # path 参数
            if request.meeting_id is not None:
                api_req.path_params['meeting_id'] = request.meeting_id
            # query 参数
            if request.userid is not None:
                api_req.query_params.append(('userid', request.userid))
            if request.instanceid is not None:
                api_req.query_params.append(('instanceid', request.instanceid))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1GuestsMeetingIdGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1GuestsMeetingIdGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_guests_meeting_id_put(
        self,
        request: ApiV1GuestsMeetingIdPutRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1GuestsMeetingIdPutResponse:
        """v1_guests_meeting_id_put 修改会议嘉宾列表（通过会议 ID 修改）[/v1/guests/{meeting_id} - PUT]

            通过会议 ID 修改会议嘉宾列表，只有会议创建人才有权限修改，支持 OAuth2.0 鉴权访问。  *  > 注意 > 只有商业版、企业版或教育版用户可以使用会议嘉宾功能，个人版尚无此功能。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/guests/{meeting_id}",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'meeting_id' is set
            if request.meeting_id is None:
                raise Exception("meeting_id is required and must be specified")
            # path 参数
            if request.meeting_id is not None:
                api_req.path_params['meeting_id'] = request.meeting_id
            # query 参数
            # 发送请求
            api_resp = self.__config.clt.put(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1GuestsMeetingIdPutResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

