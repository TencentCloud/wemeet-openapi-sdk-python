# coding: utf-8

"""
    腾讯会议OpenAPI

    SAAS版RESTFUL风格API

    API version: v1.0.8

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

from typing import *


class V1MeetingMeetingIdPhoneCalloutPost200Response(object):
    """V1MeetingMeetingIdPhoneCalloutPost200Response

    :param invalid_phone_numbers: 外呼的电话号码对象列表。 
    :type invalid_phone_numbers: Optional[List[V1MeetingMeetingIdPhoneCalloutPost200ResponseInvalidPhoneNumbersInner]]

    :param meeting_id: 会议的唯一ID 
    :type meeting_id: Optional[str]

    :param phone_numbers: 外呼的电话号码对象列表。 
    :type phone_numbers: Optional[List[V1MeetingMeetingIdPhoneCalloutPost200ResponseInvalidPhoneNumbersInner]]
    """  # noqa: E501

    invalid_phone_numbers: Optional[List[V1MeetingMeetingIdPhoneCalloutPost200ResponseInvalidPhoneNumbersInner]] = None
    meeting_id: Optional[str] = None
    phone_numbers: Optional[List[V1MeetingMeetingIdPhoneCalloutPost200ResponseInvalidPhoneNumbersInner]] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        invalid_phone_numbers: Optional[List[V1MeetingMeetingIdPhoneCalloutPost200ResponseInvalidPhoneNumbersInner] | List[Dict[str, Any]]] = None,
        meeting_id: Optional[str] = None,
        phone_numbers: Optional[List[V1MeetingMeetingIdPhoneCalloutPost200ResponseInvalidPhoneNumbersInner] | List[Dict[str, Any]]] = None,
        **kwargs
    ):
        
        if invalid_phone_numbers and isinstance(invalid_phone_numbers, (list, List)):
            self.invalid_phone_numbers = [V1MeetingMeetingIdPhoneCalloutPost200ResponseInvalidPhoneNumbersInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in invalid_phone_numbers]
        
        self.meeting_id = meeting_id
        
        if phone_numbers and isinstance(phone_numbers, (list, List)):
            self.phone_numbers = [V1MeetingMeetingIdPhoneCalloutPost200ResponseInvalidPhoneNumbersInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in phone_numbers]
        


class V1MeetingMeetingIdPhoneCalloutPost200ResponseInvalidPhoneNumbersInner(object):
    """电话号码对象

    :param area: 电话区号 
    :type area: Optional[int]

    :param extension_number:
    :type extension_number: Optional[str]

    :param phone:
    :type phone: Optional[str]
    """  # noqa: E501

    area: Optional[int] = None
    extension_number: Optional[str] = None
    phone: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        area: Optional[int] = None,
        extension_number: Optional[str] = None,
        phone: Optional[str] = None,
        **kwargs
    ):
        self.area = area
        self.extension_number = extension_number
        self.phone = phone


class V1MeetingMeetingIdPhoneCalloutPostRequest(object):
    """V1MeetingMeetingIdPhoneCalloutPostRequest

    :param operator_id: 操作者 ID。会议创建者、主持人、联席主持人可以调用该接口。 operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 (required) 
    :type operator_id: str

    :param operator_id_type: 操作者 ID 的类型： 1：企业内用户 userid。 2: openid 3. rooms_id 4: ms_open_id (required) 
    :type operator_id_type: int

    :param phone_numbers: 外呼的电话号码对象列表。 (required) 
    :type phone_numbers: List[V1MeetingMeetingIdPhoneCalloutPostRequestPhoneNumbersInner]
    """  # noqa: E501

    operator_id: str
    operator_id_type: int
    phone_numbers: List[V1MeetingMeetingIdPhoneCalloutPostRequestPhoneNumbersInner]
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        operator_id: str,
        operator_id_type: int,
        phone_numbers: List[V1MeetingMeetingIdPhoneCalloutPostRequestPhoneNumbersInner] | List[Dict[str, Any]],
        **kwargs
    ):
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        
        if phone_numbers and isinstance(phone_numbers, (list, List)):
            self.phone_numbers = [V1MeetingMeetingIdPhoneCalloutPostRequestPhoneNumbersInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in phone_numbers]
        


class V1MeetingMeetingIdPhoneCalloutPostRequestPhoneNumbersInner(object):
    """电话号码对象

    :param area: 电话区号 (required) 
    :type area: int

    :param calling_party_area: 国家/地区代码。（例如：中国是86） 当前仅支持呼叫中国大陆、中国香港、美国的号码。 
    :type calling_party_area: Optional[int]

    :param calling_party_phone_number: 电话号码或固定电话总机号。 
    :type calling_party_phone_number: Optional[str]

    :param extension_number:
    :type extension_number: Optional[str]

    :param nick_name:
    :type nick_name: Optional[str]

    :param phone:(required) 
    :type phone: str
    """  # noqa: E501

    area: int
    calling_party_area: Optional[int] = None
    calling_party_phone_number: Optional[str] = None
    extension_number: Optional[str] = None
    nick_name: Optional[str] = None
    phone: str
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        area: int,
        phone: str,
        calling_party_area: Optional[int] = None,
        calling_party_phone_number: Optional[str] = None,
        extension_number: Optional[str] = None,
        nick_name: Optional[str] = None,
        **kwargs
    ):
        self.area = area
        self.calling_party_area = calling_party_area
        self.calling_party_phone_number = calling_party_phone_number
        self.extension_number = extension_number
        self.nick_name = nick_name
        self.phone = phone


class V1MeetingMeetingIdPhoneCancelcallPost200Response(object):
    """V1MeetingMeetingIdPhoneCancelcallPost200Response

    :param failed_list: 取消呼叫失败的列表 
    :type failed_list: Optional[List[V1MeetingMeetingIdPhoneCancelcallPost200ResponseFailedListInner]]

    :param success_list: 取消呼叫成功的列表 
    :type success_list: Optional[List[V1MeetingMeetingIdPhoneCancelcallPost200ResponseSuccessListInner]]
    """  # noqa: E501

    failed_list: Optional[List[V1MeetingMeetingIdPhoneCancelcallPost200ResponseFailedListInner]] = None
    success_list: Optional[List[V1MeetingMeetingIdPhoneCancelcallPost200ResponseSuccessListInner]] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        failed_list: Optional[List[V1MeetingMeetingIdPhoneCancelcallPost200ResponseFailedListInner] | List[Dict[str, Any]]] = None,
        success_list: Optional[List[V1MeetingMeetingIdPhoneCancelcallPost200ResponseSuccessListInner] | List[Dict[str, Any]]] = None,
        **kwargs
    ):
        
        if failed_list and isinstance(failed_list, (list, List)):
            self.failed_list = [V1MeetingMeetingIdPhoneCancelcallPost200ResponseFailedListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in failed_list]
        
        
        if success_list and isinstance(success_list, (list, List)):
            self.success_list = [V1MeetingMeetingIdPhoneCancelcallPost200ResponseSuccessListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in success_list]
        


class V1MeetingMeetingIdPhoneCancelcallPost200ResponseFailedListInner(object):
    """V1MeetingMeetingIdPhoneCancelcallPost200ResponseFailedListInner

    :param area: 国家/地区代码。（例如：中国是86） 
    :type area: Optional[int]

    :param error_msg: 错误信息 
    :type error_msg: Optional[str]

    :param extension_number: 固定电话分机号。 
    :type extension_number: Optional[str]

    :param phone: 电话号码或固定电话总机号。 
    :type phone: Optional[str]
    """  # noqa: E501

    area: Optional[int] = None
    error_msg: Optional[str] = None
    extension_number: Optional[str] = None
    phone: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        area: Optional[int] = None,
        error_msg: Optional[str] = None,
        extension_number: Optional[str] = None,
        phone: Optional[str] = None,
        **kwargs
    ):
        self.area = area
        self.error_msg = error_msg
        self.extension_number = extension_number
        self.phone = phone


class V1MeetingMeetingIdPhoneCancelcallPost200ResponseSuccessListInner(object):
    """V1MeetingMeetingIdPhoneCancelcallPost200ResponseSuccessListInner

    :param area: 国家/地区代码。（例如：中国是86） 
    :type area: Optional[int]

    :param extension_number: 固定电话分机号。 
    :type extension_number: Optional[str]

    :param phone: 电话号码或固定电话总机号。 
    :type phone: Optional[str]
    """  # noqa: E501

    area: Optional[int] = None
    extension_number: Optional[str] = None
    phone: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        area: Optional[int] = None,
        extension_number: Optional[str] = None,
        phone: Optional[str] = None,
        **kwargs
    ):
        self.area = area
        self.extension_number = extension_number
        self.phone = phone


class V1MeetingMeetingIdPhoneCancelcallPostRequest(object):
    """V1MeetingMeetingIdPhoneCancelcallPostRequest

    :param operator_id: 操作者 ID。会议创建者、主持人、联席主持人可以调用该接口。 operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 (required) 
    :type operator_id: str

    :param operator_id_type: 操作者 ID 的类型： 1：企业内用户 userid。  (required) 
    :type operator_id_type: int

    :param phone_numbers: 电话号码对象数组 (required) 
    :type phone_numbers: List[V1MeetingMeetingIdPhoneCancelcallPostRequestPhoneNumbersInner]
    """  # noqa: E501

    operator_id: str
    operator_id_type: int
    phone_numbers: List[V1MeetingMeetingIdPhoneCancelcallPostRequestPhoneNumbersInner]
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        operator_id: str,
        operator_id_type: int,
        phone_numbers: List[V1MeetingMeetingIdPhoneCancelcallPostRequestPhoneNumbersInner] | List[Dict[str, Any]],
        **kwargs
    ):
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        
        if phone_numbers and isinstance(phone_numbers, (list, List)):
            self.phone_numbers = [V1MeetingMeetingIdPhoneCancelcallPostRequestPhoneNumbersInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in phone_numbers]
        


class V1MeetingMeetingIdPhoneCancelcallPostRequestPhoneNumbersInner(object):
    """V1MeetingMeetingIdPhoneCancelcallPostRequestPhoneNumbersInner

    :param area: 国家/地区代码。（例如：中国是86） (required) 
    :type area: int

    :param extension_number: 固定电话分机号。 
    :type extension_number: Optional[str]

    :param phone: 电话号码或固定电话总机号。 (required) 
    :type phone: str
    """  # noqa: E501

    area: int
    extension_number: Optional[str] = None
    phone: str
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        area: int,
        phone: str,
        extension_number: Optional[str] = None,
        **kwargs
    ):
        self.area = area
        self.extension_number = extension_number
        self.phone = phone

