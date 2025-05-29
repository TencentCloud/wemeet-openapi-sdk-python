# coding: utf-8

"""
    腾讯会议OpenAPI

    SAAS版RESTFUL风格API

    API version: v1.0.8

    Do not edit the class manually.
"""  # noqa: E501


from typing import Dict, List, Optional, Callable, BinaryIO

from wemeet_openapi.core import Config, DEFAULT_AUTHENTICATOR, DEFAULT_SERIALIZER
from wemeet_openapi.core.xhttp import ApiRequest, ApiResponse
from wemeet_openapi.core.authenticator import Authenticator
from wemeet_openapi.core.serializer import Serializer
from wemeet_openapi.core.exception import ServiceException, ClientException
from wemeet_openapi.service.pstn.model import *

from requests_toolbelt import MultipartEncoder


class ApiV1MeetingMeetingIdPhoneCalloutPostRequest(object):
    """批量外呼

    **描述**：  * 会议创建者、主持人、联席主持人可以批量外呼电话入会。 * 在拨打后，立刻返回，无需等待，客户通过查询接口和 Webhook 获得外呼状态。 * 需要支持在会议未开始、会中外呼。 * 每次调用支持批量外呼50路。 * \\*\\*鉴权方式：\\*\\*JWT 鉴权
    
    :param meeting_id: 会议的唯一ID (required)
    :type meeting_id: str

    :param body:
    :type body: V1MeetingMeetingIdPhoneCalloutPostRequest
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        body: Optional[V1MeetingMeetingIdPhoneCalloutPostRequest] = None
    ):
        self.meeting_id = meeting_id
        self.body = body

class ApiV1MeetingMeetingIdPhoneCalloutPostResponse(ApiResponse):
    data: Optional[V1MeetingMeetingIdPhoneCalloutPost200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingMeetingIdPhoneCalloutPost200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingMeetingIdPhoneCancelcallPostRequest(object):
    """批量取消外呼

    
    :param meeting_id: (required)
    :type meeting_id: str

    :param body:
    :type body: V1MeetingMeetingIdPhoneCancelcallPostRequest
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        body: Optional[V1MeetingMeetingIdPhoneCancelcallPostRequest] = None
    ):
        self.meeting_id = meeting_id
        self.body = body

class ApiV1MeetingMeetingIdPhoneCancelcallPostResponse(ApiResponse):
    data: Optional[V1MeetingMeetingIdPhoneCancelcallPost200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingMeetingIdPhoneCancelcallPost200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class PstnApi:
    def __init__(self, config: Config):
        self.__config = config

    def v1_meeting_meeting_id_phone_callout_post(
        self,
        request: ApiV1MeetingMeetingIdPhoneCalloutPostRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingMeetingIdPhoneCalloutPostResponse:
        """v1_meeting_meeting_id_phone_callout_post 批量外呼[/v1/meeting/{meeting_id}/phone/callout - POST]

            **描述**：  * 会议创建者、主持人、联席主持人可以批量外呼电话入会。 * 在拨打后，立刻返回，无需等待，客户通过查询接口和 Webhook 获得外呼状态。 * 需要支持在会议未开始、会中外呼。 * 每次调用支持批量外呼50路。 * \\*\\*鉴权方式：\\*\\*JWT 鉴权
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meeting/{meeting_id}/phone/callout",
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
            api_resp = self.__config.clt.post(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1MeetingMeetingIdPhoneCalloutPostResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingMeetingIdPhoneCalloutPost200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meeting_meeting_id_phone_cancelcall_post(
        self,
        request: ApiV1MeetingMeetingIdPhoneCancelcallPostRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingMeetingIdPhoneCancelcallPostResponse:
        """v1_meeting_meeting_id_phone_cancelcall_post 批量取消外呼[/v1/meeting/{meeting_id}/phone/cancelcall - POST]

        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meeting/{meeting_id}/phone/cancelcall",
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
            api_resp = self.__config.clt.post(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1MeetingMeetingIdPhoneCancelcallPostResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingMeetingIdPhoneCancelcallPost200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

