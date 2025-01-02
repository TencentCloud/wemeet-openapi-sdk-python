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
from wemeet_openapi.service.meeting_room.model import *

from requests_toolbelt import MultipartEncoder


class ApiV1DevicesGetRequest(object):
    """查询设备列表

    查询企业下的可用设备列表。<span class=\"colour\" style=\"color:rgb(51, 51, 51)\">目前暂不支持 OAuth2.0 鉴权访问。</span>
    
    :param page: 页码，从1开始，默认1。
    :type page: str

    :param page_size: 分页大小，从1开始，最大50，默认20。
    :type page_size: str

    :param meeting_room_name: 会议室名称
    :type meeting_room_name: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        page: Optional[str] = None,
        page_size: Optional[str] = None,
        meeting_room_name: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.page = page
        self.page_size = page_size
        self.meeting_room_name = meeting_room_name
        self.body = body

class ApiV1DevicesGetResponse(ApiResponse):
    data: Optional[V1DevicesGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1DevicesGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingRoomsCancelRoomCallPutRequest(object):
    """取消呼叫会议室

    **描述**：会议可以通过会议室 ID 进行取消呼叫操作。  * \\*\\*权限：\\*\\*同会议室呼叫权限。 * **调用方式**：PUT
    
    :param body:
    :type body: V1MeetingRoomsCancelRoomCallPutRequest
    """  # noqa: E501


    def __init__(
        self,
        body: Optional[V1MeetingRoomsCancelRoomCallPutRequest] = None
    ):
        self.body = body

class ApiV1MeetingRoomsCancelRoomCallPutResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingRoomsGetRequest(object):
    """查询会议室（Rooms）列表

    查询企业下的会议室列表。<span class=\"colour\" style=\"color:rgb(51, 51, 51)\">目前暂不支持 OAuth2.0 鉴权访问。</span>
    
    :param page: 页码
    :type page: str

    :param page_size: 分页大小
    :type page_size: str

    :param meeting_room_name: 会议室名称
    :type meeting_room_name: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        page: Optional[str] = None,
        page_size: Optional[str] = None,
        meeting_room_name: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.page = page
        self.page_size = page_size
        self.meeting_room_name = meeting_room_name
        self.body = body

class ApiV1MeetingRoomsGetResponse(ApiResponse):
    data: Optional[V1MeetingRoomsGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingRoomsGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingRoomsMeetingRoomIdActiveCodePostRequest(object):
    """生成设备激活码

    生成会议室中设备激活码。<span class=\"colour\" style=\"color:rgb(51, 51, 51)\">目前暂不支持 OAuth2.0 鉴权访问。</span>
    
    :param meeting_room_id: 会议室id (required)
    :type meeting_room_id: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        meeting_room_id: str,
        body: Optional[object] = None
    ):
        self.meeting_room_id = meeting_room_id
        self.body = body

class ApiV1MeetingRoomsMeetingRoomIdActiveCodePostResponse(ApiResponse):
    data: Optional[V1MeetingRoomsMeetingRoomIdActiveCodePost200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingRoomsMeetingRoomIdActiveCodePost200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingRoomsMeetingRoomIdBackgroundGetRequest(object):
    """查询会议室背景

    查询会议室的会议室背景
    
    :param meeting_room_id: (required)
    :type meeting_room_id: str

    :param operator_id: (required)
    :type operator_id: str

    :param operator_id_type: 1:userid (required)
    :type operator_id_type: str
    """  # noqa: E501


    def __init__(
        self,
        meeting_room_id: str,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None
    ):
        self.meeting_room_id = meeting_room_id
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type

class ApiV1MeetingRoomsMeetingRoomIdBackgroundGetResponse(ApiResponse):
    data: Optional[V1MeetingRoomsMeetingRoomIdBackgroundGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingRoomsMeetingRoomIdBackgroundGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingRoomsMeetingRoomIdBackgroundPostRequest(object):
    """设置会议室背景

    为会议室设置会议室背景，支持为批量会议室设置。异步上传背景，需要订阅素材上传结果通知。
    
    :param meeting_room_id: (required)
    :type meeting_room_id: str

    :param body:
    :type body: V1MeetingRoomsMeetingRoomIdBackgroundPostRequest
    """  # noqa: E501


    def __init__(
        self,
        meeting_room_id: str,
        body: Optional[V1MeetingRoomsMeetingRoomIdBackgroundPostRequest] = None
    ):
        self.meeting_room_id = meeting_room_id
        self.body = body

class ApiV1MeetingRoomsMeetingRoomIdBackgroundPostResponse(ApiResponse):
    data: Optional[V1MeetingRoomsMeetingRoomIdBackgroundPost200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingRoomsMeetingRoomIdBackgroundPost200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingRoomsMeetingRoomIdGetRequest(object):
    """查询会议室（Rooms）详情

    根据会议室 ID 查询该会议室详细信息。<span class=\"colour\" style=\"color:rgb(51, 51, 51)\">目前暂不支持 OAuth2.0 鉴权访问。</span>
    
    :param meeting_room_id: 会议室ID (required)
    :type meeting_room_id: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        meeting_room_id: str,
        body: Optional[object] = None
    ):
        self.meeting_room_id = meeting_room_id
        self.body = body

