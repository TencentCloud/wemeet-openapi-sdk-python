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
from wemeet_openapi.service.meeting_control.model import *

from requests_toolbelt import MultipartEncoder


class ApiV1MeetingsMeetingIdDismissPostRequest(object):
    """结束会议

    **描述**：结束一个进行中的会议。  * 只有会议创建者、主持人、联席主持人可以结束会议，且该会议是一个有效的进行中会议。 * 结束周期性会议需要传入主会议 ID。 * 企业 secret 鉴权用户可结束任何该企业该用户创建的进行中的会议，OAuth 2.0鉴权用户只能结束通过 OAuth 2.0鉴权创建的进行中的会议。 * 当您想实时监测会议结束状况时，您可以通过订阅 [会议结束](https://cloud.tencent.com/document/product/1095/51619) 的事件，接收事件通知。 * 此接口暂不支持 MRA 设备作为被操作者的情况。 * 结束会议不会释放 Rooms，如需释放请调用 [释放会议室（Rooms）](https://cloud.tencent.com/document/product/1095/55314) 接口
    
    :param meeting_id: (required)
    :type meeting_id: str

    :param body:
    :type body: V1MeetingsMeetingIdDismissPostRequest
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        body: Optional[V1MeetingsMeetingIdDismissPostRequest] = None
    ):
        self.meeting_id = meeting_id
        self.body = body

class ApiV1MeetingsMeetingIdDismissPostResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1RealControlMeetingsMeetingIdAsrPutRequest(object):
    """开启或关闭实时转写

    以创建者的身份开启/关闭会中实时转写，调用时需要会议处于进行中的状态；
    
    :param meeting_id: (required)
    :type meeting_id: str

    :param body:
    :type body: V1RealControlMeetingsMeetingIdAsrPutRequest
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        body: Optional[V1RealControlMeetingsMeetingIdAsrPutRequest] = None
    ):
        self.meeting_id = meeting_id
        self.body = body

class ApiV1RealControlMeetingsMeetingIdAsrPutResponse(ApiResponse):
    data: Optional[V1RealControlMeetingsMeetingIdAsrPut200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1RealControlMeetingsMeetingIdAsrPut200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1RealControlMeetingsMeetingIdCohostsPutRequest(object):
    """设置联席主持人

    **描述**：设置或撤销会议中的参会者联席主持人身份，目前暂不支持 MRA 设备作为被操作者的情况。企业 secret 鉴权用户可管理任何该企业该用户创建的有效会议，OAuth2.0 鉴权用户只能管理通过 OAuth2.0 鉴权创建的有效会议。  *  > 说明 >  >  > * 操作者必须是会议的主持人才可以设置。 > * 调用该接口需要权限项 ： MANAGE_MEETING 查看和管理您的会议。
    
    :param meeting_id: (required)
    :type meeting_id: str

    :param body:
    :type body: V1RealControlMeetingsMeetingIdCohostsPutRequest
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        body: Optional[V1RealControlMeetingsMeetingIdCohostsPutRequest] = None
    ):
        self.meeting_id = meeting_id
        self.body = body

class ApiV1RealControlMeetingsMeetingIdCohostsPutResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1RealControlMeetingsMeetingIdDocPutRequest(object):
    """文档上传权限设置

    **描述**：设置会议中文档上传权限，目前暂不支持 MRA 设备作为被操作者的情况，企业 secret 鉴权用户可管理任何该企业该用户创建的有效会议，OAuth2.0 鉴权用户只能管理通过 OAuth2.0 鉴权创建的有效会议。  *  > 说明 > 1：操作者必须是会议的主持人或者联席主持人才可以设置。 > 2：调用该接口需要权限项：MANAGE_MEETING 查看和管理您的会议
    
    :param meeting_id: (required)
    :type meeting_id: str

    :param body:
    :type body: V1RealControlMeetingsMeetingIdDocPutRequest
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        body: Optional[V1RealControlMeetingsMeetingIdDocPutRequest] = None
    ):
        self.meeting_id = meeting_id
        self.body = body

