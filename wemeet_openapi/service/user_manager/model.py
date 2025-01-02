# coding: utf-8

"""
    腾讯会议OpenAPI

    SAAS版RESTFUL风格API

    API version: v1.0.4

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

from typing import *


class V1MeetingsMeetingIdMsOpenIdGet200Response(object):
    """V1MeetingsMeetingIdMsOpenIdGet200Response

    :param meeting_id: 会议唯一id 
    :type meeting_id: Optional[str]

    :param ms_open_id: 当场会议的用户临时 ID，可用于会控操作，适用于所有用户。 
    :type ms_open_id: Optional[str]
    """  # noqa: E501

    meeting_id: Optional[str] = None
    ms_open_id: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        meeting_id: Optional[str] = None,
        ms_open_id: Optional[str] = None,
        **kwargs
    ):
        self.meeting_id = meeting_id
        self.ms_open_id = ms_open_id


class V1PmiMeetingsPmiConfigGet200Response(object):
    """V1PmiMeetingsPmiConfigGet200Response

    :param allow_in_before_host: 是否允许成员在主持人前入会 
    :type allow_in_before_host: Optional[bool]

    :param allow_in_waiting_room: 是否开启等候室 
    :type allow_in_waiting_room: Optional[bool]

    :param allow_multi_device: 是否允许多端入会 
    :type allow_multi_device: Optional[bool]

    :param disable_note_capture: 是否禁止笔记截屏 
    :type disable_note_capture: Optional[bool]

    :param hosts: 指定主持人列表 
    :type hosts: Optional[List[V1PmiMeetingsPmiConfigGet200ResponseHostsInner]]

    :param mute_enable_type_join: 成员入会静音设置，0-关闭，1-开启，2-超过6人后自动开启 
    :type mute_enable_type_join: Optional[int]

    :param only_enterprise_user_allowed: 是否仅企业内部成员可入会 
    :type only_enterprise_user_allowed: Optional[bool]

    :param pmi_code: 个人会议号 
    :type pmi_code: Optional[str]

    :param pmi_name: 个人会议室名称 
    :type pmi_name: Optional[str]

    :param pmi_password: 个人会议号密码，经过base64处理 
    :type pmi_password: Optional[str]

    :param water_mark_type: 水印样式，0-单排，1-多排 
    :type water_mark_type: Optional[int]

    :param watermark: 是否开启会议水印 
    :type watermark: Optional[bool]
    """  # noqa: E501

    allow_in_before_host: Optional[bool] = None
    allow_in_waiting_room: Optional[bool] = None
    allow_multi_device: Optional[bool] = None
    disable_note_capture: Optional[bool] = None
    hosts: Optional[List[V1PmiMeetingsPmiConfigGet200ResponseHostsInner]] = None
    mute_enable_type_join: Optional[int] = None
    only_enterprise_user_allowed: Optional[bool] = None
    pmi_code: Optional[str] = None
    pmi_name: Optional[str] = None
    pmi_password: Optional[str] = None
    water_mark_type: Optional[int] = None
    watermark: Optional[bool] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        allow_in_before_host: Optional[bool] = None,
        allow_in_waiting_room: Optional[bool] = None,
        allow_multi_device: Optional[bool] = None,
        disable_note_capture: Optional[bool] = None,
        hosts: Optional[List[V1PmiMeetingsPmiConfigGet200ResponseHostsInner] | List[Dict[str, Any]]] = None,
        mute_enable_type_join: Optional[int] = None,
        only_enterprise_user_allowed: Optional[bool] = None,
        pmi_code: Optional[str] = None,
        pmi_name: Optional[str] = None,
        pmi_password: Optional[str] = None,
        water_mark_type: Optional[int] = None,
        watermark: Optional[bool] = None,
        **kwargs
    ):
        self.allow_in_before_host = allow_in_before_host
        self.allow_in_waiting_room = allow_in_waiting_room
        self.allow_multi_device = allow_multi_device
        self.disable_note_capture = disable_note_capture
        
        if hosts and isinstance(hosts, (list, List)):
            self.hosts = [V1PmiMeetingsPmiConfigGet200ResponseHostsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in hosts]
        
        self.mute_enable_type_join = mute_enable_type_join
        self.only_enterprise_user_allowed = only_enterprise_user_allowed
        self.pmi_code = pmi_code
        self.pmi_name = pmi_name
        self.pmi_password = pmi_password
        self.water_mark_type = water_mark_type
        self.watermark = watermark


class V1PmiMeetingsPmiConfigGet200ResponseHostsInner(object):
    """userid

    :param userid:
    :type userid: Optional[str]
    """  # noqa: E501

    userid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        userid: Optional[str] = None,
        **kwargs
    ):
        self.userid = userid


class V1PmiMeetingsPmiConfigPutRequest(object):
    """V1PmiMeetingsPmiConfigPutRequest

    :param allow_in_before_host: 是否允许成员在主持人进会前加入会议 
    :type allow_in_before_host: Optional[bool]

    :param allow_multi_device: 是否允许成员多端入会 
    :type allow_multi_device: Optional[bool]

    :param auto_in_waiting_room: 是否开启等候室 
    :type auto_in_waiting_room: Optional[bool]

    :param disable_note_capture: 禁止笔记截屏，true-禁止，false-不禁止。当水印参数开启时生效 
    :type disable_note_capture: Optional[bool]

    :param enable_password: 是否需要密码 
    :type enable_password: Optional[bool]

    :param hosts: 指定主持人列表 
    :type hosts: Optional[List[V1PmiMeetingsPmiConfigPutRequestHostsInner]]

    :param instanceid: 设备id (required) 
    :type instanceid: int

    :param mute_enable_type_join: 成员入会静音选项，0-关闭，1-开启，2-超过6人开启 
    :type mute_enable_type_join: Optional[int]

    :param only_enterprise_user_allowed: 是否仅企业内部成员可入会 
    :type only_enterprise_user_allowed: Optional[bool]

    :param operator_id: 根据type类型传相应内容 (required) 
    :type operator_id: str

    :param operator_id_type: 操作者ID类型，1 - userid (required) 
    :type operator_id_type: int

    :param pmi_name: 个人会议室名称，最大支持18个汉字或36个英文字母。 
    :type pmi_name: Optional[str]

    :param pmi_password: 入会密码 
    :type pmi_password: Optional[str]

    :param water_mark_type: 水印样式。当水印参数为开启时，此参数才生效。 0：单排 1：多排 
    :type water_mark_type: Optional[int]

    :param watermark: 是否开启会议水印 
    :type watermark: Optional[bool]
    """  # noqa: E501

    allow_in_before_host: Optional[bool] = None
    allow_multi_device: Optional[bool] = None
    auto_in_waiting_room: Optional[bool] = None
    disable_note_capture: Optional[bool] = None
    enable_password: Optional[bool] = None
    hosts: Optional[List[V1PmiMeetingsPmiConfigPutRequestHostsInner]] = None
    instanceid: int
    mute_enable_type_join: Optional[int] = None
    only_enterprise_user_allowed: Optional[bool] = None
    operator_id: str
    operator_id_type: int
    pmi_name: Optional[str] = None
    pmi_password: Optional[str] = None
    water_mark_type: Optional[int] = None
    watermark: Optional[bool] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        instanceid: int,
        operator_id: str,
        operator_id_type: int,
        allow_in_before_host: Optional[bool] = None,
        allow_multi_device: Optional[bool] = None,
        auto_in_waiting_room: Optional[bool] = None,
        disable_note_capture: Optional[bool] = None,
        enable_password: Optional[bool] = None,
        hosts: Optional[List[V1PmiMeetingsPmiConfigPutRequestHostsInner] | List[Dict[str, Any]]] = None,
        mute_enable_type_join: Optional[int] = None,
        only_enterprise_user_allowed: Optional[bool] = None,
        pmi_name: Optional[str] = None,
        pmi_password: Optional[str] = None,
        water_mark_type: Optional[int] = None,
        watermark: Optional[bool] = None,
        **kwargs
    ):
        self.allow_in_before_host = allow_in_before_host
        self.allow_multi_device = allow_multi_device
        self.auto_in_waiting_room = auto_in_waiting_room
        self.disable_note_capture = disable_note_capture
        self.enable_password = enable_password
        
        if hosts and isinstance(hosts, (list, List)):
            self.hosts = [V1PmiMeetingsPmiConfigPutRequestHostsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in hosts]
        
        self.instanceid = instanceid
        self.mute_enable_type_join = mute_enable_type_join
        self.only_enterprise_user_allowed = only_enterprise_user_allowed
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.pmi_name = pmi_name
        self.pmi_password = pmi_password
        self.water_mark_type = water_mark_type
        self.watermark = watermark


class V1PmiMeetingsPmiConfigPutRequestHostsInner(object):
    """V1PmiMeetingsPmiConfigPutRequestHostsInner

    :param is_anonymous: 用户是否匿名入会，缺省为 false，不匿名。 true：匿名 false：不匿名 
    :type is_anonymous: Optional[bool]

    :param nick_name: 用户匿名字符串。如果字段“is_anonymous”设置为“true”，但是无指定匿名字符串, 会议将分配缺省名称，例如 “会议用户xxxx”，其中“xxxx”为随机数字 
    :type nick_name: Optional[str]

    :param operator_id: 操作者ID，根据operator_id_type的值，使用不同的类型 
    :type operator_id: Optional[str]

    :param operator_id_type: 操作者ID的类型：1:userid  2:openid 3:rooms_id  4: ms_open_id 
    :type operator_id_type: Optional[int]

    :param profile_photo: 头像地址 
    :type profile_photo: Optional[str]

    :param userid:
    :type userid: Optional[str]
    """  # noqa: E501

    is_anonymous: Optional[bool] = None
    nick_name: Optional[str] = None
    operator_id: Optional[str] = None
    operator_id_type: Optional[int] = None
    profile_photo: Optional[str] = None
    userid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        is_anonymous: Optional[bool] = None,
        nick_name: Optional[str] = None,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[int] = None,
        profile_photo: Optional[str] = None,
        userid: Optional[str] = None,
        **kwargs
    ):
        self.is_anonymous = is_anonymous
        self.nick_name = nick_name
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.profile_photo = profile_photo
        self.userid = userid


class V1UsersAccountAiAccountDeleteRequest(object):
    """V1UsersAccountAiAccountDeleteRequest

    :param operator_id: 用户拥有企管用户管理权限 (required) 
    :type operator_id: str

    :param operator_id_type: 1:userid (required) 
    :type operator_id_type: int

    :param to_operator_id:(required) 
    :type to_operator_id: str

    :param to_operator_id_type: 1:userid (required) 
    :type to_operator_id_type: int
    """  # noqa: E501

    operator_id: str
    operator_id_type: int
    to_operator_id: str
    to_operator_id_type: int
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        operator_id: str,
        operator_id_type: int,
        to_operator_id: str,
        to_operator_id_type: int,
        **kwargs
    ):
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.to_operator_id = to_operator_id
        self.to_operator_id_type = to_operator_id_type


class V1UsersAccountAiAccountPostRequest(object):
    """V1UsersAccountAiAccountPostRequest

    :param ai_account_type: 1:购买版 2:赠送版AI账号类型  1：购买版  2：赠送版  如果未传入该字段，默认分配赠送版AI账号 
    :type ai_account_type: Optional[int]

    :param operator_id: 操作者ID，拥有用户管理权限 (required) 
    :type operator_id: str

    :param operator_id_type: ID类型，1:userid (required) 
    :type operator_id_type: int

    :param to_operator_id: 被操作者ID，仅支持企业版/教育版高级账号被设置，其他类型账号会报错 (required) 
    :type to_operator_id: str

    :param to_operator_id_type: ID类型  1:userid (required) 
    :type to_operator_id_type: int
    """  # noqa: E501

    ai_account_type: Optional[int] = None
    operator_id: str
    operator_id_type: int
    to_operator_id: str
    to_operator_id_type: int
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        operator_id: str,
        operator_id_type: int,
        to_operator_id: str,
        to_operator_id_type: int,
        ai_account_type: Optional[int] = None,
        **kwargs
    ):
        self.ai_account_type = ai_account_type
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.to_operator_id = to_operator_id
        self.to_operator_id_type = to_operator_id_type


class V1UsersAccountStatisticsGet200Response(object):
    """V1UsersAccountStatisticsGet200Response

    :param ai_account_details: ai账号类型使用对象（商业版不返回） 
    :type ai_account_details: Optional[List[V1UsersAccountStatisticsGet200ResponseAiAccountDetailsInner]]

    :param user_account_details: 账号类型使用对象 
    :type user_account_details: Optional[List[V1UsersAccountStatisticsGet200ResponseUserAccountDetailsInner]]

    :param user_count: 当前用户数 
    :type user_count: Optional[int]
    """  # noqa: E501

    ai_account_details: Optional[List[V1UsersAccountStatisticsGet200ResponseAiAccountDetailsInner]] = None
    user_account_details: Optional[List[V1UsersAccountStatisticsGet200ResponseUserAccountDetailsInner]] = None
    user_count: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        ai_account_details: Optional[List[V1UsersAccountStatisticsGet200ResponseAiAccountDetailsInner] | List[Dict[str, Any]]] = None,
        user_account_details: Optional[List[V1UsersAccountStatisticsGet200ResponseUserAccountDetailsInner] | List[Dict[str, Any]]] = None,
        user_count: Optional[int] = None,
        **kwargs
    ):
        
        if ai_account_details and isinstance(ai_account_details, (list, List)):
            self.ai_account_details = [V1UsersAccountStatisticsGet200ResponseAiAccountDetailsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in ai_account_details]
        
        
        if user_account_details and isinstance(user_account_details, (list, List)):
            self.user_account_details = [V1UsersAccountStatisticsGet200ResponseUserAccountDetailsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in user_account_details]
        
        self.user_count = user_count


class V1UsersAccountStatisticsGet200ResponseAiAccountDetailsInner(object):
    """V1UsersAccountStatisticsGet200ResponseAiAccountDetailsInner

    :param ai_account_count: 账号数 
    :type ai_account_count: Optional[int]

    :param ai_account_type: ai账号类型，1:购买版 2:赠送版 
    :type ai_account_type: Optional[int]

    :param ai_account_used_count: 已分配的账号数 
    :type ai_account_used_count: Optional[int]
    """  # noqa: E501

    ai_account_count: Optional[int] = None
    ai_account_type: Optional[int] = None
    ai_account_used_count: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        ai_account_count: Optional[int] = None,
        ai_account_type: Optional[int] = None,
        ai_account_used_count: Optional[int] = None,
        **kwargs
    ):
        self.ai_account_count = ai_account_count
        self.ai_account_type = ai_account_type
        self.ai_account_used_count = ai_account_used_count


class V1UsersAccountStatisticsGet200ResponseUserAccountDetailsInner(object):
    """V1UsersAccountStatisticsGet200ResponseUserAccountDetailsInner

    :param user_account_count: 账号数 
    :type user_account_count: Optional[int]

    :param user_account_type: 账号类型，1：高级账号 （企业版，教育版）  2：免费账号  （企业版，教育版，商业版）  3：免费账号100方 （商业版）  4：高级账号300方（商业版）  5：高级账号500方（商业版）  6：高级账号1000方（商业版）  7：高级账号2000方（商业版） 
    :type user_account_type: Optional[int]

    :param user_account_used_count: 已分配账号数 
    :type user_account_used_count: Optional[int]
    """  # noqa: E501

    user_account_count: Optional[int] = None
    user_account_type: Optional[int] = None
    user_account_used_count: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        user_account_count: Optional[int] = None,
        user_account_type: Optional[int] = None,
        user_account_used_count: Optional[int] = None,
        **kwargs
    ):
        self.user_account_count = user_account_count
        self.user_account_type = user_account_type
        self.user_account_used_count = user_account_used_count


class V1UsersAdvanceListGet200Response(object):
    """V1UsersAdvanceListGet200Response

    :param has_remaining: 是否还有未拉取的数据 
    :type has_remaining: Optional[bool]

    :param next_pos: 下一次查询pos位置 
    :type next_pos: Optional[str]

    :param users:
    :type users: Optional[List[V1UsersAdvanceListGet200ResponseUsersInner]]
    """  # noqa: E501

    has_remaining: Optional[bool] = None
    next_pos: Optional[str] = None
    users: Optional[List[V1UsersAdvanceListGet200ResponseUsersInner]] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        has_remaining: Optional[bool] = None,
        next_pos: Optional[str] = None,
        users: Optional[List[V1UsersAdvanceListGet200ResponseUsersInner] | List[Dict[str, Any]]] = None,
        **kwargs
    ):
        self.has_remaining = has_remaining
        self.next_pos = next_pos
        
        if users and isinstance(users, (list, List)):
            self.users = [V1UsersAdvanceListGet200ResponseUsersInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in users]
        


class V1UsersAdvanceListGet200ResponseUsersInner(object):
    """V1UsersAdvanceListGet200ResponseUsersInner

    :param account_version: 账号版本。 0：其他 1：商业版 2：企业版 3：教育版 
    :type account_version: Optional[int]

    :param ai_account_type: AI 账号类型。 0：无账号 1：购买版 2：赠送版 
    :type ai_account_type: Optional[int]

    :param area: 手机区号 
    :type area: Optional[str]

    :param avatar_url: 头像地址 
    :type avatar_url: Optional[str]

    :param department_list: 用户部门信息 
    :type department_list: Optional[List[V1UsersAdvanceListGet200ResponseUsersInnerDepartmentListInner]]

    :param email: 邮箱 
    :type email: Optional[str]

    :param enable_ai_account: 是否有 AI 账号能力。 true：有  false：无  教育版/企业版存在有 AI 账号，商业版都具有 AI 能力，其余为 false。 
    :type enable_ai_account: Optional[bool]

    :param entry_time: 入职时间 
    :type entry_time: Optional[str]

    :param job_title: 员工职位 
    :type job_title: Optional[str]

    :param phone: 手机号 
    :type phone: Optional[str]

    :param phone_status: 手机号验证状态。 0：未知 1：已验证 2：未验证 
    :type phone_status: Optional[int]

    :param role_code: 角色类型 
    :type role_code: Optional[str]

    :param role_name: 角色名称 
    :type role_name: Optional[str]

    :param staff_id: 员工工号 
    :type staff_id: Optional[str]

    :param status: 账号状态。账号状态： 1：正常 2：注销 3：未激活 4：禁用 5：预注册 
    :type status: Optional[str]

    :param update_time: 更新时间 
    :type update_time: Optional[str]

    :param user_account_type: 账号类型。 1：高级账号（企业版/教育版） 2：免费账号（企业版/教育版） 3：免费账号100方 （商业版） 4：高级账号300方（商业版） 5：高级账号500方（商业版） 6：高级账号1000方（商业版） 7：高级账号2000方（商业版） 8：高级账号100方（商业版） 
    :type user_account_type: Optional[int]

    :param userid: 用户userid 
    :type userid: Optional[str]

    :param username: 用户名称 
    :type username: Optional[str]

    :param uuid: 用户uuid 
    :type uuid: Optional[str]
    """  # noqa: E501

    account_version: Optional[int] = None
    ai_account_type: Optional[int] = None
    area: Optional[str] = None
    avatar_url: Optional[str] = None
    department_list: Optional[List[V1UsersAdvanceListGet200ResponseUsersInnerDepartmentListInner]] = None
    email: Optional[str] = None
    enable_ai_account: Optional[bool] = None
    entry_time: Optional[str] = None
    job_title: Optional[str] = None
    phone: Optional[str] = None
    phone_status: Optional[int] = None
    role_code: Optional[str] = None
    role_name: Optional[str] = None
    staff_id: Optional[str] = None
    status: Optional[str] = None
    update_time: Optional[str] = None
    user_account_type: Optional[int] = None
    userid: Optional[str] = None
    username: Optional[str] = None
    uuid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        account_version: Optional[int] = None,
        ai_account_type: Optional[int] = None,
        area: Optional[str] = None,
        avatar_url: Optional[str] = None,
        department_list: Optional[List[V1UsersAdvanceListGet200ResponseUsersInnerDepartmentListInner] | List[Dict[str, Any]]] = None,
        email: Optional[str] = None,
        enable_ai_account: Optional[bool] = None,
        entry_time: Optional[str] = None,
        job_title: Optional[str] = None,
        phone: Optional[str] = None,
        phone_status: Optional[int] = None,
        role_code: Optional[str] = None,
        role_name: Optional[str] = None,
        staff_id: Optional[str] = None,
        status: Optional[str] = None,
        update_time: Optional[str] = None,
        user_account_type: Optional[int] = None,
        userid: Optional[str] = None,
        username: Optional[str] = None,
        uuid: Optional[str] = None,
        **kwargs
    ):
        self.account_version = account_version
        self.ai_account_type = ai_account_type
        self.area = area
        self.avatar_url = avatar_url
        
        if department_list and isinstance(department_list, (list, List)):
            self.department_list = [V1UsersAdvanceListGet200ResponseUsersInnerDepartmentListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in department_list]
        
        self.email = email
        self.enable_ai_account = enable_ai_account
        self.entry_time = entry_time
        self.job_title = job_title
        self.phone = phone
        self.phone_status = phone_status
        self.role_code = role_code
        self.role_name = role_name
        self.staff_id = staff_id
        self.status = status
        self.update_time = update_time
        self.user_account_type = user_account_type
        self.userid = userid
        self.username = username
        self.uuid = uuid


class V1UsersAdvanceListGet200ResponseUsersInnerDepartmentListInner(object):
    """V1UsersAdvanceListGet200ResponseUsersInnerDepartmentListInner

    :param department_full_name: 部门全路径 
    :type department_full_name: Optional[str]

    :param department_id: 部门ID 
    :type department_id: Optional[str]

    :param department_name: 部门名称 
    :type department_name: Optional[str]

    :param is_main: 是否主部门 
    :type is_main: Optional[bool]
    """  # noqa: E501

    department_full_name: Optional[str] = None
    department_id: Optional[str] = None
    department_name: Optional[str] = None
    is_main: Optional[bool] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        department_full_name: Optional[str] = None,
        department_id: Optional[str] = None,
        department_name: Optional[str] = None,
        is_main: Optional[bool] = None,
        **kwargs
    ):
        self.department_full_name = department_full_name
        self.department_id = department_id
        self.department_name = department_name
        self.is_main = is_main


class V1UsersDeleteTransferPostRequest(object):
    """V1UsersDeleteTransferPostRequest

    :param data_process: 删除用户的数据处理方式： 1=彻底删除； 2=转移给指定成员； 
    :type data_process: Optional[str]

    :param operator_id: 操作者 ID。 operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 operator_id_type=2，operator_id 必须和公共参数的 openid 一致。 (required) 
    :type operator_id: str

    :param operator_id_type: 操作者 ID 的类型： 1：userid 2：open_id (required) 
    :type operator_id_type: int

    :param receiver_id: 数据接收者的ID，根据receiver_id_type的值，使用不同的类型。； data_process为2时生效； 该userid不存在时，将报错； 
    :type receiver_id: Optional[str]

    :param receiver_id_type: 数据接收者 ID 的类型：  1：userid  2：open_id 
    :type receiver_id_type: Optional[int]

    :param to_operator_id: 被操作者 ID，根据 to_operator_id_type 的值，使用不同的类型，这里指被删除的用户。 (required) 
    :type to_operator_id: str

    :param to_operator_id_type: 被操作者 ID 的类型： 1：userid 2：open_id (required) 
    :type to_operator_id_type: int

    :param transfer_data: 转移的具体数据； 0=全部； 1=云录制； 2=会议列表； data_process为2时生效； 不传时默认为0； 
    :type transfer_data: Optional[str]
    """  # noqa: E501

    data_process: Optional[str] = None
    operator_id: str
    operator_id_type: int
    receiver_id: Optional[str] = None
    receiver_id_type: Optional[int] = None
    to_operator_id: str
    to_operator_id_type: int
    transfer_data: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        operator_id: str,
        operator_id_type: int,
        to_operator_id: str,
        to_operator_id_type: int,
        data_process: Optional[str] = None,
        receiver_id: Optional[str] = None,
        receiver_id_type: Optional[int] = None,
        transfer_data: Optional[str] = None,
        **kwargs
    ):
        self.data_process = data_process
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.receiver_id = receiver_id
        self.receiver_id_type = receiver_id_type
        self.to_operator_id = to_operator_id
        self.to_operator_id_type = to_operator_id_type
        self.transfer_data = transfer_data


class V1UsersGet200Response(object):
    """V1UsersGet200Response

    :param ai_account_type: ai账号类型 1：购买版 2:赠送版 
    :type ai_account_type: Optional[int]

    :param area: 地区编码（国内默认86）。 
    :type area: Optional[str]

    :param department_list: 用户部门信息。 
    :type department_list: Optional[List[V1UsersGet200ResponseDepartmentListInner]]

    :param email: 邮箱地址。 
    :type email: Optional[str]

    :param enable_ai_account: 是否有ai账号能力 
    :type enable_ai_account: Optional[bool]

    :param entry_time: 入职时间。 
    :type entry_time: Optional[str]

    :param job_title: 员工职位。 
    :type job_title: Optional[str]

    :param phone: 企业员工手机号码。 
    :type phone: Optional[str]

    :param phone_status: 手机号验证状态。 0：未知 1：已验证 2：未验证 
    :type phone_status: Optional[int]

    :param role_code: 角色类型。 
    :type role_code: Optional[str]

    :param role_name: 角色名称。 
    :type role_name: Optional[str]

    :param staff_id: 员工工号。 
    :type staff_id: Optional[str]

    :param status: 用户状态： 1：正常 2：注销 3：未激活 4：禁用 
    :type status: Optional[str]

    :param update_time: 更新时间，格式：yyyy-MM-dd HH:mm:ss。 
    :type update_time: Optional[str]

    :param userid: 调用方用于标示用户的唯一 ID（例如企业用户可以为企业账户英文名、个人用户可以为手机号等）。 
    :type userid: Optional[str]

    :param username: 用户昵称。 
    :type username: Optional[str]

    :param uuid: String 用户身份 ID（腾讯会议颁发的用于开放平台的唯一用户 ID）。 
    :type uuid: Optional[str]
    """  # noqa: E501

    ai_account_type: Optional[int] = None
    area: Optional[str] = None
    department_list: Optional[List[V1UsersGet200ResponseDepartmentListInner]] = None
    email: Optional[str] = None
    enable_ai_account: Optional[bool] = None
    entry_time: Optional[str] = None
    job_title: Optional[str] = None
    phone: Optional[str] = None
    phone_status: Optional[int] = None
    role_code: Optional[str] = None
    role_name: Optional[str] = None
    staff_id: Optional[str] = None
    status: Optional[str] = None
    update_time: Optional[str] = None
    userid: Optional[str] = None
    username: Optional[str] = None
    uuid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        ai_account_type: Optional[int] = None,
        area: Optional[str] = None,
        department_list: Optional[List[V1UsersGet200ResponseDepartmentListInner] | List[Dict[str, Any]]] = None,
        email: Optional[str] = None,
        enable_ai_account: Optional[bool] = None,
        entry_time: Optional[str] = None,
        job_title: Optional[str] = None,
        phone: Optional[str] = None,
        phone_status: Optional[int] = None,
        role_code: Optional[str] = None,
        role_name: Optional[str] = None,
        staff_id: Optional[str] = None,
        status: Optional[str] = None,
        update_time: Optional[str] = None,
        userid: Optional[str] = None,
        username: Optional[str] = None,
        uuid: Optional[str] = None,
        **kwargs
    ):
        self.ai_account_type = ai_account_type
        self.area = area
        
        if department_list and isinstance(department_list, (list, List)):
            self.department_list = [V1UsersGet200ResponseDepartmentListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in department_list]
        
        self.email = email
        self.enable_ai_account = enable_ai_account
        self.entry_time = entry_time
        self.job_title = job_title
        self.phone = phone
        self.phone_status = phone_status
        self.role_code = role_code
        self.role_name = role_name
        self.staff_id = staff_id
        self.status = status
        self.update_time = update_time
        self.userid = userid
        self.username = username
        self.uuid = uuid


class V1UsersGet200ResponseDepartmentListInner(object):
    """V1UsersGet200ResponseDepartmentListInner

    :param department_id: 部门 ID。 
    :type department_id: Optional[str]

    :param department_name: 部门名称。 
    :type department_name: Optional[str]
    """  # noqa: E501

    department_id: Optional[str] = None
    department_name: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        department_id: Optional[str] = None,
        department_name: Optional[str] = None,
        **kwargs
    ):
        self.department_id = department_id
        self.department_name = department_name


class V1UsersInfoBasicGet200Response(object):
    """V1UsersInfoBasicGet200Response

    :param account_type:
    :type account_type: Optional[int]

    :param account_version: 商企版计费需求，账号版本 
    :type account_version: Optional[int]

    :param ai_account_type: AI账号类型 1:购买版 2:赠送版 
    :type ai_account_type: Optional[int]

    :param avatar_url:
    :type avatar_url: Optional[str]

    :param enable_ai_account: 是否有AI账号能力，true：有， false：无，教育版/企业版存在ai账号，商业版都是ai账号，其余为false 
    :type enable_ai_account: Optional[bool]

    :param open_corp_id:
    :type open_corp_id: Optional[str]

    :param open_corp_name:
    :type open_corp_name: Optional[str]

    :param phone_status: 手机号验证状态。 0：未知 1：已验证 2：未验证 
    :type phone_status: Optional[int]

    :param status:
    :type status: Optional[str]

    :param user_account_type: 账号类型 1：高级账号  2：免费账号  3：免费账号100方 4:高级账号300方，5:高级账号500方，6：高级账号1000方，7:高级账号2000方 
    :type user_account_type: Optional[int]

    :param username:
    :type username: Optional[str]
    """  # noqa: E501

    account_type: Optional[int] = None
    account_version: Optional[int] = None
    ai_account_type: Optional[int] = None
    avatar_url: Optional[str] = None
    enable_ai_account: Optional[bool] = None
    open_corp_id: Optional[str] = None
    open_corp_name: Optional[str] = None
    phone_status: Optional[int] = None
    status: Optional[str] = None
    user_account_type: Optional[int] = None
    username: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        account_type: Optional[int] = None,
        account_version: Optional[int] = None,
        ai_account_type: Optional[int] = None,
        avatar_url: Optional[str] = None,
        enable_ai_account: Optional[bool] = None,
        open_corp_id: Optional[str] = None,
        open_corp_name: Optional[str] = None,
        phone_status: Optional[int] = None,
        status: Optional[str] = None,
        user_account_type: Optional[int] = None,
        username: Optional[str] = None,
        **kwargs
    ):
        self.account_type = account_type
        self.account_version = account_version
        self.ai_account_type = ai_account_type
        self.avatar_url = avatar_url
        self.enable_ai_account = enable_ai_account
        self.open_corp_id = open_corp_id
        self.open_corp_name = open_corp_name
        self.phone_status = phone_status
        self.status = status
        self.user_account_type = user_account_type
        self.username = username


class V1UsersInviteActivatePost200Response(object):
    """V1UsersInviteActivatePost200Response

    :param inactivate_user_list: 未激活用户对象列表 
    :type inactivate_user_list: Optional[List[V1UsersInviteActivatePost200ResponseInactivateUserListInner]]
    """  # noqa: E501

    inactivate_user_list: Optional[List[V1UsersInviteActivatePost200ResponseInactivateUserListInner]] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        inactivate_user_list: Optional[List[V1UsersInviteActivatePost200ResponseInactivateUserListInner] | List[Dict[str, Any]]] = None,
        **kwargs
    ):
        
        if inactivate_user_list and isinstance(inactivate_user_list, (list, List)):
            self.inactivate_user_list = [V1UsersInviteActivatePost200ResponseInactivateUserListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in inactivate_user_list]
        


class V1UsersInviteActivatePost200ResponseInactivateUserListInner(object):
    """V1UsersInviteActivatePost200ResponseInactivateUserListInner

    :param activate_url: 激活链接 
    :type activate_url: Optional[str]

    :param userid:
    :type userid: Optional[str]
    """  # noqa: E501

    activate_url: Optional[str] = None
    userid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        activate_url: Optional[str] = None,
        userid: Optional[str] = None,
        **kwargs
    ):
        self.activate_url = activate_url
        self.userid = userid


class V1UsersInviteActivatePostRequest(object):
    """V1UsersInviteActivatePostRequest

    :param operator_id: 操作者ID (required) 
    :type operator_id: str

    :param operator_id_type: 操作者ID类型，1:userid (required) 
    :type operator_id_type: int

    :param userid_list: 未激活的账号列表，最多支持传100个 (required) 
    :type userid_list: List[str]
    """  # noqa: E501

    operator_id: str
    operator_id_type: int
    userid_list: List[str]
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        operator_id: str,
        operator_id_type: int,
        userid_list: List[str],
        **kwargs
    ):
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        
        if userid_list and isinstance(userid_list, (list, List)):
            self.userid_list = userid_list
        


class V1UsersInviteAuthPost200Response(object):
    """V1UsersInviteAuthPost200Response

    :param auth_user_list: 未验证用户对象列表 
    :type auth_user_list: Optional[List[V1UsersInviteAuthPost200ResponseAuthUserListInner]]

    :param error_user_list:
    :type error_user_list: Optional[List[V1UsersInviteAuthPost200ResponseErrorUserListInner]]
    """  # noqa: E501

    auth_user_list: Optional[List[V1UsersInviteAuthPost200ResponseAuthUserListInner]] = None
    error_user_list: Optional[List[V1UsersInviteAuthPost200ResponseErrorUserListInner]] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        auth_user_list: Optional[List[V1UsersInviteAuthPost200ResponseAuthUserListInner] | List[Dict[str, Any]]] = None,
        error_user_list: Optional[List[V1UsersInviteAuthPost200ResponseErrorUserListInner] | List[Dict[str, Any]]] = None,
        **kwargs
    ):
        
        if auth_user_list and isinstance(auth_user_list, (list, List)):
            self.auth_user_list = [V1UsersInviteAuthPost200ResponseAuthUserListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in auth_user_list]
        
        
        if error_user_list and isinstance(error_user_list, (list, List)):
            self.error_user_list = [V1UsersInviteAuthPost200ResponseErrorUserListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in error_user_list]
        


class V1UsersInviteAuthPost200ResponseAuthUserListInner(object):
    """V1UsersInviteAuthPost200ResponseAuthUserListInner

    :param auth_url: 验证链接 
    :type auth_url: Optional[str]

    :param userid: 账号 ID 
    :type userid: Optional[str]
    """  # noqa: E501

    auth_url: Optional[str] = None
    userid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        auth_url: Optional[str] = None,
        userid: Optional[str] = None,
        **kwargs
    ):
        self.auth_url = auth_url
        self.userid = userid


class V1UsersInviteAuthPost200ResponseErrorUserListInner(object):
    """V1UsersInviteAuthPost200ResponseErrorUserListInner

    :param error_code: 错误码 
    :type error_code: Optional[int]

    :param error_msg: 错误描述 
    :type error_msg: Optional[str]

    :param userid: 账号ID 
    :type userid: Optional[str]
    """  # noqa: E501

    error_code: Optional[int] = None
    error_msg: Optional[str] = None
    userid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        error_code: Optional[int] = None,
        error_msg: Optional[str] = None,
        userid: Optional[str] = None,
        **kwargs
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        self.userid = userid


class V1UsersInviteAuthPostRequest(object):
    """V1UsersInviteAuthPostRequest

    :param operator_id: 操作者 ID。operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 (required) 
    :type operator_id: str

    :param operator_id_type: 操作者 ID 的类型： 1：userid (required) 
    :type operator_id_type: int

    :param userid_list: 未验证 userid 列表，最多一次支持传100个 (required) 
    :type userid_list: List[str]
    """  # noqa: E501

    operator_id: str
    operator_id_type: int
    userid_list: List[str]
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        operator_id: str,
        operator_id_type: int,
        userid_list: List[str],
        **kwargs
    ):
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        
        if userid_list and isinstance(userid_list, (list, List)):
            self.userid_list = userid_list
        


class V1UsersListGet200Response(object):
    """V1UsersListGet200Response

    :param current_page: 当前页数。 
    :type current_page: Optional[int]

    :param current_size: 当前页实际大小。 
    :type current_size: Optional[int]

    :param page_size: 分页大小。 
    :type page_size: Optional[int]

    :param total_count: 总数。 
    :type total_count: Optional[int]

    :param users: 数组格式，item 为用户对象。 
    :type users: Optional[List[V1UsersListGet200ResponseUsersInner]]
    """  # noqa: E501

    current_page: Optional[int] = None
    current_size: Optional[int] = None
    page_size: Optional[int] = None
    total_count: Optional[int] = None
    users: Optional[List[V1UsersListGet200ResponseUsersInner]] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        current_page: Optional[int] = None,
        current_size: Optional[int] = None,
        page_size: Optional[int] = None,
        total_count: Optional[int] = None,
        users: Optional[List[V1UsersListGet200ResponseUsersInner] | List[Dict[str, Any]]] = None,
        **kwargs
    ):
        self.current_page = current_page
        self.current_size = current_size
        self.page_size = page_size
        self.total_count = total_count
        
        if users and isinstance(users, (list, List)):
            self.users = [V1UsersListGet200ResponseUsersInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in users]
        


class V1UsersListGet200ResponseUsersInner(object):
    """V1UsersListGet200ResponseUsersInner

    :param account_version: 账号版本 
    :type account_version: Optional[int]

    :param ai_account_type: ai账号类型 1:购买版 2:赠送版 
    :type ai_account_type: Optional[int]

    :param area: 手机区号。 
    :type area: Optional[str]

    :param avatar_url: 用户图像地址。 
    :type avatar_url: Optional[str]

    :param department_list: 用户部门信息。 
    :type department_list: Optional[List[V1UsersListGet200ResponseUsersInnerDepartmentListInner]]

    :param email: 邮箱。 
    :type email: Optional[str]

    :param enable_ai_account: 是否有ai账号能力  true：有  false：无  教育版/企业版存在有ai账号，商业版都具有ai能力，其余为false 
    :type enable_ai_account: Optional[bool]

    :param entry_time: 入职时间。 
    :type entry_time: Optional[str]

    :param job_title: 员工职位。 
    :type job_title: Optional[str]

    :param phone: 手机号。 
    :type phone: Optional[str]

    :param phone_status: 手机号验证状态。 0：未知 1：已验证 2：未验证 
    :type phone_status: Optional[int]

    :param role_code: 角色类型。 
    :type role_code: Optional[str]

    :param role_name: 角色名称。 
    :type role_name: Optional[str]

    :param staff_id: String  员工工号。 
    :type staff_id: Optional[str]

    :param status: 账号状态： 1：正常 2：注销 3：未激活 4：禁用 
    :type status: Optional[str]

    :param update_time: String  更新时间。 
    :type update_time: Optional[str]

    :param user_account_type: 账号类型    1：高级账号 （企业版，教育版）  2：免费账号  （企业版，教育版，商业版）  3：免费账号100方 （商业版）  4：高级账号300方（商业版）  5：高级账号500方（商业版）  6：高级账号1000方（商业版）  7:高级账号2000方（商业版） 
    :type user_account_type: Optional[int]

    :param userid: String  用户 userid。 
    :type userid: Optional[str]

    :param username: 用户 name。 
    :type username: Optional[str]

    :param uuid: 用户身份 ID（腾讯会议颁发的用于开放平台的唯一用户 ID）。 
    :type uuid: Optional[str]
    """  # noqa: E501

    account_version: Optional[int] = None
    ai_account_type: Optional[int] = None
    area: Optional[str] = None
    avatar_url: Optional[str] = None
    department_list: Optional[List[V1UsersListGet200ResponseUsersInnerDepartmentListInner]] = None
    email: Optional[str] = None
    enable_ai_account: Optional[bool] = None
    entry_time: Optional[str] = None
    job_title: Optional[str] = None
    phone: Optional[str] = None
    phone_status: Optional[int] = None
    role_code: Optional[str] = None
    role_name: Optional[str] = None
    staff_id: Optional[str] = None
    status: Optional[str] = None
    update_time: Optional[str] = None
    user_account_type: Optional[int] = None
    userid: Optional[str] = None
    username: Optional[str] = None
    uuid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        account_version: Optional[int] = None,
        ai_account_type: Optional[int] = None,
        area: Optional[str] = None,
        avatar_url: Optional[str] = None,
        department_list: Optional[List[V1UsersListGet200ResponseUsersInnerDepartmentListInner] | List[Dict[str, Any]]] = None,
        email: Optional[str] = None,
        enable_ai_account: Optional[bool] = None,
        entry_time: Optional[str] = None,
        job_title: Optional[str] = None,
        phone: Optional[str] = None,
        phone_status: Optional[int] = None,
        role_code: Optional[str] = None,
        role_name: Optional[str] = None,
        staff_id: Optional[str] = None,
        status: Optional[str] = None,
        update_time: Optional[str] = None,
        user_account_type: Optional[int] = None,
        userid: Optional[str] = None,
        username: Optional[str] = None,
        uuid: Optional[str] = None,
        **kwargs
    ):
        self.account_version = account_version
        self.ai_account_type = ai_account_type
        self.area = area
        self.avatar_url = avatar_url
        
        if department_list and isinstance(department_list, (list, List)):
            self.department_list = [V1UsersListGet200ResponseUsersInnerDepartmentListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in department_list]
        
        self.email = email
        self.enable_ai_account = enable_ai_account
        self.entry_time = entry_time
        self.job_title = job_title
        self.phone = phone
        self.phone_status = phone_status
        self.role_code = role_code
        self.role_name = role_name
        self.staff_id = staff_id
        self.status = status
        self.update_time = update_time
        self.user_account_type = user_account_type
        self.userid = userid
        self.username = username
        self.uuid = uuid


class V1UsersListGet200ResponseUsersInnerDepartmentListInner(object):
    """DepartmentInfo对象数组

    :param department_id: 部门 ID。 
    :type department_id: Optional[str]

    :param department_name: String  部门名称。 
    :type department_name: Optional[str]
    """  # noqa: E501

    department_id: Optional[str] = None
    department_name: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        department_id: Optional[str] = None,
        department_name: Optional[str] = None,
        **kwargs
    ):
        self.department_id = department_id
        self.department_name = department_name


class V1UsersOpenIdToUseridPost200Response(object):
    """V1UsersOpenIdToUseridPost200Response

    :param userid_list: 转换成功的该自建应用所在企业下的userid、open_id对应关系列表。 
    :type userid_list: Optional[List[V1UsersOpenIdToUseridPost200ResponseUseridListInner]]
    """  # noqa: E501

    userid_list: Optional[List[V1UsersOpenIdToUseridPost200ResponseUseridListInner]] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        userid_list: Optional[List[V1UsersOpenIdToUseridPost200ResponseUseridListInner] | List[Dict[str, Any]]] = None,
        **kwargs
    ):
        
        if userid_list and isinstance(userid_list, (list, List)):
            self.userid_list = [V1UsersOpenIdToUseridPost200ResponseUseridListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in userid_list]
        


class V1UsersOpenIdToUseridPost200ResponseUseridListInner(object):
    """V1UsersOpenIdToUseridPost200ResponseUseridListInner

    :param open_id: 需要转换的open_id 
    :type open_id: Optional[str]

    :param userid: 转换成功后，该open_id所对应的本企业下用户的userid。 
    :type userid: Optional[str]
    """  # noqa: E501

    open_id: Optional[str] = None
    userid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        open_id: Optional[str] = None,
        userid: Optional[str] = None,
        **kwargs
    ):
        self.open_id = open_id
        self.userid = userid


class V1UsersOpenIdToUseridPostRequest(object):
    """V1UsersOpenIdToUseridPostRequest

    :param operator_id: 操作者ID (required) 
    :type operator_id: str

    :param operator_id_type: 操作者ID类型 (required) 
    :type operator_id_type: int

    :param sdkid: 第三方应用的sdkid。需要转换的open_id应为腾讯会议为该三方应用提供的open_id。 (required) 
    :type sdkid: str
    """  # noqa: E501

    operator_id: str
    operator_id_type: int
    sdkid: str
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        operator_id: str,
        operator_id_type: int,
        sdkid: str,
        **kwargs
    ):
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.sdkid = sdkid


class V1UsersPost200Response(object):
    """V1UsersPost200Response

    :param email:
    :type email: Optional[str]

    :param phone:
    :type phone: Optional[str]

    :param userid:
    :type userid: Optional[str]

    :param username:
    :type username: Optional[str]

    :param uuid:
    :type uuid: Optional[str]
    """  # noqa: E501

    email: Optional[str] = None
    phone: Optional[str] = None
    userid: Optional[str] = None
    username: Optional[str] = None
    uuid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        userid: Optional[str] = None,
        username: Optional[str] = None,
        uuid: Optional[str] = None,
        **kwargs
    ):
        self.email = email
        self.phone = phone
        self.userid = userid
        self.username = username
        self.uuid = uuid


class V1UsersPostRequest(object):
    """V1UsersPostRequest

    :param area:
    :type area: Optional[str]

    :param auto_invite: 自动发送邀请，开启之后调用接口后自动发送激活邀请 true：开启，默认开启;false：关闭 
    :type auto_invite: Optional[bool]

    :param email:
    :type email: Optional[str]

    :param entry_time:
    :type entry_time: Optional[int]

    :param job_title:
    :type job_title: Optional[str]

    :param operator_id: 操作者ID (required) 
    :type operator_id: str

    :param operator_id_type: 操作者ID类型，1:userid (required) 
    :type operator_id_type: int

    :param phone:(required) 
    :type phone: str

    :param staff_id:
    :type staff_id: Optional[str]

    :param user_account_type: 1：高级账号  2：免费账号  3：免费账号100方 4:高级账号300方，5:高级账号500方，6：高级账号1000方，7:高级账号2000方     其中企业版/教育版：1，2 。免费组织 2。 商业版：2-7      根据传入的参数判断是否有该类型账号，没有则报错。创建成功即锁定该账号资源。默认值：商业版默认为高级账号，绑定资源为由小到大，资源消耗完账号为免费账号，企业版-高级账号 
    :type user_account_type: Optional[int]

    :param userid:(required) 
    :type userid: str

    :param username:(required) 
    :type username: str
    """  # noqa: E501

    area: Optional[str] = None
    auto_invite: Optional[bool] = None
    email: Optional[str] = None
    entry_time: Optional[int] = None
    job_title: Optional[str] = None
    operator_id: str
    operator_id_type: int
    phone: str
    staff_id: Optional[str] = None
    user_account_type: Optional[int] = None
    userid: str
    username: str
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        operator_id: str,
        operator_id_type: int,
        phone: str,
        userid: str,
        username: str,
        area: Optional[str] = None,
        auto_invite: Optional[bool] = None,
        email: Optional[str] = None,
        entry_time: Optional[int] = None,
        job_title: Optional[str] = None,
        staff_id: Optional[str] = None,
        user_account_type: Optional[int] = None,
        **kwargs
    ):
        self.area = area
        self.auto_invite = auto_invite
        self.email = email
        self.entry_time = entry_time
        self.job_title = job_title
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.phone = phone
        self.staff_id = staff_id
        self.user_account_type = user_account_type
        self.userid = userid
        self.username = username


class V1UsersPutRequest(object):
    """V1UsersPutRequest

    :param avatar_url:
    :type avatar_url: Optional[str]

    :param department_list: 员工部门，暂只支持为用户分配1个部门。 
    :type department_list: Optional[List[str]]

    :param email:
    :type email: Optional[str]

    :param entry_time:
    :type entry_time: Optional[int]

    :param job_title:
    :type job_title: Optional[str]

    :param operator_id: 操作者ID (required) 
    :type operator_id: str

    :param operator_id_type: 操作者ID类型，1:userid (required) 
    :type operator_id_type: int

    :param phone:
    :type phone: Optional[str]

    :param staff_id:
    :type staff_id: Optional[str]

    :param username:
    :type username: Optional[str]
    """  # noqa: E501

    avatar_url: Optional[str] = None
    department_list: Optional[List[str]] = None
    email: Optional[str] = None
    entry_time: Optional[int] = None
    job_title: Optional[str] = None
    operator_id: str
    operator_id_type: int
    phone: Optional[str] = None
    staff_id: Optional[str] = None
    username: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        operator_id: str,
        operator_id_type: int,
        avatar_url: Optional[str] = None,
        department_list: Optional[List[str]] = None,
        email: Optional[str] = None,
        entry_time: Optional[int] = None,
        job_title: Optional[str] = None,
        phone: Optional[str] = None,
        staff_id: Optional[str] = None,
        username: Optional[str] = None,
        **kwargs
    ):
        self.avatar_url = avatar_url
        
        if department_list and isinstance(department_list, (list, List)):
            self.department_list = department_list
        
        self.email = email
        self.entry_time = entry_time
        self.job_title = job_title
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.phone = phone
        self.staff_id = staff_id
        self.username = username


class V1UsersUseridEnablePutRequest(object):
    """V1UsersUseridEnablePutRequest

    :param enable: 是否启用用户： true：启用 false：禁用 (required) 
    :type enable: bool

    :param operator_id: 操作者ID (required) 
    :type operator_id: str

    :param operator_id_type: 操作者ID类型，1:userid (required) 
    :type operator_id_type: int
    """  # noqa: E501

    enable: bool
    operator_id: str
    operator_id_type: int
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        enable: bool,
        operator_id: str,
        operator_id_type: int,
        **kwargs
    ):
        self.enable = enable
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type


class V1UsersUseridGet200Response(object):
    """V1UsersUseridGet200Response

    :param account_type:
    :type account_type: Optional[int]

    :param account_version: 账号版本 
    :type account_version: Optional[int]

    :param ai_account_type: ai账号类型 1:购买版 2:赠送版 
    :type ai_account_type: Optional[int]

    :param area:
    :type area: Optional[str]

    :param avatar_url:
    :type avatar_url: Optional[str]

    :param department_list:
    :type department_list: Optional[List[V1UsersUseridGet200ResponseDepartmentListInner]]

    :param email:
    :type email: Optional[str]

    :param enable_ai_account: 是否有ai账号能力，true：有，false：无 
    :type enable_ai_account: Optional[bool]

    :param entry_time:
    :type entry_time: Optional[str]

    :param job_title:
    :type job_title: Optional[str]

    :param phone:
    :type phone: Optional[str]

    :param phone_status: 手机号验证状态。 0：未知 1：已验证 2：未验证 
    :type phone_status: Optional[int]

    :param role_code:
    :type role_code: Optional[str]

    :param role_name:
    :type role_name: Optional[str]

    :param staff_id:
    :type staff_id: Optional[str]

    :param status:
    :type status: Optional[str]

    :param update_time:
    :type update_time: Optional[str]

    :param user_account_type:  1：高级账号  2：免费账号  3：免费账号100方 4:高级账号300方，5:高级账号500方，6：高级账号1000方，7:高级账号2000方 
    :type user_account_type: Optional[int]

    :param userid:
    :type userid: Optional[str]

    :param username:
    :type username: Optional[str]

    :param uuid:
    :type uuid: Optional[str]
    """  # noqa: E501

    account_type: Optional[int] = None
    account_version: Optional[int] = None
    ai_account_type: Optional[int] = None
    area: Optional[str] = None
    avatar_url: Optional[str] = None
    department_list: Optional[List[V1UsersUseridGet200ResponseDepartmentListInner]] = None
    email: Optional[str] = None
    enable_ai_account: Optional[bool] = None
    entry_time: Optional[str] = None
    job_title: Optional[str] = None
    phone: Optional[str] = None
    phone_status: Optional[int] = None
    role_code: Optional[str] = None
    role_name: Optional[str] = None
    staff_id: Optional[str] = None
    status: Optional[str] = None
    update_time: Optional[str] = None
    user_account_type: Optional[int] = None
    userid: Optional[str] = None
    username: Optional[str] = None
    uuid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        account_type: Optional[int] = None,
        account_version: Optional[int] = None,
        ai_account_type: Optional[int] = None,
        area: Optional[str] = None,
        avatar_url: Optional[str] = None,
        department_list: Optional[List[V1UsersUseridGet200ResponseDepartmentListInner] | List[Dict[str, Any]]] = None,
        email: Optional[str] = None,
        enable_ai_account: Optional[bool] = None,
        entry_time: Optional[str] = None,
        job_title: Optional[str] = None,
        phone: Optional[str] = None,
        phone_status: Optional[int] = None,
        role_code: Optional[str] = None,
        role_name: Optional[str] = None,
        staff_id: Optional[str] = None,
        status: Optional[str] = None,
        update_time: Optional[str] = None,
        user_account_type: Optional[int] = None,
        userid: Optional[str] = None,
        username: Optional[str] = None,
        uuid: Optional[str] = None,
        **kwargs
    ):
        self.account_type = account_type
        self.account_version = account_version
        self.ai_account_type = ai_account_type
        self.area = area
        self.avatar_url = avatar_url
        
        if department_list and isinstance(department_list, (list, List)):
            self.department_list = [V1UsersUseridGet200ResponseDepartmentListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in department_list]
        
        self.email = email
        self.enable_ai_account = enable_ai_account
        self.entry_time = entry_time
        self.job_title = job_title
        self.phone = phone
        self.phone_status = phone_status
        self.role_code = role_code
        self.role_name = role_name
        self.staff_id = staff_id
        self.status = status
        self.update_time = update_time
        self.user_account_type = user_account_type
        self.userid = userid
        self.username = username
        self.uuid = uuid


class V1UsersUseridGet200ResponseDepartmentListInner(object):
    """V1UsersUseridGet200ResponseDepartmentListInner

    :param department_id:
    :type department_id: Optional[str]

    :param department_name:
    :type department_name: Optional[str]
    """  # noqa: E501

    department_id: Optional[str] = None
    department_name: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        department_id: Optional[str] = None,
        department_name: Optional[str] = None,
        **kwargs
    ):
        self.department_id = department_id
        self.department_name = department_name


class V1UsersUseridInviteAuthPutRequest(object):
    """V1UsersUseridInviteAuthPutRequest

    :param operator_id: 操作者 ID。operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 (required) 
    :type operator_id: str

    :param operator_id_type: 操作者 ID 的类型： 1：userid (required) 
    :type operator_id_type: int
    """  # noqa: E501

    operator_id: str
    operator_id_type: int
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        operator_id: str,
        operator_id_type: int,
        **kwargs
    ):
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type


class V1UsersUseridPutRequest(object):
    """V1UsersUseridPutRequest

    :param area:
    :type area: Optional[str]

    :param avatar_url:
    :type avatar_url: Optional[str]

    :param email:
    :type email: Optional[str]

    :param entry_time:
    :type entry_time: Optional[int]

    :param job_title:
    :type job_title: Optional[str]

    :param operator_id: 操作者ID (required) 
    :type operator_id: str

    :param operator_id_type: 操作者ID类型，1:userid (required) 
    :type operator_id_type: int

    :param phone:
    :type phone: Optional[str]

    :param staff_id:
    :type staff_id: Optional[str]

    :param user_account_type: 1：高级账号 2：免费账号 3：免费账号100方 4:高级账号300方，5:高级账号500方，6：高级账号1000方，7:高级账号2000方 其中企业版/教育版：1，2 。免费组织 2。 商业版：2-7 根据传入的参数判断是否有该类型账号，没有则报错。更新后，原类型账号资源释放。 
    :type user_account_type: Optional[int]

    :param userid:
    :type userid: Optional[str]

    :param username:
    :type username: Optional[str]
    """  # noqa: E501

    area: Optional[str] = None
    avatar_url: Optional[str] = None
    email: Optional[str] = None
    entry_time: Optional[int] = None
    job_title: Optional[str] = None
    operator_id: str
    operator_id_type: int
    phone: Optional[str] = None
    staff_id: Optional[str] = None
    user_account_type: Optional[int] = None
    userid: Optional[str] = None
    username: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        operator_id: str,
        operator_id_type: int,
        area: Optional[str] = None,
        avatar_url: Optional[str] = None,
        email: Optional[str] = None,
        entry_time: Optional[int] = None,
        job_title: Optional[str] = None,
        phone: Optional[str] = None,
        staff_id: Optional[str] = None,
        user_account_type: Optional[int] = None,
        userid: Optional[str] = None,
        username: Optional[str] = None,
        **kwargs
    ):
        self.area = area
        self.avatar_url = avatar_url
        self.email = email
        self.entry_time = entry_time
        self.job_title = job_title
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.phone = phone
        self.staff_id = staff_id
        self.user_account_type = user_account_type
        self.userid = userid
        self.username = username

