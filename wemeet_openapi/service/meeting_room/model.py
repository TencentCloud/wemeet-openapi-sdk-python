# coding: utf-8

"""
    腾讯会议OpenAPI

    SAAS版RESTFUL风格API

    API version: v1.0.4

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

from typing import *


class V1DevicesGet200Response(object):
    """V1DevicesGet200Response

    :param current_page: 当前页 
    :type current_page: Optional[int]

    :param current_size: 单页条数 
    :type current_size: Optional[int]

    :param device_info_list: 设备对象列表 
    :type device_info_list: Optional[List[V1DevicesGet200ResponseDeviceInfoListInner]]

    :param total_count: 数据总条数 
    :type total_count: Optional[int]

    :param total_page: 数据总页数 
    :type total_page: Optional[int]
    """  # noqa: E501

    current_page: Optional[int] = None
    current_size: Optional[int] = None
    device_info_list: Optional[List[V1DevicesGet200ResponseDeviceInfoListInner]] = None
    total_count: Optional[int] = None
    total_page: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        current_page: Optional[int] = None,
        current_size: Optional[int] = None,
        device_info_list: Optional[List[V1DevicesGet200ResponseDeviceInfoListInner] | List[Dict[str, Any]]] = None,
        total_count: Optional[int] = None,
        total_page: Optional[int] = None,
        **kwargs
    ):
        self.current_page = current_page
        self.current_size = current_size
        
        if device_info_list and isinstance(device_info_list, (list, List)):
            self.device_info_list = [V1DevicesGet200ResponseDeviceInfoListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in device_info_list]
        
        self.total_count = total_count
        self.total_page = total_page


class V1DevicesGet200ResponseDeviceInfoListInner(object):
    """V1DevicesGet200ResponseDeviceInfoListInner

    :param app_version: 应用程序版本 
    :type app_version: Optional[str]

    :param device_model: 设备型号 
    :type device_model: Optional[str]

    :param device_monitor_info:
    :type device_monitor_info: Optional[V1DevicesGet200ResponseDeviceInfoListInnerDeviceMonitorInfo]

    :param meeting_room_id: 会议室ID 
    :type meeting_room_id: Optional[str]

    :param meeting_room_location: 会议室地址 
    :type meeting_room_location: Optional[str]

    :param meeting_room_name: 会议室名称 
    :type meeting_room_name: Optional[str]

    :param meeting_room_status: 会议室状态：0：未激活1：未绑定2：空闲3：使用中4：离线，5:未登录 
    :type meeting_room_status: Optional[int]

    :param rooms_id:
    :type rooms_id: Optional[str]
    """  # noqa: E501

    app_version: Optional[str] = None
    device_model: Optional[str] = None
    device_monitor_info: Optional[V1DevicesGet200ResponseDeviceInfoListInnerDeviceMonitorInfo] = None
    meeting_room_id: Optional[str] = None
    meeting_room_location: Optional[str] = None
    meeting_room_name: Optional[str] = None
    meeting_room_status: Optional[int] = None
    rooms_id: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        app_version: Optional[str] = None,
        device_model: Optional[str] = None,
        device_monitor_info: Optional[V1DevicesGet200ResponseDeviceInfoListInnerDeviceMonitorInfo | Dict[str, Any]] = None,
        meeting_room_id: Optional[str] = None,
        meeting_room_location: Optional[str] = None,
        meeting_room_name: Optional[str] = None,
        meeting_room_status: Optional[int] = None,
        rooms_id: Optional[str] = None,
        **kwargs
    ):
        self.app_version = app_version
        self.device_model = device_model
        self.device_monitor_info = V1DevicesGet200ResponseDeviceInfoListInnerDeviceMonitorInfo(**device_monitor_info) if isinstance(device_monitor_info, (dict, Dict)) else device_monitor_info
        self.meeting_room_id = meeting_room_id
        self.meeting_room_location = meeting_room_location
        self.meeting_room_name = meeting_room_name
        self.meeting_room_status = meeting_room_status
        self.rooms_id = rooms_id


class V1DevicesGet200ResponseDeviceInfoListInnerDeviceMonitorInfo(object):
    """V1DevicesGet200ResponseDeviceInfoListInnerDeviceMonitorInfo

    :param camera_status: 摄像头健康状态 
    :type camera_status: Optional[bool]

    :param microphone_status: 麦克风健康状态 
    :type microphone_status: Optional[bool]

    :param speaker_status: 扬声器健康状态 
    :type speaker_status: Optional[bool]
    """  # noqa: E501

    camera_status: Optional[bool] = None
    microphone_status: Optional[bool] = None
    speaker_status: Optional[bool] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        camera_status: Optional[bool] = None,
        microphone_status: Optional[bool] = None,
        speaker_status: Optional[bool] = None,
        **kwargs
    ):
        self.camera_status = camera_status
        self.microphone_status = microphone_status
        self.speaker_status = speaker_status


class V1MeetingRoomsCancelRoomCallPutRequest(object):
    """V1MeetingRoomsCancelRoomCallPutRequest

    :param instance_id:(required) 
    :type instance_id: int

    :param invite_id: 呼叫ID (required) 
    :type invite_id: str

    :param meeting_id: 会议ID (required) 
    :type meeting_id: str

    :param meeting_room_id: 会议室 ID，与 mra_address 二选一。 
    :type meeting_room_id: Optional[str]

    :param mra_address:
    :type mra_address: Optional[V1MeetingRoomsCancelRoomCallPutRequestMraAddress]

    :param operator_id:(required) 
    :type operator_id: str

    :param operator_id_type: 操作者 ID 的类型： 1：userid (required) 
    :type operator_id_type: int
    """  # noqa: E501

    instance_id: int
    invite_id: str
    meeting_id: str
    meeting_room_id: Optional[str] = None
    mra_address: Optional[V1MeetingRoomsCancelRoomCallPutRequestMraAddress] = None
    operator_id: str
    operator_id_type: int
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        instance_id: int,
        invite_id: str,
        meeting_id: str,
        operator_id: str,
        operator_id_type: int,
        meeting_room_id: Optional[str] = None,
        mra_address: Optional[V1MeetingRoomsCancelRoomCallPutRequestMraAddress | Dict[str, Any]] = None,
        **kwargs
    ):
        self.instance_id = instance_id
        self.invite_id = invite_id
        self.meeting_id = meeting_id
        self.meeting_room_id = meeting_room_id
        self.mra_address = V1MeetingRoomsCancelRoomCallPutRequestMraAddress(**mra_address) if isinstance(mra_address, (dict, Dict)) else mra_address
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type


class V1MeetingRoomsCancelRoomCallPutRequestMraAddress(object):
    """MRA 对象

    :param dial_string: 信令地址。 如果是 H.323 类型，输入 IP 地址或 E.164 号码。 如果是 SIP 类型，输入 IP 地址或 URI。 (required) 
    :type dial_string: str

    :param protocol: 信令协议。 1：SIP 2：H.323 (required) 
    :type protocol: int
    """  # noqa: E501

    dial_string: str
    protocol: int
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        dial_string: str,
        protocol: int,
        **kwargs
    ):
        self.dial_string = dial_string
        self.protocol = protocol


class V1MeetingRoomsGet200Response(object):
    """V1MeetingRoomsGet200Response

    :param current_page: 当前页 
    :type current_page: Optional[int]

    :param current_size: 单页条数 
    :type current_size: Optional[int]

    :param meeting_room_list: 会议室对象列表 
    :type meeting_room_list: Optional[List[V1MeetingRoomsGet200ResponseMeetingRoomListInner]]

    :param total_count: 数据总条数 
    :type total_count: Optional[int]

    :param total_page: 数据总页数 
    :type total_page: Optional[int]
    """  # noqa: E501

    current_page: Optional[int] = None
    current_size: Optional[int] = None
    meeting_room_list: Optional[List[V1MeetingRoomsGet200ResponseMeetingRoomListInner]] = None
    total_count: Optional[int] = None
    total_page: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        current_page: Optional[int] = None,
        current_size: Optional[int] = None,
        meeting_room_list: Optional[List[V1MeetingRoomsGet200ResponseMeetingRoomListInner] | List[Dict[str, Any]]] = None,
        total_count: Optional[int] = None,
        total_page: Optional[int] = None,
        **kwargs
    ):
        self.current_page = current_page
        self.current_size = current_size
        
        if meeting_room_list and isinstance(meeting_room_list, (list, List)):
            self.meeting_room_list = [V1MeetingRoomsGet200ResponseMeetingRoomListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in meeting_room_list]
        
        self.total_count = total_count
        self.total_page = total_page


class V1MeetingRoomsGet200ResponseMeetingRoomListInner(object):
    """V1MeetingRoomsGet200ResponseMeetingRoomListInner

    :param account_new_type: 0:基础版账号 1:专业版账号 
    :type account_new_type: Optional[int]

    :param account_type: 账号类型0:普通，1:专款，2:试用 
    :type account_type: Optional[int]

    :param active_code: 激活码 
    :type active_code: Optional[str]

    :param is_allow_call: 是否允许被呼叫 
    :type is_allow_call: Optional[bool]

    :param meeting_room_id: 会议室ID 
    :type meeting_room_id: Optional[str]

    :param meeting_room_location: 会议室地址 
    :type meeting_room_location: Optional[str]

    :param meeting_room_name: 会议室名称 
    :type meeting_room_name: Optional[str]

    :param meeting_room_status: 会议室状态0:未激活，1:未绑定，2:空闲，3:试用中，4:离线，5:未登录 
    :type meeting_room_status: Optional[int]

    :param participant_number: 容纳人数 
    :type participant_number: Optional[int]

    :param scheduled_status: 预定状态 
    :type scheduled_status: Optional[int]
    """  # noqa: E501

    account_new_type: Optional[int] = None
    account_type: Optional[int] = None
    active_code: Optional[str] = None
    is_allow_call: Optional[bool] = None
    meeting_room_id: Optional[str] = None
    meeting_room_location: Optional[str] = None
    meeting_room_name: Optional[str] = None
    meeting_room_status: Optional[int] = None
    participant_number: Optional[int] = None
    scheduled_status: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        account_new_type: Optional[int] = None,
        account_type: Optional[int] = None,
        active_code: Optional[str] = None,
        is_allow_call: Optional[bool] = None,
        meeting_room_id: Optional[str] = None,
        meeting_room_location: Optional[str] = None,
        meeting_room_name: Optional[str] = None,
        meeting_room_status: Optional[int] = None,
        participant_number: Optional[int] = None,
        scheduled_status: Optional[int] = None,
        **kwargs
    ):
        self.account_new_type = account_new_type
        self.account_type = account_type
        self.active_code = active_code
        self.is_allow_call = is_allow_call
        self.meeting_room_id = meeting_room_id
        self.meeting_room_location = meeting_room_location
        self.meeting_room_name = meeting_room_name
        self.meeting_room_status = meeting_room_status
        self.participant_number = participant_number
        self.scheduled_status = scheduled_status


class V1MeetingRoomsMeetingRoomIdActiveCodePost200Response(object):
    """V1MeetingRoomsMeetingRoomIdActiveCodePost200Response

    :param active_code: 激活码 
    :type active_code: Optional[str]
    """  # noqa: E501

    active_code: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        active_code: Optional[str] = None,
        **kwargs
    ):
        self.active_code = active_code


class V1MeetingRoomsMeetingRoomIdBackgroundGet200Response(object):
    """V1MeetingRoomsMeetingRoomIdBackgroundGet200Response

    :param background_image: 背景图片地址 
    :type background_image: Optional[str]
    """  # noqa: E501

    background_image: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        background_image: Optional[str] = None,
        **kwargs
    ):
        self.background_image = background_image


class V1MeetingRoomsMeetingRoomIdBackgroundPost200Response(object):
    """V1MeetingRoomsMeetingRoomIdBackgroundPost200Response

    :param job_id:
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


