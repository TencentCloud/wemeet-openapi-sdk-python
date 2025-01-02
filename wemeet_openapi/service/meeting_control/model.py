# coding: utf-8

"""
    腾讯会议OpenAPI

    SAAS版RESTFUL风格API

    API version: v1.0.4

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

from typing import *


class V1MeetingsMeetingIdDismissPostRequest(object):
    """V1MeetingsMeetingIdDismissPostRequest

    :param force_dismiss_meeting: 是否强制结束会议，默认值为1：0：不强制结束会议，会议中有参会者，则无法强制结束会议 1 ：强制结束会议，会议中有参会者，也会强制结束会议 
    :type force_dismiss_meeting: Optional[int]

    :param instanceid: 设备类型 (required) 
    :type instanceid: int

    :param operator_id: 操作者ID，根据operator_id_type的值，使用不同的类型 
    :type operator_id: Optional[str]

    :param operator_id_type: 操作者ID的类型：1:userid  2:openid（预留编号，本次不添加，未来新增接口使用）3:rooms_id  4: ms_open_id 
    :type operator_id_type: Optional[int]

    :param reason_code: 原因代码，可为用户自定义 (required) 
    :type reason_code: int

    :param reason_detail: 取消原因 
    :type reason_detail: Optional[str]

    :param retrieve_code: 是否回收会议号，默认值为0： 0：不回收会议号，可以重新入会 1： 回收会议号，不可重新入会 
    :type retrieve_code: Optional[int]

    :param userid: 调用方用于标示用户的唯一 ID（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId）。 企业唯一用户标识说明：企业对接 SSO 时使用的员工唯一标识 ID，企业调用创建用户接口时传递的 userid 参数。 
    :type userid: Optional[str]
    """  # noqa: E501

    force_dismiss_meeting: Optional[int] = None
    instanceid: int
    operator_id: Optional[str] = None
    operator_id_type: Optional[int] = None
    reason_code: int
    reason_detail: Optional[str] = None
    retrieve_code: Optional[int] = None
    userid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        instanceid: int,
        reason_code: int,
        force_dismiss_meeting: Optional[int] = None,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[int] = None,
        reason_detail: Optional[str] = None,
        retrieve_code: Optional[int] = None,
        userid: Optional[str] = None,
        **kwargs
    ):
        self.force_dismiss_meeting = force_dismiss_meeting
        self.instanceid = instanceid
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.reason_code = reason_code
        self.reason_detail = reason_detail
        self.retrieve_code = retrieve_code
        self.userid = userid


class V1RealControlMeetingsMeetingIdAsrPut200Response(object):
    """V1RealControlMeetingsMeetingIdAsrPut200Response

    :param code:
    :type code: Optional[int]

    :param message:
    :type message: Optional[str]
    """  # noqa: E501

    code: Optional[int] = None
    message: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        code: Optional[int] = None,
        message: Optional[str] = None,
        **kwargs
    ):
        self.code = code
        self.message = message


class V1RealControlMeetingsMeetingIdAsrPutRequest(object):
    """V1RealControlMeetingsMeetingIdAsrPutRequest

    :param instance_id: 用户的终端设备类型：  0：PSTN  1：PC  2：Mac  3：Android  4：iOS  5：Web  6：iPad  7：Android Pad  8：小程序  9：voip、sip 设备  10：Linux  20：Rooms for Touch Windows  21：Rooms for Touch MacOS  22：Rooms for Touch Android  30：Controller for Touch Windows  32：Controller for Touch Android  33：Controller for Touch iOS (required) 
    :type instance_id: int

    :param is_open: 开启/关闭实时转写 true：开启实时转写 false：关闭实时转写 (required) 
    :type is_open: bool

    :param open_asr_view: 是否自动打开转写侧边栏，仅在is_open 为 true 时生效，默认为 0， 0：打开实时转写页面 。1：不打开实时转写页面 
    :type open_asr_view: Optional[int]

    :param operator_id: 操作者 ID。operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 
    :type operator_id: Optional[str]

    :param operator_id_type: 操作者 ID 的类型： 1：userid 
    :type operator_id_type: Optional[int]
    """  # noqa: E501

    instance_id: int
    is_open: bool
    open_asr_view: Optional[int] = None
    operator_id: Optional[str] = None
    operator_id_type: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        instance_id: int,
        is_open: bool,
        open_asr_view: Optional[int] = None,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[int] = None,
        **kwargs
    ):
        self.instance_id = instance_id
        self.is_open = is_open
        self.open_asr_view = open_asr_view
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type


class V1RealControlMeetingsMeetingIdCohostsPutRequest(object):
    """V1RealControlMeetingsMeetingIdCohostsPutRequest

    :param action: 具体设置动作： true：设置联席主持人， false：撤销联席主持人 (required) 
    :type action: bool

    :param instanceid: 用户的终端设备类型： 0：PSTN 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch MacOS 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch iOS 说明：使用 ms_open_id 进行调用时，仅支持以上1-8的设备类型。 (required) 
    :type instanceid: int

    :param operator_id: 操作者 ID。 1：operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 2：接口输入参数如果需要传用户 ID 时，operator_id 和 uuid 不可以同时为空，两个参数如果都传了以 operator_id 为准。 3：如果 operator_id_type=2，operator_id 必须和公共参数的 openid 一致。 
    :type operator_id: Optional[str]

    :param operator_id_type: 操作者 ID 的类型： 2：openid 4：ms_open_id 
    :type operator_id_type: Optional[int]

    :param user:(required) 
    :type user: V1RealControlMeetingsMeetingIdCohostsPutRequestUser

    :param uuid: 操作者用户唯一身份 ID，仅支持主持人，且只适用于单场会议。即将废弃，推荐使用ms_open_id。 
    :type uuid: Optional[str]
    """  # noqa: E501

    action: bool
    instanceid: int
    operator_id: Optional[str] = None
    operator_id_type: Optional[int] = None
    user: V1RealControlMeetingsMeetingIdCohostsPutRequestUser
    uuid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        action: bool,
        instanceid: int,
        user: V1RealControlMeetingsMeetingIdCohostsPutRequestUser | Dict[str, Any],
        operator_id: Optional[str] = None,
        operator_id_type: Optional[int] = None,
        uuid: Optional[str] = None,
        **kwargs
    ):
        self.action = action
        self.instanceid = instanceid
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.user = V1RealControlMeetingsMeetingIdCohostsPutRequestUser(**user) if isinstance(user, (dict, Dict)) else user
        self.uuid = uuid


class V1RealControlMeetingsMeetingIdCohostsPutRequestUser(object):
    """V1RealControlMeetingsMeetingIdCohostsPutRequestUser

    :param instanceid: 用户的终端设备类型： 0：PSTN 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch MacOS 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch iOS 说明：请与被操作者的设备类型保持一致，否则不生效。使用 ms_open_id 进行调用时，仅支持以上1-8的设备类型。 (required) 
    :type instanceid: int

    :param to_operator_id: 用户ID，根据to_operator_id_type的值，使用不同的类型 
    :type to_operator_id: Optional[str]

    :param to_operator_id_type: 用户ID的类型：  4: ms_open_id 
    :type to_operator_id_type: Optional[int]

    :param uuid: 用户的唯一标识uuid 
    :type uuid: Optional[str]
    """  # noqa: E501

    instanceid: int
    to_operator_id: Optional[str] = None
    to_operator_id_type: Optional[int] = None
    uuid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        instanceid: int,
        to_operator_id: Optional[str] = None,
        to_operator_id_type: Optional[int] = None,
        uuid: Optional[str] = None,
        **kwargs
    ):
        self.instanceid = instanceid
        self.to_operator_id = to_operator_id
        self.to_operator_id_type = to_operator_id_type
        self.uuid = uuid


class V1RealControlMeetingsMeetingIdDocPutRequest(object):
    """V1RealControlMeetingsMeetingIdDocPutRequest

    :param enable_upload_doc: 是否允许全员上传文档  true：是 false：否 (required) 
    :type enable_upload_doc: bool

    :param instanceid: 用户的终端设备类型： 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch Mac 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch Iphone (required) 
    :type instanceid: int

    :param operator_id: 操作者 ID。 1：operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 2：接口输入参数如果需要传用户 ID 时，operator_id 和 uuid 不可以同时为空，两个参数如果都传了以 operator_id 为准。 3：如果 operator_id_type=2，operator_id 必须和公共参数的 openid 一致。 
    :type operator_id: Optional[str]

    :param operator_id_type: 操作者ID的类型：  2:openid  4: ms_open_id 
    :type operator_id_type: Optional[int]

    :param uuid: 操作者用户唯一身份 ID，仅支持主持人和联席主持人，且只适用于单场会议。即将废弃，推荐使用ms_open_id。 
    :type uuid: Optional[str]
    """  # noqa: E501

    enable_upload_doc: bool
    instanceid: int
    operator_id: Optional[str] = None
    operator_id_type: Optional[int] = None
    uuid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        enable_upload_doc: bool,
        instanceid: int,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[int] = None,
        uuid: Optional[str] = None,
        **kwargs
    ):
        self.enable_upload_doc = enable_upload_doc
        self.instanceid = instanceid
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.uuid = uuid


class V1RealControlMeetingsMeetingIdKickoutPutRequest(object):
    """V1RealControlMeetingsMeetingIdKickoutPutRequest

    :param allow_rejoin: 移出后是否允许再次入会： true：允许再次入会 false：不允许 (required) 
    :type allow_rejoin: bool

    :param instanceid: 用户的终端设备类型： 0：PSTN 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch MacOS 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch iOS (required) 
    :type instanceid: int

    :param operator_id: 操作者 ID。 1：operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 2：接口输入参数如果需要传用户 ID 时，operator_id 和 uuid 不可以同时为空，两个参数如果都传了以 operator_id 为准。 3：如果 operator_id_type=2，operator_id 必须和公共参数的 openid 一致。 
    :type operator_id: Optional[str]

    :param operator_id_type: 操作者ID的类型：2:openid 4: ms_open_id 
    :type operator_id_type: Optional[int]

    :param reason: 移出原因说明。当用户设备为 MRA 时，该参数必须填写移出原因。 
    :type reason: Optional[str]

    :param users: 被操作用户对象信息列表 (required) 
    :type users: List[V1RealControlMeetingsMeetingIdKickoutPutRequestUsersInner]

    :param uuid: 操作者用户唯一身份 ID，仅支持主持人和联席主持人，且只适用于单场会议。即将废弃，推荐使用ms_open_id。 
    :type uuid: Optional[str]
    """  # noqa: E501

    allow_rejoin: bool
    instanceid: int
    operator_id: Optional[str] = None
    operator_id_type: Optional[int] = None
    reason: Optional[str] = None
    users: List[V1RealControlMeetingsMeetingIdKickoutPutRequestUsersInner]
    uuid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        allow_rejoin: bool,
        instanceid: int,
        users: List[V1RealControlMeetingsMeetingIdKickoutPutRequestUsersInner] | List[Dict[str, Any]],
        operator_id: Optional[str] = None,
        operator_id_type: Optional[int] = None,
        reason: Optional[str] = None,
        uuid: Optional[str] = None,
        **kwargs
    ):
        self.allow_rejoin = allow_rejoin
        self.instanceid = instanceid
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.reason = reason
        
        if users and isinstance(users, (list, List)):
            self.users = [V1RealControlMeetingsMeetingIdKickoutPutRequestUsersInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in users]
        
        self.uuid = uuid


class V1RealControlMeetingsMeetingIdKickoutPutRequestUsersInner(object):
    """V1RealControlMeetingsMeetingIdKickoutPutRequestUsersInner

    :param instanceid: 用户的终端设备类型： 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch Mac 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch Iphone (required) 
    :type instanceid: int

    :param to_operator_id: 用户ID，根据to_operator_id_type的值，使用不同的类型 
    :type to_operator_id: Optional[str]

    :param to_operator_id_type: 用户ID的类型： 4: ms_open_id 
    :type to_operator_id_type: Optional[int]

    :param uuid: 用户的唯一标识uuid 
    :type uuid: Optional[str]
    """  # noqa: E501

    instanceid: int
    to_operator_id: Optional[str] = None
    to_operator_id_type: Optional[int] = None
    uuid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        instanceid: int,
        to_operator_id: Optional[str] = None,
        to_operator_id_type: Optional[int] = None,
        uuid: Optional[str] = None,
        **kwargs
    ):
        self.instanceid = instanceid
        self.to_operator_id = to_operator_id
        self.to_operator_id_type = to_operator_id_type
        self.uuid = uuid


class V1RealControlMeetingsMeetingIdMutesPutRequest(object):
    """V1RealControlMeetingsMeetingIdMutesPutRequest

    :param instanceid: 用户的终端设备类型： 0：PSTN 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch MacOS 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch iOS (required) 
    :type instanceid: int

    :param mute: 是否静音： true：静音 false：解除静音 (required) 
    :type mute: bool

    :param operator_id: 操作者 ID。 1：operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 2：接口输入参数如果需要传用户 ID 时，operator_id 和 uuid 不可以同时为空，两个参数如果都传了以 operator_id 为准。 3：如果 operator_id_type=2，operator_id 必须和公共参数的 openid 一致。 
    :type operator_id: Optional[str]

    :param operator_id_type: 操作者ID的类型：2:openid 4: ms_open_id 
    :type operator_id_type: Optional[int]

    :param user:(required) 
    :type user: V1RealControlMeetingsMeetingIdMutesPutRequestUser

    :param uuid: 操作者用户唯一身份 ID，仅支持主持人和联席主持人，且只适用于单场会议。即将废弃，推荐使用ms_open_id。 
    :type uuid: Optional[str]
    """  # noqa: E501

    instanceid: int
    mute: bool
    operator_id: Optional[str] = None
    operator_id_type: Optional[int] = None
    user: V1RealControlMeetingsMeetingIdMutesPutRequestUser
    uuid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        instanceid: int,
        mute: bool,
        user: V1RealControlMeetingsMeetingIdMutesPutRequestUser | Dict[str, Any],
        operator_id: Optional[str] = None,
        operator_id_type: Optional[int] = None,
        uuid: Optional[str] = None,
        **kwargs
    ):
        self.instanceid = instanceid
        self.mute = mute
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.user = V1RealControlMeetingsMeetingIdMutesPutRequestUser(**user) if isinstance(user, (dict, Dict)) else user
        self.uuid = uuid


class V1RealControlMeetingsMeetingIdMutesPutRequestUser(object):
    """V1RealControlMeetingsMeetingIdMutesPutRequestUser

    :param instanceid: 用户的终端设备类型： 0：PSTN 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch MacOS 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch iOS 说明：请与被操作者的设备类型保持一致，否则不生效。 (required) 
    :type instanceid: int

    :param to_operator_id: 用户ID，根据to_operator_id_type的值，使用不同的类型 
    :type to_operator_id: Optional[str]

    :param to_operator_id_type: 用户ID的类型：  4: ms_open_id 
    :type to_operator_id_type: Optional[int]

    :param uuid: 用户的唯一标识uuid 
    :type uuid: Optional[str]
    """  # noqa: E501

    instanceid: int
    to_operator_id: Optional[str] = None
    to_operator_id_type: Optional[int] = None
    uuid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        instanceid: int,
        to_operator_id: Optional[str] = None,
        to_operator_id_type: Optional[int] = None,
        uuid: Optional[str] = None,
        **kwargs
    ):
        self.instanceid = instanceid
        self.to_operator_id = to_operator_id
        self.to_operator_id_type = to_operator_id_type
        self.uuid = uuid


class V1RealControlMeetingsMeetingIdNamesPutRequest(object):
    """V1RealControlMeetingsMeetingIdNamesPutRequest

    :param instanceid: 用户的终端设备类型： 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch Mac 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch Iphone (required) 
    :type instanceid: int

    :param operator_id: 操作者 ID。 1：operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 2：如果 operator_id_type=2，operator_id 必须和公共参数的 openid 一致。 (required) 
    :type operator_id: str

    :param operator_id_type: 操作者ID的类型：2:openid 4: ms_open_id (required) 
    :type operator_id_type: int

    :param users: 要改名的用户 (required) 
    :type users: List[V1RealControlMeetingsMeetingIdNamesPutRequestUsersInner]
    """  # noqa: E501

    instanceid: int
    operator_id: str
    operator_id_type: int
    users: List[V1RealControlMeetingsMeetingIdNamesPutRequestUsersInner]
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        instanceid: int,
        operator_id: str,
        operator_id_type: int,
        users: List[V1RealControlMeetingsMeetingIdNamesPutRequestUsersInner] | List[Dict[str, Any]],
        **kwargs
    ):
        self.instanceid = instanceid
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        
        if users and isinstance(users, (list, List)):
            self.users = [V1RealControlMeetingsMeetingIdNamesPutRequestUsersInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in users]
        


class V1RealControlMeetingsMeetingIdNamesPutRequestUsersInner(object):
    """V1RealControlMeetingsMeetingIdNamesPutRequestUsersInner

    :param instanceid: 用户的终端设备类型： 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch Mac 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch Iphone (required) 
    :type instanceid: int

    :param ms_open_id: 被操作者ms_open_id (required) 
    :type ms_open_id: str

    :param nick_name: 要修改的昵称名，限制20个字符。 
    :type nick_name: Optional[str]
    """  # noqa: E501

    instanceid: int
    ms_open_id: str
    nick_name: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        instanceid: int,
        ms_open_id: str,
        nick_name: Optional[str] = None,
        **kwargs
    ):
        self.instanceid = instanceid
        self.ms_open_id = ms_open_id
        self.nick_name = nick_name


class V1RealControlMeetingsMeetingIdScreenSharedPutRequest(object):
    """V1RealControlMeetingsMeetingIdScreenSharedPutRequest

    :param instanceid: 用户的终端设备类型： 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch Mac 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch Iphone (required) 
    :type instanceid: int

    :param operator_id: 操作者 ID。 1：operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 2：接口输入参数如果需要传用户 ID 时，operator_id 和 uuid 不可以同时为空，两个参数如果都传了以 operator_id 为准。 3：如果 operator_id_type=2，operator_id 必须和公共参数的 openid 一致。 
    :type operator_id: Optional[str]

    :param operator_id_type: 操作者ID的类型：  2:openid  4: ms_open_id 
    :type operator_id_type: Optional[int]

    :param user:(required) 
    :type user: V1RealControlMeetingsMeetingIdScreenSharedPutRequestUser

    :param uuid: 操作者用户唯一身份 ID，仅支持主持人和联席主持人，且只适用于单场会议。即将废弃，推荐使用ms_open_id。 
    :type uuid: Optional[str]
    """  # noqa: E501

    instanceid: int
    operator_id: Optional[str] = None
    operator_id_type: Optional[int] = None
    user: V1RealControlMeetingsMeetingIdScreenSharedPutRequestUser
    uuid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        instanceid: int,
        user: V1RealControlMeetingsMeetingIdScreenSharedPutRequestUser | Dict[str, Any],
        operator_id: Optional[str] = None,
        operator_id_type: Optional[int] = None,
        uuid: Optional[str] = None,
        **kwargs
    ):
        self.instanceid = instanceid
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.user = V1RealControlMeetingsMeetingIdScreenSharedPutRequestUser(**user) if isinstance(user, (dict, Dict)) else user
        self.uuid = uuid


class V1RealControlMeetingsMeetingIdScreenSharedPutRequestUser(object):
    """V1RealControlMeetingsMeetingIdScreenSharedPutRequestUser

    :param instanceid: 用户的终端设备类型： 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch Mac 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch Iphone (required) 
    :type instanceid: int

    :param to_operator_id: 用户ID，根据to_operator_id_type的值，使用不同的类型 
    :type to_operator_id: Optional[str]

    :param to_operator_id_type: 用户ID的类型：4: ms_open_id 
    :type to_operator_id_type: Optional[int]

    :param uuid: 用户的唯一标识uuid 
    :type uuid: Optional[str]
    """  # noqa: E501

    instanceid: int
    to_operator_id: Optional[str] = None
    to_operator_id_type: Optional[int] = None
    uuid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        instanceid: int,
        to_operator_id: Optional[str] = None,
        to_operator_id_type: Optional[int] = None,
        uuid: Optional[str] = None,
        **kwargs
    ):
        self.instanceid = instanceid
        self.to_operator_id = to_operator_id
        self.to_operator_id_type = to_operator_id_type
        self.uuid = uuid


class V1RealControlMeetingsMeetingIdStatusPutRequest(object):
    """V1RealControlMeetingsMeetingIdStatusPutRequest

    :param allow_chat: 允许参会者聊天设置  0:允许参会者自由聊天  1:仅允许参会者公开聊天  2:只允许支持人发言 
    :type allow_chat: Optional[int]

    :param allow_unmute_by_self: 是否允许成员自己解除静音 
    :type allow_unmute_by_self: Optional[bool]

    :param auto_waiting_room: 是否开启等候室 true：开启 false：关闭 
    :type auto_waiting_room: Optional[bool]

    :param enable_red_envelope: 是否允许参会者发送红包 true：允许 false：不允许 
    :type enable_red_envelope: Optional[bool]

    :param hide_meeting_code_password: 隐藏会议号和密码 true：隐藏 false：不隐藏 
    :type hide_meeting_code_password: Optional[bool]

    :param instanceid: 用户的终端设备类型： 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch Mac 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch Iphone (required) 
    :type instanceid: int

    :param meeting_locked: 是否锁定会议 true：锁定 false：关闭锁定 
    :type meeting_locked: Optional[bool]

    :param mute_all: 是否全体静音，true：是；false关闭全体静音 
    :type mute_all: Optional[bool]

    :param only_enterprise_user_allowed: 是否仅企业成员可入会  true：仅企业成员可入会  false：不限制 
    :type only_enterprise_user_allowed: Optional[bool]

    :param operator_id: 操作者ID，根据operator_id_type的值，使用不同的类型 
    :type operator_id: Optional[str]

    :param operator_id_type: 操作者ID的类型：1:userid  2:openid（预留编号，本次不添加，未来新增接口使用）3:rooms_id  4: ms_open_id 
    :type operator_id_type: Optional[int]

    :param participant_join_mute: 成员入会静音 0:关闭静音 1:开启静音 2:超过6人自动开启静音 
    :type participant_join_mute: Optional[int]

    :param play_ivr_on_join: 成员入会是否播放提示音 true：成员入会播放提示音 false：不播放 
    :type play_ivr_on_join: Optional[bool]

    :param share_screen: 是否允许参会者发起屏幕共享 true：允许 false：不允许 
    :type share_screen: Optional[bool]

    :param uuid: 用户的唯一标识uuid 
    :type uuid: Optional[str]
    """  # noqa: E501

    allow_chat: Optional[int] = None
    allow_unmute_by_self: Optional[bool] = None
    auto_waiting_room: Optional[bool] = None
    enable_red_envelope: Optional[bool] = None
    hide_meeting_code_password: Optional[bool] = None
    instanceid: int
    meeting_locked: Optional[bool] = None
    mute_all: Optional[bool] = None
    only_enterprise_user_allowed: Optional[bool] = None
    operator_id: Optional[str] = None
    operator_id_type: Optional[int] = None
    participant_join_mute: Optional[int] = None
    play_ivr_on_join: Optional[bool] = None
    share_screen: Optional[bool] = None
    uuid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        instanceid: int,
        allow_chat: Optional[int] = None,
        allow_unmute_by_self: Optional[bool] = None,
        auto_waiting_room: Optional[bool] = None,
        enable_red_envelope: Optional[bool] = None,
        hide_meeting_code_password: Optional[bool] = None,
        meeting_locked: Optional[bool] = None,
        mute_all: Optional[bool] = None,
        only_enterprise_user_allowed: Optional[bool] = None,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[int] = None,
        participant_join_mute: Optional[int] = None,
        play_ivr_on_join: Optional[bool] = None,
        share_screen: Optional[bool] = None,
        uuid: Optional[str] = None,
        **kwargs
    ):
        self.allow_chat = allow_chat
        self.allow_unmute_by_self = allow_unmute_by_self
        self.auto_waiting_room = auto_waiting_room
        self.enable_red_envelope = enable_red_envelope
        self.hide_meeting_code_password = hide_meeting_code_password
        self.instanceid = instanceid
        self.meeting_locked = meeting_locked
        self.mute_all = mute_all
        self.only_enterprise_user_allowed = only_enterprise_user_allowed
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.participant_join_mute = participant_join_mute
        self.play_ivr_on_join = play_ivr_on_join
        self.share_screen = share_screen
        self.uuid = uuid


class V1RealControlMeetingsMeetingIdVideoPutRequest(object):
    """V1RealControlMeetingsMeetingIdVideoPutRequest

    :param instanceid: 用户的终端设备类型： 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch Mac 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch Iphone (required) 
    :type instanceid: int

    :param operator_id: 操作者 ID。 1：operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 2：接口输入参数如果需要传用户 ID 时，operator_id 和 uuid 不可以同时为空，两个参数如果都传了以 operator_id 为准。 3：如果 operator_id_type=2，operator_id 必须和公共参数的 openid 一致。 
    :type operator_id: Optional[str]

    :param operator_id_type: 操作者ID的类型： 2:openid 4: ms_open_id 
    :type operator_id_type: Optional[int]

    :param user:(required) 
    :type user: V1RealControlMeetingsMeetingIdVideoPutRequestUser

    :param uuid: 操作者用户唯一身份 ID，仅支持主持人和联席主持人，且只适用于单场会议。即将废弃，推荐使用ms_open_id。 
    :type uuid: Optional[str]

    :param video: 是否开启视频： false：关闭视频（默认值）。 true：开启视频， 仅支持 MRA 设备。 
    :type video: Optional[bool]
    """  # noqa: E501

    instanceid: int
    operator_id: Optional[str] = None
    operator_id_type: Optional[int] = None
    user: V1RealControlMeetingsMeetingIdVideoPutRequestUser
    uuid: Optional[str] = None
    video: Optional[bool] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        instanceid: int,
        user: V1RealControlMeetingsMeetingIdVideoPutRequestUser | Dict[str, Any],
        operator_id: Optional[str] = None,
        operator_id_type: Optional[int] = None,
        uuid: Optional[str] = None,
        video: Optional[bool] = None,
        **kwargs
    ):
        self.instanceid = instanceid
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.user = V1RealControlMeetingsMeetingIdVideoPutRequestUser(**user) if isinstance(user, (dict, Dict)) else user
        self.uuid = uuid
        self.video = video


class V1RealControlMeetingsMeetingIdVideoPutRequestUser(object):
    """V1RealControlMeetingsMeetingIdVideoPutRequestUser

    :param instanceid: 用户的终端设备类型： 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch Mac 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch Iphone (required) 
    :type instanceid: int

    :param to_operator_id: 被操作者 ID，根据 operator_id_type 的值，使用不同的类型。和 uuid 不可同时为空。 
    :type to_operator_id: Optional[str]

    :param to_operator_id_type: 用户ID的类型： 4: ms_open_id 
    :type to_operator_id_type: Optional[int]

    :param uuid: 用户的唯一标识uuid 
    :type uuid: Optional[str]
    """  # noqa: E501

    instanceid: int
    to_operator_id: Optional[str] = None
    to_operator_id_type: Optional[int] = None
    uuid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        instanceid: int,
        to_operator_id: Optional[str] = None,
        to_operator_id_type: Optional[int] = None,
        uuid: Optional[str] = None,
        **kwargs
    ):
        self.instanceid = instanceid
        self.to_operator_id = to_operator_id
        self.to_operator_id_type = to_operator_id_type
        self.uuid = uuid


class V1RealControlMeetingsMeetingIdWaitingRoomPutRequest(object):
    """V1RealControlMeetingsMeetingIdWaitingRoomPutRequest

    :param allow_rejoin: 移出后是否允许再次加入会议  true：允许 false：不允许  说明：操作类型参数 operete_type = 3 时才允许设置 
    :type allow_rejoin: Optional[bool]

    :param instanceid: 用户的终端设备类型： 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch Mac 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch Iphone (required) 
    :type instanceid: int

    :param operate_type: 操作类型： 1：主持人将等候室成员移入会议  2：主持人将会中成员移入等候室  3：主持人将等候室成员移出等候室 (required) 
    :type operate_type: int

    :param operator_id: 操作者 ID。 1：operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 2：接口输入参数如果需要传用户 ID 时，operator_id 和 uuid 不可以同时为空，两个参数如果都传了以 operator_id 为准。 3：如果 operator_id_type=2，operator_id 必须和公共参数的 openid 一致。 
    :type operator_id: Optional[str]

    :param operator_id_type: 操作者ID的类型： 2:openid 4: ms_open_id 
    :type operator_id_type: Optional[int]

    :param users: 被操作用户对象信息列表 (required) 
    :type users: List[V1RealControlMeetingsMeetingIdMutesPutRequestUser]

    :param uuid: 操作者用户唯一身份 ID，仅支持主持人和联席主持人，且只适用于单场会议。即将废弃，推荐使用ms_open_id。 
    :type uuid: Optional[str]
    """  # noqa: E501

    allow_rejoin: Optional[bool] = None
    instanceid: int
    operate_type: int
    operator_id: Optional[str] = None
    operator_id_type: Optional[int] = None
    users: List[V1RealControlMeetingsMeetingIdMutesPutRequestUser]
    uuid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        instanceid: int,
        operate_type: int,
        users: List[V1RealControlMeetingsMeetingIdMutesPutRequestUser] | List[Dict[str, Any]],
        allow_rejoin: Optional[bool] = None,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[int] = None,
        uuid: Optional[str] = None,
        **kwargs
    ):
        self.allow_rejoin = allow_rejoin
        self.instanceid = instanceid
        self.operate_type = operate_type
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        
        if users and isinstance(users, (list, List)):
            self.users = [V1RealControlMeetingsMeetingIdMutesPutRequestUser(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in users]
        
        self.uuid = uuid

