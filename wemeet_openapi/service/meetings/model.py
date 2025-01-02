# coding: utf-8

"""
    腾讯会议OpenAPI

    SAAS版RESTFUL风格API

    API version: v1.0.4

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

from typing import *


class V1AsrConfigPut200Response(object):
    """V1AsrConfigPut200Response

    :param customize_words: 热词设置结果 
    :type customize_words: Optional[List[str]]

    :param tag: 自定义热词标签 
    :type tag: Optional[str]
    """  # noqa: E501

    customize_words: Optional[List[str]] = None
    tag: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        customize_words: Optional[List[str]] = None,
        tag: Optional[str] = None,
        **kwargs
    ):
        
        if customize_words and isinstance(customize_words, (list, List)):
            self.customize_words = customize_words
        
        self.tag = tag


class V1AsrConfigPutRequest(object):
    """V1AsrConfigPutRequest

    :param customize_words:  自定义热词，不得包含数字、特殊字符、中英混合，中文十个字以内，英文 20 个字母以内。同场会议或同一个人每次设置会覆盖上次设置内容。会议维度最多支持设置 500 个，创建者维度最多支持设置 100 个。 (required) 
    :type customize_words: List[str]

    :param meeting_id: 会议ID，有该字段则对该场会议生效。不传该字段则对操作人创建的会议生效 
    :type meeting_id: Optional[str]

    :param operator_id: 操作者ID (required) 
    :type operator_id: str

    :param operator_id_type: 操作者ID类型 1:userid，2:openid (required) 
    :type operator_id_type: int

    :param tag: 自定义热词标签，便于热词分类，最多支持输入 32 个字符（中英文） (required) 
    :type tag: str
    """  # noqa: E501

    customize_words: List[str]
    meeting_id: Optional[str] = None
    operator_id: str
    operator_id_type: int
    tag: str
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        customize_words: List[str],
        operator_id: str,
        operator_id_type: int,
        tag: str,
        meeting_id: Optional[str] = None,
        **kwargs
    ):
        
        if customize_words and isinstance(customize_words, (list, List)):
            self.customize_words = customize_words
        
        self.meeting_id = meeting_id
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.tag = tag


class V1AsrDetailsGet200Response(object):
    """V1AsrDetailsGet200Response

    :param curr_page: 分页查询返回分页总数 
    :type curr_page: Optional[int]

    :param curr_size: 分页查询返回当前页码 
    :type curr_size: Optional[int]

    :param download_url: 文件下载链接列表，有效期2个小时 
    :type download_url: Optional[List[str]]

    :param total_count: 分页查询返回数据总数 
    :type total_count: Optional[int]

    :param total_page: 分页查询返回单页数据条数 
    :type total_page: Optional[int]
    """  # noqa: E501

    curr_page: Optional[int] = None
    curr_size: Optional[int] = None
    download_url: Optional[List[str]] = None
    total_count: Optional[int] = None
    total_page: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        curr_page: Optional[int] = None,
        curr_size: Optional[int] = None,
        download_url: Optional[List[str]] = None,
        total_count: Optional[int] = None,
        total_page: Optional[int] = None,
        **kwargs
    ):
        self.curr_page = curr_page
        self.curr_size = curr_size
        
        if download_url and isinstance(download_url, (list, List)):
            self.download_url = download_url
        
        self.total_count = total_count
        self.total_page = total_page


class V1AsrPushStatusPostRequest(object):
    """V1AsrPushStatusPostRequest

    :param is_open: 开启/取消转写内容推送 true：开启推送 false：取消推送 (required) 
    :type is_open: bool

    :param meeting_id: 会议 ID。 (required) 
    :type meeting_id: str

    :param operator_id: 操作者ID。operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 (required) 
    :type operator_id: str

    :param operator_id_type: 操作者ID类型： 1：userid 2:openid (required) 
    :type operator_id_type: int
    """  # noqa: E501

    is_open: bool
    meeting_id: str
    operator_id: str
    operator_id_type: int
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        is_open: bool,
        meeting_id: str,
        operator_id: str,
        operator_id_type: int,
        **kwargs
    ):
        self.is_open = is_open
        self.meeting_id = meeting_id
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type


class V1HistoryMeetingsUseridGet200Response(object):
    """V1HistoryMeetingsUseridGet200Response

    :param current_page: 当前页 
    :type current_page: Optional[int]

    :param current_size: 当前实际页大小 
    :type current_size: Optional[int]

    :param meeting_info_list:
    :type meeting_info_list: Optional[List[V1HistoryMeetingsUseridGet200ResponseMeetingInfoListInner]]

    :param total_count: 数据总条数 
    :type total_count: Optional[int]

    :param total_page: 数据总页数 
    :type total_page: Optional[int]
    """  # noqa: E501

    current_page: Optional[int] = None
    current_size: Optional[int] = None
    meeting_info_list: Optional[List[V1HistoryMeetingsUseridGet200ResponseMeetingInfoListInner]] = None
    total_count: Optional[int] = None
    total_page: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        current_page: Optional[int] = None,
        current_size: Optional[int] = None,
        meeting_info_list: Optional[List[V1HistoryMeetingsUseridGet200ResponseMeetingInfoListInner] | List[Dict[str, Any]]] = None,
        total_count: Optional[int] = None,
        total_page: Optional[int] = None,
        **kwargs
    ):
        self.current_page = current_page
        self.current_size = current_size
        
        if meeting_info_list and isinstance(meeting_info_list, (list, List)):
            self.meeting_info_list = [V1HistoryMeetingsUseridGet200ResponseMeetingInfoListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in meeting_info_list]
        
        self.total_count = total_count
        self.total_page = total_page


class V1HistoryMeetingsUseridGet200ResponseMeetingInfoListInner(object):
    """V1HistoryMeetingsUseridGet200ResponseMeetingInfoListInner

    :param end_time: 会议结束时间戳，UNIX 时间戳（单位秒）。 
    :type end_time: Optional[int]

    :param meeting_code: 会议 App 的呼入号码。 
    :type meeting_code: Optional[str]

    :param meeting_id: 会议ID 
    :type meeting_id: Optional[str]

    :param meeting_type: 会议类型 0：一次性会议 1：周期性会议 2：微信专属会议 3：Rooms 投屏会议 5：个人会议号会议 6：网络研讨会 
    :type meeting_type: Optional[int]

    :param start_time: 会议开始时间戳，UNIX 时间戳（单位秒）。 
    :type start_time: Optional[int]

    :param sub_meeting_id:
    :type sub_meeting_id: Optional[str]

    :param subject: 会议主题 
    :type subject: Optional[str]
    """  # noqa: E501

    end_time: Optional[int] = None
    meeting_code: Optional[str] = None
    meeting_id: Optional[str] = None
    meeting_type: Optional[int] = None
    start_time: Optional[int] = None
    sub_meeting_id: Optional[str] = None
    subject: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        end_time: Optional[int] = None,
        meeting_code: Optional[str] = None,
        meeting_id: Optional[str] = None,
        meeting_type: Optional[int] = None,
        start_time: Optional[int] = None,
        sub_meeting_id: Optional[str] = None,
        subject: Optional[str] = None,
        **kwargs
    ):
        self.end_time = end_time
        self.meeting_code = meeting_code
        self.meeting_id = meeting_id
        self.meeting_type = meeting_type
        self.start_time = start_time
        self.sub_meeting_id = sub_meeting_id
        self.subject = subject


class V1MeetingJobIdGet200Response(object):
    """V1MeetingJobIdGet200Response

    :param error_msg: 任务错误信息 
    :type error_msg: Optional[str]

    :param job_url: 任务下载链接，有效期2小时。 
    :type job_url: Optional[str]

    :param status: 任务状态。 0：未完成 1：已完成 
    :type status: Optional[int]
    """  # noqa: E501

    error_msg: Optional[str] = None
    job_url: Optional[str] = None
    status: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        error_msg: Optional[str] = None,
        job_url: Optional[str] = None,
        status: Optional[int] = None,
        **kwargs
    ):
        self.error_msg = error_msg
        self.job_url = job_url
        self.status = status


class V1MeetingMeetingIdWaitingRoomGet200Response(object):
    """V1MeetingMeetingIdWaitingRoomGet200Response

    :param current_page: 当前页码 
    :type current_page: Optional[int]

    :param current_size: 当前页数据条数 
    :type current_size: Optional[int]

    :param meeting_code: 会议CODE 
    :type meeting_code: Optional[str]

    :param meeting_id: 会议的唯一ID 
    :type meeting_id: Optional[str]

    :param participants: 人员对象数组 
    :type participants: Optional[List[V1MeetingMeetingIdWaitingRoomGet200ResponseParticipantsInner]]

    :param schedule_end_time: 预定结束时间（单位：毫秒） 
    :type schedule_end_time: Optional[int]

    :param schedule_start_time: 预定开始时间（单位：毫秒） 
    :type schedule_start_time: Optional[int]

    :param subject: 会议主题 
    :type subject: Optional[str]

    :param total_count: 总数据条数 
    :type total_count: Optional[int]

    :param total_page: 总页数 
    :type total_page: Optional[int]
    """  # noqa: E501

    current_page: Optional[int] = None
    current_size: Optional[int] = None
    meeting_code: Optional[str] = None
    meeting_id: Optional[str] = None
    participants: Optional[List[V1MeetingMeetingIdWaitingRoomGet200ResponseParticipantsInner]] = None
    schedule_end_time: Optional[int] = None
    schedule_start_time: Optional[int] = None
    subject: Optional[str] = None
    total_count: Optional[int] = None
    total_page: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        current_page: Optional[int] = None,
        current_size: Optional[int] = None,
        meeting_code: Optional[str] = None,
        meeting_id: Optional[str] = None,
        participants: Optional[List[V1MeetingMeetingIdWaitingRoomGet200ResponseParticipantsInner] | List[Dict[str, Any]]] = None,
        schedule_end_time: Optional[int] = None,
        schedule_start_time: Optional[int] = None,
        subject: Optional[str] = None,
        total_count: Optional[int] = None,
        total_page: Optional[int] = None,
        **kwargs
    ):
        self.current_page = current_page
        self.current_size = current_size
        self.meeting_code = meeting_code
        self.meeting_id = meeting_id
        
        if participants and isinstance(participants, (list, List)):
            self.participants = [V1MeetingMeetingIdWaitingRoomGet200ResponseParticipantsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in participants]
        
        self.schedule_end_time = schedule_end_time
        self.schedule_start_time = schedule_start_time
        self.subject = subject
        self.total_count = total_count
        self.total_page = total_page


class V1MeetingMeetingIdWaitingRoomGet200ResponseParticipantsInner(object):
    """V1MeetingMeetingIdWaitingRoomGet200ResponseParticipantsInner

    :param app_version: 应用版本 
    :type app_version: Optional[str]

    :param customer_data: 专属链接进入等候室的昵称 
    :type customer_data: Optional[str]

    :param instanceid: 用户的终端设备类型： 0：PSTN 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch MacOS 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch iOS 
    :type instanceid: Optional[str]

    :param join_time: 加入时间（单位：毫秒） 
    :type join_time: Optional[int]

    :param left_time: 离开时间（单位：毫秒） 
    :type left_time: Optional[int]

    :param ms_open_id: 当场会议的用户临时 ID，可用于会控操作，适用于所有用户。  
    :type ms_open_id: Optional[str]

    :param open_id: OAuth2.0 鉴权用户的ID。 
    :type open_id: Optional[str]

    :param user_name: 入会用户名（base64） 
    :type user_name: Optional[str]

    :param userid: 成员用户 ID 
    :type userid: Optional[str]
    """  # noqa: E501

    app_version: Optional[str] = None
    customer_data: Optional[str] = None
    instanceid: Optional[str] = None
    join_time: Optional[int] = None
    left_time: Optional[int] = None
    ms_open_id: Optional[str] = None
    open_id: Optional[str] = None
    user_name: Optional[str] = None
    userid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        app_version: Optional[str] = None,
        customer_data: Optional[str] = None,
        instanceid: Optional[str] = None,
        join_time: Optional[int] = None,
        left_time: Optional[int] = None,
        ms_open_id: Optional[str] = None,
        open_id: Optional[str] = None,
        user_name: Optional[str] = None,
        userid: Optional[str] = None,
        **kwargs
    ):
        self.app_version = app_version
        self.customer_data = customer_data
        self.instanceid = instanceid
        self.join_time = join_time
        self.left_time = left_time
        self.ms_open_id = ms_open_id
        self.open_id = open_id
        self.user_name = user_name
        self.userid = userid


class V1MeetingSetWaitingRoomWelcomeMessagePost200Response(object):
    """V1MeetingSetWaitingRoomWelcomeMessagePost200Response

    :param enable_welcome: 是否开启等候室欢迎语能力。 
    :type enable_welcome: Optional[bool]

    :param welcome_text: 欢迎语，文本类型，最大长度1000字符。欢迎语中如果传入占位符%NICKNAME%（大小写敏感），则该占位符会被替换为被私聊用户的会中昵称。一条消息中支持多个占位符。 
    :type welcome_text: Optional[str]
    """  # noqa: E501

    enable_welcome: Optional[bool] = None
    welcome_text: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        enable_welcome: Optional[bool] = None,
        welcome_text: Optional[str] = None,
        **kwargs
    ):
        self.enable_welcome = enable_welcome
        self.welcome_text = welcome_text


class V1MeetingSetWaitingRoomWelcomeMessagePostRequest(object):
    """V1MeetingSetWaitingRoomWelcomeMessagePostRequest

    :param enable_welcome: 是否开启等候室欢迎语能力。 (required) 
    :type enable_welcome: bool

    :param meeting_id: 会议ID (required) 
    :type meeting_id: str

    :param operator_id: 操作者 ID，设置等候室欢迎语的用户。会议的创建者、主持人、联席主持人，企业管理平台有会控权限的用户可以设置。  operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 (required) 
    :type operator_id: str

    :param operator_id_type: 操作者 ID 的类型： 1: 企业内用户 userid。 2: open_id (required) 
    :type operator_id_type: int

    :param welcome_text: 欢迎语，文本类型，最大长度1000字符。欢迎语中如果传入占位符%NICKNAME%（大小写敏感），则该占位符会被替换为被私聊用户的会中昵称。一条消息中支持多个占位符。 (required) 
    :type welcome_text: str
    """  # noqa: E501

    enable_welcome: bool
    meeting_id: str
    operator_id: str
    operator_id_type: int
    welcome_text: str
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        enable_welcome: bool,
        meeting_id: str,
        operator_id: str,
        operator_id_type: int,
        welcome_text: str,
        **kwargs
    ):
        self.enable_welcome = enable_welcome
        self.meeting_id = meeting_id
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.welcome_text = welcome_text


class V1MeetingsCustomerShortUrlPost200Response(object):
    """V1MeetingsCustomerShortUrlPost200Response

    :param meeting_short_url_customer_data:
    :type meeting_short_url_customer_data: Optional[V1MeetingsCustomerShortUrlPost200ResponseMeetingShortUrlCustomerData]
    """  # noqa: E501

    meeting_short_url_customer_data: Optional[V1MeetingsCustomerShortUrlPost200ResponseMeetingShortUrlCustomerData] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        meeting_short_url_customer_data: Optional[V1MeetingsCustomerShortUrlPost200ResponseMeetingShortUrlCustomerData | Dict[str, Any]] = None,
        **kwargs
    ):
        self.meeting_short_url_customer_data = V1MeetingsCustomerShortUrlPost200ResponseMeetingShortUrlCustomerData(**meeting_short_url_customer_data) if isinstance(meeting_short_url_customer_data, (dict, Dict)) else meeting_short_url_customer_data


class V1MeetingsCustomerShortUrlPost200ResponseMeetingShortUrlCustomerData(object):
    """用户专属参会链接对象。

    :param customer_data: 用户专属字段 
    :type customer_data: Optional[str]

    :param meeting_short_url: 用户专属参会链接 
    :type meeting_short_url: Optional[str]
    """  # noqa: E501

    customer_data: Optional[str] = None
    meeting_short_url: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        customer_data: Optional[str] = None,
        meeting_short_url: Optional[str] = None,
        **kwargs
    ):
        self.customer_data = customer_data
        self.meeting_short_url = meeting_short_url


class V1MeetingsCustomerShortUrlPostRequest(object):
    """V1MeetingsCustomerShortUrlPostRequest

    :param customer_data: 自定义参数，长度不超过256 字节。 (required) 
    :type customer_data: str

    :param meeting_id: 会议ID (required) 
    :type meeting_id: str
    """  # noqa: E501

    customer_data: str
    meeting_id: str
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        customer_data: str,
        meeting_id: str,
        **kwargs
    ):
        self.customer_data = customer_data
        self.meeting_id = meeting_id


class V1MeetingsGet200Response(object):
    """V1MeetingsGet200Response

    :param meeting_info_list:
    :type meeting_info_list: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInner]]

    :param meeting_number: 会议数量。 
    :type meeting_number: Optional[int]

    :param next_cursory: 分页获取用户会议列表，查询的会议的最后一次修改时间值，UNIX 毫秒级时间戳，分页游标。 因目前一次查询返回会议数量最多为20，当用户会议较多时，如果会议总数量超过20，则需要再次查询。此参数为非必选参数，默认值为0，表示第一次查询利用会议开始时间北京时间当日零点进行查询。 查询返回输出参数“remaining”不为0时，表示还有会议需要继续查询。返回参数“next_cursory”的值即为下一次查询的 cursory 的值。 多次调用该查询接口直到输出参数“remaining”值为0。 当只使用 pos 作为分页条件时,可能会出现查询不到第二页,数据排序出现重复数据等情况与 pos 配合使用。 
    :type next_cursory: Optional[int]

    :param next_pos: 下次查询时请求里需要携带的 pos 参数。 
    :type next_pos: Optional[int]

    :param remaining: 是否还剩下会议；因目前一次查询返回会议数量最多为20，如果会议总数量超过20则此字段被置为非0，表示需要再次查询，且下次查询的“pos”参数需从本次响应的“next_pos”字段取值 
    :type remaining: Optional[int]
    """  # noqa: E501

    meeting_info_list: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInner]] = None
    meeting_number: Optional[int] = None
    next_cursory: Optional[int] = None
    next_pos: Optional[int] = None
    remaining: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        meeting_info_list: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInner] | List[Dict[str, Any]]] = None,
        meeting_number: Optional[int] = None,
        next_cursory: Optional[int] = None,
        next_pos: Optional[int] = None,
        remaining: Optional[int] = None,
        **kwargs
    ):
        
        if meeting_info_list and isinstance(meeting_info_list, (list, List)):
            self.meeting_info_list = [V1MeetingsGet200ResponseMeetingInfoListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in meeting_info_list]
        
        self.meeting_number = meeting_number
        self.next_cursory = next_cursory
        self.next_pos = next_pos
        self.remaining = remaining


class V1MeetingsGet200ResponseMeetingInfoListInner(object):
    """V1MeetingsGet200ResponseMeetingInfoListInner

    :param current_co_hosts:
    :type current_co_hosts: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner]]

    :param current_hosts:
    :type current_hosts: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner]]

    :param current_sub_meeting_id: 当前子会议 ID（进行中 / 即将开始）。 
    :type current_sub_meeting_id: Optional[str]

    :param enable_doc_upload_permission:
    :type enable_doc_upload_permission: Optional[bool]

    :param enable_enroll:
    :type enable_enroll: Optional[bool]

    :param enable_host_key:
    :type enable_host_key: Optional[bool]

    :param enable_live:
    :type enable_live: Optional[bool]

    :param end_time:
    :type end_time: Optional[str]

    :param guests:
    :type guests: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInnerGuestsInner]]

    :param has_more_sub_meeting: 0：无更多。  1：有更多子会议特例。 
    :type has_more_sub_meeting: Optional[int]

    :param has_vote:
    :type has_vote: Optional[bool]

    :param host_key:
    :type host_key: Optional[str]

    :param hosts:
    :type hosts: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner]]

    :param join_meeting_role: 查询者在会议中的角色： creator：创建者 hoster：主持人 invitee：被邀请者 
    :type join_meeting_role: Optional[str]

    :param join_url:
    :type join_url: Optional[str]

    :param live_config:
    :type live_config: Optional[V1MeetingsGet200ResponseMeetingInfoListInnerLiveConfig]

    :param location:
    :type location: Optional[str]

    :param media_set_type: 该参数仅提供给支持混合云的企业可见，默认值为0。 0：公网会议 1：专网会议 
    :type media_set_type: Optional[int]

    :param meeting_code:
    :type meeting_code: Optional[str]

    :param meeting_id:
    :type meeting_id: Optional[str]

    :param meeting_type:
    :type meeting_type: Optional[int]

    :param need_password:
    :type need_password: Optional[bool]

    :param participants:
    :type participants: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner]]

    :param password:
    :type password: Optional[str]

    :param recurring_rule:
    :type recurring_rule: Optional[V1MeetingsGet200ResponseMeetingInfoListInnerRecurringRule]

    :param remain_sub_meetings: 剩余子会议场数。 
    :type remain_sub_meetings: Optional[int]

    :param settings:
    :type settings: Optional[V1MeetingsGet200ResponseMeetingInfoListInnerSettings]

    :param start_time:
    :type start_time: Optional[str]

    :param status: 当前会议状态： MEETING_STATE_INVALID：非法或未知的会议状态，错误状态。 MEETING_STATE_INIT：待开始，会议预定到预定结束时间前，会议中无人。 MEETING_STATE_CANCELLED：已取消，主持人主动取消会议，待开始的会议才能取消，取消的会议无法再进入。 MEETING_STATE_STARTED：会议中，只要会议中有人即表示进行中。 MEETING_STATE_ENDED：已删除，结束时间后且会议中无人时，被主持人删除，已删除的会议无法再进入。 MEETING_STATE_NULL：无状态，过了预定结束时间，会议中无人。 MEETING_STATE_RECYCLED：已回收，过了预定开始时间30天，会议号被后台回收，无法再进入。      
    :type status: Optional[str]

    :param sub_meetings: 周期性子会议列表。 
    :type sub_meetings: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInnerSubMeetingsInner]]

    :param subject:
    :type subject: Optional[str]

    :param sync_to_wework:
    :type sync_to_wework: Optional[bool]

    :param time_zone:
    :type time_zone: Optional[str]

    :param type: 会议类型： 0：预约会议类型 1：快速会议类型 
    :type type: Optional[int]
    """  # noqa: E501

    current_co_hosts: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner]] = None
    current_hosts: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner]] = None
    current_sub_meeting_id: Optional[str] = None
    enable_doc_upload_permission: Optional[bool] = None
    enable_enroll: Optional[bool] = None
    enable_host_key: Optional[bool] = None
    enable_live: Optional[bool] = None
    end_time: Optional[str] = None
    guests: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInnerGuestsInner]] = None
    has_more_sub_meeting: Optional[int] = None
    has_vote: Optional[bool] = None
    host_key: Optional[str] = None
    hosts: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner]] = None
    join_meeting_role: Optional[str] = None
    join_url: Optional[str] = None
    live_config: Optional[V1MeetingsGet200ResponseMeetingInfoListInnerLiveConfig] = None
    location: Optional[str] = None
    media_set_type: Optional[int] = None
    meeting_code: Optional[str] = None
    meeting_id: Optional[str] = None
    meeting_type: Optional[int] = None
    need_password: Optional[bool] = None
    participants: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner]] = None
    password: Optional[str] = None
    recurring_rule: Optional[V1MeetingsGet200ResponseMeetingInfoListInnerRecurringRule] = None
    remain_sub_meetings: Optional[int] = None
    settings: Optional[V1MeetingsGet200ResponseMeetingInfoListInnerSettings] = None
    start_time: Optional[str] = None
    status: Optional[str] = None
    sub_meetings: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInnerSubMeetingsInner]] = None
    subject: Optional[str] = None
    sync_to_wework: Optional[bool] = None
    time_zone: Optional[str] = None
    type: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        current_co_hosts: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner] | List[Dict[str, Any]]] = None,
        current_hosts: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner] | List[Dict[str, Any]]] = None,
        current_sub_meeting_id: Optional[str] = None,
        enable_doc_upload_permission: Optional[bool] = None,
        enable_enroll: Optional[bool] = None,
        enable_host_key: Optional[bool] = None,
        enable_live: Optional[bool] = None,
        end_time: Optional[str] = None,
        guests: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInnerGuestsInner] | List[Dict[str, Any]]] = None,
        has_more_sub_meeting: Optional[int] = None,
        has_vote: Optional[bool] = None,
        host_key: Optional[str] = None,
        hosts: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner] | List[Dict[str, Any]]] = None,
        join_meeting_role: Optional[str] = None,
        join_url: Optional[str] = None,
        live_config: Optional[V1MeetingsGet200ResponseMeetingInfoListInnerLiveConfig | Dict[str, Any]] = None,
        location: Optional[str] = None,
        media_set_type: Optional[int] = None,
        meeting_code: Optional[str] = None,
        meeting_id: Optional[str] = None,
        meeting_type: Optional[int] = None,
        need_password: Optional[bool] = None,
        participants: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner] | List[Dict[str, Any]]] = None,
        password: Optional[str] = None,
        recurring_rule: Optional[V1MeetingsGet200ResponseMeetingInfoListInnerRecurringRule | Dict[str, Any]] = None,
        remain_sub_meetings: Optional[int] = None,
        settings: Optional[V1MeetingsGet200ResponseMeetingInfoListInnerSettings | Dict[str, Any]] = None,
        start_time: Optional[str] = None,
        status: Optional[str] = None,
        sub_meetings: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInnerSubMeetingsInner] | List[Dict[str, Any]]] = None,
        subject: Optional[str] = None,
        sync_to_wework: Optional[bool] = None,
        time_zone: Optional[str] = None,
        type: Optional[int] = None,
        **kwargs
    ):
        
        if current_co_hosts and isinstance(current_co_hosts, (list, List)):
            self.current_co_hosts = [V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in current_co_hosts]
        
        
        if current_hosts and isinstance(current_hosts, (list, List)):
            self.current_hosts = [V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in current_hosts]
        
        self.current_sub_meeting_id = current_sub_meeting_id
        self.enable_doc_upload_permission = enable_doc_upload_permission
        self.enable_enroll = enable_enroll
        self.enable_host_key = enable_host_key
        self.enable_live = enable_live
        self.end_time = end_time
        
        if guests and isinstance(guests, (list, List)):
            self.guests = [V1MeetingsGet200ResponseMeetingInfoListInnerGuestsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in guests]
        
        self.has_more_sub_meeting = has_more_sub_meeting
        self.has_vote = has_vote
        self.host_key = host_key
        
        if hosts and isinstance(hosts, (list, List)):
            self.hosts = [V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in hosts]
        
        self.join_meeting_role = join_meeting_role
        self.join_url = join_url
        self.live_config = V1MeetingsGet200ResponseMeetingInfoListInnerLiveConfig(**live_config) if isinstance(live_config, (dict, Dict)) else live_config
        self.location = location
        self.media_set_type = media_set_type
        self.meeting_code = meeting_code
        self.meeting_id = meeting_id
        self.meeting_type = meeting_type
        self.need_password = need_password
        
        if participants and isinstance(participants, (list, List)):
            self.participants = [V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in participants]
        
        self.password = password
        self.recurring_rule = V1MeetingsGet200ResponseMeetingInfoListInnerRecurringRule(**recurring_rule) if isinstance(recurring_rule, (dict, Dict)) else recurring_rule
        self.remain_sub_meetings = remain_sub_meetings
        self.settings = V1MeetingsGet200ResponseMeetingInfoListInnerSettings(**settings) if isinstance(settings, (dict, Dict)) else settings
        self.start_time = start_time
        self.status = status
        
        if sub_meetings and isinstance(sub_meetings, (list, List)):
            self.sub_meetings = [V1MeetingsGet200ResponseMeetingInfoListInnerSubMeetingsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in sub_meetings]
        
        self.subject = subject
        self.sync_to_wework = sync_to_wework
        self.time_zone = time_zone
        self.type = type


class V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner(object):
    """V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner

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


