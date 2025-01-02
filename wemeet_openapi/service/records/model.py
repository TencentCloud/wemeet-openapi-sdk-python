# coding: utf-8

"""
    腾讯会议OpenAPI

    SAAS版RESTFUL风格API

    API version: v1.0.4

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

from typing import *


class V1AddressesGet200Response(object):
    """V1AddressesGet200Response

    :param current_page: 当前页 
    :type current_page: Optional[int]

    :param current_size: 当前size 
    :type current_size: Optional[int]

    :param meeting_code: 会议 code。 
    :type meeting_code: Optional[str]

    :param meeting_id: 会议唯一 ID。 
    :type meeting_id: Optional[str]

    :param meeting_record_id: 会议录制 ID。 
    :type meeting_record_id: Optional[str]

    :param record_files: 录制文件列表。 
    :type record_files: Optional[List[V1AddressesGet200ResponseRecordFilesInner]]

    :param subject: 会议主题。 
    :type subject: Optional[str]

    :param total_count: 录制总数 
    :type total_count: Optional[int]

    :param total_page: 总页数 
    :type total_page: Optional[int]
    """  # noqa: E501

    current_page: Optional[int] = None
    current_size: Optional[int] = None
    meeting_code: Optional[str] = None
    meeting_id: Optional[str] = None
    meeting_record_id: Optional[str] = None
    record_files: Optional[List[V1AddressesGet200ResponseRecordFilesInner]] = None
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
        meeting_record_id: Optional[str] = None,
        record_files: Optional[List[V1AddressesGet200ResponseRecordFilesInner] | List[Dict[str, Any]]] = None,
        subject: Optional[str] = None,
        total_count: Optional[int] = None,
        total_page: Optional[int] = None,
        **kwargs
    ):
        self.current_page = current_page
        self.current_size = current_size
        self.meeting_code = meeting_code
        self.meeting_id = meeting_id
        self.meeting_record_id = meeting_record_id
        
        if record_files and isinstance(record_files, (list, List)):
            self.record_files = [V1AddressesGet200ResponseRecordFilesInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in record_files]
        
        self.subject = subject
        self.total_count = total_count
        self.total_page = total_page


class V1AddressesGet200ResponseRecordFilesInner(object):
    """V1AddressesGet200ResponseRecordFilesInner

    :param audio_address: 音频下载地址。OAuth 鉴权方式下，账号类型为个人免费版、企微创建企业时，该值返回为空。 
    :type audio_address: Optional[str]

    :param audio_address_file_type: 下载音频文件格式，例如：m4a。OAuth 鉴权方式下，账号类型为个人免费版、企微创建企业时，该值返回为空。 
    :type audio_address_file_type: Optional[str]

    :param download_address: 下载地址，过期时间6小时。OAuth 鉴权方式下，账号类型为个人免费版、企微创建企业时，该值返回为空。 
    :type download_address: Optional[str]

    :param download_address_file_type: 下载视频文件格式，例如：mp4。 
    :type download_address_file_type: Optional[str]

    :param meeting_summary: 会议纪要文件列表。。OAuth 鉴权方式下，账号类型为个人免费版、企微创建企业时，该值返回为空。 
    :type meeting_summary: Optional[List[V1AddressesGet200ResponseRecordFilesInnerMeetingSummaryInner]]

    :param record_file_id: 录制文件 ID。 
    :type record_file_id: Optional[str]

    :param view_address: 播放地址。 
    :type view_address: Optional[str]
    """  # noqa: E501

    audio_address: Optional[str] = None
    audio_address_file_type: Optional[str] = None
    download_address: Optional[str] = None
    download_address_file_type: Optional[str] = None
    meeting_summary: Optional[List[V1AddressesGet200ResponseRecordFilesInnerMeetingSummaryInner]] = None
    record_file_id: Optional[str] = None
    view_address: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        audio_address: Optional[str] = None,
        audio_address_file_type: Optional[str] = None,
        download_address: Optional[str] = None,
        download_address_file_type: Optional[str] = None,
        meeting_summary: Optional[List[V1AddressesGet200ResponseRecordFilesInnerMeetingSummaryInner] | List[Dict[str, Any]]] = None,
        record_file_id: Optional[str] = None,
        view_address: Optional[str] = None,
        **kwargs
    ):
        self.audio_address = audio_address
        self.audio_address_file_type = audio_address_file_type
        self.download_address = download_address
        self.download_address_file_type = download_address_file_type
        
        if meeting_summary and isinstance(meeting_summary, (list, List)):
            self.meeting_summary = [V1AddressesGet200ResponseRecordFilesInnerMeetingSummaryInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in meeting_summary]
        
        self.record_file_id = record_file_id
        self.view_address = view_address


class V1AddressesGet200ResponseRecordFilesInnerMeetingSummaryInner(object):
    """V1AddressesGet200ResponseRecordFilesInnerMeetingSummaryInner

    :param download_address: 下载文件地址。OAuth 鉴权方式下，账号类型为个人免费版、企微创建企业时，该值返回为空。 
    :type download_address: Optional[str]

    :param file_type: 下载文件类型，例如：txt、pdf、docs。OAuth 鉴权方式下，账号类型为个人免费版、企微创建企业时，该值返回为空。 
    :type file_type: Optional[str]
    """  # noqa: E501

    download_address: Optional[str] = None
    file_type: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        download_address: Optional[str] = None,
        file_type: Optional[str] = None,
        **kwargs
    ):
        self.download_address = download_address
        self.file_type = file_type


class V1AddressesRecordFileIdGet200Response(object):
    """V1AddressesRecordFileIdGet200Response

    :param ai_meeting_transcripts: 录制转写文件（智能优化版）列表。OAuth 鉴权方式下，账号类型为个人免费版、企微创建企业时，该值返回为空。 
    :type ai_meeting_transcripts: Optional[List[V1AddressesRecordFileIdGet200ResponseAiMeetingTranscriptsInner]]

    :param ai_minutes: 智能纪要列表。OAuth 鉴权方式下，账号类型为个人免费版、企微创建企业时，该值返回为空。 
    :type ai_minutes: Optional[List[V1AddressesRecordFileIdGet200ResponseAiMeetingTranscriptsInner]]

    :param audio_address: 音频下载地址。OAuth 鉴权方式下，账号类型为个人免费版、企微创建企业时，该值返回为空。 
    :type audio_address: Optional[str]

    :param audio_address_file_type: 下载音频文件格式，例如：m4a。OAuth 鉴权方式下，账号类型为个人免费版、企微创建企业时，该值返回为空。 
    :type audio_address_file_type: Optional[str]

    :param download_address: 下载地址，过期时间6小时。OAuth 鉴权方式下，账号类型为个人免费版、企微创建企业时，该值返回为空。 
    :type download_address: Optional[str]

    :param download_address_file_type: 下载视频文件格式，例如：mp4。 
    :type download_address_file_type: Optional[str]

    :param meeting_code: 会议 code。 
    :type meeting_code: Optional[str]

    :param meeting_id: 会议唯一 ID。 
    :type meeting_id: Optional[str]

    :param meeting_summary: 会议转写文件列表。OAuth 鉴权方式下，账号类型为个人免费版、企微创建企业时，该值返回为空。 
    :type meeting_summary: Optional[List[V1AddressesGet200ResponseRecordFilesInnerMeetingSummaryInner]]

    :param record_file_id: 录制文件 ID。 
    :type record_file_id: Optional[str]

    :param view_address: 播放地址。 
    :type view_address: Optional[str]
    """  # noqa: E501

    ai_meeting_transcripts: Optional[List[V1AddressesRecordFileIdGet200ResponseAiMeetingTranscriptsInner]] = None
    ai_minutes: Optional[List[V1AddressesRecordFileIdGet200ResponseAiMeetingTranscriptsInner]] = None
    audio_address: Optional[str] = None
    audio_address_file_type: Optional[str] = None
    download_address: Optional[str] = None
    download_address_file_type: Optional[str] = None
    meeting_code: Optional[str] = None
    meeting_id: Optional[str] = None
    meeting_summary: Optional[List[V1AddressesGet200ResponseRecordFilesInnerMeetingSummaryInner]] = None
    record_file_id: Optional[str] = None
    view_address: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        ai_meeting_transcripts: Optional[List[V1AddressesRecordFileIdGet200ResponseAiMeetingTranscriptsInner] | List[Dict[str, Any]]] = None,
        ai_minutes: Optional[List[V1AddressesRecordFileIdGet200ResponseAiMeetingTranscriptsInner] | List[Dict[str, Any]]] = None,
        audio_address: Optional[str] = None,
        audio_address_file_type: Optional[str] = None,
        download_address: Optional[str] = None,
        download_address_file_type: Optional[str] = None,
        meeting_code: Optional[str] = None,
        meeting_id: Optional[str] = None,
        meeting_summary: Optional[List[V1AddressesGet200ResponseRecordFilesInnerMeetingSummaryInner] | List[Dict[str, Any]]] = None,
        record_file_id: Optional[str] = None,
        view_address: Optional[str] = None,
        **kwargs
    ):
        
        if ai_meeting_transcripts and isinstance(ai_meeting_transcripts, (list, List)):
            self.ai_meeting_transcripts = [V1AddressesRecordFileIdGet200ResponseAiMeetingTranscriptsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in ai_meeting_transcripts]
        
        
        if ai_minutes and isinstance(ai_minutes, (list, List)):
            self.ai_minutes = [V1AddressesRecordFileIdGet200ResponseAiMeetingTranscriptsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in ai_minutes]
        
        self.audio_address = audio_address
        self.audio_address_file_type = audio_address_file_type
        self.download_address = download_address
        self.download_address_file_type = download_address_file_type
        self.meeting_code = meeting_code
        self.meeting_id = meeting_id
        
        if meeting_summary and isinstance(meeting_summary, (list, List)):
            self.meeting_summary = [V1AddressesGet200ResponseRecordFilesInnerMeetingSummaryInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in meeting_summary]
        
        self.record_file_id = record_file_id
        self.view_address = view_address


class V1AddressesRecordFileIdGet200ResponseAiMeetingTranscriptsInner(object):
    """V1AddressesRecordFileIdGet200ResponseAiMeetingTranscriptsInner

    :param download_address: 录制转写文件下载文件地址，链接有效期为5分钟。OAuth 鉴权方式下，账号类型为个人免费版、企微创建企业时，该值返回为空。 
    :type download_address: Optional[str]

    :param file_type: 下载文件类型，例如：txt、pdf、docx。OAuth 鉴权方式下，账号类型为个人免费版、企微创建企业时，该值返回为空。 
    :type file_type: Optional[str]
    """  # noqa: E501

    download_address: Optional[str] = None
    file_type: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        download_address: Optional[str] = None,
        file_type: Optional[str] = None,
        **kwargs
    ):
        self.download_address = download_address
        self.file_type = file_type


class V1FilesRecordsUploadAllPost200Response(object):
    """V1FilesRecordsUploadAllPost200Response

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


