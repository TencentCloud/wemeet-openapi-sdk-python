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
from wemeet_openapi.service.layout.model import *

from requests_toolbelt import MultipartEncoder


class ApiV1MeetingsMeetingIdAdvancedLayoutsPostRequest(object):
    """添加自定义布局

    **描述：**  * 对当前会议添加高级自定义布局，支持批量添加。 * 用户座次设置需设置参会成员。 * 单个会议最多允许添加20个布局。 * 目前暂不支持 OAuth2.0 鉴权访问。 * 目前仅会应用于 H.323/SIP 终端
    
    :param meeting_id: 会议ID (required)
    :type meeting_id: str

    :param body:
    :type body: V1MeetingsMeetingIdAdvancedLayoutsPostRequest
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        body: Optional[V1MeetingsMeetingIdAdvancedLayoutsPostRequest] = None
    ):
        self.meeting_id = meeting_id
        self.body = body

class ApiV1MeetingsMeetingIdAdvancedLayoutsPostResponse(ApiResponse):
    data: Optional[V1MeetingsMeetingIdAdvancedLayoutsPost200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingsMeetingIdAdvancedLayoutsPost200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingsMeetingIdApplyingLayoutPutRequest(object):
    """应用布局

    **描述：**  * 将会议中的高级自定义布局应用到指定成员或者整个会议。 * 恢复指定成员或整个会议的默认布局。 * 目前暂不支持 OAuth2.0 鉴权访问。 * 目前仅会应用于 H.323/SIP 终端。  <span class=\"colour\" style=\"color:rgb(51, 51, 51)\"></span>
    
    :param meeting_id: 会议ID (required)
    :type meeting_id: str

    :param body:
    :type body: V1MeetingsMeetingIdApplyingLayoutPutRequest
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        body: Optional[V1MeetingsMeetingIdApplyingLayoutPutRequest] = None
    ):
        self.meeting_id = meeting_id
        self.body = body

class ApiV1MeetingsMeetingIdApplyingLayoutPutResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingsMeetingIdLayoutsPostRequest(object):
    """添加会议布局

    对成功预定的会议添加会议布局，支持多个布局的添加，每个布局支持多页模板，默认选中第一页模板作为该布局的首页进行展示。  * 用户座次设置区分会前和会中两种方式：会前只允许设置邀请者成员，会中只允许设置参会成员。 * 一场会议最多添加10个布局，添加成功返回新增的会议布局信息。 * 目前暂不支持 OAuth2.0 鉴权访问。
    
    :param meeting_id: 会议ID (required)
    :type meeting_id: str

    :param body:
    :type body: V1MeetingsMeetingIdLayoutsPostRequest
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        body: Optional[V1MeetingsMeetingIdLayoutsPostRequest] = None
    ):
        self.meeting_id = meeting_id
        self.body = body

class ApiV1MeetingsMeetingIdLayoutsPostResponse(ApiResponse):
    data: Optional[V1MeetingsMeetingIdLayoutsPost200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingsMeetingIdLayoutsPost200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class LayoutApi:
    def __init__(self, config: Config):
        self.__config = config

    def v1_meetings_meeting_id_advanced_layouts_post(
        self,
        request: ApiV1MeetingsMeetingIdAdvancedLayoutsPostRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingsMeetingIdAdvancedLayoutsPostResponse:
        """v1_meetings_meeting_id_advanced_layouts_post 添加自定义布局[/v1/meetings/{meeting_id}/advanced-layouts - POST]

            **描述：**  * 对当前会议添加高级自定义布局，支持批量添加。 * 用户座次设置需设置参会成员。 * 单个会议最多允许添加20个布局。 * 目前暂不支持 OAuth2.0 鉴权访问。 * 目前仅会应用于 H.323/SIP 终端
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meetings/{meeting_id}/advanced-layouts",
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
                response = ApiV1MeetingsMeetingIdAdvancedLayoutsPostResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingsMeetingIdAdvancedLayoutsPost200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meetings_meeting_id_applying_layout_put(
        self,
        request: ApiV1MeetingsMeetingIdApplyingLayoutPutRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingsMeetingIdApplyingLayoutPutResponse:
        """v1_meetings_meeting_id_applying_layout_put 应用布局[/v1/meetings/{meeting_id}/applying-layout - PUT]

            **描述：**  * 将会议中的高级自定义布局应用到指定成员或者整个会议。 * 恢复指定成员或整个会议的默认布局。 * 目前暂不支持 OAuth2.0 鉴权访问。 * 目前仅会应用于 H.323/SIP 终端。  <span class=\"colour\" style=\"color:rgb(51, 51, 51)\"></span>
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meetings/{meeting_id}/applying-layout",
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
                response = ApiV1MeetingsMeetingIdApplyingLayoutPutResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meetings_meeting_id_layouts_post(
        self,
        request: ApiV1MeetingsMeetingIdLayoutsPostRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingsMeetingIdLayoutsPostResponse:
        """v1_meetings_meeting_id_layouts_post 添加会议布局[/v1/meetings/{meeting_id}/layouts - POST]

            对成功预定的会议添加会议布局，支持多个布局的添加，每个布局支持多页模板，默认选中第一页模板作为该布局的首页进行展示。  * 用户座次设置区分会前和会中两种方式：会前只允许设置邀请者成员，会中只允许设置参会成员。 * 一场会议最多添加10个布局，添加成功返回新增的会议布局信息。 * 目前暂不支持 OAuth2.0 鉴权访问。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meetings/{meeting_id}/layouts",
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
                response = ApiV1MeetingsMeetingIdLayoutsPostResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingsMeetingIdLayoutsPost200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