class V1MeetingsGet200ResponseMeetingInfoListInnerGuestsInner(object):
    """V1MeetingsGet200ResponseMeetingInfoListInnerGuestsInner

    :param area:
    :type area: Optional[str]

    :param guest_name:
    :type guest_name: Optional[str]

    :param phone_number:
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


class V1MeetingsGet200ResponseMeetingInfoListInnerLiveConfig(object):
    """V1MeetingsGet200ResponseMeetingInfoListInnerLiveConfig

    :param enable_live_im:
    :type enable_live_im: Optional[bool]

    :param enable_live_password:
    :type enable_live_password: Optional[bool]

    :param enable_live_replay:
    :type enable_live_replay: Optional[bool]

    :param live_addr:
    :type live_addr: Optional[str]

    :param live_password:
    :type live_password: Optional[str]

    :param live_subject:
    :type live_subject: Optional[str]

    :param live_summary:
    :type live_summary: Optional[str]

    :param live_watermark:
    :type live_watermark: Optional[V1MeetingsGet200ResponseMeetingInfoListInnerLiveConfigLiveWatermark]
    """  # noqa: E501

    enable_live_im: Optional[bool] = None
    enable_live_password: Optional[bool] = None
    enable_live_replay: Optional[bool] = None
    live_addr: Optional[str] = None
    live_password: Optional[str] = None
    live_subject: Optional[str] = None
    live_summary: Optional[str] = None
    live_watermark: Optional[V1MeetingsGet200ResponseMeetingInfoListInnerLiveConfigLiveWatermark] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        enable_live_im: Optional[bool] = None,
        enable_live_password: Optional[bool] = None,
        enable_live_replay: Optional[bool] = None,
        live_addr: Optional[str] = None,
        live_password: Optional[str] = None,
        live_subject: Optional[str] = None,
        live_summary: Optional[str] = None,
        live_watermark: Optional[V1MeetingsGet200ResponseMeetingInfoListInnerLiveConfigLiveWatermark | Dict[str, Any]] = None,
        **kwargs
    ):
        self.enable_live_im = enable_live_im
        self.enable_live_password = enable_live_password
        self.enable_live_replay = enable_live_replay
        self.live_addr = live_addr
        self.live_password = live_password
        self.live_subject = live_subject
        self.live_summary = live_summary
        self.live_watermark = V1MeetingsGet200ResponseMeetingInfoListInnerLiveConfigLiveWatermark(**live_watermark) if isinstance(live_watermark, (dict, Dict)) else live_watermark


class V1MeetingsGet200ResponseMeetingInfoListInnerLiveConfigLiveWatermark(object):
    """V1MeetingsGet200ResponseMeetingInfoListInnerLiveConfigLiveWatermark

    :param watermark_opt:
    :type watermark_opt: Optional[int]
    """  # noqa: E501

    watermark_opt: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        watermark_opt: Optional[int] = None,
        **kwargs
    ):
        self.watermark_opt = watermark_opt


class V1MeetingsGet200ResponseMeetingInfoListInnerRecurringRule(object):
    """周期性会议设置。

    :param customized_recurring_days:
    :type customized_recurring_days: Optional[int]

    :param customized_recurring_step:
    :type customized_recurring_step: Optional[int]

    :param customized_recurring_type:
    :type customized_recurring_type: Optional[int]

    :param recurring_type: 周期性会议频率，默认值为0。 0：每天 1：每周一至周五 2：每周 3：每两周 4：每月 
    :type recurring_type: Optional[int]

    :param until_count: integer  限定会议次数（1-50次）默认值为7次。 
    :type until_count: Optional[int]

    :param until_date: 结束日期时间戳，默认值为当前日期 + 7天。 
    :type until_date: Optional[int]

    :param until_type: 结束重复类型，默认值为0。 0：按日期结束重复 1：按次数结束重复 
    :type until_type: Optional[int]
    """  # noqa: E501

    customized_recurring_days: Optional[int] = None
    customized_recurring_step: Optional[int] = None
    customized_recurring_type: Optional[int] = None
    recurring_type: Optional[int] = None
    until_count: Optional[int] = None
    until_date: Optional[int] = None
    until_type: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        customized_recurring_days: Optional[int] = None,
        customized_recurring_step: Optional[int] = None,
        customized_recurring_type: Optional[int] = None,
        recurring_type: Optional[int] = None,
        until_count: Optional[int] = None,
        until_date: Optional[int] = None,
        until_type: Optional[int] = None,
        **kwargs
    ):
        self.customized_recurring_days = customized_recurring_days
        self.customized_recurring_step = customized_recurring_step
        self.customized_recurring_type = customized_recurring_type
        self.recurring_type = recurring_type
        self.until_count = until_count
        self.until_date = until_date
        self.until_type = until_type


class V1MeetingsGet200ResponseMeetingInfoListInnerSettings(object):
    """V1MeetingsGet200ResponseMeetingInfoListInnerSettings

    :param allow_in_before_host:
    :type allow_in_before_host: Optional[bool]

    :param allow_screen_shared_watermark:
    :type allow_screen_shared_watermark: Optional[bool]

    :param allow_unmute_self:
    :type allow_unmute_self: Optional[bool]

    :param auto_in_waiting_room:
    :type auto_in_waiting_room: Optional[bool]

    :param auto_record_type:
    :type auto_record_type: Optional[str]

    :param enable_host_pause_auto_record:
    :type enable_host_pause_auto_record: Optional[bool]

    :param mute_enable_join:
    :type mute_enable_join: Optional[bool]

    :param mute_enable_type_join:
    :type mute_enable_type_join: Optional[int]

    :param only_allow_enterprise_user_join:
    :type only_allow_enterprise_user_join: Optional[bool]

    :param participant_join_auto_record:
    :type participant_join_auto_record: Optional[bool]

    :param water_mark_type:
    :type water_mark_type: Optional[int]
    """  # noqa: E501

    allow_in_before_host: Optional[bool] = None
    allow_screen_shared_watermark: Optional[bool] = None
    allow_unmute_self: Optional[bool] = None
    auto_in_waiting_room: Optional[bool] = None
    auto_record_type: Optional[str] = None
    enable_host_pause_auto_record: Optional[bool] = None
    mute_enable_join: Optional[bool] = None
    mute_enable_type_join: Optional[int] = None
    only_allow_enterprise_user_join: Optional[bool] = None
    participant_join_auto_record: Optional[bool] = None
    water_mark_type: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        allow_in_before_host: Optional[bool] = None,
        allow_screen_shared_watermark: Optional[bool] = None,
        allow_unmute_self: Optional[bool] = None,
        auto_in_waiting_room: Optional[bool] = None,
        auto_record_type: Optional[str] = None,
        enable_host_pause_auto_record: Optional[bool] = None,
        mute_enable_join: Optional[bool] = None,
        mute_enable_type_join: Optional[int] = None,
        only_allow_enterprise_user_join: Optional[bool] = None,
        participant_join_auto_record: Optional[bool] = None,
        water_mark_type: Optional[int] = None,
        **kwargs
    ):
        self.allow_in_before_host = allow_in_before_host
        self.allow_screen_shared_watermark = allow_screen_shared_watermark
        self.allow_unmute_self = allow_unmute_self
        self.auto_in_waiting_room = auto_in_waiting_room
        self.auto_record_type = auto_record_type
        self.enable_host_pause_auto_record = enable_host_pause_auto_record
        self.mute_enable_join = mute_enable_join
        self.mute_enable_type_join = mute_enable_type_join
        self.only_allow_enterprise_user_join = only_allow_enterprise_user_join
        self.participant_join_auto_record = participant_join_auto_record
        self.water_mark_type = water_mark_type


class V1MeetingsGet200ResponseMeetingInfoListInnerSubMeetingsInner(object):
    """V1MeetingsGet200ResponseMeetingInfoListInnerSubMeetingsInner

    :param end_time:
    :type end_time: Optional[str]

    :param start_time:
    :type start_time: Optional[str]

    :param status: 子会议状态： 0：默认（存在）  1：已删除 
    :type status: Optional[int]

    :param sub_meeting_id:
    :type sub_meeting_id: Optional[str]
    """  # noqa: E501

    end_time: Optional[str] = None
    start_time: Optional[str] = None
    status: Optional[int] = None
    sub_meeting_id: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        end_time: Optional[str] = None,
        start_time: Optional[str] = None,
        status: Optional[int] = None,
        sub_meeting_id: Optional[str] = None,
        **kwargs
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.status = status
        self.sub_meeting_id = sub_meeting_id


class V1MeetingsMeetingIdCancelPostRequest(object):
    """V1MeetingsMeetingIdCancelPostRequest

    :param instanceid: 用户的终端设备类型： 0：PSTN 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch MacOS 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch iOS (required) 
    :type instanceid: int

    :param meeting_type: 会议类型，默认值为0。 0：普通会议 1：周期性会议 
    :type meeting_type: Optional[int]

    :param reason_code: 原因代码，可为用户自定义 (required) 
    :type reason_code: int

    :param reason_detail: 取消原因描述 
    :type reason_detail: Optional[str]

    :param sub_meeting_id: 周期性子会议 ID，如果不传，则会取消该系列的周期性会议 
    :type sub_meeting_id: Optional[str]

    :param userid: 调用 API 的用户 ID（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId）。 企业唯一用户标识说明： 1：企业对接 SSO 时使用的员工唯一标识 ID。 2：企业调用创建用户接口时传递的 userid 参数。  (required) 
    :type userid: str
    """  # noqa: E501

    instanceid: int
    meeting_type: Optional[int] = None
    reason_code: int
    reason_detail: Optional[str] = None
    sub_meeting_id: Optional[str] = None
    userid: str
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        instanceid: int,
        reason_code: int,
        userid: str,
        meeting_type: Optional[int] = None,
        reason_detail: Optional[str] = None,
        sub_meeting_id: Optional[str] = None,
        **kwargs
    ):
        self.instanceid = instanceid
        self.meeting_type = meeting_type
        self.reason_code = reason_code
        self.reason_detail = reason_detail
        self.sub_meeting_id = sub_meeting_id
        self.userid = userid


class V1MeetingsMeetingIdCustomerShortUrlGet200Response(object):
    """V1MeetingsMeetingIdCustomerShortUrlGet200Response

    :param meeting_short_url_customer_data: 用户专属参会链接对象。 
    :type meeting_short_url_customer_data: Optional[List[V1MeetingsMeetingIdCustomerShortUrlGet200ResponseMeetingShortUrlCustomerDataInner]]
    """  # noqa: E501

    meeting_short_url_customer_data: Optional[List[V1MeetingsMeetingIdCustomerShortUrlGet200ResponseMeetingShortUrlCustomerDataInner]] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        meeting_short_url_customer_data: Optional[List[V1MeetingsMeetingIdCustomerShortUrlGet200ResponseMeetingShortUrlCustomerDataInner] | List[Dict[str, Any]]] = None,
        **kwargs
    ):
        
        if meeting_short_url_customer_data and isinstance(meeting_short_url_customer_data, (list, List)):
            self.meeting_short_url_customer_data = [V1MeetingsMeetingIdCustomerShortUrlGet200ResponseMeetingShortUrlCustomerDataInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in meeting_short_url_customer_data]
        


class V1MeetingsMeetingIdCustomerShortUrlGet200ResponseMeetingShortUrlCustomerDataInner(object):
    """V1MeetingsMeetingIdCustomerShortUrlGet200ResponseMeetingShortUrlCustomerDataInner

    :param customer_data: 用户专属信息字段，用户自定义参数customerData 
    :type customer_data: Optional[str]

    :param meeting_short_url: 根据customerData生成的专属参会链接 
    :type meeting_short_url: Optional[str]
    """  # noqa: E501

    customer_data: Optional[str] = None
    meeting_short_url: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        customer_data: Optional[str] = None,
        meeting_short_url: Optional[str] = None,
        **kwargs
    ):
        self.customer_data = customer_data
        self.meeting_short_url = meeting_short_url


class V1MeetingsMeetingIdEnrollApprovalsGet200Response(object):
    """V1MeetingsMeetingIdEnrollApprovalsGet200Response

    :param current_page: 当前页 
    :type current_page: Optional[int]

    :param current_size: 当前页实际大小 
    :type current_size: Optional[int]

    :param enroll_list: 当前页的报名列表，current_size为0时无该字段 
    :type enroll_list: Optional[List[V1MeetingsMeetingIdEnrollApprovalsGet200ResponseEnrollListInner]]

    :param total_count: 根据条件筛选后的总报名人数 
    :type total_count: Optional[int]

    :param total_page: 根据条件筛选后的总分页数 
    :type total_page: Optional[int]
    """  # noqa: E501

    current_page: Optional[int] = None
    current_size: Optional[int] = None
    enroll_list: Optional[List[V1MeetingsMeetingIdEnrollApprovalsGet200ResponseEnrollListInner]] = None
    total_count: Optional[int] = None
    total_page: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        current_page: Optional[int] = None,
        current_size: Optional[int] = None,
        enroll_list: Optional[List[V1MeetingsMeetingIdEnrollApprovalsGet200ResponseEnrollListInner] | List[Dict[str, Any]]] = None,
        total_count: Optional[int] = None,
        total_page: Optional[int] = None,
        **kwargs
    ):
        self.current_page = current_page
        self.current_size = current_size
        
        if enroll_list and isinstance(enroll_list, (list, List)):
            self.enroll_list = [V1MeetingsMeetingIdEnrollApprovalsGet200ResponseEnrollListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in enroll_list]
        
        self.total_count = total_count
        self.total_page = total_page


class V1MeetingsMeetingIdEnrollApprovalsGet200ResponseEnrollListInner(object):
    """V1MeetingsMeetingIdEnrollApprovalsGet200ResponseEnrollListInner

    :param answer_list: 答题列表 
    :type answer_list: Optional[List[V1MeetingsMeetingIdEnrollApprovalsGet200ResponseEnrollListInnerAnswerListInner]]

    :param enroll_code: pstn入会凭证 
    :type enroll_code: Optional[str]

    :param enroll_id: 报名id 
    :type enroll_id: Optional[int]

    :param enroll_source_type: 报名来源： 1：用户手动报名 2：批量导入报名 
    :type enroll_source_type: Optional[int]

    :param enroll_time: 报名时间（utc+8，非时间戳） 
    :type enroll_time: Optional[str]

    :param ms_open_id: 当场会议的用户临时id，所有用户都有 
    :type ms_open_id: Optional[str]

    :param nick_name: 昵称 
    :type nick_name: Optional[str]

    :param open_id: 报名者已授权过会议创建的应用时返回openid，否则为空 
    :type open_id: Optional[str]

    :param status: 报名状态：1 待审批，2 已拒绝，3 已批准 
    :type status: Optional[int]

    :param userid: 报名者与会议创建者为同企业时，返回userid，否则为空,导入报名入参为手机号的情况不返回userid。 
    :type userid: Optional[str]
    """  # noqa: E501

    answer_list: Optional[List[V1MeetingsMeetingIdEnrollApprovalsGet200ResponseEnrollListInnerAnswerListInner]] = None
    enroll_code: Optional[str] = None
    enroll_id: Optional[int] = None
    enroll_source_type: Optional[int] = None
    enroll_time: Optional[str] = None
    ms_open_id: Optional[str] = None
    nick_name: Optional[str] = None
    open_id: Optional[str] = None
    status: Optional[int] = None
    userid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        answer_list: Optional[List[V1MeetingsMeetingIdEnrollApprovalsGet200ResponseEnrollListInnerAnswerListInner] | List[Dict[str, Any]]] = None,
        enroll_code: Optional[str] = None,
        enroll_id: Optional[int] = None,
        enroll_source_type: Optional[int] = None,
        enroll_time: Optional[str] = None,
        ms_open_id: Optional[str] = None,
        nick_name: Optional[str] = None,
        open_id: Optional[str] = None,
        status: Optional[int] = None,
        userid: Optional[str] = None,
        **kwargs
    ):
        
        if answer_list and isinstance(answer_list, (list, List)):
            self.answer_list = [V1MeetingsMeetingIdEnrollApprovalsGet200ResponseEnrollListInnerAnswerListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in answer_list]
        
        self.enroll_code = enroll_code
        self.enroll_id = enroll_id
        self.enroll_source_type = enroll_source_type
        self.enroll_time = enroll_time
        self.ms_open_id = ms_open_id
        self.nick_name = nick_name
        self.open_id = open_id
        self.status = status
        self.userid = userid


class V1MeetingsMeetingIdEnrollApprovalsGet200ResponseEnrollListInnerAnswerListInner(object):
    """V1MeetingsMeetingIdEnrollApprovalsGet200ResponseEnrollListInnerAnswerListInner

    :param answer_content: 回答内容：单选/简答只有一个元素，多选会有多个 
    :type answer_content: Optional[List[str]]

    :param is_required: 是否必填：1 否，2 是 
    :type is_required: Optional[int]

    :param question_num: 问题编号，1,2,3...等形式 
    :type question_num: Optional[int]

    :param question_title: 问题标题 
    :type question_title: Optional[str]

    :param question_type: 问题类型：1 单选，2 多选，3 简答 
    :type question_type: Optional[int]

    :param special_type: 特殊问题类型：1 无，2 手机号，3 邮箱，4 姓名，5 公司名称（目前4种特殊问题均为简答题） 
    :type special_type: Optional[int]
    """  # noqa: E501

    answer_content: Optional[List[str]] = None
    is_required: Optional[int] = None
    question_num: Optional[int] = None
    question_title: Optional[str] = None
    question_type: Optional[int] = None
    special_type: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        answer_content: Optional[List[str]] = None,
        is_required: Optional[int] = None,
        question_num: Optional[int] = None,
        question_title: Optional[str] = None,
        question_type: Optional[int] = None,
        special_type: Optional[int] = None,
        **kwargs
    ):
        
        if answer_content and isinstance(answer_content, (list, List)):
            self.answer_content = answer_content
        
        self.is_required = is_required
        self.question_num = question_num
        self.question_title = question_title
        self.question_type = question_type
        self.special_type = special_type


class V1MeetingsMeetingIdEnrollApprovalsPut200Response(object):
    """V1MeetingsMeetingIdEnrollApprovalsPut200Response

    :param handled_count: 成功处理的数量 
    :type handled_count: Optional[int]

    :param meeting_id: 在线大会唯一标识 
    :type meeting_id: Optional[str]
    """  # noqa: E501

    handled_count: Optional[int] = None
    meeting_id: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        handled_count: Optional[int] = None,
        meeting_id: Optional[str] = None,
        **kwargs
    ):
        self.handled_count = handled_count
        self.meeting_id = meeting_id


class V1MeetingsMeetingIdEnrollApprovalsPutRequest(object):
    """V1MeetingsMeetingIdEnrollApprovalsPutRequest

    :param action: 审批动作：1 取消批准，2 拒绝，3.批准，取消批准后状态将变成待审批 (required) 
    :type action: int

    :param enroll_id_list: 报名id列表效 (required) 
    :type enroll_id_list: List[int]

    :param instanceid: 设备类型 
    :type instanceid: Optional[int]

    :param operator_id: 操作者 ID。会议创建者可以导入报名信息。 operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。  operator_id_type=2，operator_id必须和公共参数的openid一致。  operator_id和userid至少填写一个，两个参数如果都传了以operator_id为准。  使用OAuth公参鉴权后不能使用userid为入参。 
    :type operator_id: Optional[str]

    :param operator_id_type: 操作者 ID 的类型：  1: userid 2: open_id  如果operator_id和userid具有值，则以operator_id为准； (required) 
    :type operator_id_type: int

    :param userid: 用户id 
    :type userid: Optional[str]
    """  # noqa: E501

    action: int
    enroll_id_list: List[int]
    instanceid: Optional[int] = None
    operator_id: Optional[str] = None
    operator_id_type: int
    userid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        action: int,
        enroll_id_list: List[int],
        operator_id_type: int,
        instanceid: Optional[int] = None,
        operator_id: Optional[str] = None,
        userid: Optional[str] = None,
        **kwargs
    ):
        self.action = action
        
        if enroll_id_list and isinstance(enroll_id_list, (list, List)):
            self.enroll_id_list = enroll_id_list
        
        self.instanceid = instanceid
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.userid = userid


class V1MeetingsMeetingIdEnrollConfigGet200Response(object):
    """V1MeetingsMeetingIdEnrollConfigGet200Response

    :param approve_type: 审批类型：1 自动审批，2 手动审批，默认自动审批 
    :type approve_type: Optional[int]

    :param cover_image: 报名页封面图URL（base64编码） 
    :type cover_image: Optional[List[str]]

    :param display_number_of_participants: 显示已报名/预约人数。0：不展示 1：展示，默认开启 
    :type display_number_of_participants: Optional[int]

    :param enroll_deadline: 报名截止时间（秒级时间戳） 
    :type enroll_deadline: Optional[str]

    :param enroll_description: 报名页简介 
    :type enroll_description: Optional[str]

    :param enroll_number: 报名人数上限 
    :type enroll_number: Optional[int]

    :param enroll_push_type: 报名审批自动通知方式，1-短信通知；2-邮件中文；3-邮件英文；4-邮件中英文；5-公众号 
    :type enroll_push_type: Optional[List[int]]

    :param is_collect_question: 是否收集问题：1 不收集，2 收集，默认不收集问题 
    :type is_collect_question: Optional[int]

    :param meeting_id: 会议id 
    :type meeting_id: Optional[str]

    :param no_registration_needed_for_staff: 本企业用户无需报名。 true: 本企业用户无需报名。 false：默认配置，所有用户需要报名。  
    :type no_registration_needed_for_staff: Optional[bool]

    :param question_list: 报名问题列表，自定义问题按传入的顺序排序，预设问题会优先放在最前面，仅开启收集问题时有效 
    :type question_list: Optional[List[V1MeetingsMeetingIdEnrollConfigGet200ResponseQuestionListInner]]
    """  # noqa: E501

    approve_type: Optional[int] = None
    cover_image: Optional[List[str]] = None
    display_number_of_participants: Optional[int] = None
    enroll_deadline: Optional[str] = None
    enroll_description: Optional[str] = None
    enroll_number: Optional[int] = None
    enroll_push_type: Optional[List[int]] = None
    is_collect_question: Optional[int] = None
    meeting_id: Optional[str] = None
    no_registration_needed_for_staff: Optional[bool] = None
    question_list: Optional[List[V1MeetingsMeetingIdEnrollConfigGet200ResponseQuestionListInner]] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        approve_type: Optional[int] = None,
        cover_image: Optional[List[str]] = None,
        display_number_of_participants: Optional[int] = None,
        enroll_deadline: Optional[str] = None,
        enroll_description: Optional[str] = None,
        enroll_number: Optional[int] = None,
        enroll_push_type: Optional[List[int]] = None,
        is_collect_question: Optional[int] = None,
        meeting_id: Optional[str] = None,
        no_registration_needed_for_staff: Optional[bool] = None,
        question_list: Optional[List[V1MeetingsMeetingIdEnrollConfigGet200ResponseQuestionListInner] | List[Dict[str, Any]]] = None,
        **kwargs
    ):
        self.approve_type = approve_type
        
        if cover_image and isinstance(cover_image, (list, List)):
            self.cover_image = cover_image
        
        self.display_number_of_participants = display_number_of_participants
        self.enroll_deadline = enroll_deadline
        self.enroll_description = enroll_description
        self.enroll_number = enroll_number
        
        if enroll_push_type and isinstance(enroll_push_type, (list, List)):
            self.enroll_push_type = enroll_push_type
        
        self.is_collect_question = is_collect_question
        self.meeting_id = meeting_id
        self.no_registration_needed_for_staff = no_registration_needed_for_staff
        
        if question_list and isinstance(question_list, (list, List)):
            self.question_list = [V1MeetingsMeetingIdEnrollConfigGet200ResponseQuestionListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in question_list]
        


class V1MeetingsMeetingIdEnrollConfigGet200ResponseQuestionListInner(object):
    """V1MeetingsMeetingIdEnrollConfigGet200ResponseQuestionListInner

    :param is_required: 是否必填：1 否，2 是 
    :type is_required: Optional[int]

    :param option_list: 问题选项列表，按传入的顺序排序，仅单选/多选时有效，最多8个选项，每个选项限40个汉字 
    :type option_list: Optional[List[V1MeetingsMeetingIdEnrollConfigGet200ResponseQuestionListInnerOptionListInner]]

    :param question_title: 问题标题，限制40个汉字 
    :type question_title: Optional[str]

    :param question_type: 问题类型：1 单选，2 多选，3 简答 
    :type question_type: Optional[int]

    :param special_type: 特殊问题类型：1 无，2 手机号，3 邮箱，4 姓名，5 组织名称，6 组织规模（目前除组织规模外均为简答题，组织规模为单选题） 
    :type special_type: Optional[int]
    """  # noqa: E501

    is_required: Optional[int] = None
    option_list: Optional[List[V1MeetingsMeetingIdEnrollConfigGet200ResponseQuestionListInnerOptionListInner]] = None
    question_title: Optional[str] = None
    question_type: Optional[int] = None
    special_type: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        is_required: Optional[int] = None,
        option_list: Optional[List[V1MeetingsMeetingIdEnrollConfigGet200ResponseQuestionListInnerOptionListInner] | List[Dict[str, Any]]] = None,
        question_title: Optional[str] = None,
        question_type: Optional[int] = None,
        special_type: Optional[int] = None,
        **kwargs
    ):
        self.is_required = is_required
        
        if option_list and isinstance(option_list, (list, List)):
            self.option_list = [V1MeetingsMeetingIdEnrollConfigGet200ResponseQuestionListInnerOptionListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in option_list]
        
        self.question_title = question_title
        self.question_type = question_type
        self.special_type = special_type


class V1MeetingsMeetingIdEnrollConfigGet200ResponseQuestionListInnerOptionListInner(object):
    """V1MeetingsMeetingIdEnrollConfigGet200ResponseQuestionListInnerOptionListInner

    :param content:
    :type content: Optional[str]
    """  # noqa: E501

    content: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        content: Optional[str] = None,
        **kwargs
    ):
        self.content = content


class V1MeetingsMeetingIdEnrollConfigPut200Response(object):
    """V1MeetingsMeetingIdEnrollConfigPut200Response

    :param meeting_id: 会议的唯一标识 
    :type meeting_id: Optional[str]

    :param question_count: 报名问题数量，不收集问题时该字段返回0 
    :type question_count: Optional[int]
    """  # noqa: E501

    meeting_id: Optional[str] = None
    question_count: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        meeting_id: Optional[str] = None,
        question_count: Optional[int] = None,
        **kwargs
    ):
        self.meeting_id = meeting_id
        self.question_count = question_count


class V1MeetingsMeetingIdEnrollConfigPutRequest(object):
    """V1MeetingsMeetingIdEnrollConfigPutRequest

    :param approve_type: 审批类型：1 自动审批，2 手动审批，默认自动审批 
    :type approve_type: Optional[int]

    :param cover_image: 报名封面图的URL，上传封面为异步形式，通过异步任务结果webhook获取上传结果，列表内容为空字符串时为默认图片，不传或传空列表则不做修改，最多支持5张，支持格式为jpg，jpeg，png。每张不超过5M，按照传入顺序展示。 
    :type cover_image: Optional[List[str]]

    :param display_number_of_participants: 显示已报名/预约人数。0：不展示 1：展示，默认开启 
    :type display_number_of_participants: Optional[int]

    :param enroll_deadline: 报名截止时间（秒级时间戳） 
    :type enroll_deadline: Optional[str]

    :param enroll_description: 报名页详情介绍，最多5000字符 
    :type enroll_description: Optional[str]

    :param enroll_number: 报名人数上限 
    :type enroll_number: Optional[int]

    :param enroll_push_type: 报名审批自动通知方式，1-短信通知；2-邮件中文；3-邮件英文；4-邮件中英文；5-公众号 
    :type enroll_push_type: Optional[List[int]]

    :param instanceid: 设备类型 (required) 
    :type instanceid: int

    :param is_collect_question: 是否收集问题：1 不收集，2 收集，默认不收集问题 
    :type is_collect_question: Optional[int]

    :param no_registration_needed_for_staff: 本企业用户无需报名。 true: 本企业用户无需报名。 false：默认配置，所有用户需要报名。  
    :type no_registration_needed_for_staff: Optional[bool]

    :param operator_id: 操作者 ID。会议创建者可以导入报名信息。 operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。  operator_id_type=2，operator_id必须和公共参数的openid一致。  operator_id和userid至少填写一个，两个参数如果都传了以operator_id为准。  使用OAuth公参鉴权后不能使用userid为入参。 
    :type operator_id: Optional[str]

    :param operator_id_type: 操作者 ID 的类型：  1: userid 2: open_id  如果operator_id和userid具有值，则以operator_id为准； 
    :type operator_id_type: Optional[int]

    :param question_list: 报名问题列表，非特殊问题按传入的顺序排序，特殊问题会优先放在最前面，仅开启收集问题时有效 
    :type question_list: Optional[List[V1MeetingsMeetingIdEnrollConfigPutRequestQuestionListInner]]

    :param userid: 用户id 
    :type userid: Optional[str]
    """  # noqa: E501

    approve_type: Optional[int] = None
    cover_image: Optional[List[str]] = None
    display_number_of_participants: Optional[int] = None
    enroll_deadline: Optional[str] = None
    enroll_description: Optional[str] = None
    enroll_number: Optional[int] = None
    enroll_push_type: Optional[List[int]] = None
    instanceid: int
    is_collect_question: Optional[int] = None
    no_registration_needed_for_staff: Optional[bool] = None
    operator_id: Optional[str] = None
    operator_id_type: Optional[int] = None
    question_list: Optional[List[V1MeetingsMeetingIdEnrollConfigPutRequestQuestionListInner]] = None
    userid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        instanceid: int,
        approve_type: Optional[int] = None,
        cover_image: Optional[List[str]] = None,
        display_number_of_participants: Optional[int] = None,
        enroll_deadline: Optional[str] = None,
        enroll_description: Optional[str] = None,
        enroll_number: Optional[int] = None,
        enroll_push_type: Optional[List[int]] = None,
        is_collect_question: Optional[int] = None,
        no_registration_needed_for_staff: Optional[bool] = None,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[int] = None,
        question_list: Optional[List[V1MeetingsMeetingIdEnrollConfigPutRequestQuestionListInner] | List[Dict[str, Any]]] = None,
        userid: Optional[str] = None,
        **kwargs
    ):
        self.approve_type = approve_type
        
        if cover_image and isinstance(cover_image, (list, List)):
            self.cover_image = cover_image
        
        self.display_number_of_participants = display_number_of_participants
        self.enroll_deadline = enroll_deadline
        self.enroll_description = enroll_description
        self.enroll_number = enroll_number
        
        if enroll_push_type and isinstance(enroll_push_type, (list, List)):
            self.enroll_push_type = enroll_push_type
        
        self.instanceid = instanceid
        self.is_collect_question = is_collect_question
        self.no_registration_needed_for_staff = no_registration_needed_for_staff
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        
        if question_list and isinstance(question_list, (list, List)):
            self.question_list = [V1MeetingsMeetingIdEnrollConfigPutRequestQuestionListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in question_list]
        
        self.userid = userid


class V1MeetingsMeetingIdEnrollConfigPutRequestQuestionListInner(object):
    """V1MeetingsMeetingIdEnrollConfigPutRequestQuestionListInner

    :param is_required: 是否必填：1 否，2 是 (required) 
    :type is_required: int

    :param option_list: 问题选项列表，按传入的顺序排序，仅单选/多选时有效，最多8个选项，每个选项限40个汉字 
    :type option_list: Optional[List[V1MeetingsMeetingIdEnrollConfigPutRequestQuestionListInnerOptionListInner]]

    :param question_title: 问题标题，限制40个字符（special_type为特殊问题时，该字段无效） 
    :type question_title: Optional[str]

    :param question_type: 问题类型：1 单选，2 多选，3 简答（special_type为特殊问题时，该字段无效） 
    :type question_type: Optional[int]

    :param special_type: 特殊问题类型：1 无，2 手机号，3 邮箱，4 姓名，5 组织名称，6 组织规模（目前除组织规模外均为简答题，组织规模为单选题） 
    :type special_type: Optional[int]
    """  # noqa: E501

    is_required: int
    option_list: Optional[List[V1MeetingsMeetingIdEnrollConfigPutRequestQuestionListInnerOptionListInner]] = None
    question_title: Optional[str] = None
    question_type: Optional[int] = None
    special_type: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        is_required: int,
        option_list: Optional[List[V1MeetingsMeetingIdEnrollConfigPutRequestQuestionListInnerOptionListInner] | List[Dict[str, Any]]] = None,
        question_title: Optional[str] = None,
        question_type: Optional[int] = None,
        special_type: Optional[int] = None,
        **kwargs
    ):
        self.is_required = is_required
        
        if option_list and isinstance(option_list, (list, List)):
            self.option_list = [V1MeetingsMeetingIdEnrollConfigPutRequestQuestionListInnerOptionListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in option_list]
        
        self.question_title = question_title
        self.question_type = question_type
        self.special_type = special_type


class V1MeetingsMeetingIdEnrollConfigPutRequestQuestionListInnerOptionListInner(object):
    """V1MeetingsMeetingIdEnrollConfigPutRequestQuestionListInnerOptionListInner

    :param content:
    :type content: Optional[str]
    """  # noqa: E501

    content: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        content: Optional[str] = None,
        **kwargs
    ):
        self.content = content


class V1MeetingsMeetingIdEnrollIdsPost200Response(object):
    """V1MeetingsMeetingIdEnrollIdsPost200Response

    :param enroll_id_list: 成员报名 ID 数组，仅返回已报名成员的报名 ID，若传入的用户无人报名，则无该字段。 
    :type enroll_id_list: Optional[List[V1MeetingsMeetingIdEnrollIdsPost200ResponseEnrollIdListInner]]

    :param meeting_id: 会议ID 
    :type meeting_id: Optional[str]
    """  # noqa: E501

    enroll_id_list: Optional[List[V1MeetingsMeetingIdEnrollIdsPost200ResponseEnrollIdListInner]] = None
    meeting_id: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        enroll_id_list: Optional[List[V1MeetingsMeetingIdEnrollIdsPost200ResponseEnrollIdListInner] | List[Dict[str, Any]]] = None,
        meeting_id: Optional[str] = None,
        **kwargs
    ):
        
        if enroll_id_list and isinstance(enroll_id_list, (list, List)):
            self.enroll_id_list = [V1MeetingsMeetingIdEnrollIdsPost200ResponseEnrollIdListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in enroll_id_list]
        
        self.meeting_id = meeting_id


class V1MeetingsMeetingIdEnrollIdsPost200ResponseEnrollIdListInner(object):
    """V1MeetingsMeetingIdEnrollIdsPost200ResponseEnrollIdListInner

    :param enroll_id: 报名ID 
    :type enroll_id: Optional[int]

    :param ms_open_id: 当场会议的用户临时 ID，适用于所有用户。 
    :type ms_open_id: Optional[str]
    """  # noqa: E501

    enroll_id: Optional[int] = None
    ms_open_id: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        enroll_id: Optional[int] = None,
        ms_open_id: Optional[str] = None,
        **kwargs
    ):
        self.enroll_id = enroll_id
        self.ms_open_id = ms_open_id


class V1MeetingsMeetingIdEnrollIdsPostRequest(object):
    """V1MeetingsMeetingIdEnrollIdsPostRequest

    :param instanceid: 用户的终端设备类型： 0：PSTN 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch MacOS 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch iOS (required) 
    :type instanceid: int

    :param ms_open_id_list: 当场会议的用户临时 ID（适用于所有用户）数组，单次最多支持500条。 (required) 
    :type ms_open_id_list: List[str]

    :param operator_id: 操作者 ID。会议创建者可以导入报名信息。 operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 operator_id_type=2，operator_id 必须和公共参数的 openid 一致。 operator_id 和 userid 至少填写一个，两个参数如果都传了以 operator_id 为准。 使用 OAuth 公参鉴权后不能使用 userid 为入参。 
    :type operator_id: Optional[str]

    :param operator_id_type: 操作者 ID 的类型： 1：userid 2：open_id 如果 operator_id 和 userid 具有值，则以 operator_id 为准。 
    :type operator_id_type: Optional[int]

    :param sorting_rules: 查询报名 ID 的排序规则。当该账号存在多条报名记录（手机号导入、手动报名等）时，该接口返回的顺序。 1：优先查询手机号导入报名，再查询用户手动报名，默认值。 2：优先查询用户手动报名，再查手机号导入。 
    :type sorting_rules: Optional[int]

    :param userid: 会议创建者的用户 ID。为了防止现网应用报错，此参数实则仍然兼容 openid，如无 oauth 应用使用报名接口则也可做成不兼容变更。 
    :type userid: Optional[str]
    """  # noqa: E501

    instanceid: int
    ms_open_id_list: List[str]
    operator_id: Optional[str] = None
    operator_id_type: Optional[int] = None
    sorting_rules: Optional[int] = None
    userid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        instanceid: int,
        ms_open_id_list: List[str],
        operator_id: Optional[str] = None,
        operator_id_type: Optional[int] = None,
        sorting_rules: Optional[int] = None,
        userid: Optional[str] = None,
        **kwargs
    ):
        self.instanceid = instanceid
        
        if ms_open_id_list and isinstance(ms_open_id_list, (list, List)):
            self.ms_open_id_list = ms_open_id_list
        
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.sorting_rules = sorting_rules
        self.userid = userid


class V1MeetingsMeetingIdEnrollImportPost200Response(object):
    """V1MeetingsMeetingIdEnrollImportPost200Response

    :param enroll_list: 报名对象列表  
    :type enroll_list: Optional[List[V1MeetingsMeetingIdEnrollImportPost200ResponseEnrollListInner]]

    :param total_count: 成功导入的报名信息条数 
    :type total_count: Optional[int]

    :param user_non_registered: 未注册用户列表 
    :type user_non_registered: Optional[List[str]]
    """  # noqa: E501

    enroll_list: Optional[List[V1MeetingsMeetingIdEnrollImportPost200ResponseEnrollListInner]] = None
    total_count: Optional[int] = None
    user_non_registered: Optional[List[str]] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        enroll_list: Optional[List[V1MeetingsMeetingIdEnrollImportPost200ResponseEnrollListInner] | List[Dict[str, Any]]] = None,
        total_count: Optional[int] = None,
        user_non_registered: Optional[List[str]] = None,
        **kwargs
    ):
        
        if enroll_list and isinstance(enroll_list, (list, List)):
            self.enroll_list = [V1MeetingsMeetingIdEnrollImportPost200ResponseEnrollListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in enroll_list]
        
        self.total_count = total_count
        
        if user_non_registered and isinstance(user_non_registered, (list, List)):
            self.user_non_registered = user_non_registered
        


class V1MeetingsMeetingIdEnrollImportPost200ResponseEnrollListInner(object):
    """V1MeetingsMeetingIdEnrollImportPost200ResponseEnrollListInner

    :param area: 国家/地区代码，若使用手机号，必填（例如：中国传86，不是+86） 
    :type area: Optional[str]

    :param enroll_code:
    :type enroll_code: Optional[str]

    :param enroll_id: 报名ID 
    :type enroll_id: Optional[int]

    :param nick_name: 报名的昵称，与会中昵称可能不一致 
    :type nick_name: Optional[str]

    :param open_id: OAuth授权用户ID。  导入报名对象支持本企业（或与OAuth应用同企业）内 userid、授权用户的openid、phone_number 三种形式，三者必填其一； 
    :type open_id: Optional[str]

    :param phone_number: 手机号 
    :type phone_number: Optional[str]

    :param userid: 用户的唯一 ID（企业内部请使用企业唯一用户标识）。 userid 和 phone_number 两者必填一个 
    :type userid: Optional[str]
    """  # noqa: E501

    area: Optional[str] = None
    enroll_code: Optional[str] = None
    enroll_id: Optional[int] = None
    nick_name: Optional[str] = None
    open_id: Optional[str] = None
    phone_number: Optional[str] = None
    userid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        area: Optional[str] = None,
        enroll_code: Optional[str] = None,
        enroll_id: Optional[int] = None,
        nick_name: Optional[str] = None,
        open_id: Optional[str] = None,
        phone_number: Optional[str] = None,
        userid: Optional[str] = None,
        **kwargs
    ):
        self.area = area
        self.enroll_code = enroll_code
        self.enroll_id = enroll_id
        self.nick_name = nick_name
        self.open_id = open_id
        self.phone_number = phone_number
        self.userid = userid


class V1MeetingsMeetingIdEnrollImportPostRequest(object):
    """V1MeetingsMeetingIdEnrollImportPostRequest

    :param enroll_list: 导入的报名对象列表，单次导入最大1000条。累计导入最大4000 (required) 
    :type enroll_list: List[V1MeetingsMeetingIdEnrollImportPostRequestEnrollListInner]

    :param instanceid: 操作者的终端设备类型 (required) 
    :type instanceid: int

    :param operator_id: 操作者 ID。operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。operator_id_type=2，operator_id必须和公共参数的openid一致。  使用OAuth公参鉴权后不能使用userid为入参。 (required) 
    :type operator_id: str

    :param operator_id_type: 操作者 ID 的类型： 1. 企业用户 userid 2 open_id (required) 
    :type operator_id_type: int
    """  # noqa: E501

    enroll_list: List[V1MeetingsMeetingIdEnrollImportPostRequestEnrollListInner]
    instanceid: int
    operator_id: str
    operator_id_type: int
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        enroll_list: List[V1MeetingsMeetingIdEnrollImportPostRequestEnrollListInner] | List[Dict[str, Any]],
        instanceid: int,
        operator_id: str,
        operator_id_type: int,
        **kwargs
    ):
        
        if enroll_list and isinstance(enroll_list, (list, List)):
            self.enroll_list = [V1MeetingsMeetingIdEnrollImportPostRequestEnrollListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in enroll_list]
        
        self.instanceid = instanceid
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type


class V1MeetingsMeetingIdEnrollImportPostRequestEnrollListInner(object):
    """V1MeetingsMeetingIdEnrollImportPostRequestEnrollListInner

    :param area: 国家/地区代码，若使用手机号，必填（例如：中国传86，不是+86） 
    :type area: Optional[str]

    :param nick_name: 报名的昵称，与会中昵称可能不一致 
    :type nick_name: Optional[str]

    :param open_id: OAuth授权用户ID。  导入报名对象支持本企业（或与OAuth应用同企业）内 userid、授权用户的openid、phone_number 三种形式，三者必填其一；  如果都传了以openid为准；（优先级为：openid -> userid -> phone_number）  JWT鉴权方式无法使用open_id导入报名。 
    :type open_id: Optional[str]

    :param phone_number: 手机号,导入报名支持本企业（或与OAuth应用同企业）内 userid、授权用户的openid、phone_number 三种形式，三者必填其一。 
    :type phone_number: Optional[str]

    :param userid: 用户的唯一 ID（企业内部请使用企业唯一用户标识）。 导入报名支持本企业（或与OAuth应用同企业）内 userid、授权用户的openid、phone_number 三种形式，三者必填其一。 
    :type userid: Optional[str]
    """  # noqa: E501

    area: Optional[str] = None
    nick_name: Optional[str] = None
    open_id: Optional[str] = None
    phone_number: Optional[str] = None
    userid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        area: Optional[str] = None,
        nick_name: Optional[str] = None,
        open_id: Optional[str] = None,
        phone_number: Optional[str] = None,
        userid: Optional[str] = None,
        **kwargs
    ):
        self.area = area
        self.nick_name = nick_name
        self.open_id = open_id
        self.phone_number = phone_number
        self.userid = userid


class V1MeetingsMeetingIdEnrollUnregistrationDelete200Response(object):
    """V1MeetingsMeetingIdEnrollUnregistrationDelete200Response

    :param total_count: 成功删除的报名信息数量 
    :type total_count: Optional[int]
    """  # noqa: E501

    total_count: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        total_count: Optional[int] = None,
        **kwargs
    ):
        self.total_count = total_count


class V1MeetingsMeetingIdEnrollUnregistrationDeleteRequest(object):
    """V1MeetingsMeetingIdEnrollUnregistrationDeleteRequest

    :param enroll_id_list: 报名对象列表 (required) 
    :type enroll_id_list: List[V1MeetingsMeetingIdEnrollUnregistrationDeleteRequestEnrollIdListInner]

    :param instanceid: 操作者的终端设备类型 (required) 
    :type instanceid: int

    :param operator_id: 操作者 ID。operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 (required) 
    :type operator_id: str

    :param operator_id_type: 操作者 ID 的类型： 1. 企业用户 userid 2: open_id (required) 
    :type operator_id_type: int
    """  # noqa: E501

    enroll_id_list: List[V1MeetingsMeetingIdEnrollUnregistrationDeleteRequestEnrollIdListInner]
    instanceid: int
    operator_id: str
    operator_id_type: int
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        enroll_id_list: List[V1MeetingsMeetingIdEnrollUnregistrationDeleteRequestEnrollIdListInner] | List[Dict[str, Any]],
        instanceid: int,
        operator_id: str,
        operator_id_type: int,
        **kwargs
    ):
        
        if enroll_id_list and isinstance(enroll_id_list, (list, List)):
            self.enroll_id_list = [V1MeetingsMeetingIdEnrollUnregistrationDeleteRequestEnrollIdListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in enroll_id_list]
        
        self.instanceid = instanceid
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type


class V1MeetingsMeetingIdEnrollUnregistrationDeleteRequestEnrollIdListInner(object):
    """V1MeetingsMeetingIdEnrollUnregistrationDeleteRequestEnrollIdListInner

    :param enroll_id: 报名ID (required) 
    :type enroll_id: int
    """  # noqa: E501

    enroll_id: int
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        enroll_id: int,
        **kwargs
    ):
        self.enroll_id = enroll_id


class V1MeetingsMeetingIdGet200Response(object):
    """V1MeetingsMeetingIdGet200Response

    :param meeting_info_list:
    :type meeting_info_list: Optional[List[V1MeetingsMeetingIdGet200ResponseMeetingInfoListInner]]

    :param meeting_number:
    :type meeting_number: Optional[int]
    """  # noqa: E501

    meeting_info_list: Optional[List[V1MeetingsMeetingIdGet200ResponseMeetingInfoListInner]] = None
    meeting_number: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        meeting_info_list: Optional[List[V1MeetingsMeetingIdGet200ResponseMeetingInfoListInner] | List[Dict[str, Any]]] = None,
        meeting_number: Optional[int] = None,
        **kwargs
    ):
        
        if meeting_info_list and isinstance(meeting_info_list, (list, List)):
            self.meeting_info_list = [V1MeetingsMeetingIdGet200ResponseMeetingInfoListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in meeting_info_list]
        
        self.meeting_number = meeting_number


class V1MeetingsMeetingIdGet200ResponseMeetingInfoListInner(object):
    """V1MeetingsMeetingIdGet200ResponseMeetingInfoListInner

    :param current_co_hosts:
    :type current_co_hosts: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner]]

    :param current_hosts:
    :type current_hosts: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner]]

    :param current_sub_meeting_id:
    :type current_sub_meeting_id: Optional[str]

    :param enable_doc_upload_permission:
    :type enable_doc_upload_permission: Optional[bool]

    :param enable_enroll:
    :type enable_enroll: Optional[bool]

    :param enable_host_key:
    :type enable_host_key: Optional[bool]

    :param enable_live:
    :type enable_live: Optional[bool]

    :param end_time:
    :type end_time: Optional[str]

    :param guests:
    :type guests: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInnerGuestsInner]]

    :param has_more_sub_meeting:
    :type has_more_sub_meeting: Optional[int]

    :param has_vote:
    :type has_vote: Optional[bool]

    :param host_key:
    :type host_key: Optional[str]

    :param hosts:
    :type hosts: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner]]

    :param join_url:
    :type join_url: Optional[str]

    :param live_config:
    :type live_config: Optional[V1MeetingsMeetingIdGet200ResponseMeetingInfoListInnerLiveConfig]

    :param location:
    :type location: Optional[str]

    :param meeting_code:
    :type meeting_code: Optional[str]

    :param meeting_id:
    :type meeting_id: Optional[str]

    :param meeting_type:
    :type meeting_type: Optional[int]

    :param need_password:
    :type need_password: Optional[bool]

    :param participants:
    :type participants: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner]]

    :param password:
    :type password: Optional[str]

    :param recurring_rule:
    :type recurring_rule: Optional[V1MeetingsMeetingIdGet200ResponseMeetingInfoListInnerRecurringRule]

    :param remain_sub_meetings:
    :type remain_sub_meetings: Optional[int]

    :param settings:
    :type settings: Optional[V1MeetingsMeetingIdGet200ResponseMeetingInfoListInnerSettings]

    :param start_time:
    :type start_time: Optional[str]

    :param status:
    :type status: Optional[str]

    :param sub_meetings:
    :type sub_meetings: Optional[List[V1MeetingsMeetingIdGet200ResponseMeetingInfoListInnerSubMeetingsInner]]

    :param subject:
    :type subject: Optional[str]

    :param sync_to_wework:
    :type sync_to_wework: Optional[bool]

    :param time_zone:
    :type time_zone: Optional[str]

    :param type:
    :type type: Optional[int]
    """  # noqa: E501

    current_co_hosts: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner]] = None
    current_hosts: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner]] = None
    current_sub_meeting_id: Optional[str] = None
    enable_doc_upload_permission: Optional[bool] = None
    enable_enroll: Optional[bool] = None
    enable_host_key: Optional[bool] = None
    enable_live: Optional[bool] = None
    end_time: Optional[str] = None
    guests: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInnerGuestsInner]] = None
    has_more_sub_meeting: Optional[int] = None
    has_vote: Optional[bool] = None
    host_key: Optional[str] = None
    hosts: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner]] = None
    join_url: Optional[str] = None
    live_config: Optional[V1MeetingsMeetingIdGet200ResponseMeetingInfoListInnerLiveConfig] = None
    location: Optional[str] = None
    meeting_code: Optional[str] = None
    meeting_id: Optional[str] = None
    meeting_type: Optional[int] = None
    need_password: Optional[bool] = None
    participants: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner]] = None
    password: Optional[str] = None
    recurring_rule: Optional[V1MeetingsMeetingIdGet200ResponseMeetingInfoListInnerRecurringRule] = None
    remain_sub_meetings: Optional[int] = None
    settings: Optional[V1MeetingsMeetingIdGet200ResponseMeetingInfoListInnerSettings] = None
    start_time: Optional[str] = None
    status: Optional[str] = None
    sub_meetings: Optional[List[V1MeetingsMeetingIdGet200ResponseMeetingInfoListInnerSubMeetingsInner]] = None
    subject: Optional[str] = None
    sync_to_wework: Optional[bool] = None
    time_zone: Optional[str] = None
    type: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        current_co_hosts: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner] | List[Dict[str, Any]]] = None,
        current_hosts: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner] | List[Dict[str, Any]]] = None,
        current_sub_meeting_id: Optional[str] = None,
        enable_doc_upload_permission: Optional[bool] = None,
        enable_enroll: Optional[bool] = None,
        enable_host_key: Optional[bool] = None,
        enable_live: Optional[bool] = None,
        end_time: Optional[str] = None,
        guests: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInnerGuestsInner] | List[Dict[str, Any]]] = None,
        has_more_sub_meeting: Optional[int] = None,
        has_vote: Optional[bool] = None,
        host_key: Optional[str] = None,
        hosts: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner] | List[Dict[str, Any]]] = None,
        join_url: Optional[str] = None,
        live_config: Optional[V1MeetingsMeetingIdGet200ResponseMeetingInfoListInnerLiveConfig | Dict[str, Any]] = None,
        location: Optional[str] = None,
        meeting_code: Optional[str] = None,
        meeting_id: Optional[str] = None,
        meeting_type: Optional[int] = None,
        need_password: Optional[bool] = None,
        participants: Optional[List[V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner] | List[Dict[str, Any]]] = None,
        password: Optional[str] = None,
        recurring_rule: Optional[V1MeetingsMeetingIdGet200ResponseMeetingInfoListInnerRecurringRule | Dict[str, Any]] = None,
        remain_sub_meetings: Optional[int] = None,
        settings: Optional[V1MeetingsMeetingIdGet200ResponseMeetingInfoListInnerSettings | Dict[str, Any]] = None,
        start_time: Optional[str] = None,
        status: Optional[str] = None,
        sub_meetings: Optional[List[V1MeetingsMeetingIdGet200ResponseMeetingInfoListInnerSubMeetingsInner] | List[Dict[str, Any]]] = None,
        subject: Optional[str] = None,
        sync_to_wework: Optional[bool] = None,
        time_zone: Optional[str] = None,
        type: Optional[int] = None,
        **kwargs
    ):
        
        if current_co_hosts and isinstance(current_co_hosts, (list, List)):
            self.current_co_hosts = [V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in current_co_hosts]
        
        
        if current_hosts and isinstance(current_hosts, (list, List)):
            self.current_hosts = [V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in current_hosts]
        
        self.current_sub_meeting_id = current_sub_meeting_id
        self.enable_doc_upload_permission = enable_doc_upload_permission
        self.enable_enroll = enable_enroll
        self.enable_host_key = enable_host_key
        self.enable_live = enable_live
        self.end_time = end_time
        
        if guests and isinstance(guests, (list, List)):
            self.guests = [V1MeetingsGet200ResponseMeetingInfoListInnerGuestsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in guests]
        
        self.has_more_sub_meeting = has_more_sub_meeting
        self.has_vote = has_vote
        self.host_key = host_key
        
        if hosts and isinstance(hosts, (list, List)):
            self.hosts = [V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in hosts]
        
        self.join_url = join_url
        self.live_config = V1MeetingsMeetingIdGet200ResponseMeetingInfoListInnerLiveConfig(**live_config) if isinstance(live_config, (dict, Dict)) else live_config
        self.location = location
        self.meeting_code = meeting_code
        self.meeting_id = meeting_id
        self.meeting_type = meeting_type
        self.need_password = need_password
        
        if participants and isinstance(participants, (list, List)):
            self.participants = [V1MeetingsGet200ResponseMeetingInfoListInnerCurrentCoHostsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in participants]
        
        self.password = password
        self.recurring_rule = V1MeetingsMeetingIdGet200ResponseMeetingInfoListInnerRecurringRule(**recurring_rule) if isinstance(recurring_rule, (dict, Dict)) else recurring_rule
        self.remain_sub_meetings = remain_sub_meetings
        self.settings = V1MeetingsMeetingIdGet200ResponseMeetingInfoListInnerSettings(**settings) if isinstance(settings, (dict, Dict)) else settings
        self.start_time = start_time
        self.status = status
        
        if sub_meetings and isinstance(sub_meetings, (list, List)):
            self.sub_meetings = [V1MeetingsMeetingIdGet200ResponseMeetingInfoListInnerSubMeetingsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in sub_meetings]
        
        self.subject = subject
        self.sync_to_wework = sync_to_wework
        self.time_zone = time_zone
        self.type = type


class V1MeetingsMeetingIdGet200ResponseMeetingInfoListInnerLiveConfig(object):
    """V1MeetingsMeetingIdGet200ResponseMeetingInfoListInnerLiveConfig

    :param enable_live_im:
    :type enable_live_im: Optional[bool]

    :param enable_live_replay:
    :type enable_live_replay: Optional[bool]

    :param live_addr:
    :type live_addr: Optional[str]

    :param live_password:
    :type live_password: Optional[str]

    :param live_subject:
    :type live_subject: Optional[str]

    :param live_summary:
    :type live_summary: Optional[str]

    :param live_watermark:
    :type live_watermark: Optional[V1MeetingsGet200ResponseMeetingInfoListInnerLiveConfigLiveWatermark]
    """  # noqa: E501

    enable_live_im: Optional[bool] = None
    enable_live_replay: Optional[bool] = None
    live_addr: Optional[str] = None
    live_password: Optional[str] = None
    live_subject: Optional[str] = None
    live_summary: Optional[str] = None
    live_watermark: Optional[V1MeetingsGet200ResponseMeetingInfoListInnerLiveConfigLiveWatermark] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        enable_live_im: Optional[bool] = None,
        enable_live_replay: Optional[bool] = None,
        live_addr: Optional[str] = None,
        live_password: Optional[str] = None,
        live_subject: Optional[str] = None,
        live_summary: Optional[str] = None,
        live_watermark: Optional[V1MeetingsGet200ResponseMeetingInfoListInnerLiveConfigLiveWatermark | Dict[str, Any]] = None,
        **kwargs
    ):
        self.enable_live_im = enable_live_im
        self.enable_live_replay = enable_live_replay
        self.live_addr = live_addr
        self.live_password = live_password
        self.live_subject = live_subject
        self.live_summary = live_summary
        self.live_watermark = V1MeetingsGet200ResponseMeetingInfoListInnerLiveConfigLiveWatermark(**live_watermark) if isinstance(live_watermark, (dict, Dict)) else live_watermark


class V1MeetingsMeetingIdGet200ResponseMeetingInfoListInnerRecurringRule(object):
    """V1MeetingsMeetingIdGet200ResponseMeetingInfoListInnerRecurringRule

    :param customized_recurring_days:
    :type customized_recurring_days: Optional[int]

    :param customized_recurring_step:
    :type customized_recurring_step: Optional[int]

    :param customized_recurring_type:
    :type customized_recurring_type: Optional[int]

    :param recurring_type:
    :type recurring_type: Optional[int]

    :param until_count:
    :type until_count: Optional[int]

    :param until_date:
    :type until_date: Optional[int]

    :param until_type:
    :type until_type: Optional[int]
    """  # noqa: E501

    customized_recurring_days: Optional[int] = None
    customized_recurring_step: Optional[int] = None
    customized_recurring_type: Optional[int] = None
    recurring_type: Optional[int] = None
    until_count: Optional[int] = None
    until_date: Optional[int] = None
    until_type: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        customized_recurring_days: Optional[int] = None,
        customized_recurring_step: Optional[int] = None,
        customized_recurring_type: Optional[int] = None,
        recurring_type: Optional[int] = None,
        until_count: Optional[int] = None,
        until_date: Optional[int] = None,
        until_type: Optional[int] = None,
        **kwargs
    ):
        self.customized_recurring_days = customized_recurring_days
        self.customized_recurring_step = customized_recurring_step
        self.customized_recurring_type = customized_recurring_type
        self.recurring_type = recurring_type
        self.until_count = until_count
        self.until_date = until_date
        self.until_type = until_type


class V1MeetingsMeetingIdGet200ResponseMeetingInfoListInnerSettings(object):
    """V1MeetingsMeetingIdGet200ResponseMeetingInfoListInnerSettings

    :param allow_in_before_host:
    :type allow_in_before_host: Optional[bool]

    :param allow_screen_shared_watermark:
    :type allow_screen_shared_watermark: Optional[bool]

    :param allow_unmute_self:
    :type allow_unmute_self: Optional[bool]

    :param auto_in_waiting_room:
    :type auto_in_waiting_room: Optional[bool]

    :param auto_record_type:
    :type auto_record_type: Optional[str]

    :param change_nickname: 是否允许用户自己改名 1:允许用户自己改名，2:不允许用户自己改名，默认为1 
    :type change_nickname: Optional[int]

    :param enable_host_pause_auto_record:
    :type enable_host_pause_auto_record: Optional[bool]

    :param mute_enable_join:
    :type mute_enable_join: Optional[bool]

    :param mute_enable_type_join:
    :type mute_enable_type_join: Optional[int]

    :param only_allow_enterprise_user_join:
    :type only_allow_enterprise_user_join: Optional[bool]

    :param only_invitees_allowed: 是否仅受邀成员可入会，默认值为false，true：仅受邀成员可入会，false：所有成员可入会 
    :type only_invitees_allowed: Optional[bool]

    :param participant_join_auto_record:
    :type participant_join_auto_record: Optional[bool]

    :param water_mark_type:
    :type water_mark_type: Optional[int]
    """  # noqa: E501

    allow_in_before_host: Optional[bool] = None
    allow_screen_shared_watermark: Optional[bool] = None
    allow_unmute_self: Optional[bool] = None
    auto_in_waiting_room: Optional[bool] = None
    auto_record_type: Optional[str] = None
    change_nickname: Optional[int] = None
    enable_host_pause_auto_record: Optional[bool] = None
    mute_enable_join: Optional[bool] = None
    mute_enable_type_join: Optional[int] = None
    only_allow_enterprise_user_join: Optional[bool] = None
    only_invitees_allowed: Optional[bool] = None
    participant_join_auto_record: Optional[bool] = None
    water_mark_type: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        allow_in_before_host: Optional[bool] = None,
        allow_screen_shared_watermark: Optional[bool] = None,
        allow_unmute_self: Optional[bool] = None,
        auto_in_waiting_room: Optional[bool] = None,
        auto_record_type: Optional[str] = None,
        change_nickname: Optional[int] = None,
        enable_host_pause_auto_record: Optional[bool] = None,
        mute_enable_join: Optional[bool] = None,
        mute_enable_type_join: Optional[int] = None,
        only_allow_enterprise_user_join: Optional[bool] = None,
        only_invitees_allowed: Optional[bool] = None,
        participant_join_auto_record: Optional[bool] = None,
        water_mark_type: Optional[int] = None,
        **kwargs
    ):
        self.allow_in_before_host = allow_in_before_host
        self.allow_screen_shared_watermark = allow_screen_shared_watermark
        self.allow_unmute_self = allow_unmute_self
        self.auto_in_waiting_room = auto_in_waiting_room
        self.auto_record_type = auto_record_type
        self.change_nickname = change_nickname
        self.enable_host_pause_auto_record = enable_host_pause_auto_record
        self.mute_enable_join = mute_enable_join
        self.mute_enable_type_join = mute_enable_type_join
        self.only_allow_enterprise_user_join = only_allow_enterprise_user_join
        self.only_invitees_allowed = only_invitees_allowed
        self.participant_join_auto_record = participant_join_auto_record
        self.water_mark_type = water_mark_type


class V1MeetingsMeetingIdGet200ResponseMeetingInfoListInnerSubMeetingsInner(object):
    """V1MeetingsMeetingIdGet200ResponseMeetingInfoListInnerSubMeetingsInner

    :param end_time:
    :type end_time: Optional[str]

    :param start_time:
    :type start_time: Optional[str]

    :param status:
    :type status: Optional[int]

    :param sub_meeting_id:
    :type sub_meeting_id: Optional[str]
    """  # noqa: E501

    end_time: Optional[str] = None
    start_time: Optional[str] = None
    status: Optional[int] = None
    sub_meeting_id: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        end_time: Optional[str] = None,
        start_time: Optional[str] = None,
        status: Optional[int] = None,
        sub_meeting_id: Optional[str] = None,
        **kwargs
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.status = status
        self.sub_meeting_id = sub_meeting_id


class V1MeetingsMeetingIdInviteesGet200Response(object):
    """V1MeetingsMeetingIdInviteesGet200Response

    :param has_remaining: 是否还存在受邀成员需要继续查询。 
    :type has_remaining: Optional[bool]

    :param invitees: 会议邀请的参会者 
    :type invitees: Optional[List[V1MeetingsMeetingIdInviteesGet200ResponseInviteesInner]]

    :param next_pos: 当has_remaining为true时，下次查询时输入参数pos的值 
    :type next_pos: Optional[int]
    """  # noqa: E501

    has_remaining: Optional[bool] = None
    invitees: Optional[List[V1MeetingsMeetingIdInviteesGet200ResponseInviteesInner]] = None
    next_pos: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        has_remaining: Optional[bool] = None,
        invitees: Optional[List[V1MeetingsMeetingIdInviteesGet200ResponseInviteesInner] | List[Dict[str, Any]]] = None,
        next_pos: Optional[int] = None,
        **kwargs
    ):
        self.has_remaining = has_remaining
        
        if invitees and isinstance(invitees, (list, List)):
            self.invitees = [V1MeetingsMeetingIdInviteesGet200ResponseInviteesInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in invitees]
        
        self.next_pos = next_pos


class V1MeetingsMeetingIdInviteesGet200ResponseInviteesInner(object):
    """V1MeetingsMeetingIdInviteesGet200ResponseInviteesInner

    :param nick_name: 用户昵称 
    :type nick_name: Optional[str]

    :param userid: 用户的唯一 ID（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId） 
    :type userid: Optional[str]
    """  # noqa: E501

    nick_name: Optional[str] = None
    userid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        nick_name: Optional[str] = None,
        userid: Optional[str] = None,
        **kwargs
    ):
        self.nick_name = nick_name
        self.userid = userid


class V1MeetingsMeetingIdInviteesPutRequest(object):
    """V1MeetingsMeetingIdInviteesPutRequest

    :param instanceid: 用户的终端设备类型：1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch Mac 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch Iphone (required) 
    :type instanceid: int

    :param invitees: 会议邀请的参会者（传空数组或不传会清空受邀成员列表，最大支持2000人） 
    :type invitees: Optional[List[V1MeetingsMeetingIdInviteesPutRequestInviteesInner]]

    :param userid: 会议创建者ID。调用方用于标示用户的唯一 ID（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId）。 企业唯一用户标识说明： 1. 企业对接 SSO 时使用的员工唯一标识 ID。 2. 企业调用创建用户接口时传递的 userid 参数。 (required) 
    :type userid: str
    """  # noqa: E501

    instanceid: int
    invitees: Optional[List[V1MeetingsMeetingIdInviteesPutRequestInviteesInner]] = None
    userid: str
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        instanceid: int,
        userid: str,
        invitees: Optional[List[V1MeetingsMeetingIdInviteesPutRequestInviteesInner] | List[Dict[str, Any]]] = None,
        **kwargs
    ):
        self.instanceid = instanceid
        
        if invitees and isinstance(invitees, (list, List)):
            self.invitees = [V1MeetingsMeetingIdInviteesPutRequestInviteesInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in invitees]
        
        self.userid = userid


class V1MeetingsMeetingIdInviteesPutRequestInviteesInner(object):
    """V1MeetingsMeetingIdInviteesPutRequestInviteesInner

    :param userid: 调用方用于标示用户的唯一 ID，仅支持邀请与会议创建者同企业的成员（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId）。 企业唯一用户标识说明： 企业对接 SSO 时使用的员工唯一标识 ID。 企业调用创建用户接口时传递的 userid 参数。 (required) 
    :type userid: str
    """  # noqa: E501

    userid: str
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        userid: str,
        **kwargs
    ):
        self.userid = userid


class V1MeetingsMeetingIdParticipantsGet200Response(object):
    """V1MeetingsMeetingIdParticipantsGet200Response

    :param has_remaining: 是否还有未拉取的数据，该接口可多次拉取到的数据总量上限为5w条。 
    :type has_remaining: Optional[bool]

    :param meeting_code: 会议号码。 
    :type meeting_code: Optional[str]

    :param meeting_id: 会议的唯一 ID。 
    :type meeting_id: Optional[str]

    :param next_pos: 和“has_remaining”一起，数据量比较大的情况下支持参会成员列表的多次获取。 
    :type next_pos: Optional[int]

    :param participants: 参会人员对象数组。 
    :type participants: Optional[List[V1MeetingsMeetingIdParticipantsGet200ResponseParticipantsInner]]

    :param schedule_end_time: 预定会议开始时间戳（单位秒）。 
    :type schedule_end_time: Optional[str]

    :param schedule_start_time: 预定会议结束时间戳（单位秒）。 
    :type schedule_start_time: Optional[str]

    :param subject: 会议主题。 
    :type subject: Optional[str]

    :param total_count: 当前参会总人次。 
    :type total_count: Optional[int]
    """  # noqa: E501

    has_remaining: Optional[bool] = None
    meeting_code: Optional[str] = None
    meeting_id: Optional[str] = None
    next_pos: Optional[int] = None
    participants: Optional[List[V1MeetingsMeetingIdParticipantsGet200ResponseParticipantsInner]] = None
    schedule_end_time: Optional[str] = None
    schedule_start_time: Optional[str] = None
    subject: Optional[str] = None
    total_count: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        has_remaining: Optional[bool] = None,
        meeting_code: Optional[str] = None,
        meeting_id: Optional[str] = None,
        next_pos: Optional[int] = None,
        participants: Optional[List[V1MeetingsMeetingIdParticipantsGet200ResponseParticipantsInner] | List[Dict[str, Any]]] = None,
        schedule_end_time: Optional[str] = None,
        schedule_start_time: Optional[str] = None,
        subject: Optional[str] = None,
        total_count: Optional[int] = None,
        **kwargs
    ):
        self.has_remaining = has_remaining
        self.meeting_code = meeting_code
        self.meeting_id = meeting_id
        self.next_pos = next_pos
        
        if participants and isinstance(participants, (list, List)):
            self.participants = [V1MeetingsMeetingIdParticipantsGet200ResponseParticipantsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in participants]
        
        self.schedule_end_time = schedule_end_time
        self.schedule_start_time = schedule_start_time
        self.subject = subject
        self.total_count = total_count


class V1MeetingsMeetingIdParticipantsGet200ResponseParticipantsInner(object):
    """V1MeetingsMeetingIdParticipantsGet200ResponseParticipantsInner

    :param app_version: 用户的客户端版本。当用户在会中时才能返回。 
    :type app_version: Optional[str]

    :param audio_state: 麦克风状态： true：开启 false：关闭 
    :type audio_state: Optional[bool]

    :param customer_data: 专属字段 
    :type customer_data: Optional[str]

    :param instanceid: 用户的终端设备类型： 0：PSTN 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备（即MRA设备） 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch MacOS 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch iOS/iPadOS 
    :type instanceid: Optional[int]

    :param ip: 用户的 IP 地址。当用户在会中时才能返回。 
    :type ip: Optional[str]

    :param join_time: 参会者加入会议时间戳（单位秒）。 
    :type join_time: Optional[str]

    :param join_type: 入会方式： 0：PSTN 普通用户，标准的手机或固话类型 1：普通 VOIP 用户 2：附属投屏 VOIP 3：linux sdk for VOIP 4：附属语音 PSTN 5：附属视频 PSTN 6：linux sdk for PSTN 
    :type join_type: Optional[int]

    :param left_time: 参会者离开会议时间戳（单位秒）。 
    :type left_time: Optional[str]

    :param link_type: 用户的连接方式：UDP、TCP、未知，当用户在会中时才能返回。 
    :type link_type: Optional[str]

    :param location: 用户的地理位置信息。当用户在会中时才能返回。 
    :type location: Optional[str]

    :param ms_open_id: 当场会议的用户临时 ID，可用于会控操作，适用于所有用户。 
    :type ms_open_id: Optional[str]

    :param net: 网络类型：有线、WIFI、2G、3G、4G、未知。当用户在会中时才能返回。 
    :type net: Optional[str]

    :param open_id:
    :type open_id: Optional[str]

    :param phone: 参会者手机号 hash 值 SHA256（手机号 + \"/\" + secretid）。 
    :type phone: Optional[str]

    :param screen_shared_state: 屏幕共享状态： true：开启 false：关闭 
    :type screen_shared_state: Optional[bool]

    :param user_name: 入会用户名（base64）。 
    :type user_name: Optional[str]

    :param user_role: 用户角色： 0：普通成员角色 1：创建者角色 2：主持人 3：创建者+主持人 4：游客 5：游客+主持人 6：联席主持人 7：创建者+联席主持人 
    :type user_role: Optional[int]

    :param userid: 参会者用户 ID。 使用企业自建应用鉴权方式（JWT）时，该值为企业唯一用户标识。 
    :type userid: Optional[str]

    :param uuid: 用户的身份 ID，仅适用于单场会议。 
    :type uuid: Optional[str]

    :param video_state: 摄像头状态： true：开启 false：关闭 
    :type video_state: Optional[bool]

    :param webinar_member_role: 网络研讨会成员角色： 0：普通参会角色 1：内部嘉宾 2：外部嘉宾 3：邀请链接入会嘉宾 4：观众 5：有音视频权限的研讨会观众 
    :type webinar_member_role: Optional[int]
    """  # noqa: E501

    app_version: Optional[str] = None
    audio_state: Optional[bool] = None
    customer_data: Optional[str] = None
    instanceid: Optional[int] = None
    ip: Optional[str] = None
    join_time: Optional[str] = None
    join_type: Optional[int] = None
    left_time: Optional[str] = None
    link_type: Optional[str] = None
    location: Optional[str] = None
    ms_open_id: Optional[str] = None
    net: Optional[str] = None
    open_id: Optional[str] = None
    phone: Optional[str] = None
    screen_shared_state: Optional[bool] = None
    user_name: Optional[str] = None
    user_role: Optional[int] = None
    userid: Optional[str] = None
    uuid: Optional[str] = None
    video_state: Optional[bool] = None
    webinar_member_role: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        app_version: Optional[str] = None,
        audio_state: Optional[bool] = None,
        customer_data: Optional[str] = None,
        instanceid: Optional[int] = None,
        ip: Optional[str] = None,
        join_time: Optional[str] = None,
        join_type: Optional[int] = None,
        left_time: Optional[str] = None,
        link_type: Optional[str] = None,
        location: Optional[str] = None,
        ms_open_id: Optional[str] = None,
        net: Optional[str] = None,
        open_id: Optional[str] = None,
        phone: Optional[str] = None,
        screen_shared_state: Optional[bool] = None,
        user_name: Optional[str] = None,
        user_role: Optional[int] = None,
        userid: Optional[str] = None,
        uuid: Optional[str] = None,
        video_state: Optional[bool] = None,
        webinar_member_role: Optional[int] = None,
        **kwargs
    ):
        self.app_version = app_version
        self.audio_state = audio_state
        self.customer_data = customer_data
        self.instanceid = instanceid
        self.ip = ip
        self.join_time = join_time
        self.join_type = join_type
        self.left_time = left_time
        self.link_type = link_type
        self.location = location
        self.ms_open_id = ms_open_id
        self.net = net
        self.open_id = open_id
        self.phone = phone
        self.screen_shared_state = screen_shared_state
        self.user_name = user_name
        self.user_role = user_role
        self.userid = userid
        self.uuid = uuid
        self.video_state = video_state
        self.webinar_member_role = webinar_member_role


class V1MeetingsMeetingIdPut200Response(object):
    """V1MeetingsMeetingIdPut200Response

    :param meeting_info_list: 会议列表 
    :type meeting_info_list: Optional[List[V1MeetingsMeetingIdPut200ResponseMeetingInfoListInner]]

    :param meeting_number: 会议数量 
    :type meeting_number: Optional[int]
    """  # noqa: E501

    meeting_info_list: Optional[List[V1MeetingsMeetingIdPut200ResponseMeetingInfoListInner]] = None
    meeting_number: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        meeting_info_list: Optional[List[V1MeetingsMeetingIdPut200ResponseMeetingInfoListInner] | List[Dict[str, Any]]] = None,
        meeting_number: Optional[int] = None,
        **kwargs
    ):
        
        if meeting_info_list and isinstance(meeting_info_list, (list, List)):
            self.meeting_info_list = [V1MeetingsMeetingIdPut200ResponseMeetingInfoListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in meeting_info_list]
        
        self.meeting_number = meeting_number


class V1MeetingsMeetingIdPut200ResponseMeetingInfoListInner(object):
    """V1MeetingsMeetingIdPut200ResponseMeetingInfoListInner

    :param enable_live: 是否开启直播 
    :type enable_live: Optional[bool]

    :param host_key: 主持人密钥，仅支持6位数字。 如开启主持人密钥后没有填写此项，将自动分配一个6位数字的密钥。  
    :type host_key: Optional[str]

    :param live_config:
    :type live_config: Optional[V1MeetingsMeetingIdPut200ResponseMeetingInfoListInnerLiveConfig]

    :param meeting_code: 会议号码 
    :type meeting_code: Optional[str]

    :param meeting_id: 会议的唯一 ID 
    :type meeting_id: Optional[str]

    :param settings:
    :type settings: Optional[V1MeetingsMeetingIdPut200ResponseMeetingInfoListInnerSettings]
    """  # noqa: E501

    enable_live: Optional[bool] = None
    host_key: Optional[str] = None
    live_config: Optional[V1MeetingsMeetingIdPut200ResponseMeetingInfoListInnerLiveConfig] = None
    meeting_code: Optional[str] = None
    meeting_id: Optional[str] = None
    settings: Optional[V1MeetingsMeetingIdPut200ResponseMeetingInfoListInnerSettings] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        enable_live: Optional[bool] = None,
        host_key: Optional[str] = None,
        live_config: Optional[V1MeetingsMeetingIdPut200ResponseMeetingInfoListInnerLiveConfig | Dict[str, Any]] = None,
        meeting_code: Optional[str] = None,
        meeting_id: Optional[str] = None,
        settings: Optional[V1MeetingsMeetingIdPut200ResponseMeetingInfoListInnerSettings | Dict[str, Any]] = None,
        **kwargs
    ):
        self.enable_live = enable_live
        self.host_key = host_key
        self.live_config = V1MeetingsMeetingIdPut200ResponseMeetingInfoListInnerLiveConfig(**live_config) if isinstance(live_config, (dict, Dict)) else live_config
        self.meeting_code = meeting_code
        self.meeting_id = meeting_id
        self.settings = V1MeetingsMeetingIdPut200ResponseMeetingInfoListInnerSettings(**settings) if isinstance(settings, (dict, Dict)) else settings


class V1MeetingsMeetingIdPut200ResponseMeetingInfoListInnerLiveConfig(object):
    """直播配置对象，内部只返回 live_addr（直播观看地址）。

    :param live_addr: 直播观看地址 
    :type live_addr: Optional[str]
    """  # noqa: E501

    live_addr: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        live_addr: Optional[str] = None,
        **kwargs
    ):
        self.live_addr = live_addr


class V1MeetingsMeetingIdPut200ResponseMeetingInfoListInnerSettings(object):
    """V1MeetingsMeetingIdPut200ResponseMeetingInfoListInnerSettings

    :param change_nickname: 是否允许用户自己改名 1:允许用户自己改名，2:不允许用户自己改名，默认为1 
    :type change_nickname: Optional[int]

    :param only_invitees_allowed: 是否仅受邀成员可入会，默认值为false，true：仅受邀成员可入会，false：所有成员可入会 
    :type only_invitees_allowed: Optional[bool]
    """  # noqa: E501

    change_nickname: Optional[int] = None
    only_invitees_allowed: Optional[bool] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        change_nickname: Optional[int] = None,
        only_invitees_allowed: Optional[bool] = None,
        **kwargs
    ):
        self.change_nickname = change_nickname
        self.only_invitees_allowed = only_invitees_allowed


class V1MeetingsMeetingIdPutRequest(object):
    """V1MeetingsMeetingIdPutRequest

    :param allow_enterprise_intranet_only: 如果没有权限创建专网会议，该字段忽略 
    :type allow_enterprise_intranet_only: Optional[bool]

    :param enable_doc_upload_permission: 是否允许成员上传文档，默认为允许 
    :type enable_doc_upload_permission: Optional[bool]

    :param enable_enroll: 是否开启报名开关，默认不开启 
    :type enable_enroll: Optional[bool]

    :param enable_host_key: 是否开启主持人密钥，默认为false。 true：开启 false：关闭 修改周期性会议的主持人密钥适用于接下来的所有子会议。 
    :type enable_host_key: Optional[bool]

    :param enable_live: 是否开启直播,默认不开启 
    :type enable_live: Optional[bool]

    :param end_time: 会议结束时间戳（单位秒） 
    :type end_time: Optional[str]

    :param guests: 会议嘉宾列表，会议嘉宾不受会议密码和等候室的限制。不传该字段代表不修改。注意：传空数组会清空嘉宾列表。 
    :type guests: Optional[List[V1MeetingsPostRequestGuestsInner]]

    :param host_key: 主持人密钥，仅支持6位数字。 如开启主持人密钥后没有填写此项，将自动分配一个6位数字的密钥。 
    :type host_key: Optional[str]

    :param hosts: 主持人列表。 不传入该字段则不修改，传入空列表即覆盖为空。 
    :type hosts: Optional[List[V1MeetingsMeetingIdPutRequestHostsInner]]

    :param instanceid: 用户的终端设备类型： 0：PSTN 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch MacOS 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch iOS (required) 
    :type instanceid: int

    :param invitees: 邀请人列表，调用方用于标示用户的唯一 ID，仅支持邀请与会议创建者同企业的成员（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId）。 企业唯一用户标识说明： 企业对接 SSO 时使用的员工唯一标识 ID。 企业调用创建用户接口时传递的 userid 参数。 注意：仅腾讯会议商业版和企业版可邀请参会者，邀请者列表仅支持300人；需要邀请超过300人的场景请调用 设置会议邀请成员 接口。 
    :type invitees: Optional[List[V1MeetingsPostRequestInviteesInner]]

    :param live_config:
    :type live_config: Optional[V1MeetingsMeetingIdPutRequestLiveConfig]

    :param location: 会议地点。最长支持18个汉字或36个英文字母。 
    :type location: Optional[str]

    :param media_set_type: 该参数仅提供给支持混合云的企业可见，默认值为0。 0：外部会议 1：内部会议 
    :type media_set_type: Optional[int]

    :param meeting_type: 默认值为0。  0：普通会议  1：周期性会议（周期性会议时 type 不能为快速会议，同一账号同时最多可预定50场周期性会议） 
    :type meeting_type: Optional[int]

    :param password: 会议密码（4~6位数字），可不填。如果将字段值改为空字符串\"\"，则表示取消会议密码 
    :type password: Optional[str]

    :param recurring_rule:
    :type recurring_rule: Optional[V1MeetingsMeetingIdPutRequestRecurringRule]

    :param settings:
    :type settings: Optional[V1MeetingsMeetingIdPutRequestSettings]

    :param start_time: 会议开始时间戳（单位秒） 
    :type start_time: Optional[str]

    :param subject: 会议主题 
    :type subject: Optional[str]

    :param time_zone: 时区，可参见 Oracle-TimeZone 标准。 
    :type time_zone: Optional[str]

    :param userid: 会议创建者 ID（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId）。 企业唯一用户标识说明： 1. 企业对接 SSO 时使用的员工唯一标识 ID。 2. 企业调用创建用户接口时传递的 userid 参数。  (required) 
    :type userid: str
    """  # noqa: E501

    allow_enterprise_intranet_only: Optional[bool] = None
    enable_doc_upload_permission: Optional[bool] = None
    enable_enroll: Optional[bool] = None
    enable_host_key: Optional[bool] = None
    enable_live: Optional[bool] = None
    end_time: Optional[str] = None
    guests: Optional[List[V1MeetingsPostRequestGuestsInner]] = None
    host_key: Optional[str] = None
    hosts: Optional[List[V1MeetingsMeetingIdPutRequestHostsInner]] = None
    instanceid: int
    invitees: Optional[List[V1MeetingsPostRequestInviteesInner]] = None
    live_config: Optional[V1MeetingsMeetingIdPutRequestLiveConfig] = None
    location: Optional[str] = None
    media_set_type: Optional[int] = None
    meeting_type: Optional[int] = None
    password: Optional[str] = None
    recurring_rule: Optional[V1MeetingsMeetingIdPutRequestRecurringRule] = None
    settings: Optional[V1MeetingsMeetingIdPutRequestSettings] = None
    start_time: Optional[str] = None
    subject: Optional[str] = None
    time_zone: Optional[str] = None
    userid: str
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        instanceid: int,
        userid: str,
        allow_enterprise_intranet_only: Optional[bool] = None,
        enable_doc_upload_permission: Optional[bool] = None,
        enable_enroll: Optional[bool] = None,
        enable_host_key: Optional[bool] = None,
        enable_live: Optional[bool] = None,
        end_time: Optional[str] = None,
        guests: Optional[List[V1MeetingsPostRequestGuestsInner] | List[Dict[str, Any]]] = None,
        host_key: Optional[str] = None,
        hosts: Optional[List[V1MeetingsMeetingIdPutRequestHostsInner] | List[Dict[str, Any]]] = None,
        invitees: Optional[List[V1MeetingsPostRequestInviteesInner] | List[Dict[str, Any]]] = None,
        live_config: Optional[V1MeetingsMeetingIdPutRequestLiveConfig | Dict[str, Any]] = None,
        location: Optional[str] = None,
        media_set_type: Optional[int] = None,
        meeting_type: Optional[int] = None,
        password: Optional[str] = None,
        recurring_rule: Optional[V1MeetingsMeetingIdPutRequestRecurringRule | Dict[str, Any]] = None,
        settings: Optional[V1MeetingsMeetingIdPutRequestSettings | Dict[str, Any]] = None,
        start_time: Optional[str] = None,
        subject: Optional[str] = None,
        time_zone: Optional[str] = None,
        **kwargs
    ):
        self.allow_enterprise_intranet_only = allow_enterprise_intranet_only
        self.enable_doc_upload_permission = enable_doc_upload_permission
        self.enable_enroll = enable_enroll
        self.enable_host_key = enable_host_key
        self.enable_live = enable_live
        self.end_time = end_time
        
        if guests and isinstance(guests, (list, List)):
            self.guests = [V1MeetingsPostRequestGuestsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in guests]
        
        self.host_key = host_key
        
        if hosts and isinstance(hosts, (list, List)):
            self.hosts = [V1MeetingsMeetingIdPutRequestHostsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in hosts]
        
        self.instanceid = instanceid
        
        if invitees and isinstance(invitees, (list, List)):
            self.invitees = [V1MeetingsPostRequestInviteesInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in invitees]
        
        self.live_config = V1MeetingsMeetingIdPutRequestLiveConfig(**live_config) if isinstance(live_config, (dict, Dict)) else live_config
        self.location = location
        self.media_set_type = media_set_type
        self.meeting_type = meeting_type
        self.password = password
        self.recurring_rule = V1MeetingsMeetingIdPutRequestRecurringRule(**recurring_rule) if isinstance(recurring_rule, (dict, Dict)) else recurring_rule
        self.settings = V1MeetingsMeetingIdPutRequestSettings(**settings) if isinstance(settings, (dict, Dict)) else settings
        self.start_time = start_time
        self.subject = subject
        self.time_zone = time_zone
        self.userid = userid


class V1MeetingsMeetingIdPutRequestHostsInner(object):
    """V1MeetingsMeetingIdPutRequestHostsInner

    :param is_anonymous: 用户是否匿名入会，缺省为 false，不匿名。 true：匿名 false：不匿名 
    :type is_anonymous: Optional[bool]

    :param nick_name: 用户匿名字符串。如果字段“is_anonymous”设置为“true”，但是无指定匿名字符串, 会议将分配缺省名称，例如 “会议用户xxxx”，其中“xxxx”为随机数字。 
    :type nick_name: Optional[str]

    :param userid: 用户 ID（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId）。  企业唯一用户标识说明：  企业对接 SSO 时使用的员工唯一标识 ID，企业调用创建用户接口时传递的 userid 参数。 (required) 
    :type userid: str
    """  # noqa: E501

    is_anonymous: Optional[bool] = None
    nick_name: Optional[str] = None
    userid: str
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        userid: str,
        is_anonymous: Optional[bool] = None,
        nick_name: Optional[str] = None,
        **kwargs
    ):
        self.is_anonymous = is_anonymous
        self.nick_name = nick_name
        self.userid = userid


class V1MeetingsMeetingIdPutRequestLiveConfig(object):
    """直播配置对象，enable_live 为 true 时才生效。

    :param enable_live_im: 允许观众讨论。 true：开启 false：不开启 
    :type enable_live_im: Optional[bool]

    :param enable_live_password: 是否开启直播密码，默认值false.  true：开启, false：不开启 
    :type enable_live_password: Optional[bool]

    :param enable_live_replay: 开启直播回看。 true：开启 false：不开启 
    :type enable_live_replay: Optional[bool]

    :param live_password: 直播密码。当设置开启直播密码时，该参数必填。 
    :type live_password: Optional[str]

    :param live_subject: 直播主题 
    :type live_subject: Optional[str]

    :param live_summary: 直播简介 
    :type live_summary: Optional[str]

    :param live_watermark:
    :type live_watermark: Optional[V1MeetingsMeetingIdPutRequestLiveConfigLiveWatermark]
    """  # noqa: E501

    enable_live_im: Optional[bool] = None
    enable_live_password: Optional[bool] = None
    enable_live_replay: Optional[bool] = None
    live_password: Optional[str] = None
    live_subject: Optional[str] = None
    live_summary: Optional[str] = None
    live_watermark: Optional[V1MeetingsMeetingIdPutRequestLiveConfigLiveWatermark] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        enable_live_im: Optional[bool] = None,
        enable_live_password: Optional[bool] = None,
        enable_live_replay: Optional[bool] = None,
        live_password: Optional[str] = None,
        live_subject: Optional[str] = None,
        live_summary: Optional[str] = None,
        live_watermark: Optional[V1MeetingsMeetingIdPutRequestLiveConfigLiveWatermark | Dict[str, Any]] = None,
        **kwargs
    ):
        self.enable_live_im = enable_live_im
        self.enable_live_password = enable_live_password
        self.enable_live_replay = enable_live_replay
        self.live_password = live_password
        self.live_subject = live_subject
        self.live_summary = live_summary
        self.live_watermark = V1MeetingsMeetingIdPutRequestLiveConfigLiveWatermark(**live_watermark) if isinstance(live_watermark, (dict, Dict)) else live_watermark


class V1MeetingsMeetingIdPutRequestLiveConfigLiveWatermark(object):
    """直播水印对象信息

    :param watermark_opt: 水印选项，默认为0。 0：默认水印  1：无水印 
    :type watermark_opt: Optional[int]
    """  # noqa: E501

    watermark_opt: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        watermark_opt: Optional[int] = None,
        **kwargs
    ):
        self.watermark_opt = watermark_opt


class V1MeetingsMeetingIdPutRequestRecurringRule(object):
    """周期性会议配置，meeting_type 为1时必填。

    :param customized_recurring_days: 哪些天重复。根据 customized_recurring_type 和 customized_recurring_step 的不同，该字段可取值与表达含义不同。如需选择多个日期，加和即可。 customized_recurring_type = 0 时，传入该字段将被忽略。 详细请参见 自定义周期规则 API 调用示例 
    :type customized_recurring_days: Optional[int]

    :param customized_recurring_step: 每[n]（天、周、月）重复，使用自定义周期性会议时传入。 例如：customized_recurring_type=0 && customized_recurring_step=5 表示每5天重复一次。 customized_recurring_type=2 && customized_recurring_step=3 表示每3个月重复一次，重复的时间依赖于 customized_recurring_days 字段。 
    :type customized_recurring_step: Optional[int]

    :param customized_recurring_type: 自定义周期性会议的循环类型。 0：按天。 1：按周。 2：按月，以周为粒度重复。例如：每3个月的第二周的周四。 3：按月，以日期为粒度重复。例如：每3个月的16日。 按周；按月、以周为粒度； 按月、以日期为粒度时，需要包含会议开始时间所在的日期。 
    :type customized_recurring_type: Optional[int]

    :param recurring_type: 重复类型，默认值为0。 0：每天 1：每周一至周五 2：每周 3：每两周 4：每月 5：自定义，示例请参见 自定义周期规则 API 调用示例 
    :type recurring_type: Optional[int]

    :param sub_meeting_id: 子会议 ID，表示修改该子会议时间，不可与周期性会议规则同时修改。 如不填写，默认修改整个周期性会议时间。 
    :type sub_meeting_id: Optional[str]

    :param until_count: 限定会议次数（1-50次）。 
    :type until_count: Optional[int]

    :param until_date: 结束日期时间戳，最大支持预定50场子会议。 
    :type until_date: Optional[int]

    :param until_type: 结束重复类型。 0：按日期结束重复 1：按次数结束重复 
    :type until_type: Optional[int]
    """  # noqa: E501

    customized_recurring_days: Optional[int] = None
    customized_recurring_step: Optional[int] = None
    customized_recurring_type: Optional[int] = None
    recurring_type: Optional[int] = None
    sub_meeting_id: Optional[str] = None
    until_count: Optional[int] = None
    until_date: Optional[int] = None
    until_type: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        customized_recurring_days: Optional[int] = None,
        customized_recurring_step: Optional[int] = None,
        customized_recurring_type: Optional[int] = None,
        recurring_type: Optional[int] = None,
        sub_meeting_id: Optional[str] = None,
        until_count: Optional[int] = None,
        until_date: Optional[int] = None,
        until_type: Optional[int] = None,
        **kwargs
    ):
        self.customized_recurring_days = customized_recurring_days
        self.customized_recurring_step = customized_recurring_step
        self.customized_recurring_type = customized_recurring_type
        self.recurring_type = recurring_type
        self.sub_meeting_id = sub_meeting_id
        self.until_count = until_count
        self.until_date = until_date
        self.until_type = until_type


class V1MeetingsMeetingIdPutRequestSettings(object):
    """会议的配置，可为缺省配置。

    :param allow_in_before_host: 允许成员在主持人进会前加入会议，默认值为 true。 true：允许 false：不允许 
    :type allow_in_before_host: Optional[bool]

    :param allow_multi_device: 是否允许多端入会 
    :type allow_multi_device: Optional[bool]

    :param allow_screen_shared_watermark: 是否开启屏幕共享水印，默认值为 false。 true：开启 false：不开启 
    :type allow_screen_shared_watermark: Optional[bool]

    :param allow_unmute_self: 允许参会者取消静音，默认值为 true。 true：开启 false：关闭 
    :type allow_unmute_self: Optional[bool]

    :param auto_in_waiting_room: 是否开启等候室，默认值为 false。 true：开启 false：不开启 
    :type auto_in_waiting_room: Optional[bool]

    :param auto_record_type: 自动录制类型： none：禁用，代表不开启自动会议录制。 local：本地录制，代表主持人入会后自动开启本地录制。 cloud：云录制，代表主持人入会后自动开启云录制。 说明： 该参数依赖企业账户设置，当企业强制锁定后，该参数必须与企业配置保持一致。 仅客户端2.7及以上版本可生效。 
    :type auto_record_type: Optional[str]

    :param change_nickname: 是否允许用户自己改名 1:允许用户自己改名，2:不允许用户自己改名，默认为1 
    :type change_nickname: Optional[int]

    :param enable_host_pause_auto_record: 允许主持人暂停或者停止云录制，默认值为 true 开启，开启时，主持人允许暂停和停止云录制；当设置为关闭时，则主持人不允许暂停和关闭云录制。 说明： 该参数必须将 auto_record_type 设置为“cloud”时才生效，该参数依赖企业账户设置，当企业强制锁定后，该参数必须与企业配置保持一致。 仅客户端2.7及以上版本生效。 
    :type enable_host_pause_auto_record: Optional[bool]

    :param mute_enable_join: 入会时静音 
    :type mute_enable_join: Optional[bool]

    :param mute_enable_type_join: 成员入会时静音选项，默认值为2。 当同时传入“mute_enable_join”和“mute_enable_type_join”时，将以“mute_enable_type_join”的选项为准。 0：关闭 1：开启 2：超过6人后自动开启 
    :type mute_enable_type_join: Optional[int]

    :param only_enterprise_user_allowed: 是否仅企业内部成员可入会，默认值为 false。 true：仅企业内部用户可入会 false：所有人可入会 
    :type only_enterprise_user_allowed: Optional[bool]

    :param only_invitees_allowed: 是否仅受邀成员可入会，默认值为false，true：仅受邀成员可入会，false：所有成员可入会 
    :type only_invitees_allowed: Optional[bool]

    :param participant_join_auto_record: 当有参会成员入会时立即开启云录制，默认值为 false 关闭，关闭时，主持人入会自动开启云录制；当设置为开启时，则有参会成员入会自动开启云录制。 说明： 该参数必须 auto_record_type 设置为“cloud”时才生效，该参数依赖企业账户设置，当企业强制锁定后，该参数必须与企业配置保持一致。 仅客户端2.7及以上版本生效。 
    :type participant_join_auto_record: Optional[bool]

    :param play_ivr_on_join: 有新的与会者加入时播放提示音 
    :type play_ivr_on_join: Optional[bool]

    :param play_ivr_on_leave: 参会者离开时播放提示音。 
    :type play_ivr_on_leave: Optional[bool]

    :param water_mark_type: 水印样式，默认为单排。当屏幕共享水印参数为开启时，此参数才生效。 0：单排 1：多排 
    :type water_mark_type: Optional[int]
    """  # noqa: E501

    allow_in_before_host: Optional[bool] = None
    allow_multi_device: Optional[bool] = None
    allow_screen_shared_watermark: Optional[bool] = None
    allow_unmute_self: Optional[bool] = None
    auto_in_waiting_room: Optional[bool] = None
    auto_record_type: Optional[str] = None
    change_nickname: Optional[int] = None
    enable_host_pause_auto_record: Optional[bool] = None
    mute_enable_join: Optional[bool] = None
    mute_enable_type_join: Optional[int] = None
    only_enterprise_user_allowed: Optional[bool] = None
    only_invitees_allowed: Optional[bool] = None
    participant_join_auto_record: Optional[bool] = None
    play_ivr_on_join: Optional[bool] = None
    play_ivr_on_leave: Optional[bool] = None
    water_mark_type: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        allow_in_before_host: Optional[bool] = None,
        allow_multi_device: Optional[bool] = None,
        allow_screen_shared_watermark: Optional[bool] = None,
        allow_unmute_self: Optional[bool] = None,
        auto_in_waiting_room: Optional[bool] = None,
        auto_record_type: Optional[str] = None,
        change_nickname: Optional[int] = None,
        enable_host_pause_auto_record: Optional[bool] = None,
        mute_enable_join: Optional[bool] = None,
        mute_enable_type_join: Optional[int] = None,
        only_enterprise_user_allowed: Optional[bool] = None,
        only_invitees_allowed: Optional[bool] = None,
        participant_join_auto_record: Optional[bool] = None,
        play_ivr_on_join: Optional[bool] = None,
        play_ivr_on_leave: Optional[bool] = None,
        water_mark_type: Optional[int] = None,
        **kwargs
    ):
        self.allow_in_before_host = allow_in_before_host
        self.allow_multi_device = allow_multi_device
        self.allow_screen_shared_watermark = allow_screen_shared_watermark
        self.allow_unmute_self = allow_unmute_self
        self.auto_in_waiting_room = auto_in_waiting_room
        self.auto_record_type = auto_record_type
        self.change_nickname = change_nickname
        self.enable_host_pause_auto_record = enable_host_pause_auto_record
        self.mute_enable_join = mute_enable_join
        self.mute_enable_type_join = mute_enable_type_join
        self.only_enterprise_user_allowed = only_enterprise_user_allowed
        self.only_invitees_allowed = only_invitees_allowed
        self.participant_join_auto_record = participant_join_auto_record
        self.play_ivr_on_join = play_ivr_on_join
        self.play_ivr_on_leave = play_ivr_on_leave
        self.water_mark_type = water_mark_type


class V1MeetingsMeetingIdQosGet200Response(object):
    """V1MeetingsMeetingIdQosGet200Response

    :param current_page: 当前页码 
    :type current_page: Optional[int]

    :param current_size: 当前页大小 
    :type current_size: Optional[int]

    :param participants: 成员列表 
    :type participants: Optional[List[V1MeetingsMeetingIdQosGet200ResponseParticipantsInner]]

    :param total_count: 数据总条数 
    :type total_count: Optional[int]

    :param total_page: 总页数 
    :type total_page: Optional[int]
    """  # noqa: E501

    current_page: Optional[int] = None
    current_size: Optional[int] = None
    participants: Optional[List[V1MeetingsMeetingIdQosGet200ResponseParticipantsInner]] = None
    total_count: Optional[int] = None
    total_page: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        current_page: Optional[int] = None,
        current_size: Optional[int] = None,
        participants: Optional[List[V1MeetingsMeetingIdQosGet200ResponseParticipantsInner] | List[Dict[str, Any]]] = None,
        total_count: Optional[int] = None,
        total_page: Optional[int] = None,
        **kwargs
    ):
        self.current_page = current_page
        self.current_size = current_size
        
        if participants and isinstance(participants, (list, List)):
            self.participants = [V1MeetingsMeetingIdQosGet200ResponseParticipantsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in participants]
        
        self.total_count = total_count
        self.total_page = total_page


class V1MeetingsMeetingIdQosGet200ResponseParticipantsInner(object):
    """V1MeetingsMeetingIdQosGet200ResponseParticipantsInner

    :param ms_open_id: 会中ID 
    :type ms_open_id: Optional[str]

    :param nick_name: 会中用户名 
    :type nick_name: Optional[str]

    :param qos_details:
    :type qos_details: Optional[List[V1MeetingsMeetingIdQosGet200ResponseParticipantsInnerQosDetailsInner]]
    """  # noqa: E501

    ms_open_id: Optional[str] = None
    nick_name: Optional[str] = None
    qos_details: Optional[List[V1MeetingsMeetingIdQosGet200ResponseParticipantsInnerQosDetailsInner]] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        ms_open_id: Optional[str] = None,
        nick_name: Optional[str] = None,
        qos_details: Optional[List[V1MeetingsMeetingIdQosGet200ResponseParticipantsInnerQosDetailsInner] | List[Dict[str, Any]]] = None,
        **kwargs
    ):
        self.ms_open_id = ms_open_id
        self.nick_name = nick_name
        
        if qos_details and isinstance(qos_details, (list, List)):
            self.qos_details = [V1MeetingsMeetingIdQosGet200ResponseParticipantsInnerQosDetailsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in qos_details]
        


class V1MeetingsMeetingIdQosGet200ResponseParticipantsInnerQosDetailsInner(object):
    """V1MeetingsMeetingIdQosGet200ResponseParticipantsInnerQosDetailsInner

    :param audio:
    :type audio: Optional[V1MeetingsMeetingIdQosGet200ResponseParticipantsInnerQosDetailsInnerAudio]

    :param instanceid: 设备类型 
    :type instanceid: Optional[int]

    :param network:
    :type network: Optional[V1MeetingsMeetingIdQosGet200ResponseParticipantsInnerQosDetailsInnerNetwork]

    :param share_screen:
    :type share_screen: Optional[V1MeetingsMeetingIdQosGet200ResponseParticipantsInnerQosDetailsInnerShareScreen]

    :param video:
    :type video: Optional[V1MeetingsMeetingIdQosGet200ResponseParticipantsInnerQosDetailsInnerVideo]
    """  # noqa: E501

    audio: Optional[V1MeetingsMeetingIdQosGet200ResponseParticipantsInnerQosDetailsInnerAudio] = None
    instanceid: Optional[int] = None
    network: Optional[V1MeetingsMeetingIdQosGet200ResponseParticipantsInnerQosDetailsInnerNetwork] = None
    share_screen: Optional[V1MeetingsMeetingIdQosGet200ResponseParticipantsInnerQosDetailsInnerShareScreen] = None
    video: Optional[V1MeetingsMeetingIdQosGet200ResponseParticipantsInnerQosDetailsInnerVideo] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        audio: Optional[V1MeetingsMeetingIdQosGet200ResponseParticipantsInnerQosDetailsInnerAudio | Dict[str, Any]] = None,
        instanceid: Optional[int] = None,
        network: Optional[V1MeetingsMeetingIdQosGet200ResponseParticipantsInnerQosDetailsInnerNetwork | Dict[str, Any]] = None,
        share_screen: Optional[V1MeetingsMeetingIdQosGet200ResponseParticipantsInnerQosDetailsInnerShareScreen | Dict[str, Any]] = None,
        video: Optional[V1MeetingsMeetingIdQosGet200ResponseParticipantsInnerQosDetailsInnerVideo | Dict[str, Any]] = None,
        **kwargs
    ):
        self.audio = V1MeetingsMeetingIdQosGet200ResponseParticipantsInnerQosDetailsInnerAudio(**audio) if isinstance(audio, (dict, Dict)) else audio
        self.instanceid = instanceid
        self.network = V1MeetingsMeetingIdQosGet200ResponseParticipantsInnerQosDetailsInnerNetwork(**network) if isinstance(network, (dict, Dict)) else network
        self.share_screen = V1MeetingsMeetingIdQosGet200ResponseParticipantsInnerQosDetailsInnerShareScreen(**share_screen) if isinstance(share_screen, (dict, Dict)) else share_screen
        self.video = V1MeetingsMeetingIdQosGet200ResponseParticipantsInnerQosDetailsInnerVideo(**video) if isinstance(video, (dict, Dict)) else video


class V1MeetingsMeetingIdQosGet200ResponseParticipantsInnerQosDetailsInnerAudio(object):
    """音频

    :param downstream_bitrate: 下行码率（kbps） 
    :type downstream_bitrate: Optional[str]

    :param loudspeaker_volume: 扬声器播放音量（db） 
    :type loudspeaker_volume: Optional[str]

    :param mic_volume: 麦克风采集音量（db） 
    :type mic_volume: Optional[str]

    :param upstream_bitrate: 上行码率（kbps） 
    :type upstream_bitrate: Optional[str]
    """  # noqa: E501

    downstream_bitrate: Optional[str] = None
    loudspeaker_volume: Optional[str] = None
    mic_volume: Optional[str] = None
    upstream_bitrate: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        downstream_bitrate: Optional[str] = None,
        loudspeaker_volume: Optional[str] = None,
        mic_volume: Optional[str] = None,
        upstream_bitrate: Optional[str] = None,
        **kwargs
    ):
        self.downstream_bitrate = downstream_bitrate
        self.loudspeaker_volume = loudspeaker_volume
        self.mic_volume = mic_volume
        self.upstream_bitrate = upstream_bitrate


class V1MeetingsMeetingIdQosGet200ResponseParticipantsInnerQosDetailsInnerNetwork(object):
    """网络

    :param downstream_bindwidth: 下行带宽（kbps） 
    :type downstream_bindwidth: Optional[str]

    :param downstream_packet_loss: 下行丢包（%） 
    :type downstream_packet_loss: Optional[str]

    :param network_delay: 网络延迟 (ms) 
    :type network_delay: Optional[str]

    :param upstream_bindwidth: 上行带宽（kbps） 
    :type upstream_bindwidth: Optional[str]

    :param upstream_packet_loss: 上行丢包（%） 
    :type upstream_packet_loss: Optional[str]
    """  # noqa: E501

    downstream_bindwidth: Optional[str] = None
    downstream_packet_loss: Optional[str] = None
    network_delay: Optional[str] = None
    upstream_bindwidth: Optional[str] = None
    upstream_packet_loss: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        downstream_bindwidth: Optional[str] = None,
        downstream_packet_loss: Optional[str] = None,
        network_delay: Optional[str] = None,
        upstream_bindwidth: Optional[str] = None,
        upstream_packet_loss: Optional[str] = None,
        **kwargs
    ):
        self.downstream_bindwidth = downstream_bindwidth
        self.downstream_packet_loss = downstream_packet_loss
        self.network_delay = network_delay
        self.upstream_bindwidth = upstream_bindwidth
        self.upstream_packet_loss = upstream_packet_loss


class V1MeetingsMeetingIdQosGet200ResponseParticipantsInnerQosDetailsInnerShareScreen(object):
    """共享屏幕

    :param downstream_bitrate: 下行码率（kbps） 
    :type downstream_bitrate: Optional[str]

    :param downstream_framerate: 下行帧率（fps） 
    :type downstream_framerate: Optional[str]

    :param downstream_resolution: 下行分辨率 
    :type downstream_resolution: Optional[str]

    :param upstream_bitrate: 上行码率（kbps） 
    :type upstream_bitrate: Optional[str]

    :param upstream_framerate: 上行帧率（fps） 
    :type upstream_framerate: Optional[str]

    :param upstream_resolution: 上行分辨率 
    :type upstream_resolution: Optional[str]
    """  # noqa: E501

    downstream_bitrate: Optional[str] = None
    downstream_framerate: Optional[str] = None
    downstream_resolution: Optional[str] = None
    upstream_bitrate: Optional[str] = None
    upstream_framerate: Optional[str] = None
    upstream_resolution: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        downstream_bitrate: Optional[str] = None,
        downstream_framerate: Optional[str] = None,
        downstream_resolution: Optional[str] = None,
        upstream_bitrate: Optional[str] = None,
        upstream_framerate: Optional[str] = None,
        upstream_resolution: Optional[str] = None,
        **kwargs
    ):
        self.downstream_bitrate = downstream_bitrate
        self.downstream_framerate = downstream_framerate
        self.downstream_resolution = downstream_resolution
        self.upstream_bitrate = upstream_bitrate
        self.upstream_framerate = upstream_framerate
        self.upstream_resolution = upstream_resolution


class V1MeetingsMeetingIdQosGet200ResponseParticipantsInnerQosDetailsInnerVideo(object):
    """视频

    :param downstream_bitrate: 下行码率（kbps） 
    :type downstream_bitrate: Optional[str]

    :param downstream_framerate: 下行帧率（fps） 
    :type downstream_framerate: Optional[str]

    :param downstream_resolution: 下行分辨率 
    :type downstream_resolution: Optional[str]

    :param upstream_bitrate: 上行码率（kbps） 
    :type upstream_bitrate: Optional[str]

    :param upstream_framerate: 上行帧率（fps） 
    :type upstream_framerate: Optional[str]

    :param upstream_resolution: 上行分辨率 
    :type upstream_resolution: Optional[str]
    """  # noqa: E501

    downstream_bitrate: Optional[str] = None
    downstream_framerate: Optional[str] = None
    downstream_resolution: Optional[str] = None
    upstream_bitrate: Optional[str] = None
    upstream_framerate: Optional[str] = None
    upstream_resolution: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        downstream_bitrate: Optional[str] = None,
        downstream_framerate: Optional[str] = None,
        downstream_resolution: Optional[str] = None,
        upstream_bitrate: Optional[str] = None,
        upstream_framerate: Optional[str] = None,
        upstream_resolution: Optional[str] = None,
        **kwargs
    ):
        self.downstream_bitrate = downstream_bitrate
        self.downstream_framerate = downstream_framerate
        self.downstream_resolution = downstream_resolution
        self.upstream_bitrate = upstream_bitrate
        self.upstream_framerate = upstream_framerate
        self.upstream_resolution = upstream_resolution


class V1MeetingsMeetingIdQualityGet200Response(object):
    """V1MeetingsMeetingIdQualityGet200Response

    :param audio_quality: 音频质量：0-无数据，1-好、2-较好、3-中、4-差 
    :type audio_quality: Optional[int]

    :param current_page: 分页查询返回当前页码 
    :type current_page: Optional[int]

    :param current_size: 分页查询返回单页数据条数  
    :type current_size: Optional[int]

    :param meeting_id: 会议的唯一 ID 
    :type meeting_id: Optional[str]

    :param network_quality: 网络质量：0-无数据，1-好、2-较好、3-中、4-差 
    :type network_quality: Optional[int]

    :param participants: 参会人员健康度对象数组（按成员入会时间正序排列，入会越早的在越上面；成员使用不同端入会时平铺返回数据，instanceid不同） 
    :type participants: Optional[List[V1MeetingsMeetingIdQualityGet200ResponseParticipantsInner]]

    :param problems: 告警的具体问题 
    :type problems: Optional[List[str]]

    :param quality: 健康度：0-无数据，1-健康、2-告警 
    :type quality: Optional[int]

    :param screen_share_quality: 共享屏幕质量：0-无数据，1-好、2-较好、3-中、4-差 
    :type screen_share_quality: Optional[int]

    :param total_count: 分页查询返回数据总数 
    :type total_count: Optional[int]

    :param total_page: 分页查询返回分页总数 
    :type total_page: Optional[int]

    :param video_quality: 视频质量：0-无数据，1-好、2-较好、3-中、4-差 
    :type video_quality: Optional[int]
    """  # noqa: E501

    audio_quality: Optional[int] = None
    current_page: Optional[int] = None
    current_size: Optional[int] = None
    meeting_id: Optional[str] = None
    network_quality: Optional[int] = None
    participants: Optional[List[V1MeetingsMeetingIdQualityGet200ResponseParticipantsInner]] = None
    problems: Optional[List[str]] = None
    quality: Optional[int] = None
    screen_share_quality: Optional[int] = None
    total_count: Optional[int] = None
    total_page: Optional[int] = None
    video_quality: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        audio_quality: Optional[int] = None,
        current_page: Optional[int] = None,
        current_size: Optional[int] = None,
        meeting_id: Optional[str] = None,
        network_quality: Optional[int] = None,
        participants: Optional[List[V1MeetingsMeetingIdQualityGet200ResponseParticipantsInner] | List[Dict[str, Any]]] = None,
        problems: Optional[List[str]] = None,
        quality: Optional[int] = None,
        screen_share_quality: Optional[int] = None,
        total_count: Optional[int] = None,
        total_page: Optional[int] = None,
        video_quality: Optional[int] = None,
        **kwargs
    ):
        self.audio_quality = audio_quality
        self.current_page = current_page
        self.current_size = current_size
        self.meeting_id = meeting_id
        self.network_quality = network_quality
        
        if participants and isinstance(participants, (list, List)):
            self.participants = [V1MeetingsMeetingIdQualityGet200ResponseParticipantsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in participants]
        
        
        if problems and isinstance(problems, (list, List)):
            self.problems = problems
        
        self.quality = quality
        self.screen_share_quality = screen_share_quality
        self.total_count = total_count
        self.total_page = total_page
        self.video_quality = video_quality


class V1MeetingsMeetingIdQualityGet200ResponseParticipantsInner(object):
    """V1MeetingsMeetingIdQualityGet200ResponseParticipantsInner

    :param audio_quality: 音频质量：0-无数据，1-好、2-较好、3-中、4-差 
    :type audio_quality: Optional[int]

    :param instanceid: 用户的终端设备类型： 0：PSTN 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch MacOS 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch iOS 
    :type instanceid: Optional[str]

    :param ms_open_id: 当场会议的用户临时 ID，可用于会控操作，适用于所有用户。  
    :type ms_open_id: Optional[str]

    :param network_quality: 网络质量：0-无数据，1-好、2-较好、3-中、4-差 
    :type network_quality: Optional[int]

    :param open_id: OAuth2.0 鉴权用户请使用 open_id。 
    :type open_id: Optional[str]

    :param problems: 告警的具体问题 
    :type problems: Optional[List[str]]

    :param quality: 用户健康度：0-无数据，1-健康、2-告警 
    :type quality: Optional[int]

    :param screen_share_quality: 共享屏幕质量：0-无数据，1-好、2-较好、3-中、4-差 
    :type screen_share_quality: Optional[int]

    :param userid: 同企业内部请使用企业唯一用户标识； 其他企业，个人，小程序没有 。 
    :type userid: Optional[str]

    :param video_quality: 视频质量：0-无数据，1-好、2-较好、3-中、4-差 
    :type video_quality: Optional[int]
    """  # noqa: E501

    audio_quality: Optional[int] = None
    instanceid: Optional[str] = None
    ms_open_id: Optional[str] = None
    network_quality: Optional[int] = None
    open_id: Optional[str] = None
    problems: Optional[List[str]] = None
    quality: Optional[int] = None
    screen_share_quality: Optional[int] = None
    userid: Optional[str] = None
    video_quality: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        audio_quality: Optional[int] = None,
        instanceid: Optional[str] = None,
        ms_open_id: Optional[str] = None,
        network_quality: Optional[int] = None,
        open_id: Optional[str] = None,
        problems: Optional[List[str]] = None,
        quality: Optional[int] = None,
        screen_share_quality: Optional[int] = None,
        userid: Optional[str] = None,
        video_quality: Optional[int] = None,
        **kwargs
    ):
        self.audio_quality = audio_quality
        self.instanceid = instanceid
        self.ms_open_id = ms_open_id
        self.network_quality = network_quality
        self.open_id = open_id
        
        if problems and isinstance(problems, (list, List)):
            self.problems = problems
        
        self.quality = quality
        self.screen_share_quality = screen_share_quality
        self.userid = userid
        self.video_quality = video_quality


class V1MeetingsMeetingIdRealTimeParticipantsGet200Response(object):
    """V1MeetingsMeetingIdRealTimeParticipantsGet200Response

    :param current_page: 当前页。 
    :type current_page: Optional[int]

    :param current_size: 当前页实际大小。 
    :type current_size: Optional[int]

    :param meeting_code: 会议号码。 
    :type meeting_code: Optional[str]

    :param meeting_id: 会议的唯一 ID。 
    :type meeting_id: Optional[str]

    :param participants: 参会人员对象数组。 
    :type participants: Optional[List[V1MeetingsMeetingIdRealTimeParticipantsGet200ResponseParticipantsInner]]

    :param schedule_end_time: 预定会议结束时间戳（单位秒）。 
    :type schedule_end_time: Optional[str]

    :param schedule_start_time: 预定会议开始时间戳（单位秒）。 
    :type schedule_start_time: Optional[str]

    :param status: 当前会议状态： 1. MEETING_STATE_INVALID： 非法或未知的会议状态，错误状态。 2. MEETING_STATE_INIT： 会议待开始。会议预定到预定结束时间前，会议尚无人进会。 3. MEETING_STATE_CANCELLED： 会议已取消。主持人主动取消会议，待开始的会议才能取消，且取消的会议无法再进入。 4. MEETING_STATE_STARTED： 会议已开始。会议中有人则表示会议进行中。 5. MEETING_STATE_ENDED： 会议已删除。会议已过预定结束时间且尚无人进会时，主持人删除会议，已删除的会议无法再进入。 6. MEETING_STATE_NULL： 会议无状态。会议已过预定结束时间，会议尚无人进会。 7. MEETING_STATE_RECYCLED： 会议已回收。会议已过预定开始时间30天，则会议号将被后台回收，无法再进入。 
    :type status: Optional[str]

    :param subject: 会议主题（base64）。 
    :type subject: Optional[str]

    :param total_count: 根据条件筛选后的总人数。 
    :type total_count: Optional[int]

    :param total_page: 根据条件筛选后的总分页数 
    :type total_page: Optional[int]
    """  # noqa: E501

    current_page: Optional[int] = None
    current_size: Optional[int] = None
    meeting_code: Optional[str] = None
    meeting_id: Optional[str] = None
    participants: Optional[List[V1MeetingsMeetingIdRealTimeParticipantsGet200ResponseParticipantsInner]] = None
    schedule_end_time: Optional[str] = None
    schedule_start_time: Optional[str] = None
    status: Optional[str] = None
    subject: Optional[str] = None
    total_count: Optional[int] = None
    total_page: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        current_page: Optional[int] = None,
        current_size: Optional[int] = None,
        meeting_code: Optional[str] = None,
        meeting_id: Optional[str] = None,
        participants: Optional[List[V1MeetingsMeetingIdRealTimeParticipantsGet200ResponseParticipantsInner] | List[Dict[str, Any]]] = None,
        schedule_end_time: Optional[str] = None,
        schedule_start_time: Optional[str] = None,
        status: Optional[str] = None,
        subject: Optional[str] = None,
        total_count: Optional[int] = None,
        total_page: Optional[int] = None,
        **kwargs
    ):
        self.current_page = current_page
        self.current_size = current_size
        self.meeting_code = meeting_code
        self.meeting_id = meeting_id
        
        if participants and isinstance(participants, (list, List)):
            self.participants = [V1MeetingsMeetingIdRealTimeParticipantsGet200ResponseParticipantsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in participants]
        
        self.schedule_end_time = schedule_end_time
        self.schedule_start_time = schedule_start_time
        self.status = status
        self.subject = subject
        self.total_count = total_count
        self.total_page = total_page


class V1MeetingsMeetingIdRealTimeParticipantsGet200ResponseParticipantsInner(object):
    """V1MeetingsMeetingIdRealTimeParticipantsGet200ResponseParticipantsInner

    :param app_version: 用户的客户端版本。当用户在会中时才能返回。 
    :type app_version: Optional[str]

    :param audio_state: 麦克风状态： true：开启 false：关闭 
    :type audio_state: Optional[bool]

    :param customer_data:
    :type customer_data: Optional[str]

    :param instanceid: 用户的终端设备类型： 0:pstn或mra 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 
    :type instanceid: Optional[int]

    :param join_time: 参会者加入会议时间戳（单位秒）。 
    :type join_time: Optional[str]

    :param join_type: 入会方式： 0：PSTN 普通用户，标准的手机或固话类型 1：普通 VOIP 用户 2：附属投屏 VOIP 3：linux sdk for VOIP 4：附属语音 PSTN 5：附属视频 PSTN 6：linux sdk for PSTN 
    :type join_type: Optional[int]

    :param ms_open_id: 当场会议的用户临时 ID，可用于会控操作，适用于所有用户。 
    :type ms_open_id: Optional[str]

    :param open_id: OAuth2.0 鉴权用户请使用 open_id 
    :type open_id: Optional[str]

    :param screen_shared_state: 屏幕共享状态： true：开启 false：关闭 
    :type screen_shared_state: Optional[bool]

    :param user_name: 入会用户名（base64）。 
    :type user_name: Optional[str]

    :param user_role: 用户角色： 0：普通成员角色 1：创建者角色 2：主持人 3：创建者+主持人 4：游客 5：游客+主持人 6：联席主持人 7：创建者+联席主持人 
    :type user_role: Optional[int]

    :param userid: 同企业内部请使用企业唯一用户标识； 其他企业，个人，小程序没有 
    :type userid: Optional[str]

    :param video_state: 摄像头状态： true：开启 false：关闭 
    :type video_state: Optional[bool]
    """  # noqa: E501

    app_version: Optional[str] = None
    audio_state: Optional[bool] = None
    customer_data: Optional[str] = None
    instanceid: Optional[int] = None
    join_time: Optional[str] = None
    join_type: Optional[int] = None
    ms_open_id: Optional[str] = None
    open_id: Optional[str] = None
    screen_shared_state: Optional[bool] = None
    user_name: Optional[str] = None
    user_role: Optional[int] = None
    userid: Optional[str] = None
    video_state: Optional[bool] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        app_version: Optional[str] = None,
        audio_state: Optional[bool] = None,
        customer_data: Optional[str] = None,
        instanceid: Optional[int] = None,
        join_time: Optional[str] = None,
        join_type: Optional[int] = None,
        ms_open_id: Optional[str] = None,
        open_id: Optional[str] = None,
        screen_shared_state: Optional[bool] = None,
        user_name: Optional[str] = None,
        user_role: Optional[int] = None,
        userid: Optional[str] = None,
        video_state: Optional[bool] = None,
        **kwargs
    ):
        self.app_version = app_version
        self.audio_state = audio_state
        self.customer_data = customer_data
        self.instanceid = instanceid
        self.join_time = join_time
        self.join_type = join_type
        self.ms_open_id = ms_open_id
        self.open_id = open_id
        self.screen_shared_state = screen_shared_state
        self.user_name = user_name
        self.user_role = user_role
        self.userid = userid
        self.video_state = video_state


class V1MeetingsMeetingIdVirtualBackgroundPost200Response(object):
    """V1MeetingsMeetingIdVirtualBackgroundPost200Response

    :param job_id: 任务ID 
    :type job_id: Optional[str]
    """  # noqa: E501

    job_id: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        job_id: Optional[str] = None,
        **kwargs
    ):
        self.job_id = job_id


class V1MeetingsMeetingIdVirtualBackgroundPostRequest(object):
    """V1MeetingsMeetingIdVirtualBackgroundPostRequest

    :param image: 背景图片 url，尺寸大小为1920*1080，小于10M，jpg/png/jpeg 格式如果不传入则使用会议室默认虚拟背景。 
    :type image: Optional[str]

    :param instanceid: 用户的终端设备类型： 0：PSTN 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：Linux 20：Rooms for Touch Windows 21：Rooms for Touch MacOS 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch iOS (required) 
    :type instanceid: int

    :param operator_id: 操作者ID (required) 
    :type operator_id: str

    :param operator_id_type: 操作者ID类型。1-userid，2-opened (required) 
    :type operator_id_type: int

    :param type: 背景生效类型。0-全部用户，1-部分用户 (required) 
    :type type: int

    :param users: userid数组 
    :type users: Optional[List[str]]
    """  # noqa: E501

    image: Optional[str] = None
    instanceid: int
    operator_id: str
    operator_id_type: int
    type: int
    users: Optional[List[str]] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        instanceid: int,
        operator_id: str,
        operator_id_type: int,
        type: int,
        image: Optional[str] = None,
        users: Optional[List[str]] = None,
        **kwargs
    ):
        self.image = image
        self.instanceid = instanceid
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.type = type
        
        if users and isinstance(users, (list, List)):
            self.users = users
        


class V1MeetingsMeetingIdWaitingRoomParticipantsGet200Response(object):
    """V1MeetingsMeetingIdWaitingRoomParticipantsGet200Response

    :param current_page: 分页查询返回当前页码 
    :type current_page: Optional[int]

    :param current_size: 分页查询返回单页数据条数 
    :type current_size: Optional[int]

    :param meeting_code: 会议CODE 
    :type meeting_code: Optional[str]

    :param meeting_id: 会议唯一 ID 
    :type meeting_id: Optional[str]

    :param participants: 等候室人员对象数组 
    :type participants: Optional[List[V1MeetingsMeetingIdWaitingRoomParticipantsGet200ResponseParticipantsInner]]

    :param schedule_end_time: 预定的会议结束时间戳（单位秒） 
    :type schedule_end_time: Optional[int]

    :param schedule_start_time: 预定的会议开始时间戳（单位秒） 
    :type schedule_start_time: Optional[int]

    :param subject: 会议主题 (base64 编码) 
    :type subject: Optional[str]

    :param total_count: 分页查询返回数据总数 
    :type total_count: Optional[int]

    :param total_page: 分页查询返回分页总数 
    :type total_page: Optional[int]
    """  # noqa: E501

    current_page: Optional[int] = None
    current_size: Optional[int] = None
    meeting_code: Optional[str] = None
    meeting_id: Optional[str] = None
    participants: Optional[List[V1MeetingsMeetingIdWaitingRoomParticipantsGet200ResponseParticipantsInner]] = None
    schedule_end_time: Optional[int] = None
    schedule_start_time: Optional[int] = None
    subject: Optional[str] = None
    total_count: Optional[int] = None
    total_page: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        current_page: Optional[int] = None,
        current_size: Optional[int] = None,
        meeting_code: Optional[str] = None,
        meeting_id: Optional[str] = None,
        participants: Optional[List[V1MeetingsMeetingIdWaitingRoomParticipantsGet200ResponseParticipantsInner] | List[Dict[str, Any]]] = None,
        schedule_end_time: Optional[int] = None,
        schedule_start_time: Optional[int] = None,
        subject: Optional[str] = None,
        total_count: Optional[int] = None,
        total_page: Optional[int] = None,
        **kwargs
    ):
        self.current_page = current_page
        self.current_size = current_size
        self.meeting_code = meeting_code
        self.meeting_id = meeting_id
        
        if participants and isinstance(participants, (list, List)):
            self.participants = [V1MeetingsMeetingIdWaitingRoomParticipantsGet200ResponseParticipantsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in participants]
        
        self.schedule_end_time = schedule_end_time
        self.schedule_start_time = schedule_start_time
        self.subject = subject
        self.total_count = total_count
        self.total_page = total_page


class V1MeetingsMeetingIdWaitingRoomParticipantsGet200ResponseParticipantsInner(object):
    """V1MeetingsMeetingIdWaitingRoomParticipantsGet200ResponseParticipantsInner

    :param app_version: 客户端版本 
    :type app_version: Optional[str]

    :param customer_data: 用户自定义参数 
    :type customer_data: Optional[str]

    :param instanceid: 用户的终端设备类型： 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch Mac 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch Iphone 
    :type instanceid: Optional[int]

    :param ms_open_id: 成员会中唯一 ID。 
    :type ms_open_id: Optional[str]

    :param open_id: 等候室 OAuth2.0 鉴权用户的 ID。 
    :type open_id: Optional[str]

    :param user_name: 入会用户名（base64） 
    :type user_name: Optional[str]

    :param userid: 等候室成员用户 ID 
    :type userid: Optional[str]

    :param uuid: 用户的唯一标识uuid 
    :type uuid: Optional[str]
    """  # noqa: E501

    app_version: Optional[str] = None
    customer_data: Optional[str] = None
    instanceid: Optional[int] = None
    ms_open_id: Optional[str] = None
    open_id: Optional[str] = None
    user_name: Optional[str] = None
    userid: Optional[str] = None
    uuid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        app_version: Optional[str] = None,
        customer_data: Optional[str] = None,
        instanceid: Optional[int] = None,
        ms_open_id: Optional[str] = None,
        open_id: Optional[str] = None,
        user_name: Optional[str] = None,
        userid: Optional[str] = None,
        uuid: Optional[str] = None,
        **kwargs
    ):
        self.app_version = app_version
        self.customer_data = customer_data
        self.instanceid = instanceid
        self.ms_open_id = ms_open_id
        self.open_id = open_id
        self.user_name = user_name
        self.userid = userid
        self.uuid = uuid


class V1MeetingsPost200Response(object):
    """V1MeetingsPost200Response

    :param meeting_info_list: 会议列表 
    :type meeting_info_list: Optional[List[V1MeetingsPost200ResponseMeetingInfoListInner]]

    :param meeting_number: 会议数量 
    :type meeting_number: Optional[int]
    """  # noqa: E501

    meeting_info_list: Optional[List[V1MeetingsPost200ResponseMeetingInfoListInner]] = None
    meeting_number: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        meeting_info_list: Optional[List[V1MeetingsPost200ResponseMeetingInfoListInner] | List[Dict[str, Any]]] = None,
        meeting_number: Optional[int] = None,
        **kwargs
    ):
        
        if meeting_info_list and isinstance(meeting_info_list, (list, List)):
            self.meeting_info_list = [V1MeetingsPost200ResponseMeetingInfoListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in meeting_info_list]
        
        self.meeting_number = meeting_number


class V1MeetingsPost200ResponseMeetingInfoListInner(object):
    """会议列表

    :param current_co_hosts: 联席主持人 
    :type current_co_hosts: Optional[List[V1MeetingsPost200ResponseMeetingInfoListInnerCurrentCoHostsInner]]

    :param enable_live: 是否开启直播（会议创建人才有权限查询） 
    :type enable_live: Optional[bool]

    :param end_time: 会议结束时间戳（秒） 
    :type end_time: Optional[str]

    :param host_key: 主持人密钥，仅支持6位数字。 
    :type host_key: Optional[str]

    :param hosts: 指定主持人列表，仅商业版和企业版可指定主持人 
    :type hosts: Optional[List[V1MeetingsPost200ResponseMeetingInfoListInnerHostsInner]]

    :param join_url: 加入会议 URL 
    :type join_url: Optional[str]

    :param live_config:
    :type live_config: Optional[V1MeetingsPost200ResponseMeetingInfoListInnerLiveConfig]

    :param meeting_code: 会议 App 的呼入号码 
    :type meeting_code: Optional[str]

    :param meeting_id: 会议唯一id 
    :type meeting_id: Optional[str]

    :param participants: 邀请的参会人 
    :type participants: Optional[List[V1MeetingsPost200ResponseMeetingInfoListInnerParticipantsInner]]

    :param password: 会议密码 
    :type password: Optional[str]

    :param settings:
    :type settings: Optional[V1MeetingsPost200ResponseMeetingInfoListInnerSettings]

    :param start_time: 会议开始时间戳（秒） 
    :type start_time: Optional[str]

    :param subject: 会议主题 
    :type subject: Optional[str]

    :param user_non_registered: 邀请的参会者中未注册用户。注意：仅腾讯会议商业版和企业版可获取该参数。 
    :type user_non_registered: Optional[List[str]]
    """  # noqa: E501

    current_co_hosts: Optional[List[V1MeetingsPost200ResponseMeetingInfoListInnerCurrentCoHostsInner]] = None
    enable_live: Optional[bool] = None
    end_time: Optional[str] = None
    host_key: Optional[str] = None
    hosts: Optional[List[V1MeetingsPost200ResponseMeetingInfoListInnerHostsInner]] = None
    join_url: Optional[str] = None
    live_config: Optional[V1MeetingsPost200ResponseMeetingInfoListInnerLiveConfig] = None
    meeting_code: Optional[str] = None
    meeting_id: Optional[str] = None
    participants: Optional[List[V1MeetingsPost200ResponseMeetingInfoListInnerParticipantsInner]] = None
    password: Optional[str] = None
    settings: Optional[V1MeetingsPost200ResponseMeetingInfoListInnerSettings] = None
    start_time: Optional[str] = None
    subject: Optional[str] = None
    user_non_registered: Optional[List[str]] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        current_co_hosts: Optional[List[V1MeetingsPost200ResponseMeetingInfoListInnerCurrentCoHostsInner] | List[Dict[str, Any]]] = None,
        enable_live: Optional[bool] = None,
        end_time: Optional[str] = None,
        host_key: Optional[str] = None,
        hosts: Optional[List[V1MeetingsPost200ResponseMeetingInfoListInnerHostsInner] | List[Dict[str, Any]]] = None,
        join_url: Optional[str] = None,
        live_config: Optional[V1MeetingsPost200ResponseMeetingInfoListInnerLiveConfig | Dict[str, Any]] = None,
        meeting_code: Optional[str] = None,
        meeting_id: Optional[str] = None,
        participants: Optional[List[V1MeetingsPost200ResponseMeetingInfoListInnerParticipantsInner] | List[Dict[str, Any]]] = None,
        password: Optional[str] = None,
        settings: Optional[V1MeetingsPost200ResponseMeetingInfoListInnerSettings | Dict[str, Any]] = None,
        start_time: Optional[str] = None,
        subject: Optional[str] = None,
        user_non_registered: Optional[List[str]] = None,
        **kwargs
    ):
        
        if current_co_hosts and isinstance(current_co_hosts, (list, List)):
            self.current_co_hosts = [V1MeetingsPost200ResponseMeetingInfoListInnerCurrentCoHostsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in current_co_hosts]
        
        self.enable_live = enable_live
        self.end_time = end_time
        self.host_key = host_key
        
        if hosts and isinstance(hosts, (list, List)):
            self.hosts = [V1MeetingsPost200ResponseMeetingInfoListInnerHostsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in hosts]
        
        self.join_url = join_url
        self.live_config = V1MeetingsPost200ResponseMeetingInfoListInnerLiveConfig(**live_config) if isinstance(live_config, (dict, Dict)) else live_config
        self.meeting_code = meeting_code
        self.meeting_id = meeting_id
        
        if participants and isinstance(participants, (list, List)):
            self.participants = [V1MeetingsPost200ResponseMeetingInfoListInnerParticipantsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in participants]
        
        self.password = password
        self.settings = V1MeetingsPost200ResponseMeetingInfoListInnerSettings(**settings) if isinstance(settings, (dict, Dict)) else settings
        self.start_time = start_time
        self.subject = subject
        
        if user_non_registered and isinstance(user_non_registered, (list, List)):
            self.user_non_registered = user_non_registered
        


class V1MeetingsPost200ResponseMeetingInfoListInnerCurrentCoHostsInner(object):
    """联席主持人

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