class V1MeetingRoomsMeetingRoomIdBackgroundPostRequest(object):
    """V1MeetingRoomsMeetingRoomIdBackgroundPostRequest

    :param background_image: 不传或者传空则设置为默认背景，目前只能设置一张 背景图片地址，1920*1080,大小10M以内，png/jpg/jpeg格式 
    :type background_image: Optional[str]

    :param operator_id:(required) 
    :type operator_id: str

    :param operator_id_type: 1:userid (required) 
    :type operator_id_type: int
    """  # noqa: E501

    background_image: Optional[str] = None
    operator_id: str
    operator_id_type: int
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        operator_id: str,
        operator_id_type: int,
        background_image: Optional[str] = None,
        **kwargs
    ):
        self.background_image = background_image
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type


class V1MeetingRoomsMeetingRoomIdGet200Response(object):
    """V1MeetingRoomsMeetingRoomIdGet200Response

    :param account_info:
    :type account_info: Optional[V1MeetingRoomsMeetingRoomIdGet200ResponseAccountInfo]

    :param basic_info:
    :type basic_info: Optional[V1MeetingRoomsMeetingRoomIdGet200ResponseBasicInfo]

    :param hardware_info:
    :type hardware_info: Optional[V1MeetingRoomsMeetingRoomIdGet200ResponseHardwareInfo]

    :param is_allow_call: 是否允许被呼叫，true：是 false：否 
    :type is_allow_call: Optional[bool]

    :param monitor_status: 告警通知状态，0：未开启 1：已开启 
    :type monitor_status: Optional[int]

    :param pmi_info:
    :type pmi_info: Optional[V1MeetingRoomsMeetingRoomIdGet200ResponsePmiInfo]

    :param scheduled_status: 预定状态： 0：未开放预定 1：开放预定 
    :type scheduled_status: Optional[int]
    """  # noqa: E501

    account_info: Optional[V1MeetingRoomsMeetingRoomIdGet200ResponseAccountInfo] = None
    basic_info: Optional[V1MeetingRoomsMeetingRoomIdGet200ResponseBasicInfo] = None
    hardware_info: Optional[V1MeetingRoomsMeetingRoomIdGet200ResponseHardwareInfo] = None
    is_allow_call: Optional[bool] = None
    monitor_status: Optional[int] = None
    pmi_info: Optional[V1MeetingRoomsMeetingRoomIdGet200ResponsePmiInfo] = None
    scheduled_status: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        account_info: Optional[V1MeetingRoomsMeetingRoomIdGet200ResponseAccountInfo | Dict[str, Any]] = None,
        basic_info: Optional[V1MeetingRoomsMeetingRoomIdGet200ResponseBasicInfo | Dict[str, Any]] = None,
        hardware_info: Optional[V1MeetingRoomsMeetingRoomIdGet200ResponseHardwareInfo | Dict[str, Any]] = None,
        is_allow_call: Optional[bool] = None,
        monitor_status: Optional[int] = None,
        pmi_info: Optional[V1MeetingRoomsMeetingRoomIdGet200ResponsePmiInfo | Dict[str, Any]] = None,
        scheduled_status: Optional[int] = None,
        **kwargs
    ):
        self.account_info = V1MeetingRoomsMeetingRoomIdGet200ResponseAccountInfo(**account_info) if isinstance(account_info, (dict, Dict)) else account_info
        self.basic_info = V1MeetingRoomsMeetingRoomIdGet200ResponseBasicInfo(**basic_info) if isinstance(basic_info, (dict, Dict)) else basic_info
        self.hardware_info = V1MeetingRoomsMeetingRoomIdGet200ResponseHardwareInfo(**hardware_info) if isinstance(hardware_info, (dict, Dict)) else hardware_info
        self.is_allow_call = is_allow_call
        self.monitor_status = monitor_status
        self.pmi_info = V1MeetingRoomsMeetingRoomIdGet200ResponsePmiInfo(**pmi_info) if isinstance(pmi_info, (dict, Dict)) else pmi_info
        self.scheduled_status = scheduled_status