class V1FilesRecordsUploadFinishPostRequest(object):
    """V1FilesRecordsUploadFinishPostRequest

    :param ai_record: 自动生成智能转写和智能纪要：true：自动生成（默认）  false：不生成 
    :type ai_record: Optional[bool]

    :param operator_id: 操作者ID (required) 
    :type operator_id: str

    :param operator_id_type: 操作者ID类型 (required) 
    :type operator_id_type: int

    :param speak_number: 上传文件中的发言人数：传具体数值代表几人发言，最多支持12人，其中0代表多人发言 (required) 
    :type speak_number: int

    :param upload_id: 上传事务ID，由upload-prepare接口返回 (required) 
    :type upload_id: str
    """  # noqa: E501

    ai_record: Optional[bool] = None
    operator_id: str
    operator_id_type: int
    speak_number: int
    upload_id: str
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        operator_id: str,
        operator_id_type: int,
        speak_number: int,
        upload_id: str,
        ai_record: Optional[bool] = None,
        **kwargs
    ):
        self.ai_record = ai_record
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.speak_number = speak_number
        self.upload_id = upload_id


class V1FilesRecordsUploadPreparePost200Response(object):
    """V1FilesRecordsUploadPreparePost200Response

    :param block_num: 分块数量 
    :type block_num: Optional[int]

    :param block_size: 分块大小策略（以字节为单位） 
    :type block_size: Optional[int]

    :param upload_id: 上传事务 ID 
    :type upload_id: Optional[str]
    """  # noqa: E501

    block_num: Optional[int] = None
    block_size: Optional[int] = None
    upload_id: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        block_num: Optional[int] = None,
        block_size: Optional[int] = None,
        upload_id: Optional[str] = None,
        **kwargs
    ):
        self.block_num = block_num
        self.block_size = block_size
        self.upload_id = upload_id


class V1FilesRecordsUploadPreparePostRequest(object):
    """V1FilesRecordsUploadPreparePostRequest

    :param file_name: 文件名base64编码 (required) 
    :type file_name: str

    :param file_size: 文件大小（以字节为单位） (required) 
    :type file_size: int

    :param file_type: 文件类型。voice：音频；video：视频 (required) 
    :type file_type: str

    :param operator_id: 操作者ID (required) 
    :type operator_id: str

    :param operator_id_type: 操作者ID类型 (required) 
    :type operator_id_type: int
    """  # noqa: E501

    file_name: str
    file_size: int
    file_type: str
    operator_id: str
    operator_id_type: int
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        file_name: str,
        file_size: int,
        file_type: str,
        operator_id: str,
        operator_id_type: int,
        **kwargs
    ):
        self.file_name = file_name
        self.file_size = file_size
        self.file_type = file_type
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type


class V1MetricsRecordsGet200Response(object):
    """V1MetricsRecordsGet200Response

    :param summaries: 概览数据集合。 
    :type summaries: Optional[List[V1MetricsRecordsGet200ResponseSummariesInner]]
    """  # noqa: E501

    summaries: Optional[List[V1MetricsRecordsGet200ResponseSummariesInner]] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        summaries: Optional[List[V1MetricsRecordsGet200ResponseSummariesInner] | List[Dict[str, Any]]] = None,
        **kwargs
    ):
        
        if summaries and isinstance(summaries, (list, List)):
            self.summaries = [V1MetricsRecordsGet200ResponseSummariesInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in summaries]
        