class V1MeetingsPost200ResponseMeetingInfoListInnerHostsInner(object):
    """指定主持人列表，仅商业版和企业版可指定主持人

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


class V1MeetingsPost200ResponseMeetingInfoListInnerLiveConfig(object):
    """会议的直播配置（会议创建人才有权限查询）

    :param enable_live_im: 是否开启直播互动 
    :type enable_live_im: Optional[bool]

    :param enable_live_password: 是否开启直播密码，默认值false. true：开启, false：不开启 
    :type enable_live_password: Optional[bool]

    :param enable_live_replay: 是否开启直播回放 
    :type enable_live_replay: Optional[bool]

    :param live_password: 直播密码 
    :type live_password: Optional[str]

    :param live_subject: 直播主题 
    :type live_subject: Optional[str]

    :param live_summary: 直播简介 
    :type live_summary: Optional[str]

    :param live_watermark:
    :type live_watermark: Optional[V1MeetingsPost200ResponseMeetingInfoListInnerLiveConfigLiveWatermark]
    """  # noqa: E501

    enable_live_im: Optional[bool] = None
    enable_live_password: Optional[bool] = None
    enable_live_replay: Optional[bool] = None
    live_password: Optional[str] = None
    live_subject: Optional[str] = None
    live_summary: Optional[str] = None
    live_watermark: Optional[V1MeetingsPost200ResponseMeetingInfoListInnerLiveConfigLiveWatermark] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        enable_live_im: Optional[bool] = None,
        enable_live_password: Optional[bool] = None,
        enable_live_replay: Optional[bool] = None,
        live_password: Optional[str] = None,
        live_subject: Optional[str] = None,
        live_summary: Optional[str] = None,
        live_watermark: Optional[V1MeetingsPost200ResponseMeetingInfoListInnerLiveConfigLiveWatermark | Dict[str, Any]] = None,
        **kwargs
    ):
        self.enable_live_im = enable_live_im
        self.enable_live_password = enable_live_password
        self.enable_live_replay = enable_live_replay
        self.live_password = live_password
        self.live_subject = live_subject
        self.live_summary = live_summary
        self.live_watermark = V1MeetingsPost200ResponseMeetingInfoListInnerLiveConfigLiveWatermark(**live_watermark) if isinstance(live_watermark, (dict, Dict)) else live_watermark


class V1MeetingsPost200ResponseMeetingInfoListInnerLiveConfigLiveWatermark(object):
    """直播水印对象信息

    :param watermark_opt: 水印选项，默认为0。 0：默认水印 1：无水印 
    :type watermark_opt: Optional[int]
    """  # noqa: E501

    watermark_opt: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        watermark_opt: Optional[int] = None,
        **kwargs
    ):
        self.watermark_opt = watermark_opt


class V1MeetingsPost200ResponseMeetingInfoListInnerParticipantsInner(object):
    """邀请的参会人

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