class V1MeetingRoomsMeetingRoomIdGet200ResponseAccountInfo(object):
    """会议室账号信息

    :param account_new_type:
    :type account_new_type: Optional[int]

    :param account_type: 账号类型，0：普通 1：专款 2：试用 
    :type account_type: Optional[int]

    :param pro_account_type: 1-预装 2-体验 3-付费 
    :type pro_account_type: Optional[int]

    :param valid_period: 有效期限 
    :type valid_period: Optional[str]
    """  # noqa: E501

    account_new_type: Optional[int] = None
    account_type: Optional[int] = None
    pro_account_type: Optional[int] = None
    valid_period: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        account_new_type: Optional[int] = None,
        account_type: Optional[int] = None,
        pro_account_type: Optional[int] = None,
        valid_period: Optional[str] = None,
        **kwargs
    ):
        self.account_new_type = account_new_type
        self.account_type = account_type
        self.pro_account_type = pro_account_type
        self.valid_period = valid_period


class V1MeetingRoomsMeetingRoomIdGet200ResponseBasicInfo(object):
    """会议室基本信息

    :param building: 建筑 
    :type building: Optional[str]

    :param city: 城市 
    :type city: Optional[str]

    :param desc: 描述（base64） 
    :type desc: Optional[str]

    :param device: 会议室设备 
    :type device: Optional[str]

    :param floor: 楼层 
    :type floor: Optional[str]

    :param meeting_room_name: 会议室名称 
    :type meeting_room_name: Optional[str]

    :param participant_number: 容纳人数 
    :type participant_number: Optional[int]

    :param password: 管理员密码（base64） 
    :type password: Optional[str]
    """  # noqa: E501

    building: Optional[str] = None
    city: Optional[str] = None
    desc: Optional[str] = None
    device: Optional[str] = None
    floor: Optional[str] = None
    meeting_room_name: Optional[str] = None
    participant_number: Optional[int] = None
    password: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        building: Optional[str] = None,
        city: Optional[str] = None,
        desc: Optional[str] = None,
        device: Optional[str] = None,
        floor: Optional[str] = None,
        meeting_room_name: Optional[str] = None,
        participant_number: Optional[int] = None,
        password: Optional[str] = None,
        **kwargs
    ):
        self.building = building
        self.city = city
        self.desc = desc
        self.device = device
        self.floor = floor
        self.meeting_room_name = meeting_room_name
        self.participant_number = participant_number
        self.password = password


class V1MeetingRoomsMeetingRoomIdGet200ResponseHardwareInfo(object):
    """会议室硬件信息

    :param active_time: 激活时间 
    :type active_time: Optional[str]

    :param camera_model: 摄像头型号 
    :type camera_model: Optional[str]

    :param cpu_info: CPU信息 
    :type cpu_info: Optional[str]

    :param cpu_usage: CPU最大占用率 
    :type cpu_usage: Optional[str]

    :param device_model: 设备型号 
    :type device_model: Optional[str]

    :param enable_video_mirror: 是否开启视频镜像 
    :type enable_video_mirror: Optional[bool]

    :param factory: 厂家 
    :type factory: Optional[str]

    :param firmware_version: 固件版本 
    :type firmware_version: Optional[str]

    :param gpu_info: GPU信息 
    :type gpu_info: Optional[str]

    :param health_status: 健康状况 
    :type health_status: Optional[str]

    :param ip: ip地址 
    :type ip: Optional[str]

    :param mac: MAC地址 
    :type mac: Optional[str]

    :param meeting_room_status: 会议室状态 
    :type meeting_room_status: Optional[int]

    :param memory_info: 内存信息 
    :type memory_info: Optional[str]

    :param microphone_info: 麦克风信息 
    :type microphone_info: Optional[str]

    :param monitor_frequency: 显示器刷新率 
    :type monitor_frequency: Optional[int]

    :param net_type: 网络类型 
    :type net_type: Optional[str]

    :param rooms_version: Rooms版本 
    :type rooms_version: Optional[str]

    :param sn: 序列号 
    :type sn: Optional[str]

    :param speaker_info: 扬声器信息 
    :type speaker_info: Optional[str]

    :param system_type: 设备系统 
    :type system_type: Optional[str]
    """  # noqa: E501

    active_time: Optional[str] = None
    camera_model: Optional[str] = None
    cpu_info: Optional[str] = None
    cpu_usage: Optional[str] = None
    device_model: Optional[str] = None
    enable_video_mirror: Optional[bool] = None
    factory: Optional[str] = None
    firmware_version: Optional[str] = None
    gpu_info: Optional[str] = None
    health_status: Optional[str] = None
    ip: Optional[str] = None
    mac: Optional[str] = None
    meeting_room_status: Optional[int] = None
    memory_info: Optional[str] = None
    microphone_info: Optional[str] = None
    monitor_frequency: Optional[int] = None
    net_type: Optional[str] = None
    rooms_version: Optional[str] = None
    sn: Optional[str] = None
    speaker_info: Optional[str] = None
    system_type: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        active_time: Optional[str] = None,
        camera_model: Optional[str] = None,
        cpu_info: Optional[str] = None,
        cpu_usage: Optional[str] = None,
        device_model: Optional[str] = None,
        enable_video_mirror: Optional[bool] = None,
        factory: Optional[str] = None,
        firmware_version: Optional[str] = None,
        gpu_info: Optional[str] = None,
        health_status: Optional[str] = None,
        ip: Optional[str] = None,
        mac: Optional[str] = None,
        meeting_room_status: Optional[int] = None,
        memory_info: Optional[str] = None,
        microphone_info: Optional[str] = None,
        monitor_frequency: Optional[int] = None,
        net_type: Optional[str] = None,
        rooms_version: Optional[str] = None,
        sn: Optional[str] = None,
        speaker_info: Optional[str] = None,
        system_type: Optional[str] = None,
        **kwargs
    ):
        self.active_time = active_time
        self.camera_model = camera_model
        self.cpu_info = cpu_info
        self.cpu_usage = cpu_usage
        self.device_model = device_model
        self.enable_video_mirror = enable_video_mirror
        self.factory = factory
        self.firmware_version = firmware_version
        self.gpu_info = gpu_info
        self.health_status = health_status
        self.ip = ip
        self.mac = mac
        self.meeting_room_status = meeting_room_status
        self.memory_info = memory_info
        self.microphone_info = microphone_info
        self.monitor_frequency = monitor_frequency
        self.net_type = net_type
        self.rooms_version = rooms_version
        self.sn = sn
        self.speaker_info = speaker_info
        self.system_type = system_type