class V1MetricsRecordsGet200ResponseSummariesInner(object):
    """V1MetricsRecordsGet200ResponseSummariesInner

    :param var_date: 统计时间，格式：yyyy-MM-dd。 
    :type var_date: Optional[str]

    :param download_counts: 下载次数（当天数据），默认0。 
    :type download_counts: Optional[int]

    :param view_counts: 观看次数（当天数据），默认0。 
    :type view_counts: Optional[int]
    """  # noqa: E501

    var_date: Optional[str] = None
    download_counts: Optional[int] = None
    view_counts: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        var_date: Optional[str] = None,
        download_counts: Optional[int] = None,
        view_counts: Optional[int] = None,
        **kwargs
    ):
        self.var_date = var_date
        self.download_counts = download_counts
        self.view_counts = view_counts


class V1RecordsAccessMeetingRecordIdDeleteRequest(object):
    """V1RecordsAccessMeetingRecordIdDeleteRequest

    :param access_members: 成员列表，如果传入非有权限的成员，则不生效 (required) 
    :type access_members: List[V1RecordsAccessMeetingRecordIdDeleteRequestAccessMembersInner]

    :param operator_id: 操作者 ID。operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 (required) 
    :type operator_id: str

    :param operator_id_type: 操作者 ID 的类型： 1:userid 2:open_id (required) 
    :type operator_id_type: int
    """  # noqa: E501

    access_members: List[V1RecordsAccessMeetingRecordIdDeleteRequestAccessMembersInner]
    operator_id: str
    operator_id_type: int
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        access_members: List[V1RecordsAccessMeetingRecordIdDeleteRequestAccessMembersInner] | List[Dict[str, Any]],
        operator_id: str,
        operator_id_type: int,
        **kwargs
    ):
        
        if access_members and isinstance(access_members, (list, List)):
            self.access_members = [V1RecordsAccessMeetingRecordIdDeleteRequestAccessMembersInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in access_members]
        
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type


class V1RecordsAccessMeetingRecordIdDeleteRequestAccessMembersInner(object):
    """V1RecordsAccessMeetingRecordIdDeleteRequestAccessMembersInner

    :param to_operator_id: 被操作者ID，根据 to_operator_id_type 的值，使用不同的类型 (required) 
    :type to_operator_id: str

    :param to_operator_id_type: 被操作者ID类型  1:userid  2:open_id  4:ms_open_id (required) 
    :type to_operator_id_type: int
    """  # noqa: E501

    to_operator_id: str
    to_operator_id_type: int
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        to_operator_id: str,
        to_operator_id_type: int,
        **kwargs
    ):
        self.to_operator_id = to_operator_id
        self.to_operator_id_type = to_operator_id_type


class V1RecordsAccessMeetingRecordIdPost200Response(object):
    """V1RecordsAccessMeetingRecordIdPost200Response

    :param fail_access_members: 未添加成功的成员列表 
    :type fail_access_members: Optional[List[V1RecordsAccessMeetingRecordIdPost200ResponseFailAccessMembersInner]]
    """  # noqa: E501

    fail_access_members: Optional[List[V1RecordsAccessMeetingRecordIdPost200ResponseFailAccessMembersInner]] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        fail_access_members: Optional[List[V1RecordsAccessMeetingRecordIdPost200ResponseFailAccessMembersInner] | List[Dict[str, Any]]] = None,
        **kwargs
    ):
        
        if fail_access_members and isinstance(fail_access_members, (list, List)):
            self.fail_access_members = [V1RecordsAccessMeetingRecordIdPost200ResponseFailAccessMembersInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in fail_access_members]
        


class V1RecordsAccessMeetingRecordIdPost200ResponseFailAccessMembersInner(object):
    """V1RecordsAccessMeetingRecordIdPost200ResponseFailAccessMembersInner

    :param permission: 成员访问权限，默认为 0 ； 0：仅查看，1：可管理 
    :type permission: Optional[int]

    :param to_operator_id: 被操作者ID，根据 to_operator_id_type 的值，使用不同的类型 
    :type to_operator_id: Optional[str]

    :param to_operator_id_type: 被操作者ID类型  1:userid  2:open_id  4:ms_open_id 
    :type to_operator_id_type: Optional[int]
    """  # noqa: E501

    permission: Optional[int] = None
    to_operator_id: Optional[str] = None
    to_operator_id_type: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        permission: Optional[int] = None,
        to_operator_id: Optional[str] = None,
        to_operator_id_type: Optional[int] = None,
        **kwargs
    ):
        self.permission = permission
        self.to_operator_id = to_operator_id
        self.to_operator_id_type = to_operator_id_type


class V1RecordsAccessMeetingRecordIdPostRequest(object):
    """V1RecordsAccessMeetingRecordIdPostRequest

    :param access_members: 成员列表，一次最多传入200个，可以多次调用接口，累加型接口 (required) 
    :type access_members: List[V1RecordsAccessMeetingRecordIdPostRequestAccessMembersInner]

    :param operator_id: 操作者 ID。operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 (required) 
    :type operator_id: str

    :param operator_id_type: 操作者 ID 的类型： 1:userid 2:open_id (required) 
    :type operator_id_type: int
    """  # noqa: E501

    access_members: List[V1RecordsAccessMeetingRecordIdPostRequestAccessMembersInner]
    operator_id: str
    operator_id_type: int
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        access_members: List[V1RecordsAccessMeetingRecordIdPostRequestAccessMembersInner] | List[Dict[str, Any]],
        operator_id: str,
        operator_id_type: int,
        **kwargs
    ):
        
        if access_members and isinstance(access_members, (list, List)):
            self.access_members = [V1RecordsAccessMeetingRecordIdPostRequestAccessMembersInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in access_members]
        
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type


class V1RecordsAccessMeetingRecordIdPostRequestAccessMembersInner(object):
    """V1RecordsAccessMeetingRecordIdPostRequestAccessMembersInner

    :param permission: 成员访问权限，默认为 0 ； 0：仅查看，1：可管理 
    :type permission: Optional[int]

    :param to_operator_id: 被操作者ID，根据 to_operator_id_type 的值，使用不同的类型 (required) 
    :type to_operator_id: str

    :param to_operator_id_type: 被操作者ID类型,只支持设置参会成员  1:userid  2:open_id  4:ms_open_id (required) 
    :type to_operator_id_type: int
    """  # noqa: E501

    permission: Optional[int] = None
    to_operator_id: str
    to_operator_id_type: int
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        to_operator_id: str,
        to_operator_id_type: int,
        permission: Optional[int] = None,
        **kwargs
    ):
        self.permission = permission
        self.to_operator_id = to_operator_id
        self.to_operator_id_type = to_operator_id_type