class V1MeetingsPost200ResponseMeetingInfoListInnerSettings(object):
    """会议媒体设置参数

    :param allow_in_before_host: 允许成员在主持人进会前加入会议 
    :type allow_in_before_host: Optional[bool]

    :param allow_multi_device: 是否允许多端入会 
    :type allow_multi_device: Optional[bool]

    :param allow_screen_shared_watermark: 开启屏幕共享水印 
    :type allow_screen_shared_watermark: Optional[bool]

    :param allow_unmute_self: 静音自解除允许 
    :type allow_unmute_self: Optional[bool]

    :param auto_in_waiting_room: 开启等候室 
    :type auto_in_waiting_room: Optional[bool]

    :param auto_record_type: 自动录制类型，仅客户端2.7及以上版本生效 none：禁用 local：本地录制 cloud：云录制 
    :type auto_record_type: Optional[str]

    :param change_nickname: 是否允许用户自己改名 1:允许用户自己改名，2:不允许用户自己改名，默认为1 
    :type change_nickname: Optional[int]

    :param enable_host_pause_auto_record: 允许主持人暂停或者停止云录制，默认值为 true 开启，开启时，主持人允许暂停和停止云录制；当设置为关闭时，则主持人不允许暂停和关闭云录制 
    :type enable_host_pause_auto_record: Optional[bool]

    :param mute_enable_join: 加入静音状态 
    :type mute_enable_join: Optional[bool]

    :param mute_enable_type_join: 加入静音状态 
    :type mute_enable_type_join: Optional[int]

    :param only_enterprise_user_allowed: 是否仅企业内部成员可入会，默认值为 false。true：仅企业内部用户可入会 false：所有人可入会 
    :type only_enterprise_user_allowed: Optional[bool]

    :param only_user_join_type: 成员入会限制，1：所有成员可入会，2：仅受邀成员可入会，3：仅企业内部成员可入会 ；当only_user_join_type和only_allow_enterprise_user_join同时传的时候，以only_user_join_type为准 
    :type only_user_join_type: Optional[int]

    :param participant_join_auto_record: 当有参会成员入会时立即开启云录制，默认值为 false 关闭，关闭时，主持人入会自动开启云录制；当设置为开启时，则有参会成员入会自动开启云录制。 
    :type participant_join_auto_record: Optional[bool]

    :param play_ivr_on_join: 有新的与会者加入时播放提示音，暂不支持，可在客户端设置 
    :type play_ivr_on_join: Optional[bool]

    :param play_ivr_on_leave: 参会者离开时播放提示音，暂时不支持，可在客户端设置。 
    :type play_ivr_on_leave: Optional[bool]

    :param water_mark_type: 水印样式，默认为单排：0：单排 1：多排 
    :type water_mark_type: Optional[int]
    """  # noqa: E501

    allow_in_before_host: Optional[bool] = None
    allow_multi_device: Optional[bool] = None
    allow_screen_shared_watermark: Optional[bool] = None
    allow_unmute_self: Optional[bool] = None
    auto_in_waiting_room: Optional[bool] = None
    auto_record_type: Optional[str] = None
    change_nickname: Optional[int] = None
    enable_host_pause_auto_record: Optional[bool] = None
    mute_enable_join: Optional[bool] = None
    mute_enable_type_join: Optional[int] = None
    only_enterprise_user_allowed: Optional[bool] = None
    only_user_join_type: Optional[int] = None
    participant_join_auto_record: Optional[bool] = None
    play_ivr_on_join: Optional[bool] = None
    play_ivr_on_leave: Optional[bool] = None
    water_mark_type: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        allow_in_before_host: Optional[bool] = None,
        allow_multi_device: Optional[bool] = None,
        allow_screen_shared_watermark: Optional[bool] = None,
        allow_unmute_self: Optional[bool] = None,
        auto_in_waiting_room: Optional[bool] = None,
        auto_record_type: Optional[str] = None,
        change_nickname: Optional[int] = None,
        enable_host_pause_auto_record: Optional[bool] = None,
        mute_enable_join: Optional[bool] = None,
        mute_enable_type_join: Optional[int] = None,
        only_enterprise_user_allowed: Optional[bool] = None,
        only_user_join_type: Optional[int] = None,
        participant_join_auto_record: Optional[bool] = None,
        play_ivr_on_join: Optional[bool] = None,
        play_ivr_on_leave: Optional[bool] = None,
        water_mark_type: Optional[int] = None,
        **kwargs
    ):
        self.allow_in_before_host = allow_in_before_host
        self.allow_multi_device = allow_multi_device
        self.allow_screen_shared_watermark = allow_screen_shared_watermark
        self.allow_unmute_self = allow_unmute_self
        self.auto_in_waiting_room = auto_in_waiting_room
        self.auto_record_type = auto_record_type
        self.change_nickname = change_nickname
        self.enable_host_pause_auto_record = enable_host_pause_auto_record
        self.mute_enable_join = mute_enable_join
        self.mute_enable_type_join = mute_enable_type_join
        self.only_enterprise_user_allowed = only_enterprise_user_allowed
        self.only_user_join_type = only_user_join_type
        self.participant_join_auto_record = participant_join_auto_record
        self.play_ivr_on_join = play_ivr_on_join
        self.play_ivr_on_leave = play_ivr_on_leave
        self.water_mark_type = water_mark_type