class V1MeetingRoomsMeetingRoomIdGet200ResponsePmiInfo(object):
    """会议室 PMI 信息

    :param pmi_code: 设备会议号 
    :type pmi_code: Optional[str]

    :param pmi_pwd: 设备入会密码 
    :type pmi_pwd: Optional[str]
    """  # noqa: E501

    pmi_code: Optional[str] = None
    pmi_pwd: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        pmi_code: Optional[str] = None,
        pmi_pwd: Optional[str] = None,
        **kwargs
    ):
        self.pmi_code = pmi_code
        self.pmi_pwd = pmi_pwd


class V1MeetingRoomsModifyPutRequest(object):
    """V1MeetingRoomsModifyPutRequest

    :param instance_id:(required) 
    :type instance_id: int

    :param is_allow_call: 是否允许被呼叫 
    :type is_allow_call: Optional[bool]

    :param meeting_room_id: 要设置的会议室 ID。 (required) 
    :type meeting_room_id: str

    :param meeting_room_info:
    :type meeting_room_info: Optional[V1MeetingRoomsModifyPutRequestMeetingRoomInfo]

    :param operator_id: 操作者 ID。operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 (required) 
    :type operator_id: str

    :param operator_id_type: 操作者 ID 的类型： 1：userid (required) 
    :type operator_id_type: int

    :param scheduled_status: 是否开放预定初始值false 
    :type scheduled_status: Optional[bool]
    """  # noqa: E501

    instance_id: int
    is_allow_call: Optional[bool] = None
    meeting_room_id: str
    meeting_room_info: Optional[V1MeetingRoomsModifyPutRequestMeetingRoomInfo] = None
    operator_id: str
    operator_id_type: int
    scheduled_status: Optional[bool] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        instance_id: int,
        meeting_room_id: str,
        operator_id: str,
        operator_id_type: int,
        is_allow_call: Optional[bool] = None,
        meeting_room_info: Optional[V1MeetingRoomsModifyPutRequestMeetingRoomInfo | Dict[str, Any]] = None,
        scheduled_status: Optional[bool] = None,
        **kwargs
    ):
        self.instance_id = instance_id
        self.is_allow_call = is_allow_call
        self.meeting_room_id = meeting_room_id
        self.meeting_room_info = V1MeetingRoomsModifyPutRequestMeetingRoomInfo(**meeting_room_info) if isinstance(meeting_room_info, (dict, Dict)) else meeting_room_info
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.scheduled_status = scheduled_status


class V1MeetingRoomsModifyPutRequestMeetingRoomInfo(object):
    """编辑会议室基本信息

    :param building: 建筑。若非输入城市下现有建筑则自动创建该建筑与楼层。长度不超过36个字符或18个汉字。 
    :type building: Optional[str]

    :param city: 城市。若非已添加城市则自动创建城市及建筑与楼层。长度不超过36个字符或18个汉字。city、building、floor 需同时传入或都不传入。 
    :type city: Optional[str]

    :param desc: 描述（base64）。长度不超过1000个字符。 
    :type desc: Optional[str]

    :param device: 会议室设备，输入非现有类型内容则无效。设备类型有：TV，投影，会议电话机，MIC，视频电视，PC，无线投屏。 
    :type device: Optional[List[str]]

    :param floor: 楼层。若非输入建筑下现有楼层则自动创建楼层。输入应为数字或字母，长度不超过36个字符。 
    :type floor: Optional[str]

    :param meeting_room_name: 会议室名称。长度不超过36个字符。 (required) 
    :type meeting_room_name: str

    :param meeting_room_type: 会议室类型。 0：rooms 会议室 1：无类型会议室 2：SIP 会议室 4：H.323 会议室 (required) 
    :type meeting_room_type: int

    :param mra_address: 会议室信令地址。会议室类型为2或4时必填写，与mra_register_account 二选一。 
    :type mra_address: Optional[str]

    :param mra_register_account: SIP/ H.323注册账号。会议室类型为2或4时填写。 
    :type mra_register_account: Optional[str]

    :param participant_number: 容纳人数。不超过9位数。 
    :type participant_number: Optional[int]

    :param password: 使用管理员密码时必须填写管理员密码（base64）。若不使用密码，该字段无效。输入应为1-16位的数字、字母或字符。 
    :type password: Optional[str]

    :param use_password: 会议室类型为1时选择是否使用管理员密码，默认为 false。 true：使用 false：不使用 
    :type use_password: Optional[bool]
    """  # noqa: E501

    building: Optional[str] = None
    city: Optional[str] = None
    desc: Optional[str] = None
    device: Optional[List[str]] = None
    floor: Optional[str] = None
    meeting_room_name: str
    meeting_room_type: int
    mra_address: Optional[str] = None
    mra_register_account: Optional[str] = None
    participant_number: Optional[int] = None
    password: Optional[str] = None
    use_password: Optional[bool] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        meeting_room_name: str,
        meeting_room_type: int,
        building: Optional[str] = None,
        city: Optional[str] = None,
        desc: Optional[str] = None,
        device: Optional[List[str]] = None,
        floor: Optional[str] = None,
        mra_address: Optional[str] = None,
        mra_register_account: Optional[str] = None,
        participant_number: Optional[int] = None,
        password: Optional[str] = None,
        use_password: Optional[bool] = None,
        **kwargs
    ):
        self.building = building
        self.city = city
        self.desc = desc
        
        if device and isinstance(device, (list, List)):
            self.device = device
        
        self.floor = floor
        self.meeting_room_name = meeting_room_name
        self.meeting_room_type = meeting_room_type
        self.mra_address = mra_address
        self.mra_register_account = mra_register_account
        self.participant_number = participant_number
        self.password = password
        self.use_password = use_password


class V1MeetingRoomsModifyRoomConfigInfoPostRequest(object):
    """V1MeetingRoomsModifyRoomConfigInfoPostRequest

    :param instance_id:(required) 
    :type instance_id: int

    :param meeting_room_id: 要配置的会议室 ID。 (required) 
    :type meeting_room_id: str

    :param meeting_settings:
    :type meeting_settings: Optional[V1MeetingRoomsModifyRoomConfigInfoPostRequestMeetingSettings]

    :param operator_id:(required) 
    :type operator_id: str

    :param operator_id_type:(required) 
    :type operator_id_type: int

    :param record_settings:
    :type record_settings: Optional[V1MeetingRoomsModifyRoomConfigInfoPostRequestRecordSettings]
    """  # noqa: E501

    instance_id: int
    meeting_room_id: str
    meeting_settings: Optional[V1MeetingRoomsModifyRoomConfigInfoPostRequestMeetingSettings] = None
    operator_id: str
    operator_id_type: int
    record_settings: Optional[V1MeetingRoomsModifyRoomConfigInfoPostRequestRecordSettings] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        instance_id: int,
        meeting_room_id: str,
        operator_id: str,
        operator_id_type: int,
        meeting_settings: Optional[V1MeetingRoomsModifyRoomConfigInfoPostRequestMeetingSettings | Dict[str, Any]] = None,
        record_settings: Optional[V1MeetingRoomsModifyRoomConfigInfoPostRequestRecordSettings | Dict[str, Any]] = None,
        **kwargs
    ):
        self.instance_id = instance_id
        self.meeting_room_id = meeting_room_id
        self.meeting_settings = V1MeetingRoomsModifyRoomConfigInfoPostRequestMeetingSettings(**meeting_settings) if isinstance(meeting_settings, (dict, Dict)) else meeting_settings
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.record_settings = V1MeetingRoomsModifyRoomConfigInfoPostRequestRecordSettings(**record_settings) if isinstance(record_settings, (dict, Dict)) else record_settings


