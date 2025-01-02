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
from wemeet_openapi.service.meetings.model import *

from requests_toolbelt import MultipartEncoder


class ApiV1AsrConfigPutRequest(object):
    """设置语音识别热词

    用户可以通过接口进行您创建的会议的语音识别设置。 权限点：查看或管理您的会议
    
    :param body:
    :type body: V1AsrConfigPutRequest
    """  # noqa: E501


    def __init__(
        self,
        body: Optional[V1AsrConfigPutRequest] = None
    ):
        self.body = body

class ApiV1AsrConfigPutResponse(ApiResponse):
    data: Optional[V1AsrConfigPut200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1AsrConfigPut200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1AsrDetailsGetRequest(object):
    """导出实时转写记录

    如果会议开启了会议转写，可以导出转写记录。主持人可以设置导出权限，默认主持人可以导出，支持会中和会后导出。
    
    :param operator_id_type: 操作者 ID 的类型： 1：userid  2：openid (required)
    :type operator_id_type: str

    :param operator_id: 操作者 ID。operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 (required)
    :type operator_id: str

    :param meeting_id: 可以查询某次会议的数据 (required)
    :type meeting_id: str

    :param start_time: 查询起始时间戳，UNIX 时间戳（单位秒）。
    :type start_time: str

    :param end_time: 查询结束时间戳，UNIX 时间戳（单位秒）。
    :type end_time: str

    :param file_type: 导出文件类型,默认导出txt  0：txt  1：word  2：pdf
    :type file_type: str

    :param page: 页码，默认1
    :type page: str

    :param page_size: 分页大小，默认10，最大50
    :type page_size: str

    :param show_bilingual: 是否展示双语，默认不展示双语
    :type show_bilingual: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        operator_id_type: Optional[str] = None,
        operator_id: Optional[str] = None,
        meeting_id: Optional[str] = None,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        file_type: Optional[str] = None,
        page: Optional[str] = None,
        page_size: Optional[str] = None,
        show_bilingual: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.operator_id_type = operator_id_type
        self.operator_id = operator_id
        self.meeting_id = meeting_id
        self.start_time = start_time
        self.end_time = end_time
        self.file_type = file_type
        self.page = page
        self.page_size = page_size
        self.show_bilingual = show_bilingual
        self.body = body

class ApiV1AsrDetailsGetResponse(ApiResponse):
    data: Optional[V1AsrDetailsGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1AsrDetailsGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1AsrPushStatusPostRequest(object):
    """开启/关闭实时转写推送

     会议创建者可开启本场会议的实时转写内容推送，待开始的会议或未打开实时转写功能的会议也支持开启推送，开启推送后如果会议打开转写，则可通过webhook 实时转写推送 实时获取到转写内容。 企业 secret 鉴权用户可开启该用户所属企业下的所有会议转写推送，OAuth2.0 鉴权用户只能开启通过 OAuth2.0 鉴权创建的会议转写推送。 企业级自建应用通过 webhook 可以接收到企业下所有开启推送的会议的转写内容，应用级自建应用通过 webhook 可以接收到本应用创建的会议的转写内容。OAuth2.0 应用通过 webhook 可以接收到 OAuth2.0 鉴权创建的会议的转写内容。 
    
    :param body:
    :type body: V1AsrPushStatusPostRequest
    """  # noqa: E501


    def __init__(
        self,
        body: Optional[V1AsrPushStatusPostRequest] = None
    ):
        self.body = body

class ApiV1AsrPushStatusPostResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1HistoryMeetingsUseridGetRequest(object):
    """查询用户已结束会议列表

    获取某指定用户的已结束的会议列表，可返回用户创建与参加过的已结束会议列表，支持 OAuth2.0 鉴权和企微鉴权。 请优先使用operator_id和operator_id_type查询，当使用operator_id和operator_id_type时，userid设置为operator_id的值即可
    
    :param userid: (required)
    :type userid: str

    :param page_size: 当前页大小，最小值为1，最大值为20。 (required)
    :type page_size: str

    :param page: 当前页，从1开始。 (required)
    :type page: str

    :param meeting_code: 会议号。
    :type meeting_code: str

    :param start_time: 搜索的开始时间（预定会议的开始时间），单位秒。
    :type start_time: str

    :param end_time: 搜索的结束时间（预定会议的开始时间），单位秒。
    :type end_time: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        userid: str,
        page_size: Optional[str] = None,
        page: Optional[str] = None,
        meeting_code: Optional[str] = None,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.userid = userid
        self.page_size = page_size
        self.page = page
        self.meeting_code = meeting_code
        self.start_time = start_time
        self.end_time = end_time
        self.body = body

class ApiV1HistoryMeetingsUseridGetResponse(ApiResponse):
    data: Optional[V1HistoryMeetingsUseridGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1HistoryMeetingsUseridGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingJobIdGetRequest(object):
    """获取导出 PSTN 通话详单任务结果

    获取异步导出任务的结果。
    
    :param job_id: 任务ID (required)
    :type job_id: str

    :param operator_id_type: 操作者 ID 的类型： 1：userid (required)
    :type operator_id_type: str

    :param operator_id: 操作者 ID。operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型 (required)
    :type operator_id: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        job_id: str,
        operator_id_type: Optional[str] = None,
        operator_id: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.job_id = job_id
        self.operator_id_type = operator_id_type
        self.operator_id = operator_id
        self.body = body

class ApiV1MeetingJobIdGetResponse(ApiResponse):
    data: Optional[V1MeetingJobIdGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingJobIdGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingMeetingIdWaitingRoomGetRequest(object):
    """查询等候室成员记录

    会议创建者、主持人、联席主持人可以查询等候室成员列表，包括等候室内所有用户的进出记录。会前、会中、会后都可以查询。 “查询等候室成员列表”改为“获取实时等候室成员列表”，只有当前等候室的成员。如果是PMI会议，返回的是PMI的meeting_code。 鉴权方式：JWT鉴权、OAuth鉴权、SDK鉴权 OAuth鉴权的权限为：查询会议、查询和管理会议
    
    :param meeting_id: 会议的唯一ID (required)
    :type meeting_id: str

    :param operator_id: 操作者 ID。会议创建者、主持人、联席主持人可以调用该接口。 operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 (required)
    :type operator_id: str

    :param operator_id_type: 操作者 ID 的类型： 1：企业内用户 userid。 2：企微或者oauth open_id (required)
    :type operator_id_type: str

    :param page: 当前页，页码起始值为1。page最大值为2000 (required)
    :type page: str

    :param page_size: 每页数据条数。默认20，最大50 (required)
    :type page_size: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        page: Optional[str] = None,
        page_size: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.meeting_id = meeting_id
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.page = page
        self.page_size = page_size
        self.body = body

class ApiV1MeetingMeetingIdWaitingRoomGetResponse(ApiResponse):
    data: Optional[V1MeetingMeetingIdWaitingRoomGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingMeetingIdWaitingRoomGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingMeetingIdWaitingRoomWelcomeMessageGetRequest(object):
    """获取等候室欢迎语

    查询会议的等候室欢迎语。当有用户进入等候室时，会收到来自会议主办方的私聊消息引导。 鉴权方式: JWT鉴权、OAuth鉴权
    
    :param meeting_id: (required)
    :type meeting_id: str

    :param operator_id: (required)
    :type operator_id: str

    :param operator_id_type: (required)
    :type operator_id_type: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.meeting_id = meeting_id
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.body = body

class ApiV1MeetingMeetingIdWaitingRoomWelcomeMessageGetResponse(ApiResponse):
    data: Optional[V1MeetingSetWaitingRoomWelcomeMessagePost200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingSetWaitingRoomWelcomeMessagePost200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingSetWaitingRoomWelcomeMessagePostRequest(object):
    """设置等候室欢迎语

    为已开启等候室的会议配置等候室欢迎语。当有用户进入等候室时，会收到来自会议主办方的私聊消息引导。  鉴权方式: JWT鉴权、OAuth鉴权
    
    :param body:
    :type body: V1MeetingSetWaitingRoomWelcomeMessagePostRequest
    """  # noqa: E501


    def __init__(
        self,
        body: Optional[V1MeetingSetWaitingRoomWelcomeMessagePostRequest] = None
    ):
        self.body = body

class ApiV1MeetingSetWaitingRoomWelcomeMessagePostResponse(ApiResponse):
    data: Optional[V1MeetingSetWaitingRoomWelcomeMessagePost200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingSetWaitingRoomWelcomeMessagePost200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingsCustomerShortUrlPostRequest(object):
    """创建用户专属参会链接

    使用该接口，可用 `customer_data` 进行区分，为一场会议生成多个会议链接。通过用户入会、用户进入等候室等事件，或通过获取等候室成员列表的 API 查询到该参数。 该接口不支持个人会议号会议、网络研讨会（Webinar）。支持企业品牌化链接。 参会者腾讯会议客户端版本需大于等于 3.2.0。 暂不支持 OAuth 2.0 鉴权方式访问。
    
    :param body:
    :type body: V1MeetingsCustomerShortUrlPostRequest
    """  # noqa: E501


    def __init__(
        self,
        body: Optional[V1MeetingsCustomerShortUrlPostRequest] = None
    ):
        self.body = body

class ApiV1MeetingsCustomerShortUrlPostResponse(ApiResponse):
    data: Optional[V1MeetingsCustomerShortUrlPost200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingsCustomerShortUrlPost200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingsGetRequest(object):
    """查询用户的会议列表

    通过会议CODE查询会议详情/查询用户的会议列表 ① 通过会议CODE查询会议详情 企业 secret 鉴权用户可查询到任何该用户创建的企业下的会议，OAuth2.0 鉴权用户只能查询到通过 OAuth2.0 鉴权创建的会议。 支持企业管理员查询企业下的会议。 本接口的邀请参会成员限制调整至300人。 当会议为周期性会议时，主持人密钥每场会议固定，但单场会议只能获取一次。支持查询周期性会议的主持人密钥。 支持查询 MRA 当前所在会议信息。 若会议号被回收则无法通过 Code 查询，您可以通过会议 ID 查询到该会议。 ② 查询用户的会议列表 获取某指定用户的进行中或待开始的会议列表。企业 secret 鉴权用户可查询任何该企业该用户创建的有效会议，OAuth2.0 鉴权用户只能查询通过 OAuth2.0 鉴权创建的有效会议。
    
    :param instanceid: 用户的终端设备类型： 0：PSTN 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：Linux 20：Rooms for Touch Windows 21：Rooms for Touch MacOS 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch iOS (required)
    :type instanceid: str

    :param operator_id: 操作者 ID。operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 说明：userid 字段和 operator_id 字段二者必填一项。若两者都填，以 operator_id 字段为准。
    :type operator_id: str

    :param operator_id_type: 操作者 ID 的类型： 3：rooms_id 说明：当前仅支持 rooms_id。如操作者为企业内 userid 或 openId，请使用 userid 字段。
    :type operator_id_type: str

    :param userid: 调用方用于标示用户的唯一 ID（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId）。 企业唯一用户标识说明： 1：企业对接 SSO 时使用的员工唯一标识 ID。 2：企业调用创建用户接口时传递的 userid 参数。
    :type userid: str

    :param meeting_code: 有效的9位数字会议号码。（通过会议CODE查询会议详情时，必传）
    :type meeting_code: str

    :param cursory: 分页游标
    :type cursory: str

    :param pos: 分页获取用户会议列表的查询起始时间值，unix 秒级时间戳
    :type pos: str

    :param is_show_all_sub_meetings: 是否显示周期性会议的所有子会议，默认值为0。 0：只显示周期性会议的第一个子会议 1：显示所有周期性会议的子会议
    :type is_show_all_sub_meetings: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        instanceid: Optional[str] = None,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        userid: Optional[str] = None,
        meeting_code: Optional[str] = None,
        cursory: Optional[str] = None,
        pos: Optional[str] = None,
        is_show_all_sub_meetings: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.instanceid = instanceid
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.userid = userid
        self.meeting_code = meeting_code
        self.cursory = cursory
        self.pos = pos
        self.is_show_all_sub_meetings = is_show_all_sub_meetings
        self.body = body

class ApiV1MeetingsGetResponse(ApiResponse):
    data: Optional[V1MeetingsGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingsGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingsMeetingIdCancelPostRequest(object):
    """取消会议

    取消用户创建的会议。用户只能取消自己创建的会议，且该会议是一个有效的会议。如果不是会议创建者或者无效会议号将会返回错误。 企业 secret 鉴权用户可取消任何该用户企业下创建的有效会议，OAuth2.0 鉴权用户只能取消通过 OAuth2.0 鉴权创建的有效会议。 当您想实时监测会议取消状况时，您可以通过订阅 [会议取消](https://cloud.tencent.com/document/product/1095/51616) 的事件，接收事件通知。
    
    :param meeting_id: (required)
    :type meeting_id: str

    :param body:
    :type body: V1MeetingsMeetingIdCancelPostRequest
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        body: Optional[V1MeetingsMeetingIdCancelPostRequest] = None
    ):
        self.meeting_id = meeting_id
        self.body = body

class ApiV1MeetingsMeetingIdCancelPostResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingsMeetingIdCustomerShortUrlGetRequest(object):
    """获取用户专属参会链接

    **描述**：  * 可以获取指定会议的所有专属参会链接及 `customer_data`。 * 该接口不支持个人会议号会议、网络研讨会（Webinar）。支持企业品牌化链接。 * 参会者腾讯会议客户端版本需大于等于 3.2.0。 * 暂不支持 OAuth 2.0 鉴权方式访问。
    
    :param meeting_id: (required)
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

class ApiV1MeetingsMeetingIdCustomerShortUrlGetResponse(ApiResponse):
    data: Optional[V1MeetingsMeetingIdCustomerShortUrlGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingsMeetingIdCustomerShortUrlGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingsMeetingIdEnrollApprovalsGetRequest(object):
    """查询会议报名信息

    查询已报名观众数量和报名观众答题详情，仅会议创建者可查询。 企业 secret 鉴权用户可修改任何该企业该用户创建的有效会议，OAuth2.0 鉴权用户只能修改通过 OAuth2.0 鉴权创建的有效会议。 用户必须是注册用户，请求头部 X-TC-Registered 字段必须传入为1。
    
    :param meeting_id: 会议ID (required)
    :type meeting_id: str

    :param instanceid: 用户的终端设备类型： 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 (required)
    :type instanceid: str

    :param page: 当前页，页码起始值为1 (required)
    :type page: str

    :param page_size: 分页大小，最大50条 (required)
    :type page_size: str

    :param operator_id: 操作者 ID。会议创建者可以导入报名信息。 operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。  operator_id_type=2，operator_id必须和公共参数的openid一致。  operator_id和userid至少填写一个，两个参数如果都传了以operator_id为准。  使用OAuth公参鉴权后不能使用userid为入参。
    :type operator_id: str

    :param operator_id_type: 操作者 ID 的类型：  1: userid 2: open_id  如果operator_id和userid具有值，则以operator_id为准；
    :type operator_id_type: str

    :param userid: 会议创建者的用户 ID（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId）为了防止现网应用报错，此参数实则仍然兼容openid，如无oauth应用使用报名接口则也可做成不兼容变更。
    :type userid: str

    :param status: 审批状态筛选字段，审批状态：0 全部，1 待审批，2 已拒绝，3 已批准，默认返回全部
    :type status: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        instanceid: Optional[str] = None,
        page: Optional[str] = None,
        page_size: Optional[str] = None,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        userid: Optional[str] = None,
        status: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.meeting_id = meeting_id
        self.instanceid = instanceid
        self.page = page
        self.page_size = page_size
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.userid = userid
        self.status = status
        self.body = body

class ApiV1MeetingsMeetingIdEnrollApprovalsGetResponse(ApiResponse):
    data: Optional[V1MeetingsMeetingIdEnrollApprovalsGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingsMeetingIdEnrollApprovalsGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingsMeetingIdEnrollApprovalsPutRequest(object):
    """审批会议报名信息

    批量云会议的报名信息，仅会议创建者可审批。 企业 secret 鉴权用户可审批任何该企业该用户创建的有效会议，OAuth2.0 鉴权用户只能审批通过 OAuth2.0 鉴权创建的有效会议。 用户必须是注册用户，请求头部 X-TC-Registered 字段必须传入为1。
    
    :param meeting_id: 会议ID (required)
    :type meeting_id: str

    :param body:
    :type body: V1MeetingsMeetingIdEnrollApprovalsPutRequest
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        body: Optional[V1MeetingsMeetingIdEnrollApprovalsPutRequest] = None
    ):
        self.meeting_id = meeting_id
        self.body = body

class ApiV1MeetingsMeetingIdEnrollApprovalsPutResponse(ApiResponse):
    data: Optional[V1MeetingsMeetingIdEnrollApprovalsPut200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingsMeetingIdEnrollApprovalsPut200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingsMeetingIdEnrollConfigGetRequest(object):
    """查询会议报名配置

    查询云会议的报名配置和报名问题，仅会议创建者可查询。会议未开启报名时会返回未开启报名错误。 企业 secret 鉴权用户可查询任何该企业该用户创建的有效会议，OAuth2.0 鉴权用户只能查询通过 OAuth2.0 鉴权创建的有效会议。 用户必须是注册用户，请求头部 X-TC-Registered 字段必须传入为1。
    
    :param meeting_id: 会议ID (required)
    :type meeting_id: str

    :param instanceid: 用户的终端设备类型： 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 (required)
    :type instanceid: str

    :param operator_id: 操作者 ID。会议创建者可以导入报名信息。 operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。  operator_id_type=2，operator_id必须和公共参数的openid一致。  operator_id和userid至少填写一个，两个参数如果都传了以operator_id为准。  使用OAuth公参鉴权后不能使用userid为入参。
    :type operator_id: str

    :param operator_id_type: 操作者 ID 的类型：  1: userid 2: open_id  如果operator_id和userid具有值，则以operator_id为准；
    :type operator_id_type: str

    :param userid: 会议创建者的用户 ID（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId）
    :type userid: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        instanceid: Optional[str] = None,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        userid: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.meeting_id = meeting_id
        self.instanceid = instanceid
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.userid = userid
        self.body = body

class ApiV1MeetingsMeetingIdEnrollConfigGetResponse(ApiResponse):
    data: Optional[V1MeetingsMeetingIdEnrollConfigGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingsMeetingIdEnrollConfigGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingsMeetingIdEnrollConfigPutRequest(object):
    """修改会议报名配置

    修改云会议的报名配置和报名问题，仅会议创建者可修改，且需要会议已开启报名。 企业 secret 鉴权用户可修改任何该企业该用户创建的有效会议，OAuth2.0 鉴权用户只能修改通过 OAuth2.0 鉴权创建的有效会议。 用户必须是注册用户，请求头部 X-TC-Registered 字段必须传入为1。
    
    :param meeting_id: 会议ID (required)
    :type meeting_id: str

    :param body:
    :type body: V1MeetingsMeetingIdEnrollConfigPutRequest
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        body: Optional[V1MeetingsMeetingIdEnrollConfigPutRequest] = None
    ):
        self.meeting_id = meeting_id
        self.body = body

class ApiV1MeetingsMeetingIdEnrollConfigPutResponse(ApiResponse):
    data: Optional[V1MeetingsMeetingIdEnrollConfigPut200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingsMeetingIdEnrollConfigPut200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingsMeetingIdEnrollIdsPostRequest(object):
    """查询会议成员报名 ID

    描述： 支持查询会议中已报名成员的报名 ID，仅会议创建者可查询。
    
    :param meeting_id: 会议ID (required)
    :type meeting_id: str

    :param body:
    :type body: V1MeetingsMeetingIdEnrollIdsPostRequest
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        body: Optional[V1MeetingsMeetingIdEnrollIdsPostRequest] = None
    ):
        self.meeting_id = meeting_id
        self.body = body

class ApiV1MeetingsMeetingIdEnrollIdsPostResponse(ApiResponse):
    data: Optional[V1MeetingsMeetingIdEnrollIdsPost200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingsMeetingIdEnrollIdsPost200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingsMeetingIdEnrollImportPostRequest(object):
    """导入会议报名信息

    指定会议中导入报名信息。  企业 secret 鉴权用户可通过同企业下用户 userid 和手机号导入报名信息，OAuth2.0 鉴权用户能通过用户 open_id，与应用同企业下的 userid 以及手机号导入报名信息。 用户必须是注册用户，请求头部 X-TC-Registered 字段必须传入为1。 商业版单场会议导入上限1000条，企业版单场会议导入上限4000条。如需提升，请联系我们。
    
    :param meeting_id: 会议id (required)
    :type meeting_id: str

    :param body:
    :type body: V1MeetingsMeetingIdEnrollImportPostRequest
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        body: Optional[V1MeetingsMeetingIdEnrollImportPostRequest] = None
    ):
        self.meeting_id = meeting_id
        self.body = body

class ApiV1MeetingsMeetingIdEnrollImportPostResponse(ApiResponse):
    data: Optional[V1MeetingsMeetingIdEnrollImportPost200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingsMeetingIdEnrollImportPost200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingsMeetingIdEnrollUnregistrationDeleteRequest(object):
    """删除会议报名信息

    描述： 删除指定会议的报名信息，支持删除用户手动报名的信息和导入的报名信息。 企业 secret 鉴权用户可删除该用户企业会议下的报名信息，OAuth2.0 鉴权用户只能删除通过 OAuth2.0 鉴权创建的有效会议的报名信息。 用户必须是注册用户，请求头部 X-TC-Registered 字段必须传入为1。
    
    :param meeting_id: (required)
    :type meeting_id: str

    :param body:
    :type body: V1MeetingsMeetingIdEnrollUnregistrationDeleteRequest
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        body: Optional[V1MeetingsMeetingIdEnrollUnregistrationDeleteRequest] = None
    ):
        self.meeting_id = meeting_id
        self.body = body

class ApiV1MeetingsMeetingIdEnrollUnregistrationDeleteResponse(ApiResponse):
    data: Optional[V1MeetingsMeetingIdEnrollUnregistrationDelete200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingsMeetingIdEnrollUnregistrationDelete200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingsMeetingIdGetRequest(object):
    """查询会议

    通过会议 ID 查询会议详情。 企业 secret 鉴权用户可查询到任何该用户创建的企业下的会议，OAuth2.0 鉴权用户只能查询到通过 OAuth2.0 鉴权创建的会议。 本接口的邀请参会成员限制调整至300人。 当会议为周期性会议时，主持人密钥每场会议固定，但单场会议只能获取一次。支持查询周期性会议的主持人密钥。 支持查询 MRA 当前所在会议信息。
    
    :param meeting_id: (required)
    :type meeting_id: str

    :param instanceid: 用户的终端设备类型： 0：PSTN 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch MacOS 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch iOS (required)
    :type instanceid: str

    :param operator_id: 操作者ID，根据operator_id_type的值，使用不同的类型
    :type operator_id: str

    :param operator_id_type: 操作者ID的类型：1.userid 2.openid 3.rooms_id
    :type operator_id_type: str

    :param userid: 会议创建者的用户 ID（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId）
    :type userid: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        instanceid: Optional[str] = None,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        userid: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.meeting_id = meeting_id
        self.instanceid = instanceid
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.userid = userid
        self.body = body

class ApiV1MeetingsMeetingIdGetResponse(ApiResponse):
    data: Optional[V1MeetingsMeetingIdGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingsMeetingIdGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingsMeetingIdInviteesGetRequest(object):
    """获取会议受邀成员列表

    根据会议ID获取受邀成员列表，支持分页获取，只有会议的创建者才有权限获取。
    
    :param meeting_id: 会议ID (required)
    :type meeting_id: str

    :param userid: 会议创建者ID.调用方用于标示用户的唯一 ID（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId）。 企业唯一用户标识说明： 1. 企业对接 SSO 时使用的员工唯一标识 ID。 2. 企业调用创建用户接口时传递的 userid 参数。 (required)
    :type userid: str

    :param instanceid: 用户的终端设备类型：1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch Mac 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch Iphone (required)
    :type instanceid: str

    :param pos: 分页获取受邀成员列表的查询起始位置值。此参数为非必选参数，默认值为0，从头开始查询。（输出参数has_remaining为 true，表示还存在受邀成员需要继续查询；输出参数next_pos即下一次查询的“pos”值。多次调用该接口直到输出参数“has_remaining”为 false。
    :type pos: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        userid: Optional[str] = None,
        instanceid: Optional[str] = None,
        pos: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.meeting_id = meeting_id
        self.userid = userid
        self.instanceid = instanceid
        self.pos = pos
        self.body = body

class ApiV1MeetingsMeetingIdInviteesGetResponse(ApiResponse):
    data: Optional[V1MeetingsMeetingIdInviteesGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingsMeetingIdInviteesGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingsMeetingIdInviteesPutRequest(object):
    """设置会议邀请成员

    根据会议ID设置邀请成员，只有会议的创建者才有权限设置。 最多可以设置2000名邀请者。 注：本接口为覆盖式设置。
    
    :param meeting_id: 会议ID (required)
    :type meeting_id: str

    :param body:
    :type body: V1MeetingsMeetingIdInviteesPutRequest
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        body: Optional[V1MeetingsMeetingIdInviteesPutRequest] = None
    ):
        self.meeting_id = meeting_id
        self.body = body

class ApiV1MeetingsMeetingIdInviteesPutResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingsMeetingIdParticipantsGetRequest(object):
    """获取参会成员列表

    会议创建者和企业管理员可以查询参会成员的列表，其他用户的调用会被拒绝。  支持查询网络研讨会参会成员列表。 如果会议还未开始，调用此接口查询会返回空列表。 企业 secret 鉴权用户（会议创建者）可获取任何该企业该用户创建的有效会议中的参会成员，企业 secret 鉴权用户（企业超级管理员）可获取任何该企业下创建的有效会议中的参会成员，OAuth2.0 鉴权用户（会议创建者）只能获取用户通过 OAuth2.0 鉴权创建的有效会议中的参会成员。 当您需要实时监测参会成员入会状态或退会状态时，您可以通过订阅 [用户入会](https://cloud.tencent.com/document/product/1095/51620)和 [用户离会](https://cloud.tencent.com/document/product/1095/51622) 的事件，接收事件通知。
    
    :param meeting_id: (required)
    :type meeting_id: str

    :param sub_meeting_id: 周期性会议子会议 ID。说明：可通过查询用户的会议列表、查询会议接口获取返回的子会议 ID，即 current_sub_meeting_id；如果是周期性会议，此参数必传。
    :type sub_meeting_id: str

    :param operator_id: 操作者ID，根据operator_id_type的值，使用不同的类型
    :type operator_id: str

    :param operator_id_type: 操作者ID的类型：1.userid 2.open_id 3.rooms_id
    :type operator_id_type: str

    :param userid: 会议创建者的用户 ID（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId）。
    :type userid: str

    :param pos: 分页获取参会成员列表的查询起始位置值。当参会成员较多时，建议使用此参数进行分页查询，避免查询超时。此参数为非必选参数，默认值为0，从头开始查询。设置每页返回的数量，请参考参数“size”的说明。查询返回输出参数“has_remaining”为 true，表示该会议人数较多，还有一定数量的参会成员需要继续查询。返回参数“next_pos”的值即为下一次查询的 pos 的值。多次调用该查询接口直到输出参数“has_remaining”值为 false。
    :type pos: str

    :param size: 拉取参会成员条数，目前每页支持最大100条。
    :type size: str

    :param start_time: 参会时间过滤起始时间（单位秒）。说明：时间区间不允许超过31天，如果为空默认当前时间前推31天；start_time 和 end_time 都没传时最大查询时间跨度90天；对于周期性会议查询暂时不生效，请使用分页参数查询。
    :type start_time: str

    :param end_time:  参会时间过滤终止时间（单位秒）。说明：时间区间不允许超过31天，如果为空默认取当前时间；start_time 和 end_time 都没传时最大查询时间跨度90天；对于周期性会议查询暂时不生效，请使用分页参数查询。
    :type end_time: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        sub_meeting_id: Optional[str] = None,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        userid: Optional[str] = None,
        pos: Optional[str] = None,
        size: Optional[str] = None,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.meeting_id = meeting_id
        self.sub_meeting_id = sub_meeting_id
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.userid = userid
        self.pos = pos
        self.size = size
        self.start_time = start_time
        self.end_time = end_time
        self.body = body

class ApiV1MeetingsMeetingIdParticipantsGetResponse(ApiResponse):
    data: Optional[V1MeetingsMeetingIdParticipantsGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingsMeetingIdParticipantsGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingsMeetingIdPutRequest(object):
    """修改会议

    修改某指定会议的会议信息。  企业 secret 鉴权用户可修改任何该企业该用户创建的有效会议，OAuth2.0 鉴权用户只能修改通过 OAuth2.0 鉴权创建的有效会议。 当您想实时监测会议修改状况时，您可以通过订阅 [会议更新](https://cloud.tencent.com/document/product/1095/51615) 的事件，接收事件通知。 本接口的邀请参会成员限制调整至300人。 当会议为周期性会议时，主持人密钥每场会议固定，但单场会议只能获取一次。支持修改周期性会议的主持人密钥。
    
    :param meeting_id: (required)
    :type meeting_id: str

    :param body:
    :type body: V1MeetingsMeetingIdPutRequest
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        body: Optional[V1MeetingsMeetingIdPutRequest] = None
    ):
        self.meeting_id = meeting_id
        self.body = body

class ApiV1MeetingsMeetingIdPutResponse(ApiResponse):
    data: Optional[V1MeetingsMeetingIdPut200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingsMeetingIdPut200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingsMeetingIdQosGetRequest(object):
    """获取会议实时质量检测数据

    拥有企业“会议列表--会控”权限的成员，能够获取实时会议质量检测数据。 支持云会议和Webinar会议的数据。会议状态为进行中。
    
    :param meeting_id: 会议ID (required)
    :type meeting_id: str

    :param operator_id: 操作者ID (required)
    :type operator_id: str

    :param operator_id_type: 操作者ID类型 (required)
    :type operator_id_type: str

    :param page_size: 分页大小，20-100
    :type page_size: str

    :param page: 页码
    :type page: str

    :param to_operator_id: 筛选的用户ID
    :type to_operator_id: str

    :param to_operator_id_type: 筛选的用户ID类型 4:ms_open_id
    :type to_operator_id_type: str

    :param key: 搜索key(格式：模块_指标)
    :type key: str

    :param min_value: 搜索值,搜索大于等于该值的数据
    :type min_value: str

    :param max_value: 最大搜索值，搜索小于等于该值的数据
    :type max_value: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        page_size: Optional[str] = None,
        page: Optional[str] = None,
        to_operator_id: Optional[str] = None,
        to_operator_id_type: Optional[str] = None,
        key: Optional[str] = None,
        min_value: Optional[str] = None,
        max_value: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.meeting_id = meeting_id
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.page_size = page_size
        self.page = page
        self.to_operator_id = to_operator_id
        self.to_operator_id_type = to_operator_id_type
        self.key = key
        self.min_value = min_value
        self.max_value = max_value
        self.body = body

class ApiV1MeetingsMeetingIdQosGetResponse(ApiResponse):
    data: Optional[V1MeetingsMeetingIdQosGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingsMeetingIdQosGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingsMeetingIdQualityGetRequest(object):
    """查询会议健康度

    查询会议及参会成员的健康度，付费开通该服务的企业管理员、超管可以查询，与是否为会议创建者/主持人/联席主持人无关。 鉴权方式：支持 JWT 鉴权 和 Oauth 鉴权
    
    :param meeting_id: 会议唯一ID (required)
    :type meeting_id: str

    :param operator_id: 操作者 ID。operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。角色校验：付费开通该服务的企业管理员/超管可以查询健康度。 (required)
    :type operator_id: str

    :param operator_id_type: 操作者 ID 的类型： 1：企业内用户 userid。 2: open_id 4: ms_open_id (required)
    :type operator_id_type: str

    :param page_size: 分页大小，最小1，最大50。 (required)
    :type page_size: str

    :param page: 当前页，页码起始值，最小1，最大2000。 (required)
    :type page: str

    :param start_time: 参会时间过滤起始时间，UNIX 时间戳（单位秒），可查询的时间区间为过去7天到现在。 返回meeting_id对应会议房间下，开始时间大于等于start_time且离start_time最近的一个媒体房间数据（从第一个人入会到会中成员全部离开会议形成一个媒体房间，若同一会议号下再次有人入会则形成新的媒体房间） 如果同一会议号下有多个媒体房间，请先使用“获取账户级已结束会议列表”接口查询，获知需查询的媒体房间的start_time。 (required)
    :type start_time: str

    :param instanceid: 用户的终端设备类型： 0：PSTN 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch MacOS 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch iOS
    :type instanceid: str

    :param sub_meeting_id: 周期性会议子会议 ID。说明：可通过查询用户的会议列表、查询会议接口获取返回的子会议 ID，即 current_sub_meeting_id；如果是周期性会议，此参数必传。
    :type sub_meeting_id: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        page_size: Optional[str] = None,
        page: Optional[str] = None,
        start_time: Optional[str] = None,
        instanceid: Optional[str] = None,
        sub_meeting_id: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.meeting_id = meeting_id
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.page_size = page_size
        self.page = page
        self.start_time = start_time
        self.instanceid = instanceid
        self.sub_meeting_id = sub_meeting_id
        self.body = body

class ApiV1MeetingsMeetingIdQualityGetResponse(ApiResponse):
    data: Optional[V1MeetingsMeetingIdQualityGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingsMeetingIdQualityGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingsMeetingIdRealTimeParticipantsGetRequest(object):
    """查询实时会中成员列表

    查询当前会中成员列表，仅包括会中的成员，如果已离会，则不展示 企业超级管理员、会议创建者、会议主持人、会议联席主持人可以查询该数据。
    
    :param meeting_id: 会议唯一ID (required)
    :type meeting_id: str

    :param operator_id: 操作者 ID。operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 (required)
    :type operator_id: str

    :param operator_id_type: Integer 操作者 ID 的类型：1：企业内用户 userid。2: open_id3. rooms_id (required)
    :type operator_id_type: str

    :param page: 当前页，页码起始值为1。 (required)
    :type page: str

    :param page_size: 分页大小，最大50条。 (required)
    :type page_size: str

    :param sub_meeting_id: String 周期性会议子会议 ID。说明：可通过查询用户的会议列表、查询会议接口获取返回的子会议 ID，即 current_sub_meeting_id；如果是周期性会议，此参数必传。
    :type sub_meeting_id: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        page: Optional[str] = None,
        page_size: Optional[str] = None,
        sub_meeting_id: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.meeting_id = meeting_id
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.page = page
        self.page_size = page_size
        self.sub_meeting_id = sub_meeting_id
        self.body = body

class ApiV1MeetingsMeetingIdRealTimeParticipantsGetResponse(ApiResponse):
    data: Optional[V1MeetingsMeetingIdRealTimeParticipantsGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingsMeetingIdRealTimeParticipantsGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingsMeetingIdVirtualBackgroundPostRequest(object):
    """设置会议统一虚拟背景

    非进行中非已结束的会议，会议创建者可以设置统一虚拟背景，并设置生效范围。如果企业未开启虚拟背景开关，则该企业下会议不可进行该设置。异步方式上传。支持云会议和Webinar会议，其中Webinar会议设置为对嘉宾生效，且不能指定成员
    
    :param meeting_id: 会议ID (required)
    :type meeting_id: str

    :param body:
    :type body: V1MeetingsMeetingIdVirtualBackgroundPostRequest
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        body: Optional[V1MeetingsMeetingIdVirtualBackgroundPostRequest] = None
    ):
        self.meeting_id = meeting_id
        self.body = body

class ApiV1MeetingsMeetingIdVirtualBackgroundPostResponse(ApiResponse):
    data: Optional[V1MeetingsMeetingIdVirtualBackgroundPost200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingsMeetingIdVirtualBackgroundPost200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingsMeetingIdWaitingRoomParticipantsGetRequest(object):
    """获取实时等候室成员列表

    **描述**：  * 会议拥有者获取某指定会议的等候室成员列表，需开启等候室且为“会议进行中”状态。 * 只有会议的拥有者即创建者可以查询等候室成员列表，其他用户的调用会被拒绝。如果会议非进行中，调用此接口查询会返回空列表。 * 企业 secret 鉴权用户（会议创建者）可获取任何该企业该用户创建的会议中的等候室成员列表，OAuth2.0 鉴权用户（会议创建者）只能获取用户通过 OAuth2.0 鉴权创建的会议中的等候室成员列表。 * 此接口暂不支持 MRA 设备作为被操作者的情况。
    
    :param meeting_id: (required)
    :type meeting_id: str

    :param userid: 会议创建者的用户 ID（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId） (required)
    :type userid: str

    :param page_size: 分页大小，默认10，最大50
    :type page_size: str

    :param page: 页码，从1开始
    :type page: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        meeting_id: str,
        userid: Optional[str] = None,
        page_size: Optional[str] = None,
        page: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.meeting_id = meeting_id
        self.userid = userid
        self.page_size = page_size
        self.page = page
        self.body = body

class ApiV1MeetingsMeetingIdWaitingRoomParticipantsGetResponse(ApiResponse):
    data: Optional[V1MeetingsMeetingIdWaitingRoomParticipantsGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingsMeetingIdWaitingRoomParticipantsGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingsPostRequest(object):
    """创建会议

    快速创建或预定一个会议。  企业 secret 鉴权用户可创建该用户所属企业下的会议，OAuth2.0 鉴权用户只能创建该企业下 OAuth2.0 应用的会议。 用户必须是注册用户，请求头部 X-TC-Registered 字段必须传入为1。 当您想实时监测会议创建状况时，您可以通过订阅 [会议创建](https://cloud.tencent.com/document/product/1095/51614) 的事件，接收事件通知。 本接口的邀请参会成员限制调整至300人。 当会议为周期性会议时，主持人密钥每场会议固定，但单场会议只能获取一次。支持创建周期性会议的主持人密钥。
    
    :param body:
    :type body: V1MeetingsPostRequest
    """  # noqa: E501


    def __init__(
        self,
        body: Optional[V1MeetingsPostRequest] = None
    ):
        self.body = body

class ApiV1MeetingsPostResponse(ApiResponse):
    data: Optional[V1MeetingsPost200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingsPost200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingsQueryMeetingidForDevicePostRequest(object):
    """查询用户设备是否入会

    查询用户设备是否入会接口，用来查询本企业用户在当前时间是否有设备进入指定的会议中。 不支持OAuth2.0鉴权方式访问。
    
    :param body:
    :type body: V1MeetingsQueryMeetingidForDevicePostRequest
    """  # noqa: E501


    def __init__(
        self,
        body: Optional[V1MeetingsQueryMeetingidForDevicePostRequest] = None
    ):
        self.body = body

class ApiV1MeetingsQueryMeetingidForDevicePostResponse(ApiResponse):
    data: Optional[V1MeetingsQueryMeetingidForDevicePost200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingsQueryMeetingidForDevicePost200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1PmiMeetingsGetRequest(object):
    """查询个人会议号会议列表

    查询个人会议号（PMI）会议的会议列表（待开始、进行中、已结束），目前暂不支持 OAuth2.0 鉴权访问。
    
    :param operator_id: 企业下操作者ID，根据operator_id_type的值，使用不同的类型 (required)
    :type operator_id: str

    :param operator_id_type: 操作者ID类型： 1.企业用户userid 3.rooms设备rooms_id (required)
    :type operator_id_type: str

    :param instanceid: 用户的终端设备类型： 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch Mac 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch Iphone (required)
    :type instanceid: str

    :param start_time: 查询起始时间，时间区间不超过90天
    :type start_time: str

    :param end_time: 查询结束时间，时间区间不超过90天
    :type end_time: str

    :param page: 当前页，页码起始值为1，默认为1
    :type page: str

    :param page_size: 分页大小，默认20条，最大20条
    :type page_size: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        operator_id: Optional[str] = None,
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

class ApiV1PmiMeetingsGetResponse(ApiResponse):
    data: Optional[V1PmiMeetingsGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1PmiMeetingsGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class MeetingsApi:
    def __init__(self, config: Config):
        self.__config = config

    def v1_asr_config_put(
        self,
        request: ApiV1AsrConfigPutRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1AsrConfigPutResponse:
        """v1_asr_config_put 设置语音识别热词[/v1/asr/config - PUT]

            用户可以通过接口进行您创建的会议的语音识别设置。 权限点：查看或管理您的会议
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/asr/config",
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
                response = ApiV1AsrConfigPutResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1AsrConfigPut200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_asr_details_get(
        self,
        request: ApiV1AsrDetailsGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1AsrDetailsGetResponse:
        """v1_asr_details_get 导出实时转写记录[/v1/asr/details - GET]

            如果会议开启了会议转写，可以导出转写记录。主持人可以设置导出权限，默认主持人可以导出，支持会中和会后导出。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/asr/details",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'operator_id_type' is set
            if request.operator_id_type is None:
                raise Exception("operator_id_type is required and must be specified")
            # verify the required parameter 'operator_id' is set
            if request.operator_id is None:
                raise Exception("operator_id is required and must be specified")
            # verify the required parameter 'meeting_id' is set
            if request.meeting_id is None:
                raise Exception("meeting_id is required and must be specified")
            # path 参数
            # query 参数
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.meeting_id is not None:
                api_req.query_params.append(('meeting_id', request.meeting_id))
            if request.start_time is not None:
                api_req.query_params.append(('start_time', request.start_time))
            if request.end_time is not None:
                api_req.query_params.append(('end_time', request.end_time))
            if request.file_type is not None:
                api_req.query_params.append(('file_type', request.file_type))
            if request.page is not None:
                api_req.query_params.append(('page', request.page))
            if request.page_size is not None:
                api_req.query_params.append(('page_size', request.page_size))
            if request.show_bilingual is not None:
                api_req.query_params.append(('show_bilingual', request.show_bilingual))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1AsrDetailsGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1AsrDetailsGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_asr_push_status_post(
        self,
        request: ApiV1AsrPushStatusPostRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1AsrPushStatusPostResponse:
        """v1_asr_push_status_post 开启/关闭实时转写推送[/v1/asr/push-status - POST]

             会议创建者可开启本场会议的实时转写内容推送，待开始的会议或未打开实时转写功能的会议也支持开启推送，开启推送后如果会议打开转写，则可通过webhook 实时转写推送 实时获取到转写内容。 企业 secret 鉴权用户可开启该用户所属企业下的所有会议转写推送，OAuth2.0 鉴权用户只能开启通过 OAuth2.0 鉴权创建的会议转写推送。 企业级自建应用通过 webhook 可以接收到企业下所有开启推送的会议的转写内容，应用级自建应用通过 webhook 可以接收到本应用创建的会议的转写内容。OAuth2.0 应用通过 webhook 可以接收到 OAuth2.0 鉴权创建的会议的转写内容。 
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/asr/push-status",
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
                response = ApiV1AsrPushStatusPostResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_history_meetings_userid_get(
        self,
        request: ApiV1HistoryMeetingsUseridGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1HistoryMeetingsUseridGetResponse:
        """v1_history_meetings_userid_get 查询用户已结束会议列表[/v1/history/meetings/{userid} - GET]

            获取某指定用户的已结束的会议列表，可返回用户创建与参加过的已结束会议列表，支持 OAuth2.0 鉴权和企微鉴权。 请优先使用operator_id和operator_id_type查询，当使用operator_id和operator_id_type时，userid设置为operator_id的值即可
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/history/meetings/{userid}",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'userid' is set
            if request.userid is None:
                raise Exception("userid is required and must be specified")
            # verify the required parameter 'page_size' is set
            if request.page_size is None:
                raise Exception("page_size is required and must be specified")
            # verify the required parameter 'page' is set
            if request.page is None:
                raise Exception("page is required and must be specified")
            # path 参数
            if request.userid is not None:
                api_req.path_params['userid'] = request.userid
            # query 参数
            if request.page_size is not None:
                api_req.query_params.append(('page_size', request.page_size))
            if request.page is not None:
                api_req.query_params.append(('page', request.page))
            if request.meeting_code is not None:
                api_req.query_params.append(('meeting_code', request.meeting_code))
            if request.start_time is not None:
                api_req.query_params.append(('start_time', request.start_time))
            if request.end_time is not None:
                api_req.query_params.append(('end_time', request.end_time))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1HistoryMeetingsUseridGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1HistoryMeetingsUseridGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meeting_job_id_get(
        self,
        request: ApiV1MeetingJobIdGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingJobIdGetResponse:
        """v1_meeting_job_id_get 获取导出 PSTN 通话详单任务结果[/v1/meeting/{job_id} - GET]

            获取异步导出任务的结果。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meeting/{job_id}",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'job_id' is set
            if request.job_id is None:
                raise Exception("job_id is required and must be specified")
            # verify the required parameter 'operator_id_type' is set
            if request.operator_id_type is None:
                raise Exception("operator_id_type is required and must be specified")
            # verify the required parameter 'operator_id' is set
            if request.operator_id is None:
                raise Exception("operator_id is required and must be specified")
            # path 参数
            if request.job_id is not None:
                api_req.path_params['job_id'] = request.job_id
            # query 参数
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1MeetingJobIdGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingJobIdGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meeting_meeting_id_waiting_room_get(
        self,
        request: ApiV1MeetingMeetingIdWaitingRoomGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingMeetingIdWaitingRoomGetResponse:
        """v1_meeting_meeting_id_waiting_room_get 查询等候室成员记录[/v1/meeting/{meeting_id}/waiting-room - GET]

            会议创建者、主持人、联席主持人可以查询等候室成员列表，包括等候室内所有用户的进出记录。会前、会中、会后都可以查询。 “查询等候室成员列表”改为“获取实时等候室成员列表”，只有当前等候室的成员。如果是PMI会议，返回的是PMI的meeting_code。 鉴权方式：JWT鉴权、OAuth鉴权、SDK鉴权 OAuth鉴权的权限为：查询会议、查询和管理会议
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meeting/{meeting_id}/waiting-room",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'meeting_id' is set
            if request.meeting_id is None:
                raise Exception("meeting_id is required and must be specified")
            # verify the required parameter 'operator_id' is set
            if request.operator_id is None:
                raise Exception("operator_id is required and must be specified")
            # verify the required parameter 'operator_id_type' is set
            if request.operator_id_type is None:
                raise Exception("operator_id_type is required and must be specified")
            # verify the required parameter 'page' is set
            if request.page is None:
                raise Exception("page is required and must be specified")
            # verify the required parameter 'page_size' is set
            if request.page_size is None:
                raise Exception("page_size is required and must be specified")
            # path 参数
            if request.meeting_id is not None:
                api_req.path_params['meeting_id'] = request.meeting_id
            # query 参数
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            if request.page is not None:
                api_req.query_params.append(('page', request.page))
            if request.page_size is not None:
                api_req.query_params.append(('page_size', request.page_size))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1MeetingMeetingIdWaitingRoomGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingMeetingIdWaitingRoomGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meeting_meeting_id_waiting_room_welcome_message_get(
        self,
        request: ApiV1MeetingMeetingIdWaitingRoomWelcomeMessageGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingMeetingIdWaitingRoomWelcomeMessageGetResponse:
        """v1_meeting_meeting_id_waiting_room_welcome_message_get 获取等候室欢迎语[/v1/meeting/{meeting_id}/waiting-room-welcome-message - GET]

            查询会议的等候室欢迎语。当有用户进入等候室时，会收到来自会议主办方的私聊消息引导。 鉴权方式: JWT鉴权、OAuth鉴权
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meeting/{meeting_id}/waiting-room-welcome-message",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'meeting_id' is set
            if request.meeting_id is None:
                raise Exception("meeting_id is required and must be specified")
            # verify the required parameter 'operator_id' is set
            if request.operator_id is None:
                raise Exception("operator_id is required and must be specified")
            # verify the required parameter 'operator_id_type' is set
            if request.operator_id_type is None:
                raise Exception("operator_id_type is required and must be specified")
            # path 参数
            if request.meeting_id is not None:
                api_req.path_params['meeting_id'] = request.meeting_id
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
                response = ApiV1MeetingMeetingIdWaitingRoomWelcomeMessageGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingSetWaitingRoomWelcomeMessagePost200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meeting_set_waiting_room_welcome_message_post(
        self,
        request: ApiV1MeetingSetWaitingRoomWelcomeMessagePostRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingSetWaitingRoomWelcomeMessagePostResponse:
        """v1_meeting_set_waiting_room_welcome_message_post 设置等候室欢迎语[/v1/meeting/set-waiting-room-welcome-message - POST]

            为已开启等候室的会议配置等候室欢迎语。当有用户进入等候室时，会收到来自会议主办方的私聊消息引导。  鉴权方式: JWT鉴权、OAuth鉴权
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meeting/set-waiting-room-welcome-message",
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
                response = ApiV1MeetingSetWaitingRoomWelcomeMessagePostResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingSetWaitingRoomWelcomeMessagePost200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meetings_customer_short_url_post(
        self,
        request: ApiV1MeetingsCustomerShortUrlPostRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingsCustomerShortUrlPostResponse:
        """v1_meetings_customer_short_url_post 创建用户专属参会链接[/v1/meetings/customer-short-url - POST]

            使用该接口，可用 `customer_data` 进行区分，为一场会议生成多个会议链接。通过用户入会、用户进入等候室等事件，或通过获取等候室成员列表的 API 查询到该参数。 该接口不支持个人会议号会议、网络研讨会（Webinar）。支持企业品牌化链接。 参会者腾讯会议客户端版本需大于等于 3.2.0。 暂不支持 OAuth 2.0 鉴权方式访问。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meetings/customer-short-url",
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
                response = ApiV1MeetingsCustomerShortUrlPostResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingsCustomerShortUrlPost200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meetings_get(
        self,
        request: ApiV1MeetingsGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingsGetResponse:
        """v1_meetings_get 查询用户的会议列表[/v1/meetings - GET]

            通过会议CODE查询会议详情/查询用户的会议列表 ① 通过会议CODE查询会议详情 企业 secret 鉴权用户可查询到任何该用户创建的企业下的会议，OAuth2.0 鉴权用户只能查询到通过 OAuth2.0 鉴权创建的会议。 支持企业管理员查询企业下的会议。 本接口的邀请参会成员限制调整至300人。 当会议为周期性会议时，主持人密钥每场会议固定，但单场会议只能获取一次。支持查询周期性会议的主持人密钥。 支持查询 MRA 当前所在会议信息。 若会议号被回收则无法通过 Code 查询，您可以通过会议 ID 查询到该会议。 ② 查询用户的会议列表 获取某指定用户的进行中或待开始的会议列表。企业 secret 鉴权用户可查询任何该企业该用户创建的有效会议，OAuth2.0 鉴权用户只能查询通过 OAuth2.0 鉴权创建的有效会议。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meetings",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'instanceid' is set
            if request.instanceid is None:
                raise Exception("instanceid is required and must be specified")
            # path 参数
            # query 参数
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            if request.userid is not None:
                api_req.query_params.append(('userid', request.userid))
            if request.instanceid is not None:
                api_req.query_params.append(('instanceid', request.instanceid))
            if request.meeting_code is not None:
                api_req.query_params.append(('meeting_code', request.meeting_code))
            if request.cursory is not None:
                api_req.query_params.append(('cursory', request.cursory))
            if request.pos is not None:
                api_req.query_params.append(('pos', request.pos))
            if request.is_show_all_sub_meetings is not None:
                api_req.query_params.append(('is_show_all_sub_meetings', request.is_show_all_sub_meetings))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1MeetingsGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingsGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meetings_meeting_id_cancel_post(
        self,
        request: ApiV1MeetingsMeetingIdCancelPostRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingsMeetingIdCancelPostResponse:
        """v1_meetings_meeting_id_cancel_post 取消会议[/v1/meetings/{meeting_id}/cancel - POST]

            取消用户创建的会议。用户只能取消自己创建的会议，且该会议是一个有效的会议。如果不是会议创建者或者无效会议号将会返回错误。 企业 secret 鉴权用户可取消任何该用户企业下创建的有效会议，OAuth2.0 鉴权用户只能取消通过 OAuth2.0 鉴权创建的有效会议。 当您想实时监测会议取消状况时，您可以通过订阅 [会议取消](https://cloud.tencent.com/document/product/1095/51616) 的事件，接收事件通知。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meetings/{meeting_id}/cancel",
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
                response = ApiV1MeetingsMeetingIdCancelPostResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meetings_meeting_id_customer_short_url_get(
        self,
        request: ApiV1MeetingsMeetingIdCustomerShortUrlGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingsMeetingIdCustomerShortUrlGetResponse:
        """v1_meetings_meeting_id_customer_short_url_get 获取用户专属参会链接[/v1/meetings/{meeting_id}/customer-short-url - GET]

            **描述**：  * 可以获取指定会议的所有专属参会链接及 `customer_data`。 * 该接口不支持个人会议号会议、网络研讨会（Webinar）。支持企业品牌化链接。 * 参会者腾讯会议客户端版本需大于等于 3.2.0。 * 暂不支持 OAuth 2.0 鉴权方式访问。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meetings/{meeting_id}/customer-short-url",
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
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1MeetingsMeetingIdCustomerShortUrlGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingsMeetingIdCustomerShortUrlGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meetings_meeting_id_enroll_approvals_get(
        self,
        request: ApiV1MeetingsMeetingIdEnrollApprovalsGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingsMeetingIdEnrollApprovalsGetResponse:
        """v1_meetings_meeting_id_enroll_approvals_get 查询会议报名信息[/v1/meetings/{meeting_id}/enroll/approvals - GET]

            查询已报名观众数量和报名观众答题详情，仅会议创建者可查询。 企业 secret 鉴权用户可修改任何该企业该用户创建的有效会议，OAuth2.0 鉴权用户只能修改通过 OAuth2.0 鉴权创建的有效会议。 用户必须是注册用户，请求头部 X-TC-Registered 字段必须传入为1。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meetings/{meeting_id}/enroll/approvals",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'meeting_id' is set
            if request.meeting_id is None:
                raise Exception("meeting_id is required and must be specified")
            # verify the required parameter 'instanceid' is set
            if request.instanceid is None:
                raise Exception("instanceid is required and must be specified")
            # verify the required parameter 'page' is set
            if request.page is None:
                raise Exception("page is required and must be specified")
            # verify the required parameter 'page_size' is set
            if request.page_size is None:
                raise Exception("page_size is required and must be specified")
            # path 参数
            if request.meeting_id is not None:
                api_req.path_params['meeting_id'] = request.meeting_id
            # query 参数
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            if request.userid is not None:
                api_req.query_params.append(('userid', request.userid))
            if request.instanceid is not None:
                api_req.query_params.append(('instanceid', request.instanceid))
            if request.page is not None:
                api_req.query_params.append(('page', request.page))
            if request.page_size is not None:
                api_req.query_params.append(('page_size', request.page_size))
            if request.status is not None:
                api_req.query_params.append(('status', request.status))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1MeetingsMeetingIdEnrollApprovalsGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingsMeetingIdEnrollApprovalsGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meetings_meeting_id_enroll_approvals_put(
        self,
        request: ApiV1MeetingsMeetingIdEnrollApprovalsPutRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingsMeetingIdEnrollApprovalsPutResponse:
        """v1_meetings_meeting_id_enroll_approvals_put 审批会议报名信息[/v1/meetings/{meeting_id}/enroll/approvals - PUT]

            批量云会议的报名信息，仅会议创建者可审批。 企业 secret 鉴权用户可审批任何该企业该用户创建的有效会议，OAuth2.0 鉴权用户只能审批通过 OAuth2.0 鉴权创建的有效会议。 用户必须是注册用户，请求头部 X-TC-Registered 字段必须传入为1。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meetings/{meeting_id}/enroll/approvals",
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
                response = ApiV1MeetingsMeetingIdEnrollApprovalsPutResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingsMeetingIdEnrollApprovalsPut200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meetings_meeting_id_enroll_config_get(
        self,
        request: ApiV1MeetingsMeetingIdEnrollConfigGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingsMeetingIdEnrollConfigGetResponse:
        """v1_meetings_meeting_id_enroll_config_get 查询会议报名配置[/v1/meetings/{meeting_id}/enroll/config - GET]

            查询云会议的报名配置和报名问题，仅会议创建者可查询。会议未开启报名时会返回未开启报名错误。 企业 secret 鉴权用户可查询任何该企业该用户创建的有效会议，OAuth2.0 鉴权用户只能查询通过 OAuth2.0 鉴权创建的有效会议。 用户必须是注册用户，请求头部 X-TC-Registered 字段必须传入为1。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meetings/{meeting_id}/enroll/config",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'meeting_id' is set
            if request.meeting_id is None:
                raise Exception("meeting_id is required and must be specified")
            # verify the required parameter 'instanceid' is set
            if request.instanceid is None:
                raise Exception("instanceid is required and must be specified")
            # path 参数
            if request.meeting_id is not None:
                api_req.path_params['meeting_id'] = request.meeting_id
            # query 参数
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            if request.userid is not None:
                api_req.query_params.append(('userid', request.userid))
            if request.instanceid is not None:
                api_req.query_params.append(('instanceid', request.instanceid))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1MeetingsMeetingIdEnrollConfigGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingsMeetingIdEnrollConfigGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meetings_meeting_id_enroll_config_put(
        self,
        request: ApiV1MeetingsMeetingIdEnrollConfigPutRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingsMeetingIdEnrollConfigPutResponse:
        """v1_meetings_meeting_id_enroll_config_put 修改会议报名配置[/v1/meetings/{meeting_id}/enroll/config - PUT]

            修改云会议的报名配置和报名问题，仅会议创建者可修改，且需要会议已开启报名。 企业 secret 鉴权用户可修改任何该企业该用户创建的有效会议，OAuth2.0 鉴权用户只能修改通过 OAuth2.0 鉴权创建的有效会议。 用户必须是注册用户，请求头部 X-TC-Registered 字段必须传入为1。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meetings/{meeting_id}/enroll/config",
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
                response = ApiV1MeetingsMeetingIdEnrollConfigPutResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingsMeetingIdEnrollConfigPut200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meetings_meeting_id_enroll_ids_post(
        self,
        request: ApiV1MeetingsMeetingIdEnrollIdsPostRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingsMeetingIdEnrollIdsPostResponse:
        """v1_meetings_meeting_id_enroll_ids_post 查询会议成员报名 ID[/v1/meetings/{meeting_id}/enroll/ids - POST]

            描述： 支持查询会议中已报名成员的报名 ID，仅会议创建者可查询。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meetings/{meeting_id}/enroll/ids",
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
                response = ApiV1MeetingsMeetingIdEnrollIdsPostResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingsMeetingIdEnrollIdsPost200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meetings_meeting_id_enroll_import_post(
        self,
        request: ApiV1MeetingsMeetingIdEnrollImportPostRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingsMeetingIdEnrollImportPostResponse:
        """v1_meetings_meeting_id_enroll_import_post 导入会议报名信息[/v1/meetings/{meeting_id}/enroll/import - POST]

            指定会议中导入报名信息。  企业 secret 鉴权用户可通过同企业下用户 userid 和手机号导入报名信息，OAuth2.0 鉴权用户能通过用户 open_id，与应用同企业下的 userid 以及手机号导入报名信息。 用户必须是注册用户，请求头部 X-TC-Registered 字段必须传入为1。 商业版单场会议导入上限1000条，企业版单场会议导入上限4000条。如需提升，请联系我们。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meetings/{meeting_id}/enroll/import",
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
                response = ApiV1MeetingsMeetingIdEnrollImportPostResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingsMeetingIdEnrollImportPost200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meetings_meeting_id_enroll_unregistration_delete(
        self,
        request: ApiV1MeetingsMeetingIdEnrollUnregistrationDeleteRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingsMeetingIdEnrollUnregistrationDeleteResponse:
        """v1_meetings_meeting_id_enroll_unregistration_delete 删除会议报名信息[/v1/meetings/{meeting_id}/enroll/unregistration - DELETE]

            描述： 删除指定会议的报名信息，支持删除用户手动报名的信息和导入的报名信息。 企业 secret 鉴权用户可删除该用户企业会议下的报名信息，OAuth2.0 鉴权用户只能删除通过 OAuth2.0 鉴权创建的有效会议的报名信息。 用户必须是注册用户，请求头部 X-TC-Registered 字段必须传入为1。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meetings/{meeting_id}/enroll/unregistration",
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
            api_resp = self.__config.clt.delete(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1MeetingsMeetingIdEnrollUnregistrationDeleteResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingsMeetingIdEnrollUnregistrationDelete200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meetings_meeting_id_get(
        self,
        request: ApiV1MeetingsMeetingIdGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingsMeetingIdGetResponse:
        """v1_meetings_meeting_id_get 查询会议[/v1/meetings/{meeting_id} - GET]

            通过会议 ID 查询会议详情。 企业 secret 鉴权用户可查询到任何该用户创建的企业下的会议，OAuth2.0 鉴权用户只能查询到通过 OAuth2.0 鉴权创建的会议。 本接口的邀请参会成员限制调整至300人。 当会议为周期性会议时，主持人密钥每场会议固定，但单场会议只能获取一次。支持查询周期性会议的主持人密钥。 支持查询 MRA 当前所在会议信息。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meetings/{meeting_id}",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'meeting_id' is set
            if request.meeting_id is None:
                raise Exception("meeting_id is required and must be specified")
            # verify the required parameter 'instanceid' is set
            if request.instanceid is None:
                raise Exception("instanceid is required and must be specified")
            # path 参数
            if request.meeting_id is not None:
                api_req.path_params['meeting_id'] = request.meeting_id
            # query 参数
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            if request.userid is not None:
                api_req.query_params.append(('userid', request.userid))
            if request.instanceid is not None:
                api_req.query_params.append(('instanceid', request.instanceid))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1MeetingsMeetingIdGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingsMeetingIdGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meetings_meeting_id_invitees_get(
        self,
        request: ApiV1MeetingsMeetingIdInviteesGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingsMeetingIdInviteesGetResponse:
        """v1_meetings_meeting_id_invitees_get 获取会议受邀成员列表[/v1/meetings/{meeting_id}/invitees - GET]

            根据会议ID获取受邀成员列表，支持分页获取，只有会议的创建者才有权限获取。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meetings/{meeting_id}/invitees",
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
            if request.pos is not None:
                api_req.query_params.append(('pos', request.pos))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1MeetingsMeetingIdInviteesGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingsMeetingIdInviteesGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meetings_meeting_id_invitees_put(
        self,
        request: ApiV1MeetingsMeetingIdInviteesPutRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingsMeetingIdInviteesPutResponse:
        """v1_meetings_meeting_id_invitees_put 设置会议邀请成员[/v1/meetings/{meeting_id}/invitees - PUT]

            根据会议ID设置邀请成员，只有会议的创建者才有权限设置。 最多可以设置2000名邀请者。 注：本接口为覆盖式设置。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meetings/{meeting_id}/invitees",
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
                response = ApiV1MeetingsMeetingIdInviteesPutResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meetings_meeting_id_participants_get(
        self,
        request: ApiV1MeetingsMeetingIdParticipantsGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingsMeetingIdParticipantsGetResponse:
        """v1_meetings_meeting_id_participants_get 获取参会成员列表[/v1/meetings/{meetingId}/participants - GET]

            会议创建者和企业管理员可以查询参会成员的列表，其他用户的调用会被拒绝。  支持查询网络研讨会参会成员列表。 如果会议还未开始，调用此接口查询会返回空列表。 企业 secret 鉴权用户（会议创建者）可获取任何该企业该用户创建的有效会议中的参会成员，企业 secret 鉴权用户（企业超级管理员）可获取任何该企业下创建的有效会议中的参会成员，OAuth2.0 鉴权用户（会议创建者）只能获取用户通过 OAuth2.0 鉴权创建的有效会议中的参会成员。 当您需要实时监测参会成员入会状态或退会状态时，您可以通过订阅 [用户入会](https://cloud.tencent.com/document/product/1095/51620)和 [用户离会](https://cloud.tencent.com/document/product/1095/51622) 的事件，接收事件通知。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meetings/{meetingId}/participants",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'meeting_id' is set
            if request.meeting_id is None:
                raise Exception("meeting_id is required and must be specified")
            # path 参数
            if request.meeting_id is not None:
                api_req.path_params['meetingId'] = request.meeting_id
            # query 参数
            if request.sub_meeting_id is not None:
                api_req.query_params.append(('sub_meeting_id', request.sub_meeting_id))
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            if request.userid is not None:
                api_req.query_params.append(('userid', request.userid))
            if request.pos is not None:
                api_req.query_params.append(('pos', request.pos))
            if request.size is not None:
                api_req.query_params.append(('size', request.size))
            if request.start_time is not None:
                api_req.query_params.append(('start_time', request.start_time))
            if request.end_time is not None:
                api_req.query_params.append(('end_time', request.end_time))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1MeetingsMeetingIdParticipantsGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingsMeetingIdParticipantsGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meetings_meeting_id_put(
        self,
        request: ApiV1MeetingsMeetingIdPutRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingsMeetingIdPutResponse:
        """v1_meetings_meeting_id_put 修改会议[/v1/meetings/{meeting_id} - PUT]

            修改某指定会议的会议信息。  企业 secret 鉴权用户可修改任何该企业该用户创建的有效会议，OAuth2.0 鉴权用户只能修改通过 OAuth2.0 鉴权创建的有效会议。 当您想实时监测会议修改状况时，您可以通过订阅 [会议更新](https://cloud.tencent.com/document/product/1095/51615) 的事件，接收事件通知。 本接口的邀请参会成员限制调整至300人。 当会议为周期性会议时，主持人密钥每场会议固定，但单场会议只能获取一次。支持修改周期性会议的主持人密钥。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meetings/{meeting_id}",
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
                response = ApiV1MeetingsMeetingIdPutResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingsMeetingIdPut200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meetings_meeting_id_qos_get(
        self,
        request: ApiV1MeetingsMeetingIdQosGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingsMeetingIdQosGetResponse:
        """v1_meetings_meeting_id_qos_get 获取会议实时质量检测数据[/v1/meetings/{meeting_id}/qos - GET]

            拥有企业“会议列表--会控”权限的成员，能够获取实时会议质量检测数据。 支持云会议和Webinar会议的数据。会议状态为进行中。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meetings/{meeting_id}/qos",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'meeting_id' is set
            if request.meeting_id is None:
                raise Exception("meeting_id is required and must be specified")
            # verify the required parameter 'operator_id' is set
            if request.operator_id is None:
                raise Exception("operator_id is required and must be specified")
            # verify the required parameter 'operator_id_type' is set
            if request.operator_id_type is None:
                raise Exception("operator_id_type is required and must be specified")
            # path 参数
            if request.meeting_id is not None:
                api_req.path_params['meeting_id'] = request.meeting_id
            # query 参数
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            if request.page_size is not None:
                api_req.query_params.append(('page_size', request.page_size))
            if request.page is not None:
                api_req.query_params.append(('page', request.page))
            if request.to_operator_id is not None:
                api_req.query_params.append(('to_operator_id', request.to_operator_id))
            if request.to_operator_id_type is not None:
                api_req.query_params.append(('to_operator_id_type', request.to_operator_id_type))
            if request.key is not None:
                api_req.query_params.append(('key', request.key))
            if request.min_value is not None:
                api_req.query_params.append(('min_value', request.min_value))
            if request.max_value is not None:
                api_req.query_params.append(('max_value', request.max_value))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1MeetingsMeetingIdQosGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingsMeetingIdQosGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meetings_meeting_id_quality_get(
        self,
        request: ApiV1MeetingsMeetingIdQualityGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingsMeetingIdQualityGetResponse:
        """v1_meetings_meeting_id_quality_get 查询会议健康度[/v1/meetings/{meeting_id}/quality - GET]

            查询会议及参会成员的健康度，付费开通该服务的企业管理员、超管可以查询，与是否为会议创建者/主持人/联席主持人无关。 鉴权方式：支持 JWT 鉴权 和 Oauth 鉴权
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meetings/{meeting_id}/quality",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'meeting_id' is set
            if request.meeting_id is None:
                raise Exception("meeting_id is required and must be specified")
            # verify the required parameter 'operator_id' is set
            if request.operator_id is None:
                raise Exception("operator_id is required and must be specified")
            # verify the required parameter 'operator_id_type' is set
            if request.operator_id_type is None:
                raise Exception("operator_id_type is required and must be specified")
            # verify the required parameter 'page_size' is set
            if request.page_size is None:
                raise Exception("page_size is required and must be specified")
            # verify the required parameter 'page' is set
            if request.page is None:
                raise Exception("page is required and must be specified")
            # verify the required parameter 'start_time' is set
            if request.start_time is None:
                raise Exception("start_time is required and must be specified")
            # path 参数
            if request.meeting_id is not None:
                api_req.path_params['meeting_id'] = request.meeting_id
            # query 参数
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            if request.instanceid is not None:
                api_req.query_params.append(('instanceid', request.instanceid))
            if request.sub_meeting_id is not None:
                api_req.query_params.append(('sub_meeting_id', request.sub_meeting_id))
            if request.page_size is not None:
                api_req.query_params.append(('page_size', request.page_size))
            if request.page is not None:
                api_req.query_params.append(('page', request.page))
            if request.start_time is not None:
                api_req.query_params.append(('start_time', request.start_time))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1MeetingsMeetingIdQualityGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingsMeetingIdQualityGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meetings_meeting_id_real_time_participants_get(
        self,
        request: ApiV1MeetingsMeetingIdRealTimeParticipantsGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingsMeetingIdRealTimeParticipantsGetResponse:
        """v1_meetings_meeting_id_real_time_participants_get 查询实时会中成员列表[/v1/meetings/{meeting_id}/real-time-participants - GET]

            查询当前会中成员列表，仅包括会中的成员，如果已离会，则不展示 企业超级管理员、会议创建者、会议主持人、会议联席主持人可以查询该数据。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meetings/{meeting_id}/real-time-participants",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'meeting_id' is set
            if request.meeting_id is None:
                raise Exception("meeting_id is required and must be specified")
            # verify the required parameter 'operator_id' is set
            if request.operator_id is None:
                raise Exception("operator_id is required and must be specified")
            # verify the required parameter 'operator_id_type' is set
            if request.operator_id_type is None:
                raise Exception("operator_id_type is required and must be specified")
            # verify the required parameter 'page' is set
            if request.page is None:
                raise Exception("page is required and must be specified")
            # verify the required parameter 'page_size' is set
            if request.page_size is None:
                raise Exception("page_size is required and must be specified")
            # path 参数
            if request.meeting_id is not None:
                api_req.path_params['meeting_id'] = request.meeting_id
            # query 参数
            if request.sub_meeting_id is not None:
                api_req.query_params.append(('sub_meeting_id', request.sub_meeting_id))
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            if request.page is not None:
                api_req.query_params.append(('page', request.page))
            if request.page_size is not None:
                api_req.query_params.append(('page_size', request.page_size))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1MeetingsMeetingIdRealTimeParticipantsGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingsMeetingIdRealTimeParticipantsGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meetings_meeting_id_virtual_background_post(
        self,
        request: ApiV1MeetingsMeetingIdVirtualBackgroundPostRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingsMeetingIdVirtualBackgroundPostResponse:
        """v1_meetings_meeting_id_virtual_background_post 设置会议统一虚拟背景[/v1/meetings/{meeting_id}/virtual-background - POST]

            非进行中非已结束的会议，会议创建者可以设置统一虚拟背景，并设置生效范围。如果企业未开启虚拟背景开关，则该企业下会议不可进行该设置。异步方式上传。支持云会议和Webinar会议，其中Webinar会议设置为对嘉宾生效，且不能指定成员
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meetings/{meeting_id}/virtual-background",
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
                response = ApiV1MeetingsMeetingIdVirtualBackgroundPostResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingsMeetingIdVirtualBackgroundPost200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meetings_meeting_id_waiting_room_participants_get(
        self,
        request: ApiV1MeetingsMeetingIdWaitingRoomParticipantsGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingsMeetingIdWaitingRoomParticipantsGetResponse:
        """v1_meetings_meeting_id_waiting_room_participants_get 获取实时等候室成员列表[/v1/meetings/{meeting_id}/waiting-room-participants - GET]

            **描述**：  * 会议拥有者获取某指定会议的等候室成员列表，需开启等候室且为“会议进行中”状态。 * 只有会议的拥有者即创建者可以查询等候室成员列表，其他用户的调用会被拒绝。如果会议非进行中，调用此接口查询会返回空列表。 * 企业 secret 鉴权用户（会议创建者）可获取任何该企业该用户创建的会议中的等候室成员列表，OAuth2.0 鉴权用户（会议创建者）只能获取用户通过 OAuth2.0 鉴权创建的会议中的等候室成员列表。 * 此接口暂不支持 MRA 设备作为被操作者的情况。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meetings/{meeting_id}/waiting-room-participants",
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
            # path 参数
            if request.meeting_id is not None:
                api_req.path_params['meeting_id'] = request.meeting_id
            # query 参数
            if request.userid is not None:
                api_req.query_params.append(('userid', request.userid))
            if request.page_size is not None:
                api_req.query_params.append(('page_size', request.page_size))
            if request.page is not None:
                api_req.query_params.append(('page', request.page))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1MeetingsMeetingIdWaitingRoomParticipantsGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingsMeetingIdWaitingRoomParticipantsGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meetings_post(
        self,
        request: ApiV1MeetingsPostRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingsPostResponse:
        """v1_meetings_post 创建会议[/v1/meetings - POST]

            快速创建或预定一个会议。  企业 secret 鉴权用户可创建该用户所属企业下的会议，OAuth2.0 鉴权用户只能创建该企业下 OAuth2.0 应用的会议。 用户必须是注册用户，请求头部 X-TC-Registered 字段必须传入为1。 当您想实时监测会议创建状况时，您可以通过订阅 [会议创建](https://cloud.tencent.com/document/product/1095/51614) 的事件，接收事件通知。 本接口的邀请参会成员限制调整至300人。 当会议为周期性会议时，主持人密钥每场会议固定，但单场会议只能获取一次。支持创建周期性会议的主持人密钥。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meetings",
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
                response = ApiV1MeetingsPostResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingsPost200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meetings_query_meetingid_for_device_post(
        self,
        request: ApiV1MeetingsQueryMeetingidForDevicePostRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingsQueryMeetingidForDevicePostResponse:
        """v1_meetings_query_meetingid_for_device_post 查询用户设备是否入会[/v1/meetings/query/meetingid-for-device - POST]

            查询用户设备是否入会接口，用来查询本企业用户在当前时间是否有设备进入指定的会议中。 不支持OAuth2.0鉴权方式访问。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meetings/query/meetingid-for-device",
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
                response = ApiV1MeetingsQueryMeetingidForDevicePostResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingsQueryMeetingidForDevicePost200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_pmi_meetings_get(
        self,
        request: ApiV1PmiMeetingsGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1PmiMeetingsGetResponse:
        """v1_pmi_meetings_get 查询个人会议号会议列表[/v1/pmi-meetings - GET]

            查询个人会议号（PMI）会议的会议列表（待开始、进行中、已结束），目前暂不支持 OAuth2.0 鉴权访问。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/pmi-meetings",
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
            # query 参数
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
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
                response = ApiV1PmiMeetingsGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1PmiMeetingsGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