class ApiV1RealControlMeetingsMeetingIdDocPutResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1RealControlMeetingsMeetingIdKickoutPutRequest(object):
    """移出用户

    **描述**：  * 将会议中用户移出会议，操作者必须是会议的主持人或者联席主持人才可以设置。 * 支持对云会议已入会成员和 Webinar 观众移出。 * 支持 MRA 设备和 PSTN 设备为被操作者时的移出用户操作。 * 企业 secret 鉴权用户可管理任何该企业该用户创建的有效会议，OAuth2.0 鉴权用户只能管理通过 OAuth2.0 鉴权创建的有效会议。  说明  *  > 1：操作者必须是会议的主持人或者联席主持人才可以设置。 > 2：调用该接口需要权限项：MANAGE_MEETING 查看和管理您的会议。
    
    :param meeting_id: (required)
    :type meeting_id: str

    :param body:
    :type body: V1RealControlMeetingsMeetingIdKickoutPutRequest
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        body: Optional[V1RealControlMeetingsMeetingIdKickoutPutRequest] = None
    ):
        self.meeting_id = meeting_id
        self.body = body

class ApiV1RealControlMeetingsMeetingIdKickoutPutResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1RealControlMeetingsMeetingIdMutesPutRequest(object):
    """静音用户

    **描述**：  * 会议中用户静音操作，操作者必须是会议的主持人或者联席主持人才可以设置。 * 支持对云会议已入会成员和 Webinar 观众静音。 * 支持 MRA 设备和 PSTN 设备作为被操作者时的静音操作。 * 企业 secret 鉴权用户可管理任何该企业该用户创建的有效会议，OAuth2.0 鉴权用户只能管理通过 OAuth2.0 鉴权创建的有效会议。  说明 1：操作者必须是会议的主持人或者联席主持人才可以设置。 2：调用该接口需要权限项：MANAGE_MEETING 查看和管理您的会议。
    
    :param meeting_id: (required)
    :type meeting_id: str

    :param body:
    :type body: V1RealControlMeetingsMeetingIdMutesPutRequest
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        body: Optional[V1RealControlMeetingsMeetingIdMutesPutRequest] = None
    ):
        self.meeting_id = meeting_id
        self.body = body

class ApiV1RealControlMeetingsMeetingIdMutesPutResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1RealControlMeetingsMeetingIdNamesPutRequest(object):
    """更改会中成员昵称

    **描述：**  * 会中修改参会者昵称，支持主持人和联席主持人对会中成员进行改名。 * 此接口支持对云会议已入会成员和 Webinar 观众进行改名。 * 操作者必须为已在会中的主持人与联席主持人。 * 支持 MRA 设备和 PSTN 设备作为被操作者时的改名操作。 * 企业 secret 鉴权用户可管理任何该企业该用户创建的有效会议，OAuth2.0 鉴权用户只能管理通过 OAuth2.0 鉴权创建的有效会议。  说明 1：操作者必须是会议的主持人或者联席主持人才可以设置。 2：调用该接口需要权限项：MANAGE_MEETING 查看和管理您的会议。
    
    :param meeting_id: (required)
    :type meeting_id: str

    :param body:
    :type body: V1RealControlMeetingsMeetingIdNamesPutRequest
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        body: Optional[V1RealControlMeetingsMeetingIdNamesPutRequest] = None
    ):
        self.meeting_id = meeting_id
        self.body = body

class ApiV1RealControlMeetingsMeetingIdNamesPutResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1RealControlMeetingsMeetingIdScreenSharedPutRequest(object):
    """关闭用户屏幕共享

    **描述**：关闭会议中用户屏幕共享权限，目前暂不支持 MRA 设备作为被操作者的情况。企业 secret 鉴权用户可管理任何该企业该用户创建的有效会议，OAuth2.0 鉴权用户只能管理通过 OAuth2.0 鉴权创建的有效会议。  *  > 说明 > 1：操作者必须是会议的主持人或者联席主持人才可以设置。 > 2：调用该接口需要权限项：MANAGE_MEETING 查看和管理您的会议
    
    :param meeting_id: (required)
    :type meeting_id: str

    :param body:
    :type body: V1RealControlMeetingsMeetingIdScreenSharedPutRequest
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        body: Optional[V1RealControlMeetingsMeetingIdScreenSharedPutRequest] = None
    ):
        self.meeting_id = meeting_id
        self.body = body