class V1MeetingRoomsModifyRoomConfigInfoPostRequestMeetingSettings(object):
    """V1MeetingRoomsModifyRoomConfigInfoPostRequestMeetingSettings

    :param auto_response: 自动接听，初始值为 false。 1：开启 2：关闭 
    :type auto_response: Optional[int]

    :param caption: 字幕，初始值为 true。 true：开启 false：关闭 
    :type caption: Optional[bool]

    :param room_notification: Rooms 屏幕是否展示消息通知，初始值为 false。 true：开启 false：不开启 
    :type room_notification: Optional[bool]

    :param room_pmi: 专属 ID，初始值为 true。 true：开启 false：关闭 
    :type room_pmi: Optional[bool]

    :param room_pmi_settings:
    :type room_pmi_settings: Optional[V1MeetingRoomsModifyRoomConfigInfoPostRequestMeetingSettingsRoomPmiSettings]

    :param water_mark: 水印，初始值为2。 0：关闭 1：单排水印 2：多排水印 
    :type water_mark: Optional[int]
    """  # noqa: E501

    auto_response: Optional[int] = None
    caption: Optional[bool] = None
    room_notification: Optional[bool] = None
    room_pmi: Optional[bool] = None
    room_pmi_settings: Optional[V1MeetingRoomsModifyRoomConfigInfoPostRequestMeetingSettingsRoomPmiSettings] = None
    water_mark: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        auto_response: Optional[int] = None,
        caption: Optional[bool] = None,
        room_notification: Optional[bool] = None,
        room_pmi: Optional[bool] = None,
        room_pmi_settings: Optional[V1MeetingRoomsModifyRoomConfigInfoPostRequestMeetingSettingsRoomPmiSettings | Dict[str, Any]] = None,
        water_mark: Optional[int] = None,
        **kwargs
    ):
        self.auto_response = auto_response
        self.caption = caption
        self.room_notification = room_notification
        self.room_pmi = room_pmi
        self.room_pmi_settings = V1MeetingRoomsModifyRoomConfigInfoPostRequestMeetingSettingsRoomPmiSettings(**room_pmi_settings) if isinstance(room_pmi_settings, (dict, Dict)) else room_pmi_settings
        self.water_mark = water_mark


class V1MeetingRoomsModifyRoomConfigInfoPostRequestMeetingSettingsRoomPmiSettings(object):
    """V1MeetingRoomsModifyRoomConfigInfoPostRequestMeetingSettingsRoomPmiSettings

    :param allow_in_before_host:
    :type allow_in_before_host: Optional[bool]

    :param mute_enable_type_join:
    :type mute_enable_type_join: Optional[int]

    :param only_enterprise_user_allowed:
    :type only_enterprise_user_allowed: Optional[bool]

    :param room_pmi_psw:
    :type room_pmi_psw: Optional[str]

    :param waiting_room:
    :type waiting_room: Optional[bool]
    """  # noqa: E501

    allow_in_before_host: Optional[bool] = None
    mute_enable_type_join: Optional[int] = None
    only_enterprise_user_allowed: Optional[bool] = None
    room_pmi_psw: Optional[str] = None
    waiting_room: Optional[bool] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        allow_in_before_host: Optional[bool] = None,
        mute_enable_type_join: Optional[int] = None,
        only_enterprise_user_allowed: Optional[bool] = None,
        room_pmi_psw: Optional[str] = None,
        waiting_room: Optional[bool] = None,
        **kwargs
    ):
        self.allow_in_before_host = allow_in_before_host
        self.mute_enable_type_join = mute_enable_type_join
        self.only_enterprise_user_allowed = only_enterprise_user_allowed
        self.room_pmi_psw = room_pmi_psw
        self.waiting_room = waiting_room


class V1MeetingRoomsModifyRoomConfigInfoPostRequestRecordSettings(object):
    """V1MeetingRoomsModifyRoomConfigInfoPostRequestRecordSettings

    :param download_record: 是否允许下载云录制，初始值为 false。 true：开启 false：关闭 
    :type download_record: Optional[bool]

    :param share_record: 分享云录制，初始值为1。 0：关闭分享 1：全部成员可查看 2：仅登录成员可查看 3：仅同企业成员可查看 4：仅参会成员可查看 
    :type share_record: Optional[int]
    """  # noqa: E501

    download_record: Optional[bool] = None
    share_record: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        download_record: Optional[bool] = None,
        share_record: Optional[int] = None,
        **kwargs
    ):
        self.download_record = download_record
        self.share_record = share_record


class V1MeetingRoomsMonitorDeviceControllerInfoGet200Response(object):
    """V1MeetingRoomsMonitorDeviceControllerInfoGet200Response

    :param controller_info_list: 控制器信息对象 
    :type controller_info_list: Optional[List[V1MeetingRoomsMonitorDeviceControllerInfoGet200ResponseControllerInfoListInner]]

    :param current_page: 分页查询返回当前页码。 
    :type current_page: Optional[int]

    :param current_size: 分页查询返回单页数据条数。 
    :type current_size: Optional[int]

    :param total_count: 分页查询返回数据总数。 
    :type total_count: Optional[int]

    :param total_page: 分页查询返回分页总数。 
    :type total_page: Optional[int]
    """  # noqa: E501

    controller_info_list: Optional[List[V1MeetingRoomsMonitorDeviceControllerInfoGet200ResponseControllerInfoListInner]] = None
    current_page: Optional[int] = None
    current_size: Optional[int] = None
    total_count: Optional[int] = None
    total_page: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        controller_info_list: Optional[List[V1MeetingRoomsMonitorDeviceControllerInfoGet200ResponseControllerInfoListInner] | List[Dict[str, Any]]] = None,
        current_page: Optional[int] = None,
        current_size: Optional[int] = None,
        total_count: Optional[int] = None,
        total_page: Optional[int] = None,
        **kwargs
    ):
        
        if controller_info_list and isinstance(controller_info_list, (list, List)):
            self.controller_info_list = [V1MeetingRoomsMonitorDeviceControllerInfoGet200ResponseControllerInfoListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in controller_info_list]
        
        self.current_page = current_page
        self.current_size = current_size
        self.total_count = total_count
        self.total_page = total_page