class V1MeetingsPostRequest(object):
    """V1MeetingsPostRequest

    :param allow_enterprise_intranet_only: 默认是false, 如果操作者无创建转网会议的权限，则该字段忽略 
    :type allow_enterprise_intranet_only: Optional[bool]

    :param enable_doc_upload_permission: 是否允许成员上传文档，默认为允许 true：允许 false：不允许 
    :type enable_doc_upload_permission: Optional[bool]

    :param enable_enroll: 是否开启报名开关，默认不开启 true：开启 false：不开启 
    :type enable_enroll: Optional[bool]

    :param enable_host_key: 是否开启主持人密钥，默认为false。 true：开启 false：关闭 
    :type enable_host_key: Optional[bool]

    :param enable_interpreter: 是否开启同声传译，默认不开启 false：不开启 true：开启同声传译 
    :type enable_interpreter: Optional[bool]

    :param enable_live: 是否开启直播 
    :type enable_live: Optional[bool]

    :param end_time: 会议结束时间戳（单位秒） (required) 
    :type end_time: str

    :param guests: 会议嘉宾列表，会议嘉宾不受会议密码和等候室的限制 
    :type guests: Optional[List[V1MeetingsPostRequestGuestsInner]]

    :param host_key: 主持人密钥，仅支持6位数字。 如开启主持人密钥后没有填写此项，将自动分配一个6位数字的密钥。 
    :type host_key: Optional[str]

    :param hosts: 主持人列表，会议指定主持人的用户 ID，如果无指定，主持人将被设定为参数 userid 的用户，即 API 调用者。 注意：仅腾讯会议商业版和企业版可指定主持人。 
    :type hosts: Optional[List[V1MeetingsPostRequestHostsInner]]

    :param instanceid: 用户的终端设备类型： 0：PSTN 1：PC 2：Mac 3：Android 4：iOS 5：Web 6：iPad 7：Android Pad 8：小程序 9：voip、sip 设备 10：linux 20：Rooms for Touch Windows 21：Rooms for Touch MacOS 22：Rooms for Touch Android 30：Controller for Touch Windows 32：Controller for Touch Android 33：Controller for Touch iOS 创建会议时 userid 对应的设备类型，不影响入会时使用的设备类型，缺省可填1。 (required) 
    :type instanceid: int

    :param invitees: 邀请人列表 仅支持邀请与会议创建者同企业的成员（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId），该会议将添加至邀请成员的会议列表中。 企业唯一用户标识说明： 企业对接 SSO 时使用的员工唯一标识 ID。 企业调用创建用户接口时传递的 userid 参数。 注意：仅腾讯会议商业版和企业版可邀请参会者，邀请者列表仅支持300人；需要邀请超过300人的场景请调用 设置会议邀请成员 接口。 
    :type invitees: Optional[List[V1MeetingsPostRequestInviteesInner]]

    :param live_config:
    :type live_config: Optional[V1MeetingsPostRequestLiveConfig]

    :param location: 会议地点。最长支持18个汉字或36个英文字母 
    :type location: Optional[str]

    :param media_set_type: 该参数仅提供给支持混合云的企业可见，默认值为0 0：外部会议 1：内部会议 
    :type media_set_type: Optional[int]

    :param meeting_type: 默认值为0。 0：普通会议 1：周期性会议（周期性会议时 type 不能为快速会议，同一账号同时最多可预定50场周期性会议） 
    :type meeting_type: Optional[int]

    :param password: 会议密码（4~6位数字），可不填 
    :type password: Optional[str]

    :param recurring_rule:
    :type recurring_rule: Optional[V1MeetingsPostRequestRecurringRule]

    :param settings:
    :type settings: Optional[V1MeetingsPostRequestSettings]

    :param start_time: 会议开始时间戳（单位秒） (required) 
    :type start_time: str

    :param subject: 会议主题 (required) 
    :type subject: str

    :param sync_to_wework: 会议是否同步至企业微信，该字段仅支持创建会议时设置，创建后无法修改。 true: 同步，默认同步  false: 不同步 
    :type sync_to_wework: Optional[bool]

    :param time_zone: 时区，可参见 Oracle-TimeZone 标准 
    :type time_zone: Optional[str]

    :param type: 会议类型 0：预约会议 1：快速会议  (required) 
    :type type: int

    :param userid: 调用方用于标示用户的唯一 ID（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId）。 企业唯一用户标识说明： 1. 企业对接 SSO 时使用的员工唯一标识 ID； 2. 企业调用创建用户接口时传递的 userid 参数。 (required) 
    :type userid: str
    """  # noqa: E501

    allow_enterprise_intranet_only: Optional[bool] = None
    enable_doc_upload_permission: Optional[bool] = None
    enable_enroll: Optional[bool] = None
    enable_host_key: Optional[bool] = None
    enable_interpreter: Optional[bool] = None
    enable_live: Optional[bool] = None
    end_time: str
    guests: Optional[List[V1MeetingsPostRequestGuestsInner]] = None
    host_key: Optional[str] = None
    hosts: Optional[List[V1MeetingsPostRequestHostsInner]] = None
    instanceid: int
    invitees: Optional[List[V1MeetingsPostRequestInviteesInner]] = None
    live_config: Optional[V1MeetingsPostRequestLiveConfig] = None
    location: Optional[str] = None
    media_set_type: Optional[int] = None
    meeting_type: Optional[int] = None
    password: Optional[str] = None
    recurring_rule: Optional[V1MeetingsPostRequestRecurringRule] = None
    settings: Optional[V1MeetingsPostRequestSettings] = None
    start_time: str
    subject: str
    sync_to_wework: Optional[bool] = None
    time_zone: Optional[str] = None
    type: int
    userid: str
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        end_time: str,
        instanceid: int,
        start_time: str,
        subject: str,
        type: int,
        userid: str,
        allow_enterprise_intranet_only: Optional[bool] = None,
        enable_doc_upload_permission: Optional[bool] = None,
        enable_enroll: Optional[bool] = None,
        enable_host_key: Optional[bool] = None,
        enable_interpreter: Optional[bool] = None,
        enable_live: Optional[bool] = None,
        guests: Optional[List[V1MeetingsPostRequestGuestsInner] | List[Dict[str, Any]]] = None,
        host_key: Optional[str] = None,
        hosts: Optional[List[V1MeetingsPostRequestHostsInner] | List[Dict[str, Any]]] = None,
        invitees: Optional[List[V1MeetingsPostRequestInviteesInner] | List[Dict[str, Any]]] = None,
        live_config: Optional[V1MeetingsPostRequestLiveConfig | Dict[str, Any]] = None,
        location: Optional[str] = None,
        media_set_type: Optional[int] = None,
        meeting_type: Optional[int] = None,
        password: Optional[str] = None,
        recurring_rule: Optional[V1MeetingsPostRequestRecurringRule | Dict[str, Any]] = None,
        settings: Optional[V1MeetingsPostRequestSettings | Dict[str, Any]] = None,
        sync_to_wework: Optional[bool] = None,
        time_zone: Optional[str] = None,
        **kwargs
    ):
        self.allow_enterprise_intranet_only = allow_enterprise_intranet_only
        self.enable_doc_upload_permission = enable_doc_upload_permission
        self.enable_enroll = enable_enroll
        self.enable_host_key = enable_host_key
        self.enable_interpreter = enable_interpreter
        self.enable_live = enable_live
        self.end_time = end_time
        
        if guests and isinstance(guests, (list, List)):
            self.guests = [V1MeetingsPostRequestGuestsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in guests]
        
        self.host_key = host_key
        
        if hosts and isinstance(hosts, (list, List)):
            self.hosts = [V1MeetingsPostRequestHostsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in hosts]
        
        self.instanceid = instanceid
        
        if invitees and isinstance(invitees, (list, List)):
            self.invitees = [V1MeetingsPostRequestInviteesInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in invitees]
        
        self.live_config = V1MeetingsPostRequestLiveConfig(**live_config) if isinstance(live_config, (dict, Dict)) else live_config
        self.location = location
        self.media_set_type = media_set_type
        self.meeting_type = meeting_type
        self.password = password
        self.recurring_rule = V1MeetingsPostRequestRecurringRule(**recurring_rule) if isinstance(recurring_rule, (dict, Dict)) else recurring_rule
        self.settings = V1MeetingsPostRequestSettings(**settings) if isinstance(settings, (dict, Dict)) else settings
        self.start_time = start_time
        self.subject = subject
        self.sync_to_wework = sync_to_wework
        self.time_zone = time_zone
        self.type = type
        self.userid = userid