class V1RecordsApprovalsMeetingRecordIdPutRequest(object):
    """V1RecordsApprovalsMeetingRecordIdPutRequest

    :param action: 审批动作。 1：同意 2：忽略 (required) 
    :type action: int

    :param apply_id_list: 申请 ID 列表，通过订阅云录制查看申请事件（可跳转链接），可以获取申请 ID。 (required) 
    :type apply_id_list: List[str]

    :param operator_id: 操作者 ID。 operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 operator_id_type=2，operator_id 必须和公共参数的 openid 一致。 operator_id 和 userid 至少填写一个，两个参数如果都传了以 operator_id 为准。 使用 OAuth 公参鉴权后不能使用 userid 为入参。 (required) 
    :type operator_id: str

    :param operator_id_type: 操作者 ID 的类型： 1：userid 2：open_id 如果 operator_id 和 userid 具有值，则以 operator_id 为准。 (required) 
    :type operator_id_type: int
    """  # noqa: E501

    action: int
    apply_id_list: List[str]
    operator_id: str
    operator_id_type: int
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        action: int,
        apply_id_list: List[str],
        operator_id: str,
        operator_id_type: int,
        **kwargs
    ):
        self.action = action
        
        if apply_id_list and isinstance(apply_id_list, (list, List)):
            self.apply_id_list = apply_id_list
        
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type


class V1RecordsEventsGet200Response(object):
    """V1RecordsEventsGet200Response

    :param current_page: 分页查询返回当前页码。 
    :type current_page: Optional[int]

    :param current_size: 分页查询返回单页数据条数。 
    :type current_size: Optional[int]

    :param events: 事件明细集合。 
    :type events: Optional[List[V1RecordsEventsGet200ResponseEventsInner]]

    :param total_count: 分页查询返回数据总数。 
    :type total_count: Optional[int]

    :param total_page: 分页查询返回分页总数。 
    :type total_page: Optional[int]
    """  # noqa: E501

    current_page: Optional[int] = None
    current_size: Optional[int] = None
    events: Optional[List[V1RecordsEventsGet200ResponseEventsInner]] = None
    total_count: Optional[int] = None
    total_page: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        current_page: Optional[int] = None,
        current_size: Optional[int] = None,
        events: Optional[List[V1RecordsEventsGet200ResponseEventsInner] | List[Dict[str, Any]]] = None,
        total_count: Optional[int] = None,
        total_page: Optional[int] = None,
        **kwargs
    ):
        self.current_page = current_page
        self.current_size = current_size
        
        if events and isinstance(events, (list, List)):
            self.events = [V1RecordsEventsGet200ResponseEventsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in events]
        
        self.total_count = total_count
        self.total_page = total_page


class V1RecordsEventsGet200ResponseEventsInner(object):
    """V1RecordsEventsGet200ResponseEventsInner

    :param event_type: 查询事件类型：1：下载，2：查看。 
    :type event_type: Optional[int]

    :param operate_time: 操作时间，UNIX 时间戳（单位毫秒）。 
    :type operate_time: Optional[int]

    :param record_name: 录制文件名称。 
    :type record_name: Optional[str]

    :param user_name: 用户名称。 
    :type user_name: Optional[str]

    :param userid: 用户 ID。 
    :type userid: Optional[str]
    """  # noqa: E501

    event_type: Optional[int] = None
    operate_time: Optional[int] = None
    record_name: Optional[str] = None
    user_name: Optional[str] = None
    userid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        event_type: Optional[int] = None,
        operate_time: Optional[int] = None,
        record_name: Optional[str] = None,
        user_name: Optional[str] = None,
        userid: Optional[str] = None,
        **kwargs
    ):
        self.event_type = event_type
        self.operate_time = operate_time
        self.record_name = record_name
        self.user_name = user_name
        self.userid = userid


class V1RecordsGet200Response(object):
    """V1RecordsGet200Response

    :param current_page: 分页查询返回当前页码。 
    :type current_page: Optional[int]

    :param current_size: 分页查询返回单页数据条数。 
    :type current_size: Optional[int]

    :param record_meetings: 会议录制列表。 
    :type record_meetings: Optional[List[V1RecordsGet200ResponseRecordMeetingsInner]]

    :param total_count: 分页查询返回数据总数。 
    :type total_count: Optional[int]

    :param total_page: 分页查询返回分页总数。 
    :type total_page: Optional[int]
    """  # noqa: E501

    current_page: Optional[int] = None
    current_size: Optional[int] = None
    record_meetings: Optional[List[V1RecordsGet200ResponseRecordMeetingsInner]] = None
    total_count: Optional[int] = None
    total_page: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        current_page: Optional[int] = None,
        current_size: Optional[int] = None,
        record_meetings: Optional[List[V1RecordsGet200ResponseRecordMeetingsInner] | List[Dict[str, Any]]] = None,
        total_count: Optional[int] = None,
        total_page: Optional[int] = None,
        **kwargs
    ):
        self.current_page = current_page
        self.current_size = current_size
        
        if record_meetings and isinstance(record_meetings, (list, List)):
            self.record_meetings = [V1RecordsGet200ResponseRecordMeetingsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in record_meetings]
        
        self.total_count = total_count
        self.total_page = total_page


class V1RecordsGet200ResponseRecordMeetingsInner(object):
    """V1RecordsGet200ResponseRecordMeetingsInner

    :param host_user_id: 主持人用户 ID。(查询会议录制文件列表接口返回。) 
    :type host_user_id: Optional[str]

    :param media_set_type: 会议类型，0-全部 1-外部会议 2-内部会议 
    :type media_set_type: Optional[int]

    :param media_start_time: 会议开始时间，UNIX 时间戳（单位毫秒）。 
    :type media_start_time: Optional[int]

    :param meeting_code: 会议 code。 
    :type meeting_code: Optional[str]

    :param meeting_id: 会议唯一 ID。 
    :type meeting_id: Optional[str]

    :param meeting_record_id: 会议录制 ID。 
    :type meeting_record_id: Optional[str]

    :param record_files: 录制文件列表。 
    :type record_files: Optional[List[V1RecordsGet200ResponseRecordMeetingsInnerRecordFilesInner]]

    :param record_type: 返回的录制文件类型，0：云录制、2：上传录制 
    :type record_type: Optional[int]

    :param state: 录制状态。1：录制中，2：转码中，3：转码完成，当状态为转码完成才会返回录制文件列表。 
    :type state: Optional[int]

    :param subject: 会议主题。 
    :type subject: Optional[str]
    """  # noqa: E501

    host_user_id: Optional[str] = None
    media_set_type: Optional[int] = None
    media_start_time: Optional[int] = None
    meeting_code: Optional[str] = None
    meeting_id: Optional[str] = None
    meeting_record_id: Optional[str] = None
    record_files: Optional[List[V1RecordsGet200ResponseRecordMeetingsInnerRecordFilesInner]] = None
    record_type: Optional[int] = None
    state: Optional[int] = None
    subject: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        host_user_id: Optional[str] = None,
        media_set_type: Optional[int] = None,
        media_start_time: Optional[int] = None,
        meeting_code: Optional[str] = None,
        meeting_id: Optional[str] = None,
        meeting_record_id: Optional[str] = None,
        record_files: Optional[List[V1RecordsGet200ResponseRecordMeetingsInnerRecordFilesInner] | List[Dict[str, Any]]] = None,
        record_type: Optional[int] = None,
        state: Optional[int] = None,
        subject: Optional[str] = None,
        **kwargs
    ):
        self.host_user_id = host_user_id
        self.media_set_type = media_set_type
        self.media_start_time = media_start_time
        self.meeting_code = meeting_code
        self.meeting_id = meeting_id
        self.meeting_record_id = meeting_record_id
        
        if record_files and isinstance(record_files, (list, List)):
            self.record_files = [V1RecordsGet200ResponseRecordMeetingsInnerRecordFilesInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in record_files]
        
        self.record_type = record_type
        self.state = state
        self.subject = subject


