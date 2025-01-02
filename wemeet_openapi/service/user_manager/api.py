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
from wemeet_openapi.service.user_manager.model import *

from requests_toolbelt import MultipartEncoder


class ApiV1AuthUsersCancelAuthPutRequest(object):
    """取消用户授权

    第三方应用可以调用该接口来取消用户的授权，针对商业版和企业版用户仅支持在授权用户所属企业开启允许企业成员自主授权应用模式时取消，且由企业管理员开通的应用无法通过接口进行取消。如果企业开启了仅管理员可授权应用，用户只能在 腾讯会议应用管理页取消授权，无法在第三方平台取消。仅支持 OAuth2.0 鉴权方式调用。
    
    :param operator_id: 操作者ID (required)
    :type operator_id: str

    :param operator_id_type: 操作者ID类型 (required)
    :type operator_id_type: str





    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        
        
        
        
        self.body = body

class ApiV1AuthUsersCancelAuthPutResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MeetingsMeetingIdMsOpenIdGetRequest(object):
    """查询 ms_open_id

    **查询指定会议的用户的 ms\\_open\\_id，支持在会议开始前查询。** 支持企业自建应用（JWT 鉴权），仅支持查询本企业创建的会议。 <span class=\"colour\" style=\"color:rgb(44, 51, 60)\">支持OAuth2.0鉴权，仅支持查询该应用所创建的会议。</span>
    
    :param meeting_id: (required)
    :type meeting_id: str

    :param operator_id: 操作者 ID。operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 (required)
    :type operator_id: str

    :param operator_id_type: 操作者 ID 的类型： 1: userid 2: open_id 3. rooms_id (required)
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

