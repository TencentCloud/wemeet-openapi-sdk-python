# coding: utf-8

"""
    腾讯会议OpenAPI

    SAAS版RESTFUL风格API

    API version: v1.0.4

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

from typing import *


class V1GuestsMeetingIdGet200Response(object):
    """V1GuestsMeetingIdGet200Response

    :param guests: 会议嘉宾列表数组。 
    :type guests: Optional[List[V1GuestsMeetingIdGet200ResponseGuestsInner]]

    :param meeting_code: 会议 Code。 
    :type meeting_code: Optional[str]

    :param meeting_id: 会议 ID。 
    :type meeting_id: Optional[str]

    :param subject: 会议主题。 
    :type subject: Optional[str]
    """  # noqa: E501

    guests: Optional[List[V1GuestsMeetingIdGet200ResponseGuestsInner]] = None
    meeting_code: Optional[str] = None
    meeting_id: Optional[str] = None
    subject: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        guests: Optional[List[V1GuestsMeetingIdGet200ResponseGuestsInner] | List[Dict[str, Any]]] = None,
        meeting_code: Optional[str] = None,
        meeting_id: Optional[str] = None,
        subject: Optional[str] = None,
        **kwargs
    ):
        
        if guests and isinstance(guests, (list, List)):
            self.guests = [V1GuestsMeetingIdGet200ResponseGuestsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in guests]
        
        self.meeting_code = meeting_code
        self.meeting_id = meeting_id
        self.subject = subject


class V1GuestsMeetingIdGet200ResponseGuestsInner(object):
    """V1GuestsMeetingIdGet200ResponseGuestsInner

    :param area: 国家/地区代码（例如：中国传86，不是+86，也不是0086）。 
    :type area: Optional[str]

    :param guest_name: 嘉宾名称。 
    :type guest_name: Optional[str]

    :param phone_number: 手机号。 
    :type phone_number: Optional[str]
    """  # noqa: E501

    area: Optional[str] = None
    guest_name: Optional[str] = None
    phone_number: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        area: Optional[str] = None,
        guest_name: Optional[str] = None,
        phone_number: Optional[str] = None,
        **kwargs
    ):
        self.area = area
        self.guest_name = guest_name
        self.phone_number = phone_number


class V1GuestsMeetingIdPutRequest(object):
    """V1GuestsMeetingIdPutRequest

    :param guests:  会议嘉宾列表（传空数组会清空嘉宾列表）。 (required) 
    :type guests: List[V1GuestsMeetingIdPutRequestGuestsInner]

    :param instanceid: 用户的终端设备类型： 0：PSTN 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch MacOS 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch iOS (required) 
    :type instanceid: int

    :param userid: 用户的 ID（企业内部请使用企业唯一用户标识，OAuth2.0 鉴权用户请使用 openId）。 (required) 
    :type userid: str
    """  # noqa: E501

    guests: List[V1GuestsMeetingIdPutRequestGuestsInner]
    instanceid: int
    userid: str
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        guests: List[V1GuestsMeetingIdPutRequestGuestsInner] | List[Dict[str, Any]],
        instanceid: int,
        userid: str,
        **kwargs
    ):
        
        if guests and isinstance(guests, (list, List)):
            self.guests = [V1GuestsMeetingIdPutRequestGuestsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in guests]
        
        self.instanceid = instanceid
        self.userid = userid


class V1GuestsMeetingIdPutRequestGuestsInner(object):
    """V1GuestsMeetingIdPutRequestGuestsInner

    :param area: 国家/地区代码（例如：中国传86，不是+86，也不是0086）。 (required) 
    :type area: str

    :param guest_name: 嘉宾名称 
    :type guest_name: Optional[str]

    :param phone_number: 手机号 (required) 
    :type phone_number: str
    """  # noqa: E501

    area: str
    guest_name: Optional[str] = None
    phone_number: str
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        area: str,
        phone_number: str,
        guest_name: Optional[str] = None,
        **kwargs
    ):
        self.area = area
        self.guest_name = guest_name
        self.phone_number = phone_number