class V1MeetingsPostRequestGuestsInner(object):
    """V1MeetingsPostRequestGuestsInner

    :param area: 国家/地区代码（例如：中国传86，不是+86，也不是0086） (required) 
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


class V1MeetingsPostRequestHostsInner(object):
    """V1MeetingsPostRequestHostsInner

    :param is_anonymous: 用户是否匿名入会，缺省为 false，不匿名 true：匿名 false：不匿名 
    :type is_anonymous: Optional[bool]

    :param nick_name: 用户匿名字符串。如果字段“is_anonymous”设置为“true”，但是无指定匿名字符串, 会议将分配缺省名称，例如 “会议用户xxxx”，其中“xxxx”为随机数字。 
    :type nick_name: Optional[str]

    :param userid: 用户 ID（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId） 企业唯一用户标识说明： 企业对接 SSO 时使用的员工唯一标识 ID，企业调用创建用户接口时传递的 userid 参数。 (required) 
    :type userid: str
    """  # noqa: E501

    is_anonymous: Optional[bool] = None
    nick_name: Optional[str] = None
    userid: str
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        userid: str,
        is_anonymous: Optional[bool] = None,
        nick_name: Optional[str] = None,
        **kwargs
    ):
        self.is_anonymous = is_anonymous
        self.nick_name = nick_name
        self.userid = userid


class V1MeetingsPostRequestInviteesInner(object):
    """V1MeetingsPostRequestInviteesInner

    :param is_anonymous: 用户是否匿名入会，缺省为 false，不匿名。 true：匿名 false：不匿名 
    :type is_anonymous: Optional[bool]

    :param nick_name: 用户匿名字符串。如果字段“is_anonymous”设置为“true”，但是无指定匿名字符串, 会议将分配缺省名称，例如 “会议用户xxxx”，其中“xxxx”为随机数字。 
    :type nick_name: Optional[str]

    :param userid: 用户 ID（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId）。 企业唯一用户标识说明： 企业对接 SSO 时使用的员工唯一标识 ID，企业调用创建用户接口时传递的 userid 参数。 (required) 
    :type userid: str
    """  # noqa: E501

    is_anonymous: Optional[bool] = None
    nick_name: Optional[str] = None
    userid: str
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        userid: str,
        is_anonymous: Optional[bool] = None,
        nick_name: Optional[str] = None,
        **kwargs
    ):
        self.is_anonymous = is_anonymous
        self.nick_name = nick_name
        self.userid = userid


class V1MeetingsPostRequestLiveConfig(object):
    """直播配置

    :param enable_live_im: 允许观众讨论，默认值为 false。 true：开启 false：不开启 
    :type enable_live_im: Optional[bool]

    :param enable_live_password: 是否开启直播密码，默认值false. true：开启, false：不开启 
    :type enable_live_password: Optional[bool]

    :param enable_live_replay: 开启直播回看，默认值为 false true：开启 false：不开启 
    :type enable_live_replay: Optional[bool]

    :param live_password: 直播密码。当设置开启直播密码时，该参数必填。 
    :type live_password: Optional[str]

    :param live_subject: 直播主题 
    :type live_subject: Optional[str]

    :param live_summary: 直播简介 
    :type live_summary: Optional[str]

    :param live_watermark:
    :type live_watermark: Optional[V1MeetingsPostRequestLiveConfigLiveWatermark]
    """  # noqa: E501

    enable_live_im: Optional[bool] = None
    enable_live_password: Optional[bool] = None
    enable_live_replay: Optional[bool] = None
    live_password: Optional[str] = None
    live_subject: Optional[str] = None
    live_summary: Optional[str] = None
    live_watermark: Optional[V1MeetingsPostRequestLiveConfigLiveWatermark] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        enable_live_im: Optional[bool] = None,
        enable_live_password: Optional[bool] = None,
        enable_live_replay: Optional[bool] = None,
        live_password: Optional[str] = None,
        live_subject: Optional[str] = None,
        live_summary: Optional[str] = None,
        live_watermark: Optional[V1MeetingsPostRequestLiveConfigLiveWatermark | Dict[str, Any]] = None,
        **kwargs
    ):
        self.enable_live_im = enable_live_im
        self.enable_live_password = enable_live_password
        self.enable_live_replay = enable_live_replay
        self.live_password = live_password
        self.live_subject = live_subject
        self.live_summary = live_summary
        self.live_watermark = V1MeetingsPostRequestLiveConfigLiveWatermark(**live_watermark) if isinstance(live_watermark, (dict, Dict)) else live_watermark


class V1MeetingsPostRequestLiveConfigLiveWatermark(object):
    """直播水印对象

    :param watermark_opt: 水印选项，默认为0。 0：默认水印 1：无水印 
    :type watermark_opt: Optional[int]
    """  # noqa: E501

    watermark_opt: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        watermark_opt: Optional[int] = None,
        **kwargs
    ):
        self.watermark_opt = watermark_opt


class V1MeetingsPostRequestRecurringRule(object):
    """周期性会议配置

    :param customized_recurring_days: 哪些天重复。根据 customized_recurring_type 和 customized_recurring_step 的不同，该字段可取值与表达含义不同。如需选择多个日期，加和即可。 customized_recurring_type = 0 时，传入该字段将被忽略。 详细请参见 自定义周期规则 API 调用示例 
    :type customized_recurring_days: Optional[int]

    :param customized_recurring_step: 每[n]（天、周、月）重复，使用自定义周期性会议时传入。 例如：customized_recurring_type=0 &amp;&amp; customized_recurring_step=5 表示每5天重复一次。 customized_recurring_type=2 &amp;&amp; customized_recurring_step=3 表示每3个月重复一次，重复的时间依赖于 customized_recurring_days 字段。 
    :type customized_recurring_step: Optional[int]

    :param customized_recurring_type: 自定义周期性会议的循环类型。 0：按天。 1：按周。 2：按月，以周为粒度重复。例如：每3个月的第二周的周四。 3：按月，以日期为粒度重复。例如：每3个月的16日。 按周；按月、以周为粒度； 按月、以日期为粒度时，需要包含会议开始时间所在的日期。 
    :type customized_recurring_type: Optional[int]

    :param recurring_type: 重复类型，默认值为0。 0：每天 1：每周一至周五 2：每周 3：每两周 4：每月 5：自定义，示例请参见 自定义周期规则 API 调用示例 
    :type recurring_type: Optional[int]

    :param until_count: 限定会议次数。 说明：每天、每个工作日、每周最大支持200场子会议；每两周、每月最大支持50场子会议。如未填写，则默认为7次。 
    :type until_count: Optional[int]

    :param until_date: 结束日期时间戳。 说明：结束日期与第一场会议的开始时间换算成的场次数不能超过以下限制：每天、每个工作日、每周最大支持200场子会议；每两周、每月最大支持50场子会议，例如：对于每天的重复类型，第一场会议开始时间为1609430400，则结束日期时间戳不能超过1609430400 + 200 × 24 × 60 × 60 - 1。如未填写，默认为当前日期往后推7天。 
    :type until_date: Optional[int]

    :param until_type: 结束重复类型，默认值为0。  0：按日期结束重复  1：按次数结束重复 
    :type until_type: Optional[int]
    """  # noqa: E501

    customized_recurring_days: Optional[int] = None
    customized_recurring_step: Optional[int] = None
    customized_recurring_type: Optional[int] = None
    recurring_type: Optional[int] = None
    until_count: Optional[int] = None
    until_date: Optional[int] = None
    until_type: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        customized_recurring_days: Optional[int] = None,
        customized_recurring_step: Optional[int] = None,
        customized_recurring_type: Optional[int] = None,
        recurring_type: Optional[int] = None,
        until_count: Optional[int] = None,
        until_date: Optional[int] = None,
        until_type: Optional[int] = None,
        **kwargs
    ):
        self.customized_recurring_days = customized_recurring_days
        self.customized_recurring_step = customized_recurring_step
        self.customized_recurring_type = customized_recurring_type
        self.recurring_type = recurring_type
        self.until_count = until_count
        self.until_date = until_date
        self.until_type = until_type


class V1MeetingsPostRequestSettings(object):
    """会议媒体参数配置

    :param allow_in_before_host: 是否允许成员在主持人进会前加入会议，默认值为 true。 true：允许 false：不允许 
    :type allow_in_before_host: Optional[bool]

    :param allow_multi_device: 是否允许多端入会 
    :type allow_multi_device: Optional[bool]

    :param allow_screen_shared_watermark: 是否开启屏幕共享水印，默认值为 false。 true： 开启 false：不开启 
    :type allow_screen_shared_watermark: Optional[bool]

    :param allow_unmute_self: 允许参会者取消静音，默认值为 true。 true：开启 false：关闭 
    :type allow_unmute_self: Optional[bool]

    :param auto_in_waiting_room: 是否开启等候室，默认值为 false。 true：开启 false：不开启 
    :type auto_in_waiting_room: Optional[bool]

    :param auto_record_type: 自动会议录制类型。 none：禁用，表示不开启自动会议录制。 local：本地录制，表示主持人入会后自动开启本地录制。 cloud：云录制，表示主持人入会后自动开启云录制。 说明： 该参数依赖企业账户设置，当企业强制锁定后，该参数必须与企业配置保持一致。 仅客户端2.7及以上版本可生效。 
    :type auto_record_type: Optional[str]

    :param change_nickname: 是否允许用户自己改名 1:允许用户自己改名，2:不允许用户自己改名，默认为1 
    :type change_nickname: Optional[int]

    :param enable_host_pause_auto_record: 允许主持人暂停或者停止云录制，默认值为 true 开启，开启时，主持人允许暂停和停止云录制；当设置为关闭时，则主持人不允许暂停和关闭云录制。 说明： 该参数必须 auto_record_type 设置为“cloud”时才生效，该参数依赖企业账户设置，当企业强制锁定后，该参数必须与企业配置保持一致。 仅客户端2.7及以上版本生效。 
    :type enable_host_pause_auto_record: Optional[bool]

    :param mute_enable_join: 入会时静音，默认值为 true true：开启 false：关闭 
    :type mute_enable_join: Optional[bool]

    :param mute_enable_type_join: 成员入会时静音选项，默认值为2。 当同时传入“mute_enable_join”和“mute_enable_type_join”时，将以“mute_enable_type_join”的选项为准。 0：关闭 1：开启 2：超过6人后自动开启 
    :type mute_enable_type_join: Optional[int]

    :param only_enterprise_user_allowed: 是否仅企业内部成员可入会，默认值为 false。 true：仅企业内部用户可入会 false：所有人可入会 
    :type only_enterprise_user_allowed: Optional[bool]

    :param only_user_join_type: 成员入会限制，1：所有成员可入会，2：仅受邀成员可入会，3：仅企业内部成员可入会 ；当only_user_join_type和only_allow_enterprise_user_join同时传的时候，以only_user_join_type为准 
    :type only_user_join_type: Optional[int]

    :param participant_join_auto_record: 当有参会成员入会时立即开启云录制，默认值为 false 关闭，关闭时，主持人入会自动开启云录制；当设置为开启时，则有参会成员入会自动开启云录制。 说明： 该参数必须 auto_record_type 设置为“cloud”时才生效，该参数依赖企业账户设置，当企业强制锁定后，该参数必须与企业配置保持一致。 仅客户端2.7及以上版本生效。 
    :type participant_join_auto_record: Optional[bool]

    :param play_ivr_on_join: 有新的与会者加入时播放提示音，暂不支持，可在客户端设置 
    :type play_ivr_on_join: Optional[bool]

    :param play_ivr_on_leave: 参会者离开时播放提示音，暂时不支持，可在客户端设置。 
    :type play_ivr_on_leave: Optional[bool]

    :param water_mark_type: 水印样式，默认为单排。当屏幕共享水印参数为开启时，此参数才生效。 0：单排 1：多排 
    :type water_mark_type: Optional[int]
    """  # noqa: E501

    allow_in_before_host: Optional[bool] = None
    allow_multi_device: Optional[bool] = None
    allow_screen_shared_watermark: Optional[bool] = None
    allow_unmute_self: Optional[bool] = None
    auto_in_waiting_room: Optional[bool] = None
    auto_record_type: Optional[str] = None
    change_nickname: Optional[int] = None
    enable_host_pause_auto_record: Optional[bool] = None
    mute_enable_join: Optional[bool] = None
    mute_enable_type_join: Optional[int] = None
    only_enterprise_user_allowed: Optional[bool] = None
    only_user_join_type: Optional[int] = None
    participant_join_auto_record: Optional[bool] = None
    play_ivr_on_join: Optional[bool] = None
    play_ivr_on_leave: Optional[bool] = None
    water_mark_type: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        allow_in_before_host: Optional[bool] = None,
        allow_multi_device: Optional[bool] = None,
        allow_screen_shared_watermark: Optional[bool] = None,
        allow_unmute_self: Optional[bool] = None,
        auto_in_waiting_room: Optional[bool] = None,
        auto_record_type: Optional[str] = None,
        change_nickname: Optional[int] = None,
        enable_host_pause_auto_record: Optional[bool] = None,
        mute_enable_join: Optional[bool] = None,
        mute_enable_type_join: Optional[int] = None,
        only_enterprise_user_allowed: Optional[bool] = None,
        only_user_join_type: Optional[int] = None,
        participant_join_auto_record: Optional[bool] = None,
        play_ivr_on_join: Optional[bool] = None,
        play_ivr_on_leave: Optional[bool] = None,
        water_mark_type: Optional[int] = None,
        **kwargs
    ):
        self.allow_in_before_host = allow_in_before_host
        self.allow_multi_device = allow_multi_device
        self.allow_screen_shared_watermark = allow_screen_shared_watermark
        self.allow_unmute_self = allow_unmute_self
        self.auto_in_waiting_room = auto_in_waiting_room
        self.auto_record_type = auto_record_type
        self.change_nickname = change_nickname
        self.enable_host_pause_auto_record = enable_host_pause_auto_record
        self.mute_enable_join = mute_enable_join
        self.mute_enable_type_join = mute_enable_type_join
        self.only_enterprise_user_allowed = only_enterprise_user_allowed
        self.only_user_join_type = only_user_join_type
        self.participant_join_auto_record = participant_join_auto_record
        self.play_ivr_on_join = play_ivr_on_join
        self.play_ivr_on_leave = play_ivr_on_leave
        self.water_mark_type = water_mark_type


class V1MeetingsQueryMeetingidForDevicePost200Response(object):
    """V1MeetingsQueryMeetingidForDevicePost200Response

    :param meeting_id_map: 用户设备已加入的会议的列表 
    :type meeting_id_map: Optional[List[V1MeetingsQueryMeetingidForDevicePost200ResponseMeetingIdMapInner]]
    """  # noqa: E501

    meeting_id_map: Optional[List[V1MeetingsQueryMeetingidForDevicePost200ResponseMeetingIdMapInner]] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        meeting_id_map: Optional[List[V1MeetingsQueryMeetingidForDevicePost200ResponseMeetingIdMapInner] | List[Dict[str, Any]]] = None,
        **kwargs
    ):
        
        if meeting_id_map and isinstance(meeting_id_map, (list, List)):
            self.meeting_id_map = [V1MeetingsQueryMeetingidForDevicePost200ResponseMeetingIdMapInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in meeting_id_map]
        


class V1MeetingsQueryMeetingidForDevicePost200ResponseMeetingIdMapInner(object):
    """V1MeetingsQueryMeetingidForDevicePost200ResponseMeetingIdMapInner

    :param instanceid: 终端设备类型。 
    :type instanceid: Optional[int]

    :param meeting_id: 会议ID。 
    :type meeting_id: Optional[str]
    """  # noqa: E501

    instanceid: Optional[int] = None
    meeting_id: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        instanceid: Optional[int] = None,
        meeting_id: Optional[str] = None,
        **kwargs
    ):
        self.instanceid = instanceid
        self.meeting_id = meeting_id


class V1MeetingsQueryMeetingidForDevicePostRequest(object):
    """V1MeetingsQueryMeetingidForDevicePostRequest

    :param operator_id: 操作者 ID，即查询者的信息。 operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 (required) 
    :type operator_id: str

    :param operator_id_type: 操作者 ID 的类型：  1：企业内用户 userid。JWT鉴权仅支持userid  (required) 
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


