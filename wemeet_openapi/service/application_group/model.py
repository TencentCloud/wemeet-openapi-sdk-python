# coding: utf-8

"""
    腾讯会议OpenAPI

    SAAS版RESTFUL风格API

    API version: v1.0.4

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

from typing import *


class V1AppToolkitPostRequest(object):
    """V1AppToolkitPostRequest

    :param auto_open_sdkid: 自动打开应用的id 
    :type auto_open_sdkid: Optional[str]

    :param instanceid: 用户的终端设备类型： 1 - PC 2 - Mac 3 - Android 4 - iOS 5 - Web 6 - iPad 7 - Android Pad 8 - 小程序  (required) 
    :type instanceid: int

    :param meeting_id: 会议id (required) 
    :type meeting_id: str

    :param tool_list: 工具箱应用列表 (required) 
    :type tool_list: List[V1AppToolkitPostRequestToolListInner]

    :param toolbar_sdkid: 外显在会中工具栏的应用id（需要保证在tool_list列表中，且列表中的可见范围对此设置也生效） 
    :type toolbar_sdkid: Optional[str]

    :param userid: 调用方用于标示用户的唯一 ID（企业内部请使用企业唯一用户标识；OAuth2.0鉴权用户请使用openId） 企业唯一用户标识说明： 1、 企业对接SSO时使用的员工唯一标识ID 2、 企业调用创建用户接口时传递的userid参数 (required) 
    :type userid: str
    """  # noqa: E501

    auto_open_sdkid: Optional[str] = None
    instanceid: int
    meeting_id: str
    tool_list: List[V1AppToolkitPostRequestToolListInner]
    toolbar_sdkid: Optional[str] = None
    userid: str
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        instanceid: int,
        meeting_id: str,
        tool_list: List[V1AppToolkitPostRequestToolListInner] | List[Dict[str, Any]],
        userid: str,
        auto_open_sdkid: Optional[str] = None,
        toolbar_sdkid: Optional[str] = None,
        **kwargs
    ):
        self.auto_open_sdkid = auto_open_sdkid
        self.instanceid = instanceid
        self.meeting_id = meeting_id
        
        if tool_list and isinstance(tool_list, (list, List)):
            self.tool_list = [V1AppToolkitPostRequestToolListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in tool_list]
        
        self.toolbar_sdkid = toolbar_sdkid
        self.userid = userid


class V1AppToolkitPostRequestToolListInner(object):
    """应用列表对象

    :param enable_add_robot: 应用是否可以拉取机器人，0:否，1:是，默认为0 
    :type enable_add_robot: Optional[int]

    :param enable_customer_data: 应用是否可以查询customerData，0:否，1:是，默认为0 
    :type enable_customer_data: Optional[int]

    :param is_shield_creator: 可见用户是否屏蔽会议创建者，visible_type=2时该字段才有效。true：屏蔽会议创建者，除非在可见用户列表中显式设置会议创建者；false：默认配置，会议创建者可见 
    :type is_shield_creator: Optional[bool]

    :param tool_appid: 工具箱应用所属企业appid (required) 
    :type tool_appid: str

    :param tool_sdkid: 工具箱应用id (required) 
    :type tool_sdkid: str

    :param unique_code: 调用方业务相关字段，最大128个字符 
    :type unique_code: Optional[str]

    :param visible_list: 可见用户列表（默认会议创建者可见），visible_type=2时该字段才有效 
    :type visible_list: Optional[List[V1AppToolkitPostRequestToolListInnerVisibleListInner]]

    :param visible_type: 工具箱应用可见类型。 0:所有人可见, 1:本企业可见, 2:指定用户可见，默认为0 
    :type visible_type: Optional[int]
    """  # noqa: E501

    enable_add_robot: Optional[int] = None
    enable_customer_data: Optional[int] = None
    is_shield_creator: Optional[bool] = None
    tool_appid: str
    tool_sdkid: str
    unique_code: Optional[str] = None
    visible_list: Optional[List[V1AppToolkitPostRequestToolListInnerVisibleListInner]] = None
    visible_type: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        tool_appid: str,
        tool_sdkid: str,
        enable_add_robot: Optional[int] = None,
        enable_customer_data: Optional[int] = None,
        is_shield_creator: Optional[bool] = None,
        unique_code: Optional[str] = None,
        visible_list: Optional[List[V1AppToolkitPostRequestToolListInnerVisibleListInner] | List[Dict[str, Any]]] = None,
        visible_type: Optional[int] = None,
        **kwargs
    ):
        self.enable_add_robot = enable_add_robot
        self.enable_customer_data = enable_customer_data
        self.is_shield_creator = is_shield_creator
        self.tool_appid = tool_appid
        self.tool_sdkid = tool_sdkid
        self.unique_code = unique_code
        
        if visible_list and isinstance(visible_list, (list, List)):
            self.visible_list = [V1AppToolkitPostRequestToolListInnerVisibleListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in visible_list]
        
        self.visible_type = visible_type


class V1AppToolkitPostRequestToolListInnerVisibleListInner(object):
    """可见列表对象

    :param visible_appid: 对哪个企业的用户可见 
    :type visible_appid: Optional[str]

    :param visible_openid: 可见用户openid，OAuth2.0鉴权用户请用此字段（visible_userid和visible_openid二者选一，同时存在时以visible_openid为准） 
    :type visible_openid: Optional[str]

    :param visible_userid: 可见用户userid，若不填则对该企业下所有用户可见 
    :type visible_userid: Optional[str]
    """  # noqa: E501

    visible_appid: Optional[str] = None
    visible_openid: Optional[str] = None
    visible_userid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        visible_appid: Optional[str] = None,
        visible_openid: Optional[str] = None,
        visible_userid: Optional[str] = None,
        **kwargs
    ):
        self.visible_appid = visible_appid
        self.visible_openid = visible_openid
        self.visible_userid = visible_userid