class ApiV1RealControlMeetingsMeetingIdScreenSharedPutResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1RealControlMeetingsMeetingIdStatusPutRequest(object):
    """会中状态设置

    **描述**：设置会议中的会议属性，例如：全体静音、是否允许参会者聊天设置、锁定会议、隐藏会议号和密码、是否开启等候室等，具体设置内容可以查询接口协议，目前暂不支持 MRA 设备作为被操作者的情况。企业 secret 鉴权用户可管理任何该企业该用户创建的有效会议，OAuth2.0 鉴权用户只能管理通过 OAuth2.0 鉴权创建的有效会议。  *  > 说明 > 1：操作者必须是会议的主持人或者联席主持人才可以设置。 > 2：调用该接口需要权限项 ：MANAGE_MEETING 查看和管理您的会议。
    
    :param meeting_id: (required)
    :type meeting_id: str

    :param body:
    :type body: V1RealControlMeetingsMeetingIdStatusPutRequest
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        body: Optional[V1RealControlMeetingsMeetingIdStatusPutRequest] = None
    ):
        self.meeting_id = meeting_id
        self.body = body

class ApiV1RealControlMeetingsMeetingIdStatusPutResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1RealControlMeetingsMeetingIdVideoPutRequest(object):
    """关闭或开启用户视频

    关闭指定用户视频，支持关闭或开启 MRA 设备的视频。 企业 secret 鉴权用户可管理任何该企业该用户创建的有效会议，OAuth2.0 鉴权用户只能管理通过 OAuth2.0 鉴权创建的有效会议。 > 说明 > 1：操作者必须是会议的主持人或者联席主持人才可以设置。 > 2：使用 OAuth 2.0 鉴权方式时，调用该接口需要权限项：MANAGE_MEETING 查看和管理您的会议。
    
    :param meeting_id: (required)
    :type meeting_id: str

    :param body:
    :type body: V1RealControlMeetingsMeetingIdVideoPutRequest
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        body: Optional[V1RealControlMeetingsMeetingIdVideoPutRequest] = None
    ):
        self.meeting_id = meeting_id
        self.body = body