class ApiV1MeetingRoomsMeetingRoomIdGetResponse(ApiResponse):
    data: Optional[V1MeetingRoomsMeetingRoomIdGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingRoomsMeetingRoomIdGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingRoomsModifyPutRequest(object):
    """修改会议室信息

    **描述**：对会议室信息进行设置。  * \\*\\*权限：\\*\\*支持 JWT 鉴权，拥有会议室管理编辑权限。暂不支持 OAuth 2\\.0鉴权。 * **调用方式**：PUT
    
    :param body:
    :type body: V1MeetingRoomsModifyPutRequest
    """  # noqa: E501


    def __init__(
        self,
        body: Optional[V1MeetingRoomsModifyPutRequest] = None
    ):
        self.body = body

class ApiV1MeetingRoomsModifyPutResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingRoomsModifyRoomConfigInfoPostRequest(object):
    """修改会议室配置项

    **描述**：修改会议室各种配置项。  * \\*\\*权限：\\*\\*JWT 鉴权，拥有会议室管理编辑权限，暂不支持 OAuth 2\\.0鉴权。 * **调用方式**：POST
    
    :param body:
    :type body: V1MeetingRoomsModifyRoomConfigInfoPostRequest
    """  # noqa: E501


    def __init__(
        self,
        body: Optional[V1MeetingRoomsModifyRoomConfigInfoPostRequest] = None
    ):
        self.body = body

class ApiV1MeetingRoomsModifyRoomConfigInfoPostResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingRoomsMonitorDeviceControllerInfoGetRequest(object):
    """查询控制器列表

    \\*\\*描述：\\*\\*查询企业下的控制器列表，目前暂不支持 OAuth2\\.0 鉴权访问。
    
    :param controller_name: 需要查询的设备名称（支持模糊匹配查找），如需获取全量列表，则不需要传入。
    :type controller_name: str

    :param page: 页码，从1开始，默认1。
    :type page: str

    :param page_size: 分页大小，从1开始，最大50，默认20。
    :type page_size: str
    """  # noqa: E501


    def __init__(
        self,
        controller_name: Optional[str] = None,
        page: Optional[str] = None,
        page_size: Optional[str] = None
    ):
        self.controller_name = controller_name
        self.page = page
        self.page_size = page_size

class ApiV1MeetingRoomsMonitorDeviceControllerInfoGetResponse(ApiResponse):
    data: Optional[V1MeetingRoomsMonitorDeviceControllerInfoGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingRoomsMonitorDeviceControllerInfoGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingRoomsOperatorIdMeetingsGetRequest(object):
    """查询会议室（Rooms）下的会议列表

    <span class=\"colour\" style=\"color:rgb(51, 51, 51)\">查询指定会议室（Rooms）下的会议列表，目前暂不支持 OAuth2.0 鉴权访问。</span>
    
    :param operator_id: (required)
    :type operator_id: str

    :param operator_id_type: 操作者 ID 的类型： 3. rooms 设备 rooms_id 5. 会议室ID meeting_room_id (required)
    :type operator_id_type: str

    :param instanceid: 用户的终端设备类型： 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch Mac 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch Iphone (required)
    :type instanceid: str

    :param start_time: Unix 时间戳。查询起始时间，时间区间不超过90天。
    :type start_time: str

    :param end_time: Unix 时间戳。查询结束时间，时间区间不超过90天。
    :type end_time: str

    :param page: 当前页，页码起始值为1，默认为1。
    :type page: str

    :param page_size: 分页大小，默认20条，最大20条。
    :type page_size: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        operator_id: str,
        operator_id_type: Optional[str] = None,
        instanceid: Optional[str] = None,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        page: Optional[str] = None,
        page_size: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.instanceid = instanceid
        self.start_time = start_time
        self.end_time = end_time
        self.page = page
        self.page_size = page_size
        self.body = body

class ApiV1MeetingRoomsOperatorIdMeetingsGetResponse(ApiResponse):
    data: Optional[V1MeetingRoomsOperatorIdMeetingsGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingRoomsOperatorIdMeetingsGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingRoomsRoomCallInfoPostRequest(object):
    """查询会议室应答状态

    **描述**：一个会议可以查询它所呼叫的会议室对其的应答状态。  * \\*\\*权限：\\*\\*同会议室呼叫权限。 * **调用方式**：POST
    
    :param body:
    :type body: V1MeetingRoomsRoomCallInfoPostRequest
    """  # noqa: E501


    def __init__(
        self,
        body: Optional[V1MeetingRoomsRoomCallInfoPostRequest] = None
    ):
        self.body = body

class ApiV1MeetingRoomsRoomCallInfoPostResponse(ApiResponse):
    data: Optional[V1MeetingRoomsRoomCallInfoPost200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingRoomsRoomCallInfoPost200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingRoomsRoomCallPutRequest(object):
    """呼叫会议室

    **描述**：会议可以通过会议室 ID 呼叫会议室邀请其入会。  * \\*\\*权限：\\*\\*支持 JWT 鉴权，会议创建者所在企业的管理员和会议参会者可呼叫与自己同企业下的会议室入会，若使用会议室呼叫地址，需主持人或联席主持人身份，暂不支持 OAuth 2\\.0鉴权。 * **调用方式**：PUT
    
    :param body:
    :type body: V1MeetingRoomsRoomCallPutRequest
    """  # noqa: E501


    def __init__(
        self,
        body: Optional[V1MeetingRoomsRoomCallPutRequest] = None
    ):
        self.body = body

class ApiV1MeetingRoomsRoomCallPutResponse(ApiResponse):
    data: Optional[V1MeetingRoomsRoomCallPut200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingRoomsRoomCallPut200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingRoomsRoomConfigInfoPostRequest(object):
    """查询会议室配置项

    **描述**：查询会议室的配置项。  * \\*\\*权限：\\*\\*JWT 鉴权，拥有会议室查看权限，暂不支持 OAuth 2\\.0鉴权。 * **调用方式**：POST
    
    :param body:
    :type body: V1MeetingRoomsRoomConfigInfoPostRequest
    """  # noqa: E501


    def __init__(
        self,
        body: Optional[V1MeetingRoomsRoomConfigInfoPostRequest] = None
    ):
        self.body = body

class ApiV1MeetingRoomsRoomConfigInfoPostResponse(ApiResponse):
    data: Optional[V1MeetingRoomsRoomConfigInfoPost200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingRoomsRoomConfigInfoPost200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingRoomsScreencastCodeRoomsInfoGetRequest(object):
    """通过投屏码查询会议室信息

    
    :param screencast_code: 投屏码 (required)
    :type screencast_code: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        screencast_code: str,
        body: Optional[object] = None
    ):
        self.screencast_code = screencast_code
        self.body = body

class ApiV1MeetingRoomsScreencastCodeRoomsInfoGetResponse(ApiResponse):
    data: Optional[V1MeetingRoomsScreencastCodeRoomsInfoGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingRoomsScreencastCodeRoomsInfoGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingsMeetingIdBookRoomsPostRequest(object):
    """预定会议室（Rooms）

    对成功预定的会议添加会议室，支持多个会议室预定。说明：会议室预定对会议时长有硬性要求，会议时长不得小于15分钟且不得大于24小时；不支持周期性会议。）  * 通过会议 ID 预定会议室。 * 目前暂不支持 OAuth2.0 鉴权访问。
    
    :param meeting_id: 会议唯一id (required)
    :type meeting_id: str

    :param body:
    :type body: V1MeetingsMeetingIdBookRoomsPostRequest
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        body: Optional[V1MeetingsMeetingIdBookRoomsPostRequest] = None
    ):
        self.meeting_id = meeting_id
        self.body = body

class ApiV1MeetingsMeetingIdBookRoomsPostResponse(ApiResponse):
    data: Optional[V1MeetingsMeetingIdBookRoomsPost200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingsMeetingIdBookRoomsPost200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingsMeetingIdReleaseRoomsPostRequest(object):
    """释放会议室（Rooms）

    通过会议 ID 释放会议室，支持多个会议室释放。<span class=\"colour\" style=\"color:rgb(51, 51, 51)\">目前暂不支持 OAuth2.0 鉴权访问。</span>
    
    :param meeting_id: 会议唯一id (required)
    :type meeting_id: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        body: Optional[object] = None
    ):
        self.meeting_id = meeting_id
        self.body = body

class ApiV1MeetingsMeetingIdReleaseRoomsPostResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1RoomsInventoryAccountStatisticsGetRequest(object):
    """查询账号类型资源使用统计

    查询 Rooms 账号资源使用情况，暂不支持 OAuth 2.0鉴权访问。
    
    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        body: Optional[object] = None
    ):
        self.body = body

class ApiV1RoomsInventoryAccountStatisticsGetResponse(ApiResponse):
    data: Optional[V1RoomsInventoryAccountStatisticsGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1RoomsInventoryAccountStatisticsGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1RoomsInventoryGetRequest(object):
    """查询账户下 Rooms 资源

    查询企业购买的 Rooms 资源。<span class=\"colour\" style=\"color: rgb(51, 51, 51);\">目前暂不支持 OAuth2.0 鉴权访问。</span>
        """  # noqa: E501


class ApiV1RoomsInventoryGetResponse(ApiResponse):
    data: Optional[V1RoomsInventoryGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1RoomsInventoryGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class MeetingRoomApi:
    def __init__(self, config: Config):
        self.__config = config

    def v1_devices_get(
        self,
        request: ApiV1DevicesGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1DevicesGetResponse:
        """v1_devices_get 查询设备列表[/v1/devices - GET]

            查询企业下的可用设备列表。<span class=\"colour\" style=\"color:rgb(51, 51, 51)\">目前暂不支持 OAuth2.0 鉴权访问。</span>
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/devices",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # path 参数
            # query 参数
            if request.page is not None:
                api_req.query_params.append(('page', request.page))
            if request.page_size is not None:
                api_req.query_params.append(('page_size', request.page_size))
            if request.meeting_room_name is not None:
                api_req.query_params.append(('meeting_room_name', request.meeting_room_name))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1DevicesGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1DevicesGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meeting_rooms_cancel_room_call_put(
        self,
        request: ApiV1MeetingRoomsCancelRoomCallPutRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingRoomsCancelRoomCallPutResponse:
        """v1_meeting_rooms_cancel_room_call_put 取消呼叫会议室[/v1/meeting-rooms/cancel-room-call - PUT]

            **描述**：会议可以通过会议室 ID 进行取消呼叫操作。  * \\*\\*权限：\\*\\*同会议室呼叫权限。 * **调用方式**：PUT
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meeting-rooms/cancel-room-call",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # path 参数
            # query 参数
            # 发送请求
            api_resp = self.__config.clt.put(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1MeetingRoomsCancelRoomCallPutResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meeting_rooms_get(
        self,
        request: ApiV1MeetingRoomsGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingRoomsGetResponse:
        """v1_meeting_rooms_get 查询会议室（Rooms）列表[/v1/meeting-rooms - GET]

            查询企业下的会议室列表。<span class=\"colour\" style=\"color:rgb(51, 51, 51)\">目前暂不支持 OAuth2.0 鉴权访问。</span>
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meeting-rooms",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # path 参数
            # query 参数
            if request.page is not None:
                api_req.query_params.append(('page', request.page))
            if request.page_size is not None:
                api_req.query_params.append(('page_size', request.page_size))
            if request.meeting_room_name is not None:
                api_req.query_params.append(('meeting_room_name', request.meeting_room_name))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1MeetingRoomsGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingRoomsGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meeting_rooms_meeting_room_id_active_code_post(
        self,
        request: ApiV1MeetingRoomsMeetingRoomIdActiveCodePostRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingRoomsMeetingRoomIdActiveCodePostResponse:
        """v1_meeting_rooms_meeting_room_id_active_code_post 生成设备激活码[/v1/meeting-rooms/{meeting_room_id}/active-code - POST]

            生成会议室中设备激活码。<span class=\"colour\" style=\"color:rgb(51, 51, 51)\">目前暂不支持 OAuth2.0 鉴权访问。</span>
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meeting-rooms/{meeting_room_id}/active-code",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'meeting_room_id' is set
            if request.meeting_room_id is None:
                raise Exception("meeting_room_id is required and must be specified")
            # path 参数
            if request.meeting_room_id is not None:
                api_req.path_params['meeting_room_id'] = request.meeting_room_id
            # query 参数
            # 发送请求
            api_resp = self.__config.clt.post(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1MeetingRoomsMeetingRoomIdActiveCodePostResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingRoomsMeetingRoomIdActiveCodePost200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meeting_rooms_meeting_room_id_background_get(
        self,
        request: ApiV1MeetingRoomsMeetingRoomIdBackgroundGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingRoomsMeetingRoomIdBackgroundGetResponse:
        """v1_meeting_rooms_meeting_room_id_background_get 查询会议室背景[/v1/meeting-rooms/{meeting_room_id}/background - GET]

            查询会议室的会议室背景
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meeting-rooms/{meeting_room_id}/background",
                                 authenticators=authenticators,
                                 header=header, 
                                 serializer=serializer)

            # verify the required parameter 'meeting_room_id' is set
            if request.meeting_room_id is None:
                raise Exception("meeting_room_id is required and must be specified")
            # verify the required parameter 'operator_id' is set
            if request.operator_id is None:
                raise Exception("operator_id is required and must be specified")
            # verify the required parameter 'operator_id_type' is set
            if request.operator_id_type is None:
                raise Exception("operator_id_type is required and must be specified")
            # path 参数
            if request.meeting_room_id is not None:
                api_req.path_params['meeting_room_id'] = request.meeting_room_id
            # query 参数
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1MeetingRoomsMeetingRoomIdBackgroundGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingRoomsMeetingRoomIdBackgroundGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meeting_rooms_meeting_room_id_background_post(
        self,
        request: ApiV1MeetingRoomsMeetingRoomIdBackgroundPostRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingRoomsMeetingRoomIdBackgroundPostResponse:
        """v1_meeting_rooms_meeting_room_id_background_post 设置会议室背景[/v1/meeting-rooms/{meeting_room_id}/background - POST]

            为会议室设置会议室背景，支持为批量会议室设置。异步上传背景，需要订阅素材上传结果通知。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meeting-rooms/{meeting_room_id}/background",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'meeting_room_id' is set
            if request.meeting_room_id is None:
                raise Exception("meeting_room_id is required and must be specified")
            # path 参数
            if request.meeting_room_id is not None:
                api_req.path_params['meeting_room_id'] = request.meeting_room_id
            # query 参数
            # 发送请求
            api_resp = self.__config.clt.post(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1MeetingRoomsMeetingRoomIdBackgroundPostResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingRoomsMeetingRoomIdBackgroundPost200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meeting_rooms_meeting_room_id_get(
        self,
        request: ApiV1MeetingRoomsMeetingRoomIdGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingRoomsMeetingRoomIdGetResponse:
        """v1_meeting_rooms_meeting_room_id_get 查询会议室（Rooms）详情[/v1/meeting-rooms/{meeting_room_id} - GET]

            根据会议室 ID 查询该会议室详细信息。<span class=\"colour\" style=\"color:rgb(51, 51, 51)\">目前暂不支持 OAuth2.0 鉴权访问。</span>
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meeting-rooms/{meeting_room_id}",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'meeting_room_id' is set
            if request.meeting_room_id is None:
                raise Exception("meeting_room_id is required and must be specified")
            # path 参数
            if request.meeting_room_id is not None:
                api_req.path_params['meeting_room_id'] = request.meeting_room_id
            # query 参数
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1MeetingRoomsMeetingRoomIdGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingRoomsMeetingRoomIdGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meeting_rooms_modify_put(
        self,
        request: ApiV1MeetingRoomsModifyPutRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingRoomsModifyPutResponse:
        """v1_meeting_rooms_modify_put 修改会议室信息[/v1/meeting-rooms/modify - PUT]

            **描述**：对会议室信息进行设置。  * \\*\\*权限：\\*\\*支持 JWT 鉴权，拥有会议室管理编辑权限。暂不支持 OAuth 2\\.0鉴权。 * **调用方式**：PUT
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meeting-rooms/modify",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # path 参数
            # query 参数
            # 发送请求
            api_resp = self.__config.clt.put(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1MeetingRoomsModifyPutResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meeting_rooms_modify_room_config_info_post(
        self,
        request: ApiV1MeetingRoomsModifyRoomConfigInfoPostRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingRoomsModifyRoomConfigInfoPostResponse:
        """v1_meeting_rooms_modify_room_config_info_post 修改会议室配置项[/v1/meeting-rooms/modify-room-config-info - POST]

            **描述**：修改会议室各种配置项。  * \\*\\*权限：\\*\\*JWT 鉴权，拥有会议室管理编辑权限，暂不支持 OAuth 2\\.0鉴权。 * **调用方式**：POST
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meeting-rooms/modify-room-config-info",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # path 参数
            # query 参数
            # 发送请求
            api_resp = self.__config.clt.post(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1MeetingRoomsModifyRoomConfigInfoPostResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meeting_rooms_monitor_device_controller_info_get(
        self,
        request: ApiV1MeetingRoomsMonitorDeviceControllerInfoGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingRoomsMonitorDeviceControllerInfoGetResponse:
        """v1_meeting_rooms_monitor_device_controller_info_get 查询控制器列表[/v1/meeting-rooms-monitor/device-controller-info - GET]

            \\*\\*描述：\\*\\*查询企业下的控制器列表，目前暂不支持 OAuth2\\.0 鉴权访问。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meeting-rooms-monitor/device-controller-info",
                                 authenticators=authenticators,
                                 header=header, 
                                 serializer=serializer)

            # path 参数
            # query 参数
            if request.controller_name is not None:
                api_req.query_params.append(('controller_name', request.controller_name))
            if request.page is not None:
                api_req.query_params.append(('page', request.page))
            if request.page_size is not None:
                api_req.query_params.append(('page_size', request.page_size))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1MeetingRoomsMonitorDeviceControllerInfoGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingRoomsMonitorDeviceControllerInfoGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meeting_rooms_operator_id_meetings_get(
        self,
        request: ApiV1MeetingRoomsOperatorIdMeetingsGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingRoomsOperatorIdMeetingsGetResponse:
        """v1_meeting_rooms_operator_id_meetings_get 查询会议室（Rooms）下的会议列表[/v1/meeting-rooms/{operator_id}/meetings - GET]

            <span class=\"colour\" style=\"color:rgb(51, 51, 51)\">查询指定会议室（Rooms）下的会议列表，目前暂不支持 OAuth2.0 鉴权访问。</span>
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meeting-rooms/{operator_id}/meetings",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'operator_id' is set
            if request.operator_id is None:
                raise Exception("operator_id is required and must be specified")
            # verify the required parameter 'operator_id_type' is set
            if request.operator_id_type is None:
                raise Exception("operator_id_type is required and must be specified")
            # verify the required parameter 'instanceid' is set
            if request.instanceid is None:
                raise Exception("instanceid is required and must be specified")
            # path 参数
            if request.operator_id is not None:
                api_req.path_params['operator_id'] = request.operator_id
            # query 参数
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            if request.instanceid is not None:
                api_req.query_params.append(('instanceid', request.instanceid))
            if request.start_time is not None:
                api_req.query_params.append(('start_time', request.start_time))
            if request.end_time is not None:
                api_req.query_params.append(('end_time', request.end_time))
            if request.page is not None:
                api_req.query_params.append(('page', request.page))
            if request.page_size is not None:
                api_req.query_params.append(('page_size', request.page_size))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1MeetingRoomsOperatorIdMeetingsGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingRoomsOperatorIdMeetingsGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meeting_rooms_room_call_info_post(
        self,
        request: ApiV1MeetingRoomsRoomCallInfoPostRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingRoomsRoomCallInfoPostResponse:
        """v1_meeting_rooms_room_call_info_post 查询会议室应答状态[/v1/meeting-rooms/room-call-info - POST]

            **描述**：一个会议可以查询它所呼叫的会议室对其的应答状态。  * \\*\\*权限：\\*\\*同会议室呼叫权限。 * **调用方式**：POST
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meeting-rooms/room-call-info",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # path 参数
            # query 参数
            # 发送请求
            api_resp = self.__config.clt.post(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1MeetingRoomsRoomCallInfoPostResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingRoomsRoomCallInfoPost200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meeting_rooms_room_call_put(
        self,
        request: ApiV1MeetingRoomsRoomCallPutRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingRoomsRoomCallPutResponse:
        """v1_meeting_rooms_room_call_put 呼叫会议室[/v1/meeting-rooms/room-call - PUT]

            **描述**：会议可以通过会议室 ID 呼叫会议室邀请其入会。  * \\*\\*权限：\\*\\*支持 JWT 鉴权，会议创建者所在企业的管理员和会议参会者可呼叫与自己同企业下的会议室入会，若使用会议室呼叫地址，需主持人或联席主持人身份，暂不支持 OAuth 2\\.0鉴权。 * **调用方式**：PUT
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meeting-rooms/room-call",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # path 参数
            # query 参数
            # 发送请求
            api_resp = self.__config.clt.put(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1MeetingRoomsRoomCallPutResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingRoomsRoomCallPut200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meeting_rooms_room_config_info_post(
        self,
        request: ApiV1MeetingRoomsRoomConfigInfoPostRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingRoomsRoomConfigInfoPostResponse:
        """v1_meeting_rooms_room_config_info_post 查询会议室配置项[/v1/meeting-rooms/room-config-info - POST]

            **描述**：查询会议室的配置项。  * \\*\\*权限：\\*\\*JWT 鉴权，拥有会议室查看权限，暂不支持 OAuth 2\\.0鉴权。 * **调用方式**：POST
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meeting-rooms/room-config-info",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # path 参数
            # query 参数
            # 发送请求
            api_resp = self.__config.clt.post(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1MeetingRoomsRoomConfigInfoPostResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingRoomsRoomConfigInfoPost200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meeting_rooms_screencast_code_rooms_info_get(
        self,
        request: ApiV1MeetingRoomsScreencastCodeRoomsInfoGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingRoomsScreencastCodeRoomsInfoGetResponse:
        """v1_meeting_rooms_screencast_code_rooms_info_get 通过投屏码查询会议室信息[/v1/meeting-rooms/{screencast_code}/rooms-info - GET]

        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meeting-rooms/{screencast_code}/rooms-info",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'screencast_code' is set
            if request.screencast_code is None:
                raise Exception("screencast_code is required and must be specified")
            # path 参数
            if request.screencast_code is not None:
                api_req.path_params['screencast_code'] = request.screencast_code
            # query 参数
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1MeetingRoomsScreencastCodeRoomsInfoGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingRoomsScreencastCodeRoomsInfoGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meetings_meeting_id_book_rooms_post(
        self,
        request: ApiV1MeetingsMeetingIdBookRoomsPostRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingsMeetingIdBookRoomsPostResponse:
        """v1_meetings_meeting_id_book_rooms_post 预定会议室（Rooms）[/v1/meetings/{meeting_id}/book-rooms - POST]

            对成功预定的会议添加会议室，支持多个会议室预定。说明：会议室预定对会议时长有硬性要求，会议时长不得小于15分钟且不得大于24小时；不支持周期性会议。）  * 通过会议 ID 预定会议室。 * 目前暂不支持 OAuth2.0 鉴权访问。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meetings/{meeting_id}/book-rooms",
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
                response = ApiV1MeetingsMeetingIdBookRoomsPostResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingsMeetingIdBookRoomsPost200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meetings_meeting_id_release_rooms_post(
        self,
        request: ApiV1MeetingsMeetingIdReleaseRoomsPostRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingsMeetingIdReleaseRoomsPostResponse:
        """v1_meetings_meeting_id_release_rooms_post 释放会议室（Rooms）[/v1/meetings/{meeting_id}/release-rooms - POST]

            通过会议 ID 释放会议室，支持多个会议室释放。<span class=\"colour\" style=\"color:rgb(51, 51, 51)\">目前暂不支持 OAuth2.0 鉴权访问。</span>
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meetings/{meeting_id}/release-rooms",
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
                response = ApiV1MeetingsMeetingIdReleaseRoomsPostResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_rooms_inventory_account_statistics_get(
        self,
        request: ApiV1RoomsInventoryAccountStatisticsGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1RoomsInventoryAccountStatisticsGetResponse:
        """v1_rooms_inventory_account_statistics_get 查询账号类型资源使用统计[/v1/rooms-inventory/account-statistics - GET]

            查询 Rooms 账号资源使用情况，暂不支持 OAuth 2.0鉴权访问。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/rooms-inventory/account-statistics",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # path 参数
            # query 参数
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1RoomsInventoryAccountStatisticsGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1RoomsInventoryAccountStatisticsGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_rooms_inventory_get(
        self,
        request: ApiV1RoomsInventoryGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1RoomsInventoryGetResponse:
        """v1_rooms_inventory_get 查询账户下 Rooms 资源[/v1/rooms-inventory - GET]

            查询企业购买的 Rooms 资源。<span class=\"colour\" style=\"color: rgb(51, 51, 51);\">目前暂不支持 OAuth2.0 鉴权访问。</span>
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/rooms-inventory",
                                 authenticators=authenticators,
                                 header=header, 
                                 serializer=serializer)

            # path 参数
            # query 参数
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1RoomsInventoryGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1RoomsInventoryGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