class ApiV1MeetingsMeetingIdMsOpenIdGetResponse(ApiResponse):
    data: Optional[V1MeetingsMeetingIdMsOpenIdGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MeetingsMeetingIdMsOpenIdGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1PmiMeetingsPmiConfigGetRequest(object):
    """查询个人会议号配置信息

    获取用户个人会议号配置信息。仅企业下 secret 鉴权用户可获取该用户的 pmi 配置。目前暂不支持 OAuth 2.0鉴权访问。
    
    :param userid: (required)
    :type userid: str

    :param instanceid: 用户的终端设备类型： 0：PSTN 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：Linux 20：Rooms for Touch Windows 21：Rooms for Touch MacOS 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch iOS
    :type instanceid: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        userid: Optional[str] = None,
        instanceid: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.userid = userid
        self.instanceid = instanceid
        self.body = body

class ApiV1PmiMeetingsPmiConfigGetResponse(ApiResponse):
    data: Optional[V1PmiMeetingsPmiConfigGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1PmiMeetingsPmiConfigGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1PmiMeetingsPmiConfigPutRequest(object):
    """修改个人会议号配置信息

    修改个人会议号的基本配置信息
    
    :param body:
    :type body: V1PmiMeetingsPmiConfigPutRequest
    """  # noqa: E501


    def __init__(
        self,
        body: Optional[V1PmiMeetingsPmiConfigPutRequest] = None
    ):
        self.body = body

class ApiV1PmiMeetingsPmiConfigPutResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1UsersAccountAiAccountDeleteRequest(object):
    """移除AI账号能力

    移除企业账号的AI账号能力 权限点：企业用户管理，待自建应用支持权限点需求上线后生效
    
    :param body:
    :type body: V1UsersAccountAiAccountDeleteRequest
    """  # noqa: E501


    def __init__(
        self,
        body: Optional[V1UsersAccountAiAccountDeleteRequest] = None
    ):
        self.body = body

class ApiV1UsersAccountAiAccountDeleteResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1UsersAccountAiAccountPostRequest(object):
    """添加AI账号能力

    设置企业账号AI账号能力 权限点：企业用户管理。
    
    :param body:
    :type body: V1UsersAccountAiAccountPostRequest
    """  # noqa: E501


    def __init__(
        self,
        body: Optional[V1UsersAccountAiAccountPostRequest] = None
    ):
        self.body = body

class ApiV1UsersAccountAiAccountPostResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1UsersAccountStatisticsGetRequest(object):
    """获取账号资源统计

    查询企业下账号资源使用情况。 自建应用权限点：企业用户查看
    
    :param operator_id: 操作人ID，用户拥有企管用户查看权限 (required)
    :type operator_id: str

    :param operator_id_type: 操作人ID类型 1:userid (required)
    :type operator_id_type: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.body = body

class ApiV1UsersAccountStatisticsGetResponse(ApiResponse):
    data: Optional[V1UsersAccountStatisticsGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1UsersAccountStatisticsGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1UsersAdvanceListGetRequest(object):
    """获取用户列表（新）

    获取企业用户列表，支持高级搜索。企微企业暂不支持使用该接口。 自建应用权限点：查看企业用户，管理企业用户
    
    :param operator_id: (required)
    :type operator_id: str

    :param operator_id_type: (required)
    :type operator_id_type: str

    :param pos: 分页获取用户列表的查询起始位置值。当企业用户较多时，建议使用此参数进行分页查询，避免查询超时。此参数为非必选参数，默认值为空，从头开始查询。 设置每页返回的数量，请参考参数“size”的说明。查询返回输出参数“has_remaining”为 true，表示人数较多，需要继续查询。返回参数“next_pos”的值即为下一次查询的 pos 的值。多次调用该查询接口直到输出参数“has_remaining”值为 false。
    :type pos: str

    :param size: 目前每页支持最大100条。
    :type size: str

    :param status: 账号状态。1：正常  3：未激活 4：禁用 
    :type status: str

    :param user_account_type: 账号类型。 1：高级 2：免费
    :type user_account_type: str

    :param enable_ai_account: 是否有 AI 账号能力。 true：有  false：无 
    :type enable_ai_account: str

    :param department_id: 指定拉取的部门信息，不传则拉取全企业，需有指定范围的管理权限
    :type department_id: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        pos: Optional[str] = None,
        size: Optional[str] = None,
        status: Optional[str] = None,
        user_account_type: Optional[str] = None,
        enable_ai_account: Optional[str] = None,
        department_id: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.pos = pos
        self.size = size
        self.status = status
        self.user_account_type = user_account_type
        self.enable_ai_account = enable_ai_account
        self.department_id = department_id
        self.body = body

class ApiV1UsersAdvanceListGetResponse(ApiResponse):
    data: Optional[V1UsersAdvanceListGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1UsersAdvanceListGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1UsersDeleteRequest(object):
    """删除用户（通过 uuid 删除用户）

    
    :param uuid: (required)
    :type uuid: str

    :param operator_id: 操作者ID (required)
    :type operator_id: str

    :param operator_id_type: 操作者ID类型 (required)
    :type operator_id_type: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        uuid: Optional[str] = None,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.uuid = uuid
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.body = body

class ApiV1UsersDeleteResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1UsersDeleteTransferPostRequest(object):
    """用户资产转移

    
    :param body:
    :type body: V1UsersDeleteTransferPostRequest
    """  # noqa: E501


    def __init__(
        self,
        body: Optional[V1UsersDeleteTransferPostRequest] = None
    ):
        self.body = body

class ApiV1UsersDeleteTransferPostResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1UsersGetRequest(object):
    """获取用户详情（通过 uuid 获取用户详情）

    使用 uuid 获取企业用户详情。企业 secret 鉴权用户可获取该用户所属企业下的用户详情，暂不支持 OAuth2.0 鉴权访问。
    
    :param uuid: (required)
    :type uuid: str

    :param operator_id: 操作者ID (required)
    :type operator_id: str

    :param operator_id_type: 操作者ID类型，1:userid，2:open_id (required)
    :type operator_id_type: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        uuid: Optional[str] = None,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.uuid = uuid
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.body = body

class ApiV1UsersGetResponse(ApiResponse):
    data: Optional[V1UsersGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1UsersGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1UsersInfoBasicGetRequest(object):
    """获取用户基本信息

    
    :param operator_id: 操作者 ID，该接口不支持获取 MRA、Rooms、小程序的账号。 operator_id 必须与operator_id_type 配合使用。 根据 operator_id_type 的值，operator_id 代表不同类型。 (required)
    :type operator_id: str

    :param operator_id_type: 操作者 ID 的类型，2：openid。 (required)
    :type operator_id_type: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.body = body

class ApiV1UsersInfoBasicGetResponse(ApiResponse):
    data: Optional[V1UsersInfoBasicGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1UsersInfoBasicGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1UsersInviteActivatePostRequest(object):
    """获取账号激活链接

    未激活的账号，可以获取激活链接，激活链接有效期是48h。 每次获取链接为一个新链接，账号信息不变，旧链接仍然48h有效。
    
    :param body:
    :type body: V1UsersInviteActivatePostRequest
    """  # noqa: E501


    def __init__(
        self,
        body: Optional[V1UsersInviteActivatePostRequest] = None
    ):
        self.body = body

class ApiV1UsersInviteActivatePostResponse(ApiResponse):
    data: Optional[V1UsersInviteActivatePost200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1UsersInviteActivatePost200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1UsersInviteAuthPostRequest(object):
    """获取安全验证链接

    ●未验证的账号，可以获取验证链接，验证链接有效期是 48h，每次获取链接为一个新链接，账号信息不变，旧链接仍然48h有效。 ●如果没有绑定手机号，不支持调用。 ●每个 userid每天可获取10次验证链接。 
    
    :param body:
    :type body: V1UsersInviteAuthPostRequest
    """  # noqa: E501


    def __init__(
        self,
        body: Optional[V1UsersInviteAuthPostRequest] = None
    ):
        self.body = body

class ApiV1UsersInviteAuthPostResponse(ApiResponse):
    data: Optional[V1UsersInviteAuthPost200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1UsersInviteAuthPost200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1UsersListGetRequest(object):
    """获取用户列表

    获取企业用户列表，目前暂不支持 OAuth2.0 鉴权访问。
    
    :param page: 当前页，大于等于1。 (required)
    :type page: str

    :param page_size: 分页大小，最大为20。 (required)
    :type page_size: str

    :param operator_id: 操作者ID (required)
    :type operator_id: str

    :param operator_id_type: 操作者ID类型，1:userid,2:open_id (required)
    :type operator_id_type: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        page: Optional[str] = None,
        page_size: Optional[str] = None,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.page = page
        self.page_size = page_size
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.body = body

class ApiV1UsersListGetResponse(ApiResponse):
    data: Optional[V1UsersListGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1UsersListGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1UsersOpenIdToUseridPostRequest(object):
    """自建应用与三方应用 ID 转换接口

    **接口描述：** <span class=\"colour\" style=\"color:rgb(24, 43, 80)\">将三方应用获取到open_id转换为本企业用户的userid。</span> **鉴权方式：** JWT鉴权~~~~
    
    :param body:
    :type body: V1UsersOpenIdToUseridPostRequest
    """  # noqa: E501


    def __init__(
        self,
        body: Optional[V1UsersOpenIdToUseridPostRequest] = None
    ):
        self.body = body

class ApiV1UsersOpenIdToUseridPostResponse(ApiResponse):
    data: Optional[V1UsersOpenIdToUseridPost200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1UsersOpenIdToUseridPost200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1UsersPostRequest(object):
    """创建用户

    
    :param body:
    :type body: V1UsersPostRequest
    """  # noqa: E501


    def __init__(
        self,
        body: Optional[V1UsersPostRequest] = None
    ):
        self.body = body

class ApiV1UsersPostResponse(ApiResponse):
    data: Optional[V1UsersPost200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1UsersPost200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1UsersPutRequest(object):
    """更新用户（通过 uuid 更新用户）

    通过 uuid 更新用户
    
    :param uuid: (required)
    :type uuid: str

    :param body:
    :type body: V1UsersPutRequest
    """  # noqa: E501


    def __init__(
        self,
        uuid: Optional[str] = None,
        body: Optional[V1UsersPutRequest] = None
    ):
        self.uuid = uuid
        self.body = body

class ApiV1UsersPutResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1UsersUseridDeleteRequest(object):
    """删除用户（通过 userid 删除用户）

    
    :param userid: 被删除用户的userid (required)
    :type userid: str

    :param operator_id: 操作者ID (required)
    :type operator_id: str

    :param operator_id_type: 操作者ID类型，1:userid (required)
    :type operator_id_type: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        userid: str,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.userid = userid
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.body = body

class ApiV1UsersUseridDeleteResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1UsersUseridEnablePutRequest(object):
    """启用与禁用用户

    **接口描述：** 使用userid启用/禁用本企业下的用户。~~~~ **鉴权方式：** jwt鉴权 **输出参数：** <span class=\"colour\" style=\"color:rgb(51, 51, 51)\">无输出参数，成功返回空消息体，失败返回 [错误码](https://cloud.tencent.com/document/product/1095/43704) 和错误信息。</span>
    
    :param userid: 调用方用于标示用户的唯一 ID（例如：企业用户可以为企业账户英文名、个人用户可以为手机号等，暂不支持中文）。 (required)
    :type userid: str

    :param body:
    :type body: V1UsersUseridEnablePutRequest
    """  # noqa: E501


    def __init__(
        self,
        userid: str,
        body: Optional[V1UsersUseridEnablePutRequest] = None
    ):
        self.userid = userid
        self.body = body

class ApiV1UsersUseridEnablePutResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1UsersUseridGetRequest(object):
    """获取用户详情（通过 userid 获取用户详情）

    
    :param userid: 调用方用于标示用户的唯一 ID（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId）。 企业唯一用户标识说明： 1. 企业对接 SSO 时使用的员工唯一标识 ID； 2. 企业调用创建用户接口时传递的 userid 参数。  (required)
    :type userid: str

    :param operator_id: 操作者ID (required)
    :type operator_id: str

    :param operator_id_type: 操作者ID类型，1:userid,2:open_id (required)
    :type operator_id_type: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        userid: str,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.userid = userid
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.body = body

class ApiV1UsersUseridGetResponse(ApiResponse):
    data: Optional[V1UsersUseridGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1UsersUseridGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1UsersUseridInviteActivatePutRequest(object):
    """发送用户激活邀请

    通过 userid 发送认证短信或邮件，邀请用户认证账号，用户确认后账号变为激活态。若使用手机号创建发送短信，使用邮箱创建发送邮件。 仅未激活的用户能够成功发送激活邀请。 每个手机号或邮箱一天只能发送一次邀请 
    
    :param userid: 调用方用于标示用户的唯一 ID（例如：企业用户可以为企业账户英文名、个人用户可以为手机号等，暂不支持中文）。 (required)
    :type userid: str

    :param operator_id: 操作者ID (required)
    :type operator_id: str

    :param operator_id_type: 操作者ID类型，1:userid (required)
    :type operator_id_type: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        userid: str,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.userid = userid
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.body = body

class ApiV1UsersUseridInviteActivatePutResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1UsersUseridInviteAuthPutRequest(object):
    """用户安全验证

    ●通过 userid 发送验证短信，邀请成员验证账号，成员确认后账号变为已认证状态。 ●仅已激活的用户能够成功发送验证短信。 ●每个手机号一天只能发送一次邀请验证。 
    
    :param userid: (required)
    :type userid: str

    :param body:
    :type body: V1UsersUseridInviteAuthPutRequest
    """  # noqa: E501


    def __init__(
        self,
        userid: str,
        body: Optional[V1UsersUseridInviteAuthPutRequest] = None
    ):
        self.userid = userid
        self.body = body

class ApiV1UsersUseridInviteAuthPutResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1UsersUseridPutRequest(object):
    """更新用户（通过 userid 更新用户）

    
    :param userid: (required)
    :type userid: str

    :param body:
    :type body: V1UsersUseridPutRequest
    """  # noqa: E501


    def __init__(
        self,
        userid: str,
        body: Optional[V1UsersUseridPutRequest] = None
    ):
        self.userid = userid
        self.body = body

class ApiV1UsersUseridPutResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class UserManagerApi:
    def __init__(self, config: Config):
        self.__config = config

    def v1_auth_users_cancel_auth_put(
        self,
        request: ApiV1AuthUsersCancelAuthPutRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1AuthUsersCancelAuthPutResponse:
        """v1_auth_users_cancel_auth_put 取消用户授权[/v1/auth-users/cancel-auth - PUT]

            第三方应用可以调用该接口来取消用户的授权，针对商业版和企业版用户仅支持在授权用户所属企业开启允许企业成员自主授权应用模式时取消，且由企业管理员开通的应用无法通过接口进行取消。如果企业开启了仅管理员可授权应用，用户只能在 腾讯会议应用管理页取消授权，无法在第三方平台取消。仅支持 OAuth2.0 鉴权方式调用。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/auth-users/cancel-auth",
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
            # path 参数
            # query 参数
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            # 发送请求
            api_resp = self.__config.clt.put(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1AuthUsersCancelAuthPutResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_meetings_meeting_id_ms_open_id_get(
        self,
        request: ApiV1MeetingsMeetingIdMsOpenIdGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MeetingsMeetingIdMsOpenIdGetResponse:
        """v1_meetings_meeting_id_ms_open_id_get 查询 ms_open_id[/v1/meetings/{meeting_id}/ms-open-id - GET]

            **查询指定会议的用户的 ms\\_open\\_id，支持在会议开始前查询。** 支持企业自建应用（JWT 鉴权），仅支持查询本企业创建的会议。 <span class=\"colour\" style=\"color:rgb(44, 51, 60)\">支持OAuth2.0鉴权，仅支持查询该应用所创建的会议。</span>
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/meetings/{meeting_id}/ms-open-id",
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
                response = ApiV1MeetingsMeetingIdMsOpenIdGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MeetingsMeetingIdMsOpenIdGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_pmi_meetings_pmi_config_get(
        self,
        request: ApiV1PmiMeetingsPmiConfigGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1PmiMeetingsPmiConfigGetResponse:
        """v1_pmi_meetings_pmi_config_get 查询个人会议号配置信息[/v1/pmi-meetings/pmi-config - GET]

            获取用户个人会议号配置信息。仅企业下 secret 鉴权用户可获取该用户的 pmi 配置。目前暂不支持 OAuth 2.0鉴权访问。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/pmi-meetings/pmi-config",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'userid' is set
            if request.userid is None:
                raise Exception("userid is required and must be specified")
            # path 参数
            # query 参数
            if request.instanceid is not None:
                api_req.query_params.append(('instanceid', request.instanceid))
            if request.userid is not None:
                api_req.query_params.append(('userid', request.userid))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1PmiMeetingsPmiConfigGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1PmiMeetingsPmiConfigGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_pmi_meetings_pmi_config_put(
        self,
        request: ApiV1PmiMeetingsPmiConfigPutRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1PmiMeetingsPmiConfigPutResponse:
        """v1_pmi_meetings_pmi_config_put 修改个人会议号配置信息[/v1/pmi-meetings/pmi-config - PUT]

            修改个人会议号的基本配置信息
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/pmi-meetings/pmi-config",
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
                response = ApiV1PmiMeetingsPmiConfigPutResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_users_account_ai_account_delete(
        self,
        request: ApiV1UsersAccountAiAccountDeleteRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1UsersAccountAiAccountDeleteResponse:
        """v1_users_account_ai_account_delete 移除AI账号能力[/v1/users/account/ai-account - DELETE]

            移除企业账号的AI账号能力 权限点：企业用户管理，待自建应用支持权限点需求上线后生效
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/users/account/ai-account",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # path 参数
            # query 参数
            # 发送请求
            api_resp = self.__config.clt.delete(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1UsersAccountAiAccountDeleteResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_users_account_ai_account_post(
        self,
        request: ApiV1UsersAccountAiAccountPostRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1UsersAccountAiAccountPostResponse:
        """v1_users_account_ai_account_post 添加AI账号能力[/v1/users/account/ai-account - POST]

            设置企业账号AI账号能力 权限点：企业用户管理。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/users/account/ai-account",
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
                response = ApiV1UsersAccountAiAccountPostResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_users_account_statistics_get(
        self,
        request: ApiV1UsersAccountStatisticsGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1UsersAccountStatisticsGetResponse:
        """v1_users_account_statistics_get 获取账号资源统计[/v1/users/account/statistics - GET]

            查询企业下账号资源使用情况。 自建应用权限点：企业用户查看
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/users/account/statistics",
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
            # path 参数
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
                response = ApiV1UsersAccountStatisticsGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1UsersAccountStatisticsGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_users_advance_list_get(
        self,
        request: ApiV1UsersAdvanceListGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1UsersAdvanceListGetResponse:
        """v1_users_advance_list_get 获取用户列表（新）[/v1/users/advance/list - GET]

            获取企业用户列表，支持高级搜索。企微企业暂不支持使用该接口。 自建应用权限点：查看企业用户，管理企业用户
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/users/advance/list",
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
            # path 参数
            # query 参数
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            if request.pos is not None:
                api_req.query_params.append(('pos', request.pos))
            if request.size is not None:
                api_req.query_params.append(('size', request.size))
            if request.status is not None:
                api_req.query_params.append(('status', request.status))
            if request.user_account_type is not None:
                api_req.query_params.append(('user_account_type', request.user_account_type))
            if request.enable_ai_account is not None:
                api_req.query_params.append(('enable_ai_account', request.enable_ai_account))
            if request.department_id is not None:
                api_req.query_params.append(('department_id', request.department_id))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1UsersAdvanceListGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1UsersAdvanceListGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_users_delete(
        self,
        request: ApiV1UsersDeleteRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1UsersDeleteResponse:
        """v1_users_delete 删除用户（通过 uuid 删除用户）[/v1/users - DELETE]

        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/users",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'uuid' is set
            if request.uuid is None:
                raise Exception("uuid is required and must be specified")
            # verify the required parameter 'operator_id' is set
            if request.operator_id is None:
                raise Exception("operator_id is required and must be specified")
            # verify the required parameter 'operator_id_type' is set
            if request.operator_id_type is None:
                raise Exception("operator_id_type is required and must be specified")
            # path 参数
            # query 参数
            if request.uuid is not None:
                api_req.query_params.append(('uuid', request.uuid))
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            # 发送请求
            api_resp = self.__config.clt.delete(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1UsersDeleteResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_users_delete_transfer_post(
        self,
        request: ApiV1UsersDeleteTransferPostRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1UsersDeleteTransferPostResponse:
        """v1_users_delete_transfer_post 用户资产转移[/v1/users/delete-transfer - POST]

        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/users/delete-transfer",
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
                response = ApiV1UsersDeleteTransferPostResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_users_get(
        self,
        request: ApiV1UsersGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1UsersGetResponse:
        """v1_users_get 获取用户详情（通过 uuid 获取用户详情）[/v1/users - GET]

            使用 uuid 获取企业用户详情。企业 secret 鉴权用户可获取该用户所属企业下的用户详情，暂不支持 OAuth2.0 鉴权访问。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/users",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'uuid' is set
            if request.uuid is None:
                raise Exception("uuid is required and must be specified")
            # verify the required parameter 'operator_id' is set
            if request.operator_id is None:
                raise Exception("operator_id is required and must be specified")
            # verify the required parameter 'operator_id_type' is set
            if request.operator_id_type is None:
                raise Exception("operator_id_type is required and must be specified")
            # path 参数
            # query 参数
            if request.uuid is not None:
                api_req.query_params.append(('uuid', request.uuid))
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1UsersGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1UsersGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_users_info_basic_get(
        self,
        request: ApiV1UsersInfoBasicGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1UsersInfoBasicGetResponse:
        """v1_users_info_basic_get 获取用户基本信息[/v1/users/info/basic - GET]

        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/users/info/basic",
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
            # path 参数
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
                response = ApiV1UsersInfoBasicGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1UsersInfoBasicGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_users_invite_activate_post(
        self,
        request: ApiV1UsersInviteActivatePostRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1UsersInviteActivatePostResponse:
        """v1_users_invite_activate_post 获取账号激活链接[/v1/users/invite-activate - POST]

            未激活的账号，可以获取激活链接，激活链接有效期是48h。 每次获取链接为一个新链接，账号信息不变，旧链接仍然48h有效。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/users/invite-activate",
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
                response = ApiV1UsersInviteActivatePostResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1UsersInviteActivatePost200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_users_invite_auth_post(
        self,
        request: ApiV1UsersInviteAuthPostRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1UsersInviteAuthPostResponse:
        """v1_users_invite_auth_post 获取安全验证链接[/v1/users/invite-auth - POST]

            ●未验证的账号，可以获取验证链接，验证链接有效期是 48h，每次获取链接为一个新链接，账号信息不变，旧链接仍然48h有效。 ●如果没有绑定手机号，不支持调用。 ●每个 userid每天可获取10次验证链接。 
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/users/invite-auth",
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
                response = ApiV1UsersInviteAuthPostResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1UsersInviteAuthPost200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_users_list_get(
        self,
        request: ApiV1UsersListGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1UsersListGetResponse:
        """v1_users_list_get 获取用户列表[/v1/users/list - GET]

            获取企业用户列表，目前暂不支持 OAuth2.0 鉴权访问。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/users/list",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'page' is set
            if request.page is None:
                raise Exception("page is required and must be specified")
            # verify the required parameter 'page_size' is set
            if request.page_size is None:
                raise Exception("page_size is required and must be specified")
            # verify the required parameter 'operator_id' is set
            if request.operator_id is None:
                raise Exception("operator_id is required and must be specified")
            # verify the required parameter 'operator_id_type' is set
            if request.operator_id_type is None:
                raise Exception("operator_id_type is required and must be specified")
            # path 参数
            # query 参数
            if request.page is not None:
                api_req.query_params.append(('page', request.page))
            if request.page_size is not None:
                api_req.query_params.append(('page_size', request.page_size))
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1UsersListGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1UsersListGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_users_open_id_to_userid_post(
        self,
        request: ApiV1UsersOpenIdToUseridPostRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1UsersOpenIdToUseridPostResponse:
        """v1_users_open_id_to_userid_post 自建应用与三方应用 ID 转换接口[/v1/users/open-id-to-userid - POST]

            **接口描述：** <span class=\"colour\" style=\"color:rgb(24, 43, 80)\">将三方应用获取到open_id转换为本企业用户的userid。</span> **鉴权方式：** JWT鉴权~~~~
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/users/open-id-to-userid",
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
                response = ApiV1UsersOpenIdToUseridPostResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1UsersOpenIdToUseridPost200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_users_post(
        self,
        request: ApiV1UsersPostRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1UsersPostResponse:
        """v1_users_post 创建用户[/v1/users - POST]

        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/users",
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
                response = ApiV1UsersPostResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1UsersPost200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_users_put(
        self,
        request: ApiV1UsersPutRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1UsersPutResponse:
        """v1_users_put 更新用户（通过 uuid 更新用户）[/v1/users - PUT]

            通过 uuid 更新用户
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/users",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'uuid' is set
            if request.uuid is None:
                raise Exception("uuid is required and must be specified")
            # path 参数
            # query 参数
            if request.uuid is not None:
                api_req.query_params.append(('uuid', request.uuid))
            # 发送请求
            api_resp = self.__config.clt.put(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1UsersPutResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_users_userid_delete(
        self,
        request: ApiV1UsersUseridDeleteRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1UsersUseridDeleteResponse:
        """v1_users_userid_delete 删除用户（通过 userid 删除用户）[/v1/users/{userid} - DELETE]

        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/users/{userid}",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'userid' is set
            if request.userid is None:
                raise Exception("userid is required and must be specified")
            # verify the required parameter 'operator_id' is set
            if request.operator_id is None:
                raise Exception("operator_id is required and must be specified")
            # verify the required parameter 'operator_id_type' is set
            if request.operator_id_type is None:
                raise Exception("operator_id_type is required and must be specified")
            # path 参数
            if request.userid is not None:
                api_req.path_params['userid'] = request.userid
            # query 参数
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            # 发送请求
            api_resp = self.__config.clt.delete(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1UsersUseridDeleteResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_users_userid_enable_put(
        self,
        request: ApiV1UsersUseridEnablePutRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1UsersUseridEnablePutResponse:
        """v1_users_userid_enable_put 启用与禁用用户[/v1/users/{userid}/enable - PUT]

            **接口描述：** 使用userid启用/禁用本企业下的用户。~~~~ **鉴权方式：** jwt鉴权 **输出参数：** <span class=\"colour\" style=\"color:rgb(51, 51, 51)\">无输出参数，成功返回空消息体，失败返回 [错误码](https://cloud.tencent.com/document/product/1095/43704) 和错误信息。</span>
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/users/{userid}/enable",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'userid' is set
            if request.userid is None:
                raise Exception("userid is required and must be specified")
            # path 参数
            if request.userid is not None:
                api_req.path_params['userid'] = request.userid
            # query 参数
            # 发送请求
            api_resp = self.__config.clt.put(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1UsersUseridEnablePutResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_users_userid_get(
        self,
        request: ApiV1UsersUseridGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1UsersUseridGetResponse:
        """v1_users_userid_get 获取用户详情（通过 userid 获取用户详情）[/v1/users/{userid} - GET]

        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/users/{userid}",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'userid' is set
            if request.userid is None:
                raise Exception("userid is required and must be specified")
            # verify the required parameter 'operator_id' is set
            if request.operator_id is None:
                raise Exception("operator_id is required and must be specified")
            # verify the required parameter 'operator_id_type' is set
            if request.operator_id_type is None:
                raise Exception("operator_id_type is required and must be specified")
            # path 参数
            if request.userid is not None:
                api_req.path_params['userid'] = request.userid
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
                response = ApiV1UsersUseridGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1UsersUseridGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_users_userid_invite_activate_put(
        self,
        request: ApiV1UsersUseridInviteActivatePutRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1UsersUseridInviteActivatePutResponse:
        """v1_users_userid_invite_activate_put 发送用户激活邀请[/v1/users/{userid}/invite-activate - PUT]

            通过 userid 发送认证短信或邮件，邀请用户认证账号，用户确认后账号变为激活态。若使用手机号创建发送短信，使用邮箱创建发送邮件。 仅未激活的用户能够成功发送激活邀请。 每个手机号或邮箱一天只能发送一次邀请 
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/users/{userid}/invite-activate",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'userid' is set
            if request.userid is None:
                raise Exception("userid is required and must be specified")
            # verify the required parameter 'operator_id' is set
            if request.operator_id is None:
                raise Exception("operator_id is required and must be specified")
            # verify the required parameter 'operator_id_type' is set
            if request.operator_id_type is None:
                raise Exception("operator_id_type is required and must be specified")
            # path 参数
            if request.userid is not None:
                api_req.path_params['userid'] = request.userid
            # query 参数
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            # 发送请求
            api_resp = self.__config.clt.put(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1UsersUseridInviteActivatePutResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_users_userid_invite_auth_put(
        self,
        request: ApiV1UsersUseridInviteAuthPutRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1UsersUseridInviteAuthPutResponse:
        """v1_users_userid_invite_auth_put 用户安全验证[/v1/users/{userid}/invite-auth - PUT]

            ●通过 userid 发送验证短信，邀请成员验证账号，成员确认后账号变为已认证状态。 ●仅已激活的用户能够成功发送验证短信。 ●每个手机号一天只能发送一次邀请验证。 
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/users/{userid}/invite-auth",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'userid' is set
            if request.userid is None:
                raise Exception("userid is required and must be specified")
            # path 参数
            if request.userid is not None:
                api_req.path_params['userid'] = request.userid
            # query 参数
            # 发送请求
            api_resp = self.__config.clt.put(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1UsersUseridInviteAuthPutResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_users_userid_put(
        self,
        request: ApiV1UsersUseridPutRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1UsersUseridPutResponse:
        """v1_users_userid_put 更新用户（通过 userid 更新用户）[/v1/users/{userid} - PUT]

        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/users/{userid}",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'userid' is set
            if request.userid is None:
                raise Exception("userid is required and must be specified")
            # path 参数
            if request.userid is not None:
                api_req.path_params['userid'] = request.userid
            # query 参数
            # 发送请求
            api_resp = self.__config.clt.put(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1UsersUseridPutResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