class V1MeetingRoomsMonitorDeviceControllerInfoGet200ResponseControllerInfoListInner(object):
    """V1MeetingRoomsMonitorDeviceControllerInfoGet200ResponseControllerInfoListInner

    :param app_version: 应用程序版本。 
    :type app_version: Optional[str]

    :param controller_model: 控制器型号 
    :type controller_model: Optional[str]

    :param controller_name: 控制器名称 
    :type controller_name: Optional[str]

    :param cpu_type: CPU 类型 
    :type cpu_type: Optional[str]

    :param cpu_usage: CPU 当前占有率 
    :type cpu_usage: Optional[str]

    :param framework_version: 固件版本 
    :type framework_version: Optional[str]

    :param ip_address: IP 地址 
    :type ip_address: Optional[str]

    :param mac_address: MAC 地址 
    :type mac_address: Optional[str]

    :param manufacture_name: 厂商 
    :type manufacture_name: Optional[str]

    :param meeting_room_location: 会议室地址。 
    :type meeting_room_location: Optional[str]

    :param meeting_room_name: 会议室名称。 
    :type meeting_room_name: Optional[str]

    :param mem_usage: 内存使用大小 
    :type mem_usage: Optional[str]

    :param network_type: 网络类型 
    :type network_type: Optional[str]

    :param rooms_id: 会议室 ID。 
    :type rooms_id: Optional[str]

    :param status: 设备状态；0:离线 1:在线 
    :type status: Optional[str]
    """  # noqa: E501

    app_version: Optional[str] = None
    controller_model: Optional[str] = None
    controller_name: Optional[str] = None
    cpu_type: Optional[str] = None
    cpu_usage: Optional[str] = None
    framework_version: Optional[str] = None
    ip_address: Optional[str] = None
    mac_address: Optional[str] = None
    manufacture_name: Optional[str] = None
    meeting_room_location: Optional[str] = None
    meeting_room_name: Optional[str] = None
    mem_usage: Optional[str] = None
    network_type: Optional[str] = None
    rooms_id: Optional[str] = None
    status: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        app_version: Optional[str] = None,
        controller_model: Optional[str] = None,
        controller_name: Optional[str] = None,
        cpu_type: Optional[str] = None,
        cpu_usage: Optional[str] = None,
        framework_version: Optional[str] = None,
        ip_address: Optional[str] = None,
        mac_address: Optional[str] = None,
        manufacture_name: Optional[str] = None,
        meeting_room_location: Optional[str] = None,
        meeting_room_name: Optional[str] = None,
        mem_usage: Optional[str] = None,
        network_type: Optional[str] = None,
        rooms_id: Optional[str] = None,
        status: Optional[str] = None,
        **kwargs
    ):
        self.app_version = app_version
        self.controller_model = controller_model
        self.controller_name = controller_name
        self.cpu_type = cpu_type
        self.cpu_usage = cpu_usage
        self.framework_version = framework_version
        self.ip_address = ip_address
        self.mac_address = mac_address
        self.manufacture_name = manufacture_name
        self.meeting_room_location = meeting_room_location
        self.meeting_room_name = meeting_room_name
        self.mem_usage = mem_usage
        self.network_type = network_type
        self.rooms_id = rooms_id
        self.status = status


class V1MeetingRoomsOperatorIdMeetingsGet200Response(object):
    """V1MeetingRoomsOperatorIdMeetingsGet200Response

    :param current_page: 当前页。 
    :type current_page: Optional[int]

    :param current_size: 当前实际页大小。 
    :type current_size: Optional[int]

    :param meeting_info_list:
    :type meeting_info_list: Optional[List[V1MeetingRoomsOperatorIdMeetingsGet200ResponseMeetingInfoListInner]]

    :param total_count: 数据总条数。 
    :type total_count: Optional[int]

    :param total_page: 数据总页数。 
    :type total_page: Optional[int]
    """  # noqa: E501

    current_page: Optional[int] = None
    current_size: Optional[int] = None
    meeting_info_list: Optional[List[V1MeetingRoomsOperatorIdMeetingsGet200ResponseMeetingInfoListInner]] = None
    total_count: Optional[int] = None
    total_page: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        current_page: Optional[int] = None,
        current_size: Optional[int] = None,
        meeting_info_list: Optional[List[V1MeetingRoomsOperatorIdMeetingsGet200ResponseMeetingInfoListInner] | List[Dict[str, Any]]] = None,
        total_count: Optional[int] = None,
        total_page: Optional[int] = None,
        **kwargs
    ):
        self.current_page = current_page
        self.current_size = current_size
        
        if meeting_info_list and isinstance(meeting_info_list, (list, List)):
            self.meeting_info_list = [V1MeetingRoomsOperatorIdMeetingsGet200ResponseMeetingInfoListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in meeting_info_list]
        
        self.total_count = total_count
        self.total_page = total_page


class V1MeetingRoomsOperatorIdMeetingsGet200ResponseMeetingInfoListInner(object):
    """会议对象列表。

    :param end_time: 会议预订结束时间（Unix 秒）。 
    :type end_time: Optional[int]

    :param meeting_code: 有效会议 Code。PMI会议需返回PMI号，不是真实的meeting_code 
    :type meeting_code: Optional[str]

    :param meeting_id: 会议 ID。 
    :type meeting_id: Optional[str]

    :param meeting_type: 会议类型(0-一次性会议，1-周期性会议，2-微信专属会议，4-rooms投屏会议，5-个人会议号会议，6-网络研讨会（Webinar）) 
    :type meeting_type: Optional[int]

    :param start_time: 会议预订开始时间（Unix 秒）。 
    :type start_time: Optional[int]

    :param status: 会议状态。 
    :type status: Optional[str]

    :param subject: 会议主题。 
    :type subject: Optional[str]
    """  # noqa: E501

    end_time: Optional[int] = None
    meeting_code: Optional[str] = None
    meeting_id: Optional[str] = None
    meeting_type: Optional[int] = None
    start_time: Optional[int] = None
    status: Optional[str] = None
    subject: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        end_time: Optional[int] = None,
        meeting_code: Optional[str] = None,
        meeting_id: Optional[str] = None,
        meeting_type: Optional[int] = None,
        start_time: Optional[int] = None,
        status: Optional[str] = None,
        subject: Optional[str] = None,
        **kwargs
    ):
        self.end_time = end_time
        self.meeting_code = meeting_code
        self.meeting_id = meeting_id
        self.meeting_type = meeting_type
        self.start_time = start_time
        self.status = status
        self.subject = subject


class V1MeetingRoomsRoomCallInfoPost200Response(object):
    """V1MeetingRoomsRoomCallInfoPost200Response

    :param response_time: 最近一次应答时间。 
    :type response_time: Optional[str]

    :param status: 应答状态： 0：无应答，60秒无回应 1：未呼叫 2：入会中 3：被拒绝 4：呼叫中 5：取消呼叫（仅 Rooms 会议室有该状态） 6：已离会 
    :type status: Optional[int]
    """  # noqa: E501

    response_time: Optional[str] = None
    status: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        response_time: Optional[str] = None,
        status: Optional[int] = None,
        **kwargs
    ):
        self.response_time = response_time
        self.status = status


class V1MeetingRoomsRoomCallInfoPostRequest(object):
    """V1MeetingRoomsRoomCallInfoPostRequest

    :param instance_id:(required) 
    :type instance_id: int

    :param meeting_id: 会议ID (required) 
    :type meeting_id: str

    :param meeting_room_id: 会议室 ID，与 mra_address 二选一。 
    :type meeting_room_id: Optional[str]

    :param mra_address:
    :type mra_address: Optional[V1MeetingRoomsCancelRoomCallPutRequestMraAddress]

    :param operator_id:(required) 
    :type operator_id: str

    :param operator_id_type: 操作者 ID 的类型： 1：userid (required) 
    :type operator_id_type: int
    """  # noqa: E501

    instance_id: int
    meeting_id: str
    meeting_room_id: Optional[str] = None
    mra_address: Optional[V1MeetingRoomsCancelRoomCallPutRequestMraAddress] = None
    operator_id: str
    operator_id_type: int
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        instance_id: int,
        meeting_id: str,
        operator_id: str,
        operator_id_type: int,
        meeting_room_id: Optional[str] = None,
        mra_address: Optional[V1MeetingRoomsCancelRoomCallPutRequestMraAddress | Dict[str, Any]] = None,
        **kwargs
    ):
        self.instance_id = instance_id
        self.meeting_id = meeting_id
        self.meeting_room_id = meeting_room_id
        self.mra_address = V1MeetingRoomsCancelRoomCallPutRequestMraAddress(**mra_address) if isinstance(mra_address, (dict, Dict)) else mra_address
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type