class V1RecordsGet200ResponseRecordMeetingsInnerRecordFilesInner(object):
    """V1RecordsGet200ResponseRecordMeetingsInnerRecordFilesInner

    :param allow_download: 是否允许下载，开启共享时返回。 
    :type allow_download: Optional[bool]

    :param password: 访问密码，开启共享时返回。 
    :type password: Optional[str]

    :param record_end_time: 结束录制时间，UNIX 时间戳（单位毫秒）。 
    :type record_end_time: Optional[int]

    :param record_file_id: 录制文件 ID。 
    :type record_file_id: Optional[str]

    :param record_size: 文件大小（单位字节）。 
    :type record_size: Optional[int]

    :param record_start_time: 开始录制时间，UNIX 时间戳（单位毫秒）。 
    :type record_start_time: Optional[int]

    :param required_participant: 仅参会成员可查看，开启共享时返回。 
    :type required_participant: Optional[bool]

    :param required_same_corp: 仅企业用户可查看，开启共享时返回。 
    :type required_same_corp: Optional[bool]

    :param sharing_expire: 共享链接有效期（单位毫秒），当未开启共享时，返回0表示永久有效；开启共享时返回。 
    :type sharing_expire: Optional[int]

    :param sharing_state: 共享状态，是否开启共享。0：未开启1：开启，当开启共享时返回访问权限、访问密码、共享链接有效期、是否允许下载。 
    :type sharing_state: Optional[int]

    :param sharing_url: 共享链接，开启共享时返回。 
    :type sharing_url: Optional[str]
    """  # noqa: E501

    allow_download: Optional[bool] = None
    password: Optional[str] = None
    record_end_time: Optional[int] = None
    record_file_id: Optional[str] = None
    record_size: Optional[int] = None
    record_start_time: Optional[int] = None
    required_participant: Optional[bool] = None
    required_same_corp: Optional[bool] = None
    sharing_expire: Optional[int] = None
    sharing_state: Optional[int] = None
    sharing_url: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        allow_download: Optional[bool] = None,
        password: Optional[str] = None,
        record_end_time: Optional[int] = None,
        record_file_id: Optional[str] = None,
        record_size: Optional[int] = None,
        record_start_time: Optional[int] = None,
        required_participant: Optional[bool] = None,
        required_same_corp: Optional[bool] = None,
        sharing_expire: Optional[int] = None,
        sharing_state: Optional[int] = None,
        sharing_url: Optional[str] = None,
        **kwargs
    ):
        self.allow_download = allow_download
        self.password = password
        self.record_end_time = record_end_time
        self.record_file_id = record_file_id
        self.record_size = record_size
        self.record_start_time = record_start_time
        self.required_participant = required_participant
        self.required_same_corp = required_same_corp
        self.sharing_expire = sharing_expire
        self.sharing_state = sharing_state
        self.sharing_url = sharing_url


class V1RecordsSettingsMeetingRecordIdGet200Response(object):
    """V1RecordsSettingsMeetingRecordIdGet200Response

    :param meeting_id: 会议ID 
    :type meeting_id: Optional[str]

    :param meeting_record_name: 录制名称 
    :type meeting_record_name: Optional[str]

    :param sharing_config:
    :type sharing_config: Optional[V1RecordsSettingsMeetingRecordIdGet200ResponseSharingConfig]
    """  # noqa: E501

    meeting_id: Optional[str] = None
    meeting_record_name: Optional[str] = None
    sharing_config: Optional[V1RecordsSettingsMeetingRecordIdGet200ResponseSharingConfig] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        meeting_id: Optional[str] = None,
        meeting_record_name: Optional[str] = None,
        sharing_config: Optional[V1RecordsSettingsMeetingRecordIdGet200ResponseSharingConfig | Dict[str, Any]] = None,
        **kwargs
    ):
        self.meeting_id = meeting_id
        self.meeting_record_name = meeting_record_name
        self.sharing_config = V1RecordsSettingsMeetingRecordIdGet200ResponseSharingConfig(**sharing_config) if isinstance(sharing_config, (dict, Dict)) else sharing_config


class V1RecordsSettingsMeetingRecordIdGet200ResponseSharingConfig(object):
    """共享配置对象

    :param allow_download: 是否允许下载 
    :type allow_download: Optional[bool]

    :param allow_view_transcripts: 是否允许查看录制转写 
    :type allow_view_transcripts: Optional[bool]

    :param enable_approve: 是否需要审批 
    :type enable_approve: Optional[bool]

    :param enable_password: 是否开启秘密 
    :type enable_password: Optional[bool]

    :param enable_sharing: 共享链接开关，true-开启，false-未开启 
    :type enable_sharing: Optional[bool]

    :param enable_sharing_expire: 是否开启共享链接有效期 
    :type enable_sharing_expire: Optional[bool]

    :param password: 录制上传者、会议创建者、企业超级管理员或有企业录制管理权限的用户返回， 
    :type password: Optional[str]

    :param share_scope: 访问范围，0-所有人，1-同企业 
    :type share_scope: Optional[int]

    :param sharing_expire: 共享链接有效期，毫秒级时间戳 
    :type sharing_expire: Optional[int]
    """  # noqa: E501

    allow_download: Optional[bool] = None
    allow_view_transcripts: Optional[bool] = None
    enable_approve: Optional[bool] = None
    enable_password: Optional[bool] = None
    enable_sharing: Optional[bool] = None
    enable_sharing_expire: Optional[bool] = None
    password: Optional[str] = None
    share_scope: Optional[int] = None
    sharing_expire: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        allow_download: Optional[bool] = None,
        allow_view_transcripts: Optional[bool] = None,
        enable_approve: Optional[bool] = None,
        enable_password: Optional[bool] = None,
        enable_sharing: Optional[bool] = None,
        enable_sharing_expire: Optional[bool] = None,
        password: Optional[str] = None,
        share_scope: Optional[int] = None,
        sharing_expire: Optional[int] = None,
        **kwargs
    ):
        self.allow_download = allow_download
        self.allow_view_transcripts = allow_view_transcripts
        self.enable_approve = enable_approve
        self.enable_password = enable_password
        self.enable_sharing = enable_sharing
        self.enable_sharing_expire = enable_sharing_expire
        self.password = password
        self.share_scope = share_scope
        self.sharing_expire = sharing_expire