class V1PmiMeetingsGet200Response(object):
    """V1PmiMeetingsGet200Response

    :param current_page: 当前页。 
    :type current_page: Optional[int]

    :param current_size: 当前实际页大小。 
    :type current_size: Optional[int]

    :param meeting_info_list: 会议列表。 
    :type meeting_info_list: Optional[List[V1PmiMeetingsGet200ResponseMeetingInfoListInner]]

    :param total_count: 数据总条数。 
    :type total_count: Optional[int]

    :param total_page: 数据总页数。 
    :type total_page: Optional[int]
    """  # noqa: E501

    current_page: Optional[int] = None
    current_size: Optional[int] = None
    meeting_info_list: Optional[List[V1PmiMeetingsGet200ResponseMeetingInfoListInner]] = None
    total_count: Optional[int] = None
    total_page: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        current_page: Optional[int] = None,
        current_size: Optional[int] = None,
        meeting_info_list: Optional[List[V1PmiMeetingsGet200ResponseMeetingInfoListInner] | List[Dict[str, Any]]] = None,
        total_count: Optional[int] = None,
        total_page: Optional[int] = None,
        **kwargs
    ):
        self.current_page = current_page
        self.current_size = current_size
        
        if meeting_info_list and isinstance(meeting_info_list, (list, List)):
            self.meeting_info_list = [V1PmiMeetingsGet200ResponseMeetingInfoListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in meeting_info_list]
        
        self.total_count = total_count
        self.total_page = total_page