class V1MeetingRoomsRoomCallPut200Response(object):
    """V1MeetingRoomsRoomCallPut200Response

    :param invite_id: 呼叫ID 
    :type invite_id: Optional[str]
    """  # noqa: E501

    invite_id: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        invite_id: Optional[str] = None,
        **kwargs
    ):
        self.invite_id = invite_id


class V1MeetingRoomsRoomCallPutRequest(object):
    """V1MeetingRoomsRoomCallPutRequest

    :param meeting_id: 会议ID (required) 
    :type meeting_id: int

    :param meeting_room_id: 会议室 ID，与 mra_address 二选一。 
    :type meeting_room_id: Optional[str]

    :param mra_address:
    :type mra_address: Optional[V1MeetingRoomsCancelRoomCallPutRequestMraAddress]

    :param operator_id:(required) 
    :type operator_id: str

    :param operator_id_type: 操作者 ID 的类型： 1：userid (required) 
    :type operator_id_type: int
    """  # noqa: E501

    meeting_id: int
    meeting_room_id: Optional[str] = None
    mra_address: Optional[V1MeetingRoomsCancelRoomCallPutRequestMraAddress] = None
    operator_id: str
    operator_id_type: int
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        meeting_id: int,
        operator_id: str,
        operator_id_type: int,
        meeting_room_id: Optional[str] = None,
        mra_address: Optional[V1MeetingRoomsCancelRoomCallPutRequestMraAddress | Dict[str, Any]] = None,
        **kwargs
    ):
        self.meeting_id = meeting_id
        self.meeting_room_id = meeting_room_id
        self.mra_address = V1MeetingRoomsCancelRoomCallPutRequestMraAddress(**mra_address) if isinstance(mra_address, (dict, Dict)) else mra_address
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type


class V1MeetingRoomsRoomConfigInfoPost200Response(object):
    """V1MeetingRoomsRoomConfigInfoPost200Response

    :param meeting_settings:
    :type meeting_settings: Optional[V1MeetingRoomsRoomConfigInfoPost200ResponseMeetingSettings]

    :param record_settings:
    :type record_settings: Optional[V1MeetingRoomsRoomConfigInfoPost200ResponseRecordSettings]
    """  # noqa: E501

    meeting_settings: Optional[V1MeetingRoomsRoomConfigInfoPost200ResponseMeetingSettings] = None
    record_settings: Optional[V1MeetingRoomsRoomConfigInfoPost200ResponseRecordSettings] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        meeting_settings: Optional[V1MeetingRoomsRoomConfigInfoPost200ResponseMeetingSettings | Dict[str, Any]] = None,
        record_settings: Optional[V1MeetingRoomsRoomConfigInfoPost200ResponseRecordSettings | Dict[str, Any]] = None,
        **kwargs
    ):
        self.meeting_settings = V1MeetingRoomsRoomConfigInfoPost200ResponseMeetingSettings(**meeting_settings) if isinstance(meeting_settings, (dict, Dict)) else meeting_settings
        self.record_settings = V1MeetingRoomsRoomConfigInfoPost200ResponseRecordSettings(**record_settings) if isinstance(record_settings, (dict, Dict)) else record_settings


class V1MeetingRoomsRoomConfigInfoPost200ResponseMeetingSettings(object):
    """会议室会议配置对象

    :param auto_response: 自动接听。 1：开启 2：关闭 
    :type auto_response: Optional[int]

    :param caption: 字幕。 true：开启 false：关闭 
    :type caption: Optional[bool]

    :param room_notification: Rooms 屏幕是否展示消息通知。 true：开启 false：不开启 
    :type room_notification: Optional[bool]

    :param room_pmi: 专属 ID。 true：开启 false：关闭 
    :type room_pmi: Optional[bool]

    :param room_pmi_settings:
    :type room_pmi_settings: Optional[V1MeetingRoomsRoomConfigInfoPost200ResponseMeetingSettingsRoomPmiSettings]

    :param water_mark: 水印。 0：关闭 1：单排水印 2：多排水印 
    :type water_mark: Optional[int]
    """  # noqa: E501

    auto_response: Optional[int] = None
    caption: Optional[bool] = None
    room_notification: Optional[bool] = None
    room_pmi: Optional[bool] = None
    room_pmi_settings: Optional[V1MeetingRoomsRoomConfigInfoPost200ResponseMeetingSettingsRoomPmiSettings] = None
    water_mark: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        auto_response: Optional[int] = None,
        caption: Optional[bool] = None,
        room_notification: Optional[bool] = None,
        room_pmi: Optional[bool] = None,
        room_pmi_settings: Optional[V1MeetingRoomsRoomConfigInfoPost200ResponseMeetingSettingsRoomPmiSettings | Dict[str, Any]] = None,
        water_mark: Optional[int] = None,
        **kwargs
    ):
        self.auto_response = auto_response
        self.caption = caption
        self.room_notification = room_notification
        self.room_pmi = room_pmi
        self.room_pmi_settings = V1MeetingRoomsRoomConfigInfoPost200ResponseMeetingSettingsRoomPmiSettings(**room_pmi_settings) if isinstance(room_pmi_settings, (dict, Dict)) else room_pmi_settings
        self.water_mark = water_mark


class V1MeetingRoomsRoomConfigInfoPost200ResponseMeetingSettingsRoomPmiSettings(object):
    """会议室专属会议号配置，仅专属 ID 开启时有效。

    :param allow_in_before_host: 是否允许成员在主持人进会前入会。 
    :type allow_in_before_host: Optional[bool]

    :param hosts: 会议指定主持人 ID。 
    :type hosts: Optional[List[str]]

    :param mute_enable_type_join: 成员入会静音设置。 0：关闭 1：开启 2：超过6人自动开启 
    :type mute_enable_type_join: Optional[int]

    :param only_enterprise_user_allowed: 入会成员设置。 true：仅企业内部用户可入会 false：所有人可入会 
    :type only_enterprise_user_allowed: Optional[bool]

    :param room_pmi_psw: 专属会议室密码，4-6位数字。 
    :type room_pmi_psw: Optional[str]

    :param waiting_room: 是否开启等候室。 
    :type waiting_room: Optional[bool]
    """  # noqa: E501

    allow_in_before_host: Optional[bool] = None
    hosts: Optional[List[str]] = None
    mute_enable_type_join: Optional[int] = None
    only_enterprise_user_allowed: Optional[bool] = None
    room_pmi_psw: Optional[str] = None
    waiting_room: Optional[bool] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        allow_in_before_host: Optional[bool] = None,
        hosts: Optional[List[str]] = None,
        mute_enable_type_join: Optional[int] = None,
        only_enterprise_user_allowed: Optional[bool] = None,
        room_pmi_psw: Optional[str] = None,
        waiting_room: Optional[bool] = None,
        **kwargs
    ):
        self.allow_in_before_host = allow_in_before_host
        
        if hosts and isinstance(hosts, (list, List)):
            self.hosts = hosts
        
        self.mute_enable_type_join = mute_enable_type_join
        self.only_enterprise_user_allowed = only_enterprise_user_allowed
        self.room_pmi_psw = room_pmi_psw
        self.waiting_room = waiting_room


class V1MeetingRoomsRoomConfigInfoPost200ResponseRecordSettings(object):
    """会议室录制配置对象

    :param download_record: 是否允许下载云录制。 true：开启 false：关闭 
    :type download_record: Optional[bool]

    :param share_record: 分享云录制。 0：关闭分享 1：全部成员可查看 2：仅登录成员可查看 3：仅同企业成员可查看 4：仅参会成员可查看 
    :type share_record: Optional[int]
    """  # noqa: E501

    download_record: Optional[bool] = None
    share_record: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        download_record: Optional[bool] = None,
        share_record: Optional[int] = None,
        **kwargs
    ):
        self.download_record = download_record
        self.share_record = share_record