class V1RecordsSettingsMeetingRecordIdPutRequest(object):
    """V1RecordsSettingsMeetingRecordIdPutRequest

    :param meeting_id: 会议id 
    :type meeting_id: Optional[str]

    :param operator_id: 操作者ID 
    :type operator_id: Optional[str]

    :param operator_id_type: 操作者ID的类型。3. rooms_id 说明：当前仅支持 rooms_id。如操作者为企业内 userid 或 openId，请使用 userid 字段。 
    :type operator_id_type: Optional[int]

    :param sharing_config:
    :type sharing_config: Optional[V1RecordsSettingsMeetingRecordIdPutRequestSharingConfig]

    :param userid: 用户id。仅会议创建者、企业超级管理员或有企业录制管理权限的用户可调用。调用方用于标示用户的唯一 ID（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId）。 企业唯一用户标识说明： 1. 企业对接 SSO 时使用的员工唯一标识 ID。 2. 企业调用创建用户接口时传递的 userid 参数。 
    :type userid: Optional[str]
    """  # noqa: E501

    meeting_id: Optional[str] = None
    operator_id: Optional[str] = None
    operator_id_type: Optional[int] = None
    sharing_config: Optional[V1RecordsSettingsMeetingRecordIdPutRequestSharingConfig] = None
    userid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        meeting_id: Optional[str] = None,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[int] = None,
        sharing_config: Optional[V1RecordsSettingsMeetingRecordIdPutRequestSharingConfig | Dict[str, Any]] = None,
        userid: Optional[str] = None,
        **kwargs
    ):
        self.meeting_id = meeting_id
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.sharing_config = V1RecordsSettingsMeetingRecordIdPutRequestSharingConfig(**sharing_config) if isinstance(sharing_config, (dict, Dict)) else sharing_config
        self.userid = userid


class V1RecordsSettingsMeetingRecordIdPutRequestSharingConfig(object):
    """V1RecordsSettingsMeetingRecordIdPutRequestSharingConfig

    :param allow_download: 是否允许下载，默认为 false。 true：允许下载 
    :type allow_download: Optional[bool]

    :param allow_view_transcripts: 是否允许查看会议纪要，默认为 true。 
    :type allow_view_transcripts: Optional[bool]

    :param enable_approve: 是否需要审批，true：需要审批 false：不需要审批 
    :type enable_approve: Optional[bool]

    :param enable_password: 是否开启密码，默认为 true。 true：开启 
    :type enable_password: Optional[bool]

    :param enable_sharing: 共享开关，是否开启共享，默认为 true。 true：开启 false：未开启 说明： 未开启时不允许设置以下参数。 修改为 false 关闭共享后，之前设置的共享设置将不保存。 
    :type enable_sharing: Optional[bool]

    :param enable_sharing_expire: 是否开启共享链接有效期，默认为 false。 true：开启 
    :type enable_sharing_expire: Optional[bool]

    :param password: 共享密码，默认随机生成。 说明：当 enable_password = true 时，必传；当 enable_password = false 时，不可传。 
    :type password: Optional[str]

    :param share_scope: 访问范围，0：所有人 1：同企业 
    :type share_scope: Optional[int]

    :param sharing_auth_type: 共享权限类型。 0：仅允许登录用户查看 1：仅企业用户成员可查看 2：仅参会成员可查看 
    :type sharing_auth_type: Optional[int]

    :param sharing_expire: 共享链接有效期，unix 时间戳（单位毫秒），默认为空。 说明：当 enable_sharing_expire = true 时，必传；当 enable_sharing_expire = false 时，不可传。 
    :type sharing_expire: Optional[int]
    """  # noqa: E501

    allow_download: Optional[bool] = None
    allow_view_transcripts: Optional[bool] = None
    enable_approve: Optional[bool] = None
    enable_password: Optional[bool] = None
    enable_sharing: Optional[bool] = None
    enable_sharing_expire: Optional[bool] = None
    password: Optional[str] = None
    share_scope: Optional[int] = None
    sharing_auth_type: Optional[int] = None
    sharing_expire: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        allow_download: Optional[bool] = None,
        allow_view_transcripts: Optional[bool] = None,
        enable_approve: Optional[bool] = None,
        enable_password: Optional[bool] = None,
        enable_sharing: Optional[bool] = None,
        enable_sharing_expire: Optional[bool] = None,
        password: Optional[str] = None,
        share_scope: Optional[int] = None,
        sharing_auth_type: Optional[int] = None,
        sharing_expire: Optional[int] = None,
        **kwargs
    ):
        self.allow_download = allow_download
        self.allow_view_transcripts = allow_view_transcripts
        self.enable_approve = enable_approve
        self.enable_password = enable_password
        self.enable_sharing = enable_sharing
        self.enable_sharing_expire = enable_sharing_expire
        self.password = password
        self.share_scope = share_scope
        self.sharing_auth_type = sharing_auth_type
        self.sharing_expire = sharing_expire


class V1RecordsTranscriptsDetailsGet200Response(object):
    """V1RecordsTranscriptsDetailsGet200Response

    :param minutes:
    :type minutes: Optional[V1RecordsTranscriptsDetailsGet200ResponseMinutes]

    :param more: 是否还有更多 
    :type more: Optional[bool]
    """  # noqa: E501

    minutes: Optional[V1RecordsTranscriptsDetailsGet200ResponseMinutes] = None
    more: Optional[bool] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        minutes: Optional[V1RecordsTranscriptsDetailsGet200ResponseMinutes | Dict[str, Any]] = None,
        more: Optional[bool] = None,
        **kwargs
    ):
        self.minutes = V1RecordsTranscriptsDetailsGet200ResponseMinutes(**minutes) if isinstance(minutes, (dict, Dict)) else minutes
        self.more = more


class V1RecordsTranscriptsDetailsGet200ResponseMinutes(object):
    """会议纪要对象。

    :param audio_detect: 声纹识别状态0-未完成 1-已完成。说明：声纹识别是针对 Rooms 等设备出现一台设备多人讲话场景时，自动区分为多个发言人的能力。声纹识别与纪要生成的过程独立。无需声纹识别或声纹识别已完成时，该值为1。 
    :type audio_detect: Optional[int]

    :param paragraphs: 段落对象列表 
    :type paragraphs: Optional[List[V1RecordsTranscriptsDetailsGet200ResponseMinutesParagraphsInner]]
    """  # noqa: E501

    audio_detect: Optional[int] = None
    paragraphs: Optional[List[V1RecordsTranscriptsDetailsGet200ResponseMinutesParagraphsInner]] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        audio_detect: Optional[int] = None,
        paragraphs: Optional[List[V1RecordsTranscriptsDetailsGet200ResponseMinutesParagraphsInner] | List[Dict[str, Any]]] = None,
        **kwargs
    ):
        self.audio_detect = audio_detect
        
        if paragraphs and isinstance(paragraphs, (list, List)):
            self.paragraphs = [V1RecordsTranscriptsDetailsGet200ResponseMinutesParagraphsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in paragraphs]
        