class ApiV1RealControlMeetingsMeetingIdVideoPutResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1RealControlMeetingsMeetingIdWaitingRoomPutRequest(object):
    """用户等候室设置

    会议等候室设置，允许主持人将等候室成员移入会议、主持人将会议成员移入等候室、主持人将等候室成员移出等候室等操作，目前暂不支持 MRA 设备作为被操作者的情况。企业 secret 鉴权用户可管理任何该企业该用户创建的有效会议，OAuth2.0 鉴权用户只能管理通过 OAuth2.0 鉴权创建的有效会议。 > 说明 > 1：操作者必须是会议的主持人或者联席主持人才可以设置。 > 2：调用该接口需要权限项：MANAGE_MEETING 查看和管理您的会议
    
    :param meeting_id: (required)
    :type meeting_id: str

    :param body:
    :type body: V1RealControlMeetingsMeetingIdWaitingRoomPutRequest
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        body: Optional[V1RealControlMeetingsMeetingIdWaitingRoomPutRequest] = None
    ):
        self.meeting_id = meeting_id
        self.body = body

class ApiV1RealControlMeetingsMeetingIdWaitingRoomPutResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class MeetingControlApi:
    def __init__(self, config: Config):
        self.__config = config

    def v1_meetings_meeting_id_dismiss_post(
        self,
        request: ApiV1MeetingsMeetingIdDismissPostRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingsMeetingIdDismissPostResponse:
        """v1_meetings_meeting_id_dismiss_post 结束会议[/v1/meetings/{meeting_id}/dismiss - POST]

            **描述**：结束一个进行中的会议。  * 只有会议创建者、主持人、联席主持人可以结束会议，且该会议是一个有效的进行中会议。 * 结束周期性会议需要传入主会议 ID。 * 企业 secret 鉴权用户可结束任何该企业该用户创建的进行中的会议，OAuth 2.0鉴权用户只能结束通过 OAuth 2.0鉴权创建的进行中的会议。 * 当您想实时监测会议结束状况时，您可以通过订阅 [会议结束](https://cloud.tencent.com/document/product/1095/51619) 的事件，接收事件通知。 * 此接口暂不支持 MRA 设备作为被操作者的情况。 * 结束会议不会释放 Rooms，如需释放请调用 [释放会议室（Rooms）](https://cloud.tencent.com/document/product/1095/55314) 接口
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meetings/{meeting_id}/dismiss",
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
                response = ApiV1MeetingsMeetingIdDismissPostResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_real_control_meetings_meeting_id_asr_put(
        self,
        request: ApiV1RealControlMeetingsMeetingIdAsrPutRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1RealControlMeetingsMeetingIdAsrPutResponse:
        """v1_real_control_meetings_meeting_id_asr_put 开启或关闭实时转写[/v1/real-control/meetings/{meeting_id}/asr - PUT]

            以创建者的身份开启/关闭会中实时转写，调用时需要会议处于进行中的状态；
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/real-control/meetings/{meeting_id}/asr",
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
                response = ApiV1RealControlMeetingsMeetingIdAsrPutResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1RealControlMeetingsMeetingIdAsrPut200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_real_control_meetings_meeting_id_cohosts_put(
        self,
        request: ApiV1RealControlMeetingsMeetingIdCohostsPutRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1RealControlMeetingsMeetingIdCohostsPutResponse:
        """v1_real_control_meetings_meeting_id_cohosts_put 设置联席主持人[/v1/real-control/meetings/{meeting_id}/cohosts - PUT]

            **描述**：设置或撤销会议中的参会者联席主持人身份，目前暂不支持 MRA 设备作为被操作者的情况。企业 secret 鉴权用户可管理任何该企业该用户创建的有效会议，OAuth2.0 鉴权用户只能管理通过 OAuth2.0 鉴权创建的有效会议。  *  > 说明 >  >  > * 操作者必须是会议的主持人才可以设置。 > * 调用该接口需要权限项 ： MANAGE_MEETING 查看和管理您的会议。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/real-control/meetings/{meeting_id}/cohosts",
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
                response = ApiV1RealControlMeetingsMeetingIdCohostsPutResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_real_control_meetings_meeting_id_doc_put(
        self,
        request: ApiV1RealControlMeetingsMeetingIdDocPutRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1RealControlMeetingsMeetingIdDocPutResponse:
        """v1_real_control_meetings_meeting_id_doc_put 文档上传权限设置[/v1/real-control/meetings/{meeting_id}/doc - PUT]

            **描述**：设置会议中文档上传权限，目前暂不支持 MRA 设备作为被操作者的情况，企业 secret 鉴权用户可管理任何该企业该用户创建的有效会议，OAuth2.0 鉴权用户只能管理通过 OAuth2.0 鉴权创建的有效会议。  *  > 说明 > 1：操作者必须是会议的主持人或者联席主持人才可以设置。 > 2：调用该接口需要权限项：MANAGE_MEETING 查看和管理您的会议
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/real-control/meetings/{meeting_id}/doc",
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
                response = ApiV1RealControlMeetingsMeetingIdDocPutResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_real_control_meetings_meeting_id_kickout_put(
        self,
        request: ApiV1RealControlMeetingsMeetingIdKickoutPutRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1RealControlMeetingsMeetingIdKickoutPutResponse:
        """v1_real_control_meetings_meeting_id_kickout_put 移出用户[/v1/real-control/meetings/{meeting_id}/kickout - PUT]

            **描述**：  * 将会议中用户移出会议，操作者必须是会议的主持人或者联席主持人才可以设置。 * 支持对云会议已入会成员和 Webinar 观众移出。 * 支持 MRA 设备和 PSTN 设备为被操作者时的移出用户操作。 * 企业 secret 鉴权用户可管理任何该企业该用户创建的有效会议，OAuth2.0 鉴权用户只能管理通过 OAuth2.0 鉴权创建的有效会议。  说明  *  > 1：操作者必须是会议的主持人或者联席主持人才可以设置。 > 2：调用该接口需要权限项：MANAGE_MEETING 查看和管理您的会议。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/real-control/meetings/{meeting_id}/kickout",
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
                response = ApiV1RealControlMeetingsMeetingIdKickoutPutResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_real_control_meetings_meeting_id_mutes_put(
        self,
        request: ApiV1RealControlMeetingsMeetingIdMutesPutRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1RealControlMeetingsMeetingIdMutesPutResponse:
        """v1_real_control_meetings_meeting_id_mutes_put 静音用户[/v1/real-control/meetings/{meeting_id}/mutes - PUT]

            **描述**：  * 会议中用户静音操作，操作者必须是会议的主持人或者联席主持人才可以设置。 * 支持对云会议已入会成员和 Webinar 观众静音。 * 支持 MRA 设备和 PSTN 设备作为被操作者时的静音操作。 * 企业 secret 鉴权用户可管理任何该企业该用户创建的有效会议，OAuth2.0 鉴权用户只能管理通过 OAuth2.0 鉴权创建的有效会议。  说明 1：操作者必须是会议的主持人或者联席主持人才可以设置。 2：调用该接口需要权限项：MANAGE_MEETING 查看和管理您的会议。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/real-control/meetings/{meeting_id}/mutes",
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
                response = ApiV1RealControlMeetingsMeetingIdMutesPutResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_real_control_meetings_meeting_id_names_put(
        self,
        request: ApiV1RealControlMeetingsMeetingIdNamesPutRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1RealControlMeetingsMeetingIdNamesPutResponse:
        """v1_real_control_meetings_meeting_id_names_put 更改会中成员昵称[/v1/real-control/meetings/{meeting_id}/names - PUT]

            **描述：**  * 会中修改参会者昵称，支持主持人和联席主持人对会中成员进行改名。 * 此接口支持对云会议已入会成员和 Webinar 观众进行改名。 * 操作者必须为已在会中的主持人与联席主持人。 * 支持 MRA 设备和 PSTN 设备作为被操作者时的改名操作。 * 企业 secret 鉴权用户可管理任何该企业该用户创建的有效会议，OAuth2.0 鉴权用户只能管理通过 OAuth2.0 鉴权创建的有效会议。  说明 1：操作者必须是会议的主持人或者联席主持人才可以设置。 2：调用该接口需要权限项：MANAGE_MEETING 查看和管理您的会议。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/real-control/meetings/{meeting_id}/names",
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
                response = ApiV1RealControlMeetingsMeetingIdNamesPutResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_real_control_meetings_meeting_id_screen_shared_put(
        self,
        request: ApiV1RealControlMeetingsMeetingIdScreenSharedPutRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1RealControlMeetingsMeetingIdScreenSharedPutResponse:
        """v1_real_control_meetings_meeting_id_screen_shared_put 关闭用户屏幕共享[/v1/real-control/meetings/{meeting_id}/screen-shared - PUT]

            **描述**：关闭会议中用户屏幕共享权限，目前暂不支持 MRA 设备作为被操作者的情况。企业 secret 鉴权用户可管理任何该企业该用户创建的有效会议，OAuth2.0 鉴权用户只能管理通过 OAuth2.0 鉴权创建的有效会议。  *  > 说明 > 1：操作者必须是会议的主持人或者联席主持人才可以设置。 > 2：调用该接口需要权限项：MANAGE_MEETING 查看和管理您的会议
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/real-control/meetings/{meeting_id}/screen-shared",
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
                response = ApiV1RealControlMeetingsMeetingIdScreenSharedPutResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_real_control_meetings_meeting_id_status_put(
        self,
        request: ApiV1RealControlMeetingsMeetingIdStatusPutRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1RealControlMeetingsMeetingIdStatusPutResponse:
        """v1_real_control_meetings_meeting_id_status_put 会中状态设置[/v1/real-control/meetings/{meeting_id}/status - PUT]

            **描述**：设置会议中的会议属性，例如：全体静音、是否允许参会者聊天设置、锁定会议、隐藏会议号和密码、是否开启等候室等，具体设置内容可以查询接口协议，目前暂不支持 MRA 设备作为被操作者的情况。企业 secret 鉴权用户可管理任何该企业该用户创建的有效会议，OAuth2.0 鉴权用户只能管理通过 OAuth2.0 鉴权创建的有效会议。  *  > 说明 > 1：操作者必须是会议的主持人或者联席主持人才可以设置。 > 2：调用该接口需要权限项 ：MANAGE_MEETING 查看和管理您的会议。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/real-control/meetings/{meeting_id}/status",
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
                response = ApiV1RealControlMeetingsMeetingIdStatusPutResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_real_control_meetings_meeting_id_video_put(
        self,
        request: ApiV1RealControlMeetingsMeetingIdVideoPutRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1RealControlMeetingsMeetingIdVideoPutResponse:
        """v1_real_control_meetings_meeting_id_video_put 关闭或开启用户视频[/v1/real-control/meetings/{meeting_id}/video - PUT]

            关闭指定用户视频，支持关闭或开启 MRA 设备的视频。 企业 secret 鉴权用户可管理任何该企业该用户创建的有效会议，OAuth2.0 鉴权用户只能管理通过 OAuth2.0 鉴权创建的有效会议。 > 说明 > 1：操作者必须是会议的主持人或者联席主持人才可以设置。 > 2：使用 OAuth 2.0 鉴权方式时，调用该接口需要权限项：MANAGE_MEETING 查看和管理您的会议。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/real-control/meetings/{meeting_id}/video",
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
                response = ApiV1RealControlMeetingsMeetingIdVideoPutResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_real_control_meetings_meeting_id_waiting_room_put(
        self,
        request: ApiV1RealControlMeetingsMeetingIdWaitingRoomPutRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1RealControlMeetingsMeetingIdWaitingRoomPutResponse:
        """v1_real_control_meetings_meeting_id_waiting_room_put 用户等候室设置[/v1/real-control/meetings/{meeting_id}/waiting-room - PUT]

            会议等候室设置，允许主持人将等候室成员移入会议、主持人将会议成员移入等候室、主持人将等候室成员移出等候室等操作，目前暂不支持 MRA 设备作为被操作者的情况。企业 secret 鉴权用户可管理任何该企业该用户创建的有效会议，OAuth2.0 鉴权用户只能管理通过 OAuth2.0 鉴权创建的有效会议。 > 说明 > 1：操作者必须是会议的主持人或者联席主持人才可以设置。 > 2：调用该接口需要权限项：MANAGE_MEETING 查看和管理您的会议
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/real-control/meetings/{meeting_id}/waiting-room",
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
                response = ApiV1RealControlMeetingsMeetingIdWaitingRoomPutResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

