# coding: utf-8

"""
    腾讯会议OpenAPI

    SAAS版RESTFUL风格API

    API version: v1.0.4

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

from typing import *


class V1MeetingsMeetingIdAdvancedLayoutsPost200Response(object):
    """V1MeetingsMeetingIdAdvancedLayoutsPost200Response

    :param layout_list: 布局对象列表 
    :type layout_list: Optional[List[V1MeetingsMeetingIdAdvancedLayoutsPost200ResponseLayoutListInner]]
    """  # noqa: E501

    layout_list: Optional[List[V1MeetingsMeetingIdAdvancedLayoutsPost200ResponseLayoutListInner]] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        layout_list: Optional[List[V1MeetingsMeetingIdAdvancedLayoutsPost200ResponseLayoutListInner] | List[Dict[str, Any]]] = None,
        **kwargs
    ):
        
        if layout_list and isinstance(layout_list, (list, List)):
            self.layout_list = [V1MeetingsMeetingIdAdvancedLayoutsPost200ResponseLayoutListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in layout_list]
        


class V1MeetingsMeetingIdAdvancedLayoutsPost200ResponseLayoutListInner(object):
    """V1MeetingsMeetingIdAdvancedLayoutsPost200ResponseLayoutListInner

    :param layout_id: 布局 ID 
    :type layout_id: Optional[str]

    :param layout_name: 布局名称 
    :type layout_name: Optional[str]

    :param page_list: 布局单页对象列表 
    :type page_list: Optional[List[V1MeetingsMeetingIdAdvancedLayoutsPost200ResponseLayoutListInnerPageListInner]]
    """  # noqa: E501

    layout_id: Optional[str] = None
    layout_name: Optional[str] = None
    page_list: Optional[List[V1MeetingsMeetingIdAdvancedLayoutsPost200ResponseLayoutListInnerPageListInner]] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        layout_id: Optional[str] = None,
        layout_name: Optional[str] = None,
        page_list: Optional[List[V1MeetingsMeetingIdAdvancedLayoutsPost200ResponseLayoutListInnerPageListInner] | List[Dict[str, Any]]] = None,
        **kwargs
    ):
        self.layout_id = layout_id
        self.layout_name = layout_name
        
        if page_list and isinstance(page_list, (list, List)):
            self.page_list = [V1MeetingsMeetingIdAdvancedLayoutsPost200ResponseLayoutListInnerPageListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in page_list]
        


class V1MeetingsMeetingIdAdvancedLayoutsPost200ResponseLayoutListInnerPageListInner(object):
    """V1MeetingsMeetingIdAdvancedLayoutsPost200ResponseLayoutListInnerPageListInner

    :param enable_polling: 开启/关闭轮询 
    :type enable_polling: Optional[bool]

    :param layout_template_id: 布局模板 ID 
    :type layout_template_id: Optional[str]

    :param polling_setting:
    :type polling_setting: Optional[V1MeetingsMeetingIdAdvancedLayoutsPost200ResponseLayoutListInnerPageListInnerPollingSetting]

    :param user_seat_list: 用户座次对象列表 
    :type user_seat_list: Optional[List[V1MeetingsMeetingIdAdvancedLayoutsPost200ResponseLayoutListInnerPageListInnerUserSeatListInner]]
    """  # noqa: E501

    enable_polling: Optional[bool] = None
    layout_template_id: Optional[str] = None
    polling_setting: Optional[V1MeetingsMeetingIdAdvancedLayoutsPost200ResponseLayoutListInnerPageListInnerPollingSetting] = None
    user_seat_list: Optional[List[V1MeetingsMeetingIdAdvancedLayoutsPost200ResponseLayoutListInnerPageListInnerUserSeatListInner]] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        enable_polling: Optional[bool] = None,
        layout_template_id: Optional[str] = None,
        polling_setting: Optional[V1MeetingsMeetingIdAdvancedLayoutsPost200ResponseLayoutListInnerPageListInnerPollingSetting | Dict[str, Any]] = None,
        user_seat_list: Optional[List[V1MeetingsMeetingIdAdvancedLayoutsPost200ResponseLayoutListInnerPageListInnerUserSeatListInner] | List[Dict[str, Any]]] = None,
        **kwargs
    ):
        self.enable_polling = enable_polling
        self.layout_template_id = layout_template_id
        self.polling_setting = V1MeetingsMeetingIdAdvancedLayoutsPost200ResponseLayoutListInnerPageListInnerPollingSetting(**polling_setting) if isinstance(polling_setting, (dict, Dict)) else polling_setting
        
        if user_seat_list and isinstance(user_seat_list, (list, List)):
            self.user_seat_list = [V1MeetingsMeetingIdAdvancedLayoutsPost200ResponseLayoutListInnerPageListInnerUserSeatListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in user_seat_list]
        


class V1MeetingsMeetingIdAdvancedLayoutsPost200ResponseLayoutListInnerPageListInnerPollingSetting(object):
    """轮询参数设置对象

    :param ignore_user_absence: 轮询开启后设置参数， 设置是否忽略未入会成员 
    :type ignore_user_absence: Optional[bool]

    :param ignore_user_novideo: 轮询开启后设置参数，设置是否忽略没开启视频成员 
    :type ignore_user_novideo: Optional[bool]

    :param polling_interval: 轮询开启后设置参数 轮询间隔时长， 允许取值范围1～999999 
    :type polling_interval: Optional[int]

    :param polling_interval_unit: 轮询开启后设置参数。 轮询间隔时间类型： 1-秒 2-分钟 
    :type polling_interval_unit: Optional[int]
    """  # noqa: E501

    ignore_user_absence: Optional[bool] = None
    ignore_user_novideo: Optional[bool] = None
    polling_interval: Optional[int] = None
    polling_interval_unit: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        ignore_user_absence: Optional[bool] = None,
        ignore_user_novideo: Optional[bool] = None,
        polling_interval: Optional[int] = None,
        polling_interval_unit: Optional[int] = None,
        **kwargs
    ):
        self.ignore_user_absence = ignore_user_absence
        self.ignore_user_novideo = ignore_user_novideo
        self.polling_interval = polling_interval
        self.polling_interval_unit = polling_interval_unit


class V1MeetingsMeetingIdAdvancedLayoutsPost200ResponseLayoutListInnerPageListInnerUserSeatListInner(object):
    """V1MeetingsMeetingIdAdvancedLayoutsPost200ResponseLayoutListInnerPageListInnerUserSeatListInner

    :param grid_id: 宫格 ID 
    :type grid_id: Optional[str]

    :param grid_type: 宫格类型： 1-视频画面 2-共享画面 
    :type grid_type: Optional[int]

    :param user_list: 宫格中的用户列表 ● 轮询关闭， 只有一个用户 ● 轮询开启后， 可以包含多个用户 
    :type user_list: Optional[List[V1MeetingsMeetingIdAdvancedLayoutsPost200ResponseLayoutListInnerPageListInnerUserSeatListInnerUserListInner]]

    :param video_type: 视频画面来源 1-演讲者 2-自动填充 3-指定人员，根据user_list的定义显示视频内容（此类型需传递 userid 或 ms_open_id、username 入参，作为视频画面展示；若会中参会成员有外部企业用户，需传递该用户的 ms_open_id；如果 userid、ms_open_id 同时传递则以 ms_open_id 为准） 
    :type video_type: Optional[int]
    """  # noqa: E501

    grid_id: Optional[str] = None
    grid_type: Optional[int] = None
    user_list: Optional[List[V1MeetingsMeetingIdAdvancedLayoutsPost200ResponseLayoutListInnerPageListInnerUserSeatListInnerUserListInner]] = None
    video_type: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        grid_id: Optional[str] = None,
        grid_type: Optional[int] = None,
        user_list: Optional[List[V1MeetingsMeetingIdAdvancedLayoutsPost200ResponseLayoutListInnerPageListInnerUserSeatListInnerUserListInner] | List[Dict[str, Any]]] = None,
        video_type: Optional[int] = None,
        **kwargs
    ):
        self.grid_id = grid_id
        self.grid_type = grid_type
        
        if user_list and isinstance(user_list, (list, List)):
            self.user_list = [V1MeetingsMeetingIdAdvancedLayoutsPost200ResponseLayoutListInnerPageListInnerUserSeatListInnerUserListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in user_list]
        
        self.video_type = video_type


class V1MeetingsMeetingIdAdvancedLayoutsPost200ResponseLayoutListInnerPageListInnerUserSeatListInnerUserListInner(object):
    """V1MeetingsMeetingIdAdvancedLayoutsPost200ResponseLayoutListInnerPageListInnerUserSeatListInnerUserListInner

    :param ms_open_id: 用户当前会议临时身份 ID，单场会议唯一 
    :type ms_open_id: Optional[str]

    :param userid: 用户 ID 
    :type userid: Optional[str]

    :param username: 用户昵称，base64编码 
    :type username: Optional[str]
    """  # noqa: E501

    ms_open_id: Optional[str] = None
    userid: Optional[str] = None
    username: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        ms_open_id: Optional[str] = None,
        userid: Optional[str] = None,
        username: Optional[str] = None,
        **kwargs
    ):
        self.ms_open_id = ms_open_id
        self.userid = userid
        self.username = username


class V1MeetingsMeetingIdAdvancedLayoutsPostRequest(object):
    """V1MeetingsMeetingIdAdvancedLayoutsPostRequest

    :param instanceid: 设备类型 ID 0：PSTN 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch MacOS 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch iOS (required) 
    :type instanceid: int

    :param layout_list: 布局对象列表 (required) 
    :type layout_list: List[V1MeetingsMeetingIdAdvancedLayoutsPostRequestLayoutListInner]

    :param operator_id: 操作人ID (required) 
    :type operator_id: str

    :param operator_id_type: 操作人id类型，1：userid，4 :ms_open_id (required) 
    :type operator_id_type: int
    """  # noqa: E501

    instanceid: int
    layout_list: List[V1MeetingsMeetingIdAdvancedLayoutsPostRequestLayoutListInner]
    operator_id: str
    operator_id_type: int
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        instanceid: int,
        layout_list: List[V1MeetingsMeetingIdAdvancedLayoutsPostRequestLayoutListInner] | List[Dict[str, Any]],
        operator_id: str,
        operator_id_type: int,
        **kwargs
    ):
        self.instanceid = instanceid
        
        if layout_list and isinstance(layout_list, (list, List)):
            self.layout_list = [V1MeetingsMeetingIdAdvancedLayoutsPostRequestLayoutListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in layout_list]
        
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type


class V1MeetingsMeetingIdAdvancedLayoutsPostRequestLayoutListInner(object):
    """V1MeetingsMeetingIdAdvancedLayoutsPostRequestLayoutListInner

    :param layout_name: 布局名称 
    :type layout_name: Optional[str]

    :param page_list: 布局单页对象列表 (required) 
    :type page_list: List[V1MeetingsMeetingIdAdvancedLayoutsPostRequestLayoutListInnerPageListInner]
    """  # noqa: E501

    layout_name: Optional[str] = None
    page_list: List[V1MeetingsMeetingIdAdvancedLayoutsPostRequestLayoutListInnerPageListInner]
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        page_list: List[V1MeetingsMeetingIdAdvancedLayoutsPostRequestLayoutListInnerPageListInner] | List[Dict[str, Any]],
        layout_name: Optional[str] = None,
        **kwargs
    ):
        self.layout_name = layout_name
        
        if page_list and isinstance(page_list, (list, List)):
            self.page_list = [V1MeetingsMeetingIdAdvancedLayoutsPostRequestLayoutListInnerPageListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in page_list]
        


class V1MeetingsMeetingIdAdvancedLayoutsPostRequestLayoutListInnerPageListInner(object):
    """V1MeetingsMeetingIdAdvancedLayoutsPostRequestLayoutListInnerPageListInner

    :param enable_polling: 开启/关闭轮询 
    :type enable_polling: Optional[bool]

    :param layout_template_id: 布局模板 ID (required) 
    :type layout_template_id: str

    :param polling_setting:
    :type polling_setting: Optional[V1MeetingsMeetingIdAdvancedLayoutsPostRequestLayoutListInnerPageListInnerPollingSetting]

    :param user_seat_list: 用户座次对象列表 (required) 
    :type user_seat_list: List[V1MeetingsMeetingIdAdvancedLayoutsPostRequestLayoutListInnerPageListInnerUserSeatListInner]
    """  # noqa: E501

    enable_polling: Optional[bool] = None
    layout_template_id: str
    polling_setting: Optional[V1MeetingsMeetingIdAdvancedLayoutsPostRequestLayoutListInnerPageListInnerPollingSetting] = None
    user_seat_list: List[V1MeetingsMeetingIdAdvancedLayoutsPostRequestLayoutListInnerPageListInnerUserSeatListInner]
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        layout_template_id: str,
        user_seat_list: List[V1MeetingsMeetingIdAdvancedLayoutsPostRequestLayoutListInnerPageListInnerUserSeatListInner] | List[Dict[str, Any]],
        enable_polling: Optional[bool] = None,
        polling_setting: Optional[V1MeetingsMeetingIdAdvancedLayoutsPostRequestLayoutListInnerPageListInnerPollingSetting | Dict[str, Any]] = None,
        **kwargs
    ):
        self.enable_polling = enable_polling
        self.layout_template_id = layout_template_id
        self.polling_setting = V1MeetingsMeetingIdAdvancedLayoutsPostRequestLayoutListInnerPageListInnerPollingSetting(**polling_setting) if isinstance(polling_setting, (dict, Dict)) else polling_setting
        
        if user_seat_list and isinstance(user_seat_list, (list, List)):
            self.user_seat_list = [V1MeetingsMeetingIdAdvancedLayoutsPostRequestLayoutListInnerPageListInnerUserSeatListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in user_seat_list]
        


class V1MeetingsMeetingIdAdvancedLayoutsPostRequestLayoutListInnerPageListInnerPollingSetting(object):
    """轮询参数设置对象

    :param ignore_user_absence: 轮询开启后设置参数， 设置是否忽略未入会成员 (required) 
    :type ignore_user_absence: bool

    :param ignore_user_novideo: 轮询开启后设置参数，设置是否忽略没开启视频成员 (required) 
    :type ignore_user_novideo: bool

    :param polling_interval: 轮询开启后设置参数 轮询间隔时长， 允许取值范围1～999999 (required) 
    :type polling_interval: int

    :param polling_interval_unit: 轮询开启后设置参数。 轮询间隔时间类型： 1-秒 2-分钟 (required) 
    :type polling_interval_unit: int
    """  # noqa: E501

    ignore_user_absence: bool
    ignore_user_novideo: bool
    polling_interval: int
    polling_interval_unit: int
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        ignore_user_absence: bool,
        ignore_user_novideo: bool,
        polling_interval: int,
        polling_interval_unit: int,
        **kwargs
    ):
        self.ignore_user_absence = ignore_user_absence
        self.ignore_user_novideo = ignore_user_novideo
        self.polling_interval = polling_interval
        self.polling_interval_unit = polling_interval_unit


class V1MeetingsMeetingIdAdvancedLayoutsPostRequestLayoutListInnerPageListInnerUserSeatListInner(object):
    """V1MeetingsMeetingIdAdvancedLayoutsPostRequestLayoutListInnerPageListInnerUserSeatListInner

    :param grid_id: 宫格 ID (required) 
    :type grid_id: str

    :param grid_type: 宫格类型： 1-视频画面 2-共享画面 (required) 
    :type grid_type: int

    :param user_list: 宫格中的用户列表 ● 轮询关闭， 只有一个用户 ● 轮询开启后， 可以包含多个用户 
    :type user_list: Optional[List[V1MeetingsMeetingIdAdvancedLayoutsPostRequestLayoutListInnerPageListInnerUserSeatListInnerUserListInner]]

    :param video_type: 视频画面来源 1-演讲者 2-自动填充 3-指定人员，根据user_list的定义显示视频内容（此类型需传递 userid 或 ms_open_id、username 入参，作为视频画面展示；若会中参会成员有外部企业用户，需传递该用户的 ms_open_id；如果 userid、ms_open_id 同时传递则以 ms_open_id 为准） 
    :type video_type: Optional[int]
    """  # noqa: E501

    grid_id: str
    grid_type: int
    user_list: Optional[List[V1MeetingsMeetingIdAdvancedLayoutsPostRequestLayoutListInnerPageListInnerUserSeatListInnerUserListInner]] = None
    video_type: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        grid_id: str,
        grid_type: int,
        user_list: Optional[List[V1MeetingsMeetingIdAdvancedLayoutsPostRequestLayoutListInnerPageListInnerUserSeatListInnerUserListInner] | List[Dict[str, Any]]] = None,
        video_type: Optional[int] = None,
        **kwargs
    ):
        self.grid_id = grid_id
        self.grid_type = grid_type
        
        if user_list and isinstance(user_list, (list, List)):
            self.user_list = [V1MeetingsMeetingIdAdvancedLayoutsPostRequestLayoutListInnerPageListInnerUserSeatListInnerUserListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in user_list]
        
        self.video_type = video_type


class V1MeetingsMeetingIdAdvancedLayoutsPostRequestLayoutListInnerPageListInnerUserSeatListInnerUserListInner(object):
    """V1MeetingsMeetingIdAdvancedLayoutsPostRequestLayoutListInnerPageListInnerUserSeatListInnerUserListInner

    :param ms_open_id: 用户当前会议临时身份 ID，单场会议唯一 
    :type ms_open_id: Optional[str]

    :param userid: 用户 ID 
    :type userid: Optional[str]

    :param username: 用户昵称，base64编码 
    :type username: Optional[str]
    """  # noqa: E501

    ms_open_id: Optional[str] = None
    userid: Optional[str] = None
    username: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        ms_open_id: Optional[str] = None,
        userid: Optional[str] = None,
        username: Optional[str] = None,
        **kwargs
    ):
        self.ms_open_id = ms_open_id
        self.userid = userid
        self.username = username


class V1MeetingsMeetingIdApplyingLayoutPutRequest(object):
    """V1MeetingsMeetingIdApplyingLayoutPutRequest

    :param instanceid: 设备类型 ID 0：PSTN 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch MacOS 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch iOS (required) 
    :type instanceid: int

    :param layout_id: 选择应用的布局 ID （若送空\"\"，表示恢复成当前会议的默认布局）  备注：应用布局的优先级从高到低为： ● 个性布局 ● 自定义布局 ● 默认布局（MRA不支持同框模式， 如果会议设置为同框模式， MRA应用默认布局）） 
    :type layout_id: Optional[str]

    :param operator_id: 操作人ID (required) 
    :type operator_id: str

    :param operator_id_type: 操作人id类型，1 :userid，4 :ms_open_id (required) 
    :type operator_id_type: int

    :param user_list: 用户列表对象数组。如果该字段为空， 为会议设置高级自定义布局；如果该字段携带用户， 则只为指定用户设置个性布局。 单次最多支持20个用户。 
    :type user_list: Optional[List[V1MeetingsMeetingIdApplyingLayoutPutRequestUserListInner]]
    """  # noqa: E501

    instanceid: int
    layout_id: Optional[str] = None
    operator_id: str
    operator_id_type: int
    user_list: Optional[List[V1MeetingsMeetingIdApplyingLayoutPutRequestUserListInner]] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        instanceid: int,
        operator_id: str,
        operator_id_type: int,
        layout_id: Optional[str] = None,
        user_list: Optional[List[V1MeetingsMeetingIdApplyingLayoutPutRequestUserListInner] | List[Dict[str, Any]]] = None,
        **kwargs
    ):
        self.instanceid = instanceid
        self.layout_id = layout_id
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        
        if user_list and isinstance(user_list, (list, List)):
            self.user_list = [V1MeetingsMeetingIdApplyingLayoutPutRequestUserListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in user_list]
        


class V1MeetingsMeetingIdApplyingLayoutPutRequestUserListInner(object):
    """V1MeetingsMeetingIdApplyingLayoutPutRequestUserListInner

    :param instanceid: 用户的终端设备类型：  9：voip、sip 设备（H.323/SIP设备） 说明：请与被操作者的设备类型保持一致，否则不生效。 (required) 
    :type instanceid: int

    :param ms_open_id: 被操作者用户当前会议中的临时身份 ID，单场会议唯一。 (required) 
    :type ms_open_id: str
    """  # noqa: E501

    instanceid: int
    ms_open_id: str
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        instanceid: int,
        ms_open_id: str,
        **kwargs
    ):
        self.instanceid = instanceid
        self.ms_open_id = ms_open_id


class V1MeetingsMeetingIdLayoutsPost200Response(object):
    """V1MeetingsMeetingIdLayoutsPost200Response

    :param layout_list: 布局对象列表 
    :type layout_list: Optional[List[V1MeetingsMeetingIdLayoutsPost200ResponseLayoutListInner]]

    :param layout_number: 布局数量 
    :type layout_number: Optional[int]

    :param selected_layout_id: 会议应用的布局ID 
    :type selected_layout_id: Optional[str]
    """  # noqa: E501

    layout_list: Optional[List[V1MeetingsMeetingIdLayoutsPost200ResponseLayoutListInner]] = None
    layout_number: Optional[int] = None
    selected_layout_id: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        layout_list: Optional[List[V1MeetingsMeetingIdLayoutsPost200ResponseLayoutListInner] | List[Dict[str, Any]]] = None,
        layout_number: Optional[int] = None,
        selected_layout_id: Optional[str] = None,
        **kwargs
    ):
        
        if layout_list and isinstance(layout_list, (list, List)):
            self.layout_list = [V1MeetingsMeetingIdLayoutsPost200ResponseLayoutListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in layout_list]
        
        self.layout_number = layout_number
        self.selected_layout_id = selected_layout_id


class V1MeetingsMeetingIdLayoutsPost200ResponseLayoutListInner(object):
    """V1MeetingsMeetingIdLayoutsPost200ResponseLayoutListInner

    :param layout_id:
    :type layout_id: Optional[str]

    :param page_list: 布局单页对象列表 
    :type page_list: Optional[List[V1MeetingsMeetingIdLayoutsPost200ResponseLayoutListInnerPageListInner]]
    """  # noqa: E501

    layout_id: Optional[str] = None
    page_list: Optional[List[V1MeetingsMeetingIdLayoutsPost200ResponseLayoutListInnerPageListInner]] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        layout_id: Optional[str] = None,
        page_list: Optional[List[V1MeetingsMeetingIdLayoutsPost200ResponseLayoutListInnerPageListInner] | List[Dict[str, Any]]] = None,
        **kwargs
    ):
        self.layout_id = layout_id
        
        if page_list and isinstance(page_list, (list, List)):
            self.page_list = [V1MeetingsMeetingIdLayoutsPost200ResponseLayoutListInnerPageListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in page_list]
        


class V1MeetingsMeetingIdLayoutsPost200ResponseLayoutListInnerPageListInner(object):
    """V1MeetingsMeetingIdLayoutsPost200ResponseLayoutListInnerPageListInner

    :param layout_template_id: 布局模板ID 
    :type layout_template_id: Optional[str]

    :param user_seat_list: 用户座次对象列表 
    :type user_seat_list: Optional[List[V1MeetingsMeetingIdLayoutsPost200ResponseLayoutListInnerPageListInnerUserSeatListInner]]
    """  # noqa: E501

    layout_template_id: Optional[str] = None
    user_seat_list: Optional[List[V1MeetingsMeetingIdLayoutsPost200ResponseLayoutListInnerPageListInnerUserSeatListInner]] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        layout_template_id: Optional[str] = None,
        user_seat_list: Optional[List[V1MeetingsMeetingIdLayoutsPost200ResponseLayoutListInnerPageListInnerUserSeatListInner] | List[Dict[str, Any]]] = None,
        **kwargs
    ):
        self.layout_template_id = layout_template_id
        
        if user_seat_list and isinstance(user_seat_list, (list, List)):
            self.user_seat_list = [V1MeetingsMeetingIdLayoutsPost200ResponseLayoutListInnerPageListInnerUserSeatListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in user_seat_list]
        


class V1MeetingsMeetingIdLayoutsPost200ResponseLayoutListInnerPageListInnerUserSeatListInner(object):
    """V1MeetingsMeetingIdLayoutsPost200ResponseLayoutListInnerPageListInnerUserSeatListInner

    :param grid_id: 宫格ID 
    :type grid_id: Optional[str]

    :param grid_type: 宫格类型 
    :type grid_type: Optional[int]

    :param ms_open_id: 当场会议的用户临时 ID。 
    :type ms_open_id: Optional[str]

    :param tool_sdkid: 工具箱id 
    :type tool_sdkid: Optional[str]

    :param userid: 用户ID 
    :type userid: Optional[str]

    :param username: 用户昵称 
    :type username: Optional[str]

    :param uuid: 用户身份 ID（腾讯会议颁发的用于开放平台的唯一用户 ID） 
    :type uuid: Optional[str]
    """  # noqa: E501

    grid_id: Optional[str] = None
    grid_type: Optional[int] = None
    ms_open_id: Optional[str] = None
    tool_sdkid: Optional[str] = None
    userid: Optional[str] = None
    username: Optional[str] = None
    uuid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        grid_id: Optional[str] = None,
        grid_type: Optional[int] = None,
        ms_open_id: Optional[str] = None,
        tool_sdkid: Optional[str] = None,
        userid: Optional[str] = None,
        username: Optional[str] = None,
        uuid: Optional[str] = None,
        **kwargs
    ):
        self.grid_id = grid_id
        self.grid_type = grid_type
        self.ms_open_id = ms_open_id
        self.tool_sdkid = tool_sdkid
        self.userid = userid
        self.username = username
        self.uuid = uuid


class V1MeetingsMeetingIdLayoutsPostRequest(object):
    """V1MeetingsMeetingIdLayoutsPostRequest

    :param default_layout_order: 布局列表中会议需要应用的布局序号，从1开始计数（首次添加时若该参数不送，则默认选中第一个布局作为会议应用的布局） 
    :type default_layout_order: Optional[int]

    :param instanceid: 用户的终端设备类型：1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch Mac 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch Iphone (required) 
    :type instanceid: int

    :param layout_list: 布局对象列表 (required) 
    :type layout_list: List[V1MeetingsMeetingIdLayoutsPostRequestLayoutListInner]

    :param operator_id: 操作者ID  (required) 
    :type operator_id: str

    :param operator_id_type: 操作者id的类型，1:userid (required) 
    :type operator_id_type: int

    :param userid: 会议创建者ID (required) 
    :type userid: str
    """  # noqa: E501

    default_layout_order: Optional[int] = None
    instanceid: int
    layout_list: List[V1MeetingsMeetingIdLayoutsPostRequestLayoutListInner]
    operator_id: str
    operator_id_type: int
    userid: str
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        instanceid: int,
        layout_list: List[V1MeetingsMeetingIdLayoutsPostRequestLayoutListInner] | List[Dict[str, Any]],
        operator_id: str,
        operator_id_type: int,
        userid: str,
        default_layout_order: Optional[int] = None,
        **kwargs
    ):
        self.default_layout_order = default_layout_order
        self.instanceid = instanceid
        
        if layout_list and isinstance(layout_list, (list, List)):
            self.layout_list = [V1MeetingsMeetingIdLayoutsPostRequestLayoutListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in layout_list]
        
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.userid = userid


class V1MeetingsMeetingIdLayoutsPostRequestLayoutListInner(object):
    """V1MeetingsMeetingIdLayoutsPostRequestLayoutListInner

    :param layout_id:(required) 
    :type layout_id: str

    :param page_list: 布局单页对象列表 (required) 
    :type page_list: List[V1MeetingsMeetingIdLayoutsPostRequestLayoutListInnerPageListInner]
    """  # noqa: E501

    layout_id: str
    page_list: List[V1MeetingsMeetingIdLayoutsPostRequestLayoutListInnerPageListInner]
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        layout_id: str,
        page_list: List[V1MeetingsMeetingIdLayoutsPostRequestLayoutListInnerPageListInner] | List[Dict[str, Any]],
        **kwargs
    ):
        self.layout_id = layout_id
        
        if page_list and isinstance(page_list, (list, List)):
            self.page_list = [V1MeetingsMeetingIdLayoutsPostRequestLayoutListInnerPageListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in page_list]
        


class V1MeetingsMeetingIdLayoutsPostRequestLayoutListInnerPageListInner(object):
    """V1MeetingsMeetingIdLayoutsPostRequestLayoutListInnerPageListInner

    :param layout_template_id: 布局模板ID (required) 
    :type layout_template_id: str

    :param user_seat_list: 用户座次对象列表 
    :type user_seat_list: Optional[List[V1MeetingsMeetingIdLayoutsPostRequestLayoutListInnerPageListInnerUserSeatListInner]]
    """  # noqa: E501

    layout_template_id: str
    user_seat_list: Optional[List[V1MeetingsMeetingIdLayoutsPostRequestLayoutListInnerPageListInnerUserSeatListInner]] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        layout_template_id: str,
        user_seat_list: Optional[List[V1MeetingsMeetingIdLayoutsPostRequestLayoutListInnerPageListInnerUserSeatListInner] | List[Dict[str, Any]]] = None,
        **kwargs
    ):
        self.layout_template_id = layout_template_id
        
        if user_seat_list and isinstance(user_seat_list, (list, List)):
            self.user_seat_list = [V1MeetingsMeetingIdLayoutsPostRequestLayoutListInnerPageListInnerUserSeatListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in user_seat_list]
        


class V1MeetingsMeetingIdLayoutsPostRequestLayoutListInnerPageListInnerUserSeatListInner(object):
    """V1MeetingsMeetingIdLayoutsPostRequestLayoutListInnerPageListInnerUserSeatListInner

    :param grid_id: 宫格ID (required) 
    :type grid_id: str

    :param grid_type: 宫格类型，注意：多次传入同一宫格ID的对象，仅第一次出现的对象生效。 宫格类型： 1. 视频画面（此类型需传递 userid 或 uuid、username 入参，作为视频画面展示；若会中参会成员有外部企业用户，需传递该用户的 uuid；如果 userid、uuid 同时传递则以 uuid 为准）。 2. 共享画面。 3. 拓展应用（目前一页仅可添加一个应用）。 添加的应用需满足以下条件： 与会议绑定。 开启网页服务。 同企业下的仅企业内可见应用或外部企业可见应用。 (required) 
    :type grid_type: int

    :param ms_open_id: 当场会议的用户临时 ID。 
    :type ms_open_id: Optional[str]

    :param tool_sdkid: 工具箱id 
    :type tool_sdkid: Optional[str]

    :param userid: 用户ID 
    :type userid: Optional[str]

    :param username: 用户昵称 
    :type username: Optional[str]

    :param uuid: 用户身份 ID（腾讯会议颁发的用于开放平台的唯一用户 ID） 
    :type uuid: Optional[str]
    """  # noqa: E501

    grid_id: str
    grid_type: int
    ms_open_id: Optional[str] = None
    tool_sdkid: Optional[str] = None
    userid: Optional[str] = None
    username: Optional[str] = None
    uuid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        grid_id: str,
        grid_type: int,
        ms_open_id: Optional[str] = None,
        tool_sdkid: Optional[str] = None,
        userid: Optional[str] = None,
        username: Optional[str] = None,
        uuid: Optional[str] = None,
        **kwargs
    ):
        self.grid_id = grid_id
        self.grid_type = grid_type
        self.ms_open_id = ms_open_id
        self.tool_sdkid = tool_sdkid
        self.userid = userid
        self.username = username
        self.uuid = uuid