class V1RecordsTranscriptsDetailsGet200ResponseMinutesParagraphsInner(object):
    """V1RecordsTranscriptsDetailsGet200ResponseMinutesParagraphsInner

    :param end_time: 录制文件中的段落结束时间（毫秒）。 
    :type end_time: Optional[int]

    :param pid: 段落id 
    :type pid: Optional[str]

    :param sentences:
    :type sentences: Optional[List[V1RecordsTranscriptsDetailsGet200ResponseMinutesParagraphsInnerSentencesInner]]

    :param speaker_info:
    :type speaker_info: Optional[V1RecordsTranscriptsDetailsGet200ResponseMinutesParagraphsInnerSpeakerInfo]

    :param start_time: 录制文件中的段落开始时间（毫秒）。 
    :type start_time: Optional[int]
    """  # noqa: E501

    end_time: Optional[int] = None
    pid: Optional[str] = None
    sentences: Optional[List[V1RecordsTranscriptsDetailsGet200ResponseMinutesParagraphsInnerSentencesInner]] = None
    speaker_info: Optional[V1RecordsTranscriptsDetailsGet200ResponseMinutesParagraphsInnerSpeakerInfo] = None
    start_time: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        end_time: Optional[int] = None,
        pid: Optional[str] = None,
        sentences: Optional[List[V1RecordsTranscriptsDetailsGet200ResponseMinutesParagraphsInnerSentencesInner] | List[Dict[str, Any]]] = None,
        speaker_info: Optional[V1RecordsTranscriptsDetailsGet200ResponseMinutesParagraphsInnerSpeakerInfo | Dict[str, Any]] = None,
        start_time: Optional[int] = None,
        **kwargs
    ):
        self.end_time = end_time
        self.pid = pid
        
        if sentences and isinstance(sentences, (list, List)):
            self.sentences = [V1RecordsTranscriptsDetailsGet200ResponseMinutesParagraphsInnerSentencesInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in sentences]
        
        self.speaker_info = V1RecordsTranscriptsDetailsGet200ResponseMinutesParagraphsInnerSpeakerInfo(**speaker_info) if isinstance(speaker_info, (dict, Dict)) else speaker_info
        self.start_time = start_time


class V1RecordsTranscriptsDetailsGet200ResponseMinutesParagraphsInnerSentencesInner(object):
    """V1RecordsTranscriptsDetailsGet200ResponseMinutesParagraphsInnerSentencesInner

    :param end_time: 录制文件中的句子结束时间（毫秒）。 
    :type end_time: Optional[int]

    :param sid: 句子 ID。 
    :type sid: Optional[str]

    :param start_time: 录制文件中的句子开始时间（毫秒）。 
    :type start_time: Optional[int]

    :param words: 词对象列表 
    :type words: Optional[List[V1RecordsTranscriptsDetailsGet200ResponseMinutesParagraphsInnerSentencesInnerWordsInner]]
    """  # noqa: E501

    end_time: Optional[int] = None
    sid: Optional[str] = None
    start_time: Optional[int] = None
    words: Optional[List[V1RecordsTranscriptsDetailsGet200ResponseMinutesParagraphsInnerSentencesInnerWordsInner]] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        end_time: Optional[int] = None,
        sid: Optional[str] = None,
        start_time: Optional[int] = None,
        words: Optional[List[V1RecordsTranscriptsDetailsGet200ResponseMinutesParagraphsInnerSentencesInnerWordsInner] | List[Dict[str, Any]]] = None,
        **kwargs
    ):
        self.end_time = end_time
        self.sid = sid
        self.start_time = start_time
        
        if words and isinstance(words, (list, List)):
            self.words = [V1RecordsTranscriptsDetailsGet200ResponseMinutesParagraphsInnerSentencesInnerWordsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in words]
        


class V1RecordsTranscriptsDetailsGet200ResponseMinutesParagraphsInnerSentencesInnerWordsInner(object):
    """V1RecordsTranscriptsDetailsGet200ResponseMinutesParagraphsInnerSentencesInnerWordsInner

    :param end_time: 录制文件中的词结束时间（毫秒）。 
    :type end_time: Optional[int]

    :param start_time: 录制文件中的词开始时间（毫秒） 
    :type start_time: Optional[int]

    :param text: 文本内容。 
    :type text: Optional[str]

    :param wid: 词 ID 
    :type wid: Optional[str]
    """  # noqa: E501

    end_time: Optional[int] = None
    start_time: Optional[int] = None
    text: Optional[str] = None
    wid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        end_time: Optional[int] = None,
        start_time: Optional[int] = None,
        text: Optional[str] = None,
        wid: Optional[str] = None,
        **kwargs
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.text = text
        self.wid = wid


class V1RecordsTranscriptsDetailsGet200ResponseMinutesParagraphsInnerSpeakerInfo(object):
    """发言人信息对象。

    :param userid: 同企业返回企业用户 userid。 
    :type userid: Optional[str]

    :param username: 昵称 
    :type username: Optional[str]
    """  # noqa: E501

    userid: Optional[str] = None
    username: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        userid: Optional[str] = None,
        username: Optional[str] = None,
        **kwargs
    ):
        self.userid = userid
        self.username = username


class V1RecordsTranscriptsParagraphsGet200Response(object):
    """V1RecordsTranscriptsParagraphsGet200Response

    :param audio_detect: 声纹识别状态0-未完成 1-已完成。说明：声纹识别是针对 Rooms 等设备出现一台设备多人讲话场景时，自动区分为多个发言人的能力。声纹识别与纪要生成的过程独立。无需声纹识别或声纹识别已完成时，该值为1。 
    :type audio_detect: Optional[int]

    :param pids: 段落对象列表 
    :type pids: Optional[List[V1RecordsTranscriptsParagraphsGet200ResponsePidsInner]]

    :param total: 段落总数。 
    :type total: Optional[int]
    """  # noqa: E501

    audio_detect: Optional[int] = None
    pids: Optional[List[V1RecordsTranscriptsParagraphsGet200ResponsePidsInner]] = None
    total: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        audio_detect: Optional[int] = None,
        pids: Optional[List[V1RecordsTranscriptsParagraphsGet200ResponsePidsInner] | List[Dict[str, Any]]] = None,
        total: Optional[int] = None,
        **kwargs
    ):
        self.audio_detect = audio_detect
        
        if pids and isinstance(pids, (list, List)):
            self.pids = [V1RecordsTranscriptsParagraphsGet200ResponsePidsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in pids]
        
        self.total = total


class V1RecordsTranscriptsParagraphsGet200ResponsePidsInner(object):
    """V1RecordsTranscriptsParagraphsGet200ResponsePidsInner

    :param end_time: 录制文件中的段落结束时间（毫秒）。 
    :type end_time: Optional[int]

    :param pid: 段落 ID。 
    :type pid: Optional[str]

    :param start_time: 录制文件中的段落开始时间（毫秒）。 
    :type start_time: Optional[int]
    """  # noqa: E501

    end_time: Optional[int] = None
    pid: Optional[str] = None
    start_time: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        end_time: Optional[int] = None,
        pid: Optional[str] = None,
        start_time: Optional[int] = None,
        **kwargs
    ):
        self.end_time = end_time
        self.pid = pid
        self.start_time = start_time