class V1PmiMeetingsGet200ResponseMeetingInfoListInner(object):
    """V1PmiMeetingsGet200ResponseMeetingInfoListInner

    :param end_time: 会议预订结束时间（UTC 秒）（UTC 秒） 
    :type end_time: Optional[int]

    :param meeting_code: 有效会议Code 
    :type meeting_code: Optional[str]

    :param meeting_id: 会议 ID 
    :type meeting_id: Optional[str]

    :param start_time: 会议预订开始时间（UTC 秒）（UTC 秒） 
    :type start_time: Optional[int]

    :param status: 会议状态 
    :type status: Optional[int]

    :param subject: 会议主题 
    :type subject: Optional[str]
    """  # noqa: E501

    end_time: Optional[int] = None
    meeting_code: Optional[str] = None
    meeting_id: Optional[str] = None
    start_time: Optional[int] = None
    status: Optional[int] = None
    subject: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        end_time: Optional[int] = None,
        meeting_code: Optional[str] = None,
        meeting_id: Optional[str] = None,
        start_time: Optional[int] = None,
        status: Optional[int] = None,
        subject: Optional[str] = None,
        **kwargs
    ):
        self.end_time = end_time
        self.meeting_code = meeting_code
        self.meeting_id = meeting_id
        self.start_time = start_time
        self.status = status
        self.subject = subject