class V1MeetingRoomsRoomConfigInfoPostRequest(object):
    """V1MeetingRoomsRoomConfigInfoPostRequest

    :param instance_id: 设备类型 ID (required) 
    :type instance_id: int

    :param meeting_room_id: 会议室 ID。 (required) 
    :type meeting_room_id: str

    :param operator_id: 操作者 ID。 operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 (required) 
    :type operator_id: str

    :param operator_id_type: 操作者 ID 的类型： 1：userid (required) 
    :type operator_id_type: int
    """  # noqa: E501

    instance_id: int
    meeting_room_id: str
    operator_id: str
    operator_id_type: int
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        instance_id: int,
        meeting_room_id: str,
        operator_id: str,
        operator_id_type: int,
        **kwargs
    ):
        self.instance_id = instance_id
        self.meeting_room_id = meeting_room_id
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type


class V1MeetingRoomsScreencastCodeRoomsInfoGet200Response(object):
    """V1MeetingRoomsScreencastCodeRoomsInfoGet200Response

    :param api_password: 中控API密码 
    :type api_password: Optional[str]

    :param cs_api_enable: 中控API开关 
    :type cs_api_enable: Optional[bool]

    :param meeting_room_id: 会议室ID 
    :type meeting_room_id: Optional[str]

    :param rooms_id: Rooms ID 
    :type rooms_id: Optional[str]

    :param rooms_ip_list: rooms的IP列表 
    :type rooms_ip_list: Optional[List[str]]
    """  # noqa: E501

    api_password: Optional[str] = None
    cs_api_enable: Optional[bool] = None
    meeting_room_id: Optional[str] = None
    rooms_id: Optional[str] = None
    rooms_ip_list: Optional[List[str]] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        api_password: Optional[str] = None,
        cs_api_enable: Optional[bool] = None,
        meeting_room_id: Optional[str] = None,
        rooms_id: Optional[str] = None,
        rooms_ip_list: Optional[List[str]] = None,
        **kwargs
    ):
        self.api_password = api_password
        self.cs_api_enable = cs_api_enable
        self.meeting_room_id = meeting_room_id
        self.rooms_id = rooms_id
        
        if rooms_ip_list and isinstance(rooms_ip_list, (list, List)):
            self.rooms_ip_list = rooms_ip_list
        


class V1MeetingsMeetingIdBookRoomsPost200Response(object):
    """V1MeetingsMeetingIdBookRoomsPost200Response

    :param meeting_room_list: 会议室对象列表 
    :type meeting_room_list: Optional[List[V1MeetingsMeetingIdBookRoomsPost200ResponseMeetingRoomListInner]]

    :param meeting_room_number: 会议室数量 
    :type meeting_room_number: Optional[int]
    """  # noqa: E501

    meeting_room_list: Optional[List[V1MeetingsMeetingIdBookRoomsPost200ResponseMeetingRoomListInner]] = None
    meeting_room_number: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        meeting_room_list: Optional[List[V1MeetingsMeetingIdBookRoomsPost200ResponseMeetingRoomListInner] | List[Dict[str, Any]]] = None,
        meeting_room_number: Optional[int] = None,
        **kwargs
    ):
        
        if meeting_room_list and isinstance(meeting_room_list, (list, List)):
            self.meeting_room_list = [V1MeetingsMeetingIdBookRoomsPost200ResponseMeetingRoomListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in meeting_room_list]
        
        self.meeting_room_number = meeting_room_number


class V1MeetingsMeetingIdBookRoomsPost200ResponseMeetingRoomListInner(object):
    """V1MeetingsMeetingIdBookRoomsPost200ResponseMeetingRoomListInner

    :param meeting_room_id: 会议室ID 
    :type meeting_room_id: Optional[str]

    :param meeting_room_location: 会议室地址 
    :type meeting_room_location: Optional[str]

    :param meeting_room_name: 会议室名称 
    :type meeting_room_name: Optional[str]
    """  # noqa: E501

    meeting_room_id: Optional[str] = None
    meeting_room_location: Optional[str] = None
    meeting_room_name: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        meeting_room_id: Optional[str] = None,
        meeting_room_location: Optional[str] = None,
        meeting_room_name: Optional[str] = None,
        **kwargs
    ):
        self.meeting_room_id = meeting_room_id
        self.meeting_room_location = meeting_room_location
        self.meeting_room_name = meeting_room_name


class V1MeetingsMeetingIdBookRoomsPostRequest(object):
    """V1MeetingsMeetingIdBookRoomsPostRequest

    :param subject_visible: true：在会议开始前的一小时内，在 Room 上显示会议主题。默认值为 true。 false：在会议开始前的一小时内，在 Room 上不显示会议主题。 说明：该参数并不影响预定时间晚过当前时间一个小时以上的会议。超过一小时的会议默认不显示会议主题。 
    :type subject_visible: Optional[bool]
    """  # noqa: E501

    subject_visible: Optional[bool] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        subject_visible: Optional[bool] = None,
        **kwargs
    ):
        self.subject_visible = subject_visible


class V1RoomsInventoryAccountStatisticsGet200Response(object):
    """V1RoomsInventoryAccountStatisticsGet200Response

    :param custom_used_count: 基础版账号使用数 
    :type custom_used_count: Optional[int]

    :param pro_count: 专业版账号数 
    :type pro_count: Optional[int]

    :param pro_used_count: 专业版账号使用数 
    :type pro_used_count: Optional[int]
    """  # noqa: E501

    custom_used_count: Optional[int] = None
    pro_count: Optional[int] = None
    pro_used_count: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        custom_used_count: Optional[int] = None,
        pro_count: Optional[int] = None,
        pro_used_count: Optional[int] = None,
        **kwargs
    ):
        self.custom_used_count = custom_used_count
        self.pro_count = pro_count
        self.pro_used_count = pro_used_count


class V1RoomsInventoryGet200Response(object):
    """V1RoomsInventoryGet200Response

    :param normal_count: 普通设备数 
    :type normal_count: Optional[int]

    :param normal_expired_count: 普通设备过期数 
    :type normal_expired_count: Optional[int]

    :param normal_used_count: 普通设备使用数 
    :type normal_used_count: Optional[int]

    :param special_count: 专款设备数 
    :type special_count: Optional[int]

    :param special_expired_count: 专款设备过期数 
    :type special_expired_count: Optional[int]

    :param special_used_count: 专款设备使用数 
    :type special_used_count: Optional[int]
    """  # noqa: E501

    normal_count: Optional[int] = None
    normal_expired_count: Optional[int] = None
    normal_used_count: Optional[int] = None
    special_count: Optional[int] = None
    special_expired_count: Optional[int] = None
    special_used_count: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        normal_count: Optional[int] = None,
        normal_expired_count: Optional[int] = None,
        normal_used_count: Optional[int] = None,
        special_count: Optional[int] = None,
        special_expired_count: Optional[int] = None,
        special_used_count: Optional[int] = None,
        **kwargs
    ):
        self.normal_count = normal_count
        self.normal_expired_count = normal_expired_count
        self.normal_used_count = normal_used_count
        self.special_count = special_count
        self.special_expired_count = special_expired_count
        self.special_used_count = special_used_count