class V1RecordsTranscriptsSearchGet200Response(object):
    """V1RecordsTranscriptsSearchGet200Response

    :param hits: 搜索结果列表 
    :type hits: Optional[List[V1RecordsTranscriptsSearchGet200ResponseHitsInner]]

    :param timelines: 搜索结果时间戳对象列表 
    :type timelines: Optional[List[V1RecordsTranscriptsSearchGet200ResponseTimelinesInner]]
    """  # noqa: E501

    hits: Optional[List[V1RecordsTranscriptsSearchGet200ResponseHitsInner]] = None
    timelines: Optional[List[V1RecordsTranscriptsSearchGet200ResponseTimelinesInner]] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        hits: Optional[List[V1RecordsTranscriptsSearchGet200ResponseHitsInner] | List[Dict[str, Any]]] = None,
        timelines: Optional[List[V1RecordsTranscriptsSearchGet200ResponseTimelinesInner] | List[Dict[str, Any]]] = None,
        **kwargs
    ):
        
        if hits and isinstance(hits, (list, List)):
            self.hits = [V1RecordsTranscriptsSearchGet200ResponseHitsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in hits]
        
        
        if timelines and isinstance(timelines, (list, List)):
            self.timelines = [V1RecordsTranscriptsSearchGet200ResponseTimelinesInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in timelines]
        


class V1RecordsTranscriptsSearchGet200ResponseHitsInner(object):
    """V1RecordsTranscriptsSearchGet200ResponseHitsInner

    :param length: 匹配长度 
    :type length: Optional[int]

    :param offset: text 相对词的偏移。 
    :type offset: Optional[int]

    :param pid: 段落 ID 
    :type pid: Optional[str]

    :param sid: 句子 ID 
    :type sid: Optional[str]
    """  # noqa: E501

    length: Optional[int] = None
    offset: Optional[int] = None
    pid: Optional[str] = None
    sid: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        length: Optional[int] = None,
        offset: Optional[int] = None,
        pid: Optional[str] = None,
        sid: Optional[str] = None,
        **kwargs
    ):
        self.length = length
        self.offset = offset
        self.pid = pid
        self.sid = sid


class V1RecordsTranscriptsSearchGet200ResponseTimelinesInner(object):
    """V1RecordsTranscriptsSearchGet200ResponseTimelinesInner

    :param pid: 段落id 
    :type pid: Optional[str]

    :param sid: 句子id 
    :type sid: Optional[str]

    :param start_time: 录制文件中的词开始时间（毫秒） 
    :type start_time: Optional[int]
    """  # noqa: E501

    pid: Optional[str] = None
    sid: Optional[str] = None
    start_time: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        pid: Optional[str] = None,
        sid: Optional[str] = None,
        start_time: Optional[int] = None,
        **kwargs
    ):
        self.pid = pid
        self.sid = sid
        self.start_time = start_time


class V1RecordsTransferRecordingPutRequest(object):
    """V1RecordsTransferRecordingPutRequest

    :param delete_recording_after_transfer: 如果参数未带， 则按集群删除策略对指定录制删除操作。    转存完成后删除录制策略：  0 - 转存完成后立刻删除录制文件  1～30 - 转存完成后1～30天后删除录制文件  不删除 - 转存完成后不删除录制文件 
    :type delete_recording_after_transfer: Optional[str]

    :param instanceid:(required) 
    :type instanceid: int

    :param operator_id: 操作者 ID，根据 operator_id_type 的值，使用不同的类型。 (required) 
    :type operator_id: str

    :param operator_id_type: 操作者 ID 的类型： 1：userid (required) 
    :type operator_id_type: int
    """  # noqa: E501

    delete_recording_after_transfer: Optional[str] = None
    instanceid: int
    operator_id: str
    operator_id_type: int
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        instanceid: int,
        operator_id: str,
        operator_id_type: int,
        delete_recording_after_transfer: Optional[str] = None,
        **kwargs
    ):
        self.delete_recording_after_transfer = delete_recording_after_transfer
        self.instanceid = instanceid
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type


class V1RecordsViewDetailsGet200Response(object):
    """V1RecordsViewDetailsGet200Response

    :param current_page:
    :type current_page: Optional[int]

    :param current_size:
    :type current_size: Optional[int]

    :param total_count:
    :type total_count: Optional[int]

    :param total_page:
    :type total_page: Optional[int]

    :param view_details: 事件明细集合。 
    :type view_details: Optional[List[V1RecordsViewDetailsGet200ResponseViewDetailsInner]]
    """  # noqa: E501

    current_page: Optional[int] = None
    current_size: Optional[int] = None
    total_count: Optional[int] = None
    total_page: Optional[int] = None
    view_details: Optional[List[V1RecordsViewDetailsGet200ResponseViewDetailsInner]] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        current_page: Optional[int] = None,
        current_size: Optional[int] = None,
        total_count: Optional[int] = None,
        total_page: Optional[int] = None,
        view_details: Optional[List[V1RecordsViewDetailsGet200ResponseViewDetailsInner] | List[Dict[str, Any]]] = None,
        **kwargs
    ):
        self.current_page = current_page
        self.current_size = current_size
        self.total_count = total_count
        self.total_page = total_page
        
        if view_details and isinstance(view_details, (list, List)):
            self.view_details = [V1RecordsViewDetailsGet200ResponseViewDetailsInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in view_details]
        


class V1RecordsViewDetailsGet200ResponseViewDetailsInner(object):
    """V1RecordsViewDetailsGet200ResponseViewDetailsInner

    :param record_file_name: 录制文件名称。 
    :type record_file_name: Optional[str]

    :param total_view_progress: 观看完成度（百分比），该用户累计观看该视频的完成度。 
    :type total_view_progress: Optional[str]

    :param user_name: 用户名称。匿名用户给出匿名用户标识。 
    :type user_name: Optional[str]

    :param userid: 所在同一企业下的用户 ID。 
    :type userid: Optional[str]

    :param view_end_time: 观看结束时间，UNIX时间戳（单位毫秒）。 
    :type view_end_time: Optional[int]

    :param view_start_time: Integer 观看开始时间，UNIX 时间戳（单位毫秒）。 
    :type view_start_time: Optional[int]

    :param view_time: 实际观看时长（单位毫秒）。 
    :type view_time: Optional[int]
    """  # noqa: E501

    record_file_name: Optional[str] = None
    total_view_progress: Optional[str] = None
    user_name: Optional[str] = None
    userid: Optional[str] = None
    view_end_time: Optional[int] = None
    view_start_time: Optional[int] = None
    view_time: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        record_file_name: Optional[str] = None,
        total_view_progress: Optional[str] = None,
        user_name: Optional[str] = None,
        userid: Optional[str] = None,
        view_end_time: Optional[int] = None,
        view_start_time: Optional[int] = None,
        view_time: Optional[int] = None,
        **kwargs
    ):
        self.record_file_name = record_file_name
        self.total_view_progress = total_view_progress
        self.user_name = user_name
        self.userid = userid
        self.view_end_time = view_end_time
        self.view_start_time = view_start_time
        self.view_time = view_time

