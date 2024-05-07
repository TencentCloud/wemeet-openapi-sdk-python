# coding: utf-8

"""
    腾讯会议OpenAPI

    SAAS版RESTFUL风格API

    API version: v1.0.1

    Do not edit the class manually.
"""  # noqa: E501


from typing import Dict, List, Optional, Callable

from wemeet_openapi.core import Config, DEFAULT_AUTHENTICATOR, DEFAULT_SERIALIZER
from wemeet_openapi.core.xhttp import ApiRequest, ApiResponse
from wemeet_openapi.core.authenticator import Authenticator
from wemeet_openapi.core.serializer import Serializer
from wemeet_openapi.core.exception import ServiceException, ClientException
from wemeet_openapi.service.records.model import *


class ApiV1AddressesGetRequest(object):
    """查询会议录制地址

    **描述：**  * 查询会议录制地址，可获取会议云录制的播放地址和下载地址。 * 企业 secret 鉴权用户可获取该用户所属企业下的会议录制地址，OAuth2.0 鉴权用户只能获取该企业下 OAuth2.0 应用的会议录制地址。 * 当您想实时监测会议录制相关状况时，您可以通过订阅 [录制管理](https://cloud.tencent.com/document/product/1095/53226) 中的相关事件，接收事件通知。 * 当前同一场会议的不同录制文件共用分享链接。
    
    :param meeting_record_id: 会议录制 ID。 (required)
    :type meeting_record_id: str

    :param userid: 用户 ID（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId）。
    :type userid: str

    :param operator_id: 操作者ID 必须与operator_id_type 同时提供
    :type operator_id: str

    :param operator_id_type: 操作者ID的类型 3为rooms_id 必须与operator_id_type 同时提供
    :type operator_id_type: str

    :param page: 分页page
    :type page: str

    :param page_size: 分页size
    :type page_size: str
    """  # noqa: E501

    def __init__(
        self,
        meeting_record_id: Optional[str] = None,
        userid: Optional[str] = None,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        page: Optional[str] = None,
        page_size: Optional[str] = None
    ):
        self.meeting_record_id = meeting_record_id
        self.userid = userid
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.page = page
        self.page_size = page_size


class ApiV1AddressesGetResponse(ApiResponse):
    data: Optional[V1AddressesGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1AddressesGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1AddressesRecordFileIdGetRequest(object):
    """查询单个录制文件详情（文件、纪要）

    查询单个云录制的详情信息，包括录制文件和会议纪要，并可获取播放地址和下载地址。企业 secert 鉴权用户可获取该用户所属企业下的单个录制列表，OAuth2.0 鉴权用户只能获取该企业下 OAuth2.0 应用的单个录制列表。
    
    :param record_file_id: (required)
    :type record_file_id: str

    :param userid: 用户 ID（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId）。
    :type userid: str

    :param operator_id: 操作者ID，必须与operator_id_type同时出现。
    :type operator_id: str

    :param operator_id_type: 操作者ID的类型 rooms_Id是3，必须与operator_id同时出现。
    :type operator_id_type: str

    :param body:
    :type body: object
    """  # noqa: E501

    def __init__(
        self,
        record_file_id: str,
        userid: Optional[str] = None,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.record_file_id = record_file_id
        self.userid = userid
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.body = body


class ApiV1AddressesRecordFileIdGetResponse(ApiResponse):
    data: Optional[V1AddressesRecordFileIdGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1AddressesRecordFileIdGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1MetricsRecordsGetRequest(object):
    """查询录制文件访问数据

    \\*\\*描述：\\*\\*查询会议录制 ID 对应的访问数据，按照天维度返回，支持 OAuth2\\.0 鉴权调用。  * \\*\\*所需权限点为：\\*\\*查看会议录制（VIEW\\_VIDEO） 或 管理会议录制（MANAGE\\_VIDEO）。 * \\*\\*接口请求方法：\\*\\*GET
    
    :param meeting_record_id: 会议录制 ID。 (required)
    :type meeting_record_id: str

    :param start_time: 查询起始时间戳，UNIX 时间戳（单位秒）。说明：时间区间不允许超过31天。
    :type start_time: str

    :param end_time: 查询结束时间戳，UNIX 时间戳（单位秒）。说明：时间区间不允许超过31天。
    :type end_time: str
    """  # noqa: E501

    def __init__(
        self,
        meeting_record_id: Optional[str] = None,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None
    ):
        self.meeting_record_id = meeting_record_id
        self.start_time = start_time
        self.end_time = end_time


class ApiV1MetricsRecordsGetResponse(ApiResponse):
    data: Optional[V1MetricsRecordsGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1MetricsRecordsGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1RecordsApprovalsMeetingRecordIdPutRequest(object):
    """云录制权限审批

    会议创建者，企业超级管理员，有企业录制管理权限的用户，可以对云录制观看申请进行审批操作。OAuth权限点录制管理
    
    :param meeting_record_id: 会议录制 ID，列表查询接口返回的 meeting_record_id。 (required)
    :type meeting_record_id: str

    :param body:
    :type body: V1RecordsApprovalsMeetingRecordIdPutRequest
    """  # noqa: E501

    def __init__(
        self,
        meeting_record_id: str,
        body: Optional[V1RecordsApprovalsMeetingRecordIdPutRequest] = None
    ):
        self.meeting_record_id = meeting_record_id
        self.body = body


class ApiV1RecordsApprovalsMeetingRecordIdPutResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1RecordsDeleteRequest(object):
    """删除会议的所有录制文件

    删除会议的所有录制文件，该接口会删除会议录制 ID 里对应的所有云录制文件。企业 secret 鉴权用户可删除该用户所属企业下的会议录制，OAuth2.0 鉴权用户只能删除该企业下 OAuth2.0 应用的会议录制。 <span class=\"colour\" style=\"color:rgb(51, 51, 51)\">当您想实时监测会议录制删除状况时，您可以通过订阅 </span>[删除云录制](https://cloud.tencent.com/document/product/1095/53232)<span class=\"colour\" style=\"color:rgb(51, 51, 51)\"> 的事件，接收事件通知。</span>
    
    :param meeting_id: 会议 ID。 (required)
    :type meeting_id: str

    :param meeting_record_id: 会议录制 ID。 (required)
    :type meeting_record_id: str

    :param userid: 用户 ID（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId）。
    :type userid: str

    :param operator_id_type: 操作者ID的类型，必须与operator_id同时出现
    :type operator_id_type: str

    :param operator_id: 操作者ID，根据operator_id_type的值，使用不同的类型
    :type operator_id: str
    """  # noqa: E501

    def __init__(
        self,
        meeting_id: Optional[str] = None,
        meeting_record_id: Optional[str] = None,
        userid: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        operator_id: Optional[str] = None
    ):
        self.meeting_id = meeting_id
        self.meeting_record_id = meeting_record_id
        self.userid = userid
        self.operator_id_type = operator_id_type
        self.operator_id = operator_id


class ApiV1RecordsDeleteResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1RecordsEventsGetRequest(object):
    """获取会议录制操作（查看、下载）记录

    \\*\\*描述：\\*\\*查询会议录制 ID 对应的操作记录，包括用户查看和下载，支持 OAuth2\\.0 鉴权调用。  * \\*\\*所需权限点为：\\*\\*查看会议录制（VIEW\\_VIDEO） 或 管理会议录制（MANAGE\\_VIDEO）。 * \\*\\*接口请求方法：\\*\\*GET
    
    :param meeting_record_id: 会议录制 ID，列表接口返回的是 meeting_record_id。 (required)
    :type meeting_record_id: str

    :param event_type: 查询事件类型：1：下载，2：查看。 (required)
    :type event_type: str

    :param page: 页码，从1开始，默认值为1。
    :type page: str

    :param page_size: 分页大小，默认值为20，最大为50。
    :type page_size: str

    :param start_time: 查询起始时间戳，UNIX 时间戳（单位秒）。说明：时间区间不允许超过31天。
    :type start_time: str

    :param end_time: 查询结束时间戳，UNIX 时间戳（单位秒）。说明：时间区间不允许超过31天。
    :type end_time: str
    """  # noqa: E501

    def __init__(
        self,
        meeting_record_id: Optional[str] = None,
        event_type: Optional[str] = None,
        page: Optional[str] = None,
        page_size: Optional[str] = None,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None
    ):
        self.meeting_record_id = meeting_record_id
        self.event_type = event_type
        self.page = page
        self.page_size = page_size
        self.start_time = start_time
        self.end_time = end_time


class ApiV1RecordsEventsGetResponse(ApiResponse):
    data: Optional[V1RecordsEventsGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1RecordsEventsGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1RecordsGetRequest(object):
    """查询会议录制列表

    获取用户云录制记录，根据用户 ID、会议 ID、会议 code 进行查询，支持根据时间区间分页获取。 企业 secret 鉴权用户可获取该用户所属企业下的会议录制列表，OAuth2.0 鉴权用户只能获取该企业下 OAuth2.0 应用的会议录制列表。 当您想实时监测会议录制相关状况时，您可以通过订阅 [录制管理](https://cloud.tencent.com/document/product/1095/53226) 中的相关事件，接收事件通知。 当前同一场会议的不同录制文件共用分享链接。
    
    :param start_time: 查询起始时间戳，UNIX 时间戳（单位秒）。说明：时间区间不允许超过31天。 (required)
    :type start_time: str

    :param end_time: 查询结束时间戳，UNIX 时间戳（单位秒）。说明：时间区间不允许超过31天。 (required)
    :type end_time: str

    :param userid: 用户 ID（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId），当会议 ID 和会议 code 均为空时，表示查询用户所有会议的录制列表。
    :type userid: str

    :param meeting_id: 会议的唯一 ID，不为空时优先根据会议 ID 查询。
    :type meeting_id: str

    :param meeting_code: 会议 code，当 meeting_id 为空且 meeting_code 不为空时根据会议 code 查询。
    :type meeting_code: str

    :param page: 页码，从1开始，默认值为1。
    :type page: str

    :param page_size: 分页大小，默认值为10，最大为20。
    :type page_size: str

    :param operator_id: 操作者ID，必须与operator_id_type同时出现。
    :type operator_id: str

    :param operator_id_type: 操作者ID的类型，必须与operator_id同时出现。
    :type operator_id_type: str

    :param media_set_type:
    :type media_set_type: str

    :param body:
    :type body: object
    """  # noqa: E501

    def __init__(
        self,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        userid: Optional[str] = None,
        meeting_id: Optional[str] = None,
        meeting_code: Optional[str] = None,
        page: Optional[str] = None,
        page_size: Optional[str] = None,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        media_set_type: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.userid = userid
        self.meeting_id = meeting_id
        self.meeting_code = meeting_code
        self.page = page
        self.page_size = page_size
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.media_set_type = media_set_type
        self.body = body


class ApiV1RecordsGetResponse(ApiResponse):
    data: Optional[V1RecordsGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1RecordsGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1RecordsRecordFileIdDeleteRequest(object):
    """删除单个录制文件

    删除单个录制文件，该接口支持从会议中删除指定的某个录制文件。企业 secret 鉴权用户可删除该用户所属企业下的单个录制文件，OAuth2.0 鉴权用户只能删除该企业下 OAuth2.0 应用的单个录制文件。 <span class=\"colour\" style=\"color:rgb(51, 51, 51)\">当您想实时监测会议录制删除状况时，您可以通过订阅 </span>[删除云录制](https://cloud.tencent.com/document/product/1095/53232)<span class=\"colour\" style=\"color:rgb(51, 51, 51)\"> 的事件，接收事件通知。</span>
    
    :param record_file_id: 录制文件 ID。 (required)
    :type record_file_id: str

    :param meeting_id: 会议 ID。 (required)
    :type meeting_id: str

    :param userid: 用户 ID（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId）。
    :type userid: str

    :param operator_id: 操作者ID，根据operator_id_type的值，使用不同的类型，必须与operator_id_type同时出现
    :type operator_id: str

    :param operator_id_type: 操作者ID的类型，必须与operator_id同时出现
    :type operator_id_type: str

    :param body:
    :type body: object
    """  # noqa: E501

    def __init__(
        self,
        record_file_id: str,
        meeting_id: Optional[str] = None,
        userid: Optional[str] = None,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.record_file_id = record_file_id
        self.meeting_id = meeting_id
        self.userid = userid
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.body = body


class ApiV1RecordsRecordFileIdDeleteResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1RecordsSettingsMeetingRecordIdPutRequest(object):
    """修改会议录制共享设置

    根据会议录制 ID 修改共享等配置，支持修改共享权限、共享密码、共享有效期等信息，支持 OAuth2.0 鉴权调用。 所需权限点为：管理会议录制（MANAGE\\_VIDEO）。
    
    :param meeting_record_id: 会议录制 ID。 (required)
    :type meeting_record_id: str

    :param body:
    :type body: V1RecordsSettingsMeetingRecordIdPutRequest
    """  # noqa: E501

    def __init__(
        self,
        meeting_record_id: str,
        body: Optional[V1RecordsSettingsMeetingRecordIdPutRequest] = None
    ):
        self.meeting_record_id = meeting_record_id
        self.body = body


class ApiV1RecordsSettingsMeetingRecordIdPutResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1RecordsTranscriptsDetailsGetRequest(object):
    """查询会议纪要详情

    获取云录制会议纪要的详情，包含时间戳、文本等内容。支持 OAuth2.0 鉴权调用，仅支持授权用户为商业版、企业版、教育版。  所需权限点为：查看会议录制（VIEW\\_VIDEO） 或 管理会议录制（MANAGE\\_VIDEO）。
    
    :param meeting_id: 会议id (required)
    :type meeting_id: str

    :param record_file_id: 录制id (required)
    :type record_file_id: str

    :param operator_id: 操作者ID。operator_id 必须与 operator_id_type 配合使用。根据operator_id_type的值，operator_id 代表不同类型。 (required)
    :type operator_id: str

    :param operator_id_type: 操作者ID的类型：  1. 企业用户userid 2：open_id 3. rooms设备rooms_id (required)
    :type operator_id_type: str

    :param pid: 查询的起始段落 ID。获取 pid 后（含）的段落，默认从0开始。
    :type pid: str

    :param limit: 查询的段落数，默认查询全量数据
    :type limit: str

    :param transcripts_type: 转写类型，默认是0。 0：原文版 1：智能优化版
    :type transcripts_type: str

    :param body:
    :type body: object
    """  # noqa: E501

    def __init__(
        self,
        meeting_id: Optional[str] = None,
        record_file_id: Optional[str] = None,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        pid: Optional[str] = None,
        limit: Optional[str] = None,
        transcripts_type: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.meeting_id = meeting_id
        self.record_file_id = record_file_id
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.pid = pid
        self.limit = limit
        self.transcripts_type = transcripts_type
        self.body = body


class ApiV1RecordsTranscriptsDetailsGetResponse(ApiResponse):
    data: Optional[V1RecordsTranscriptsDetailsGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1RecordsTranscriptsDetailsGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1RecordsTranscriptsParagraphsGetRequest(object):
    """查询会议纪要段落信息

    获取云录制会议纪要的段落信息（段落总数、段落 ID）。支持 OAuth2\\.0 鉴权调用，仅支持授权用户为商业版、企业版、教育版。  所需权限点为：查看会议录制（VIEW\\_VIDEO） 或 管理会议录制（MANAGE\\_VIDEO）。
    
    :param meeting_id: 会议 ID。 (required)
    :type meeting_id: str

    :param record_file_id: 录制文件 ID。 (required)
    :type record_file_id: str

    :param operator_id_type: 操作者ID的类型：  1. 企业用户userid 2：open_id 3. rooms设备rooms_id (required)
    :type operator_id_type: str

    :param operator_id: 操作者ID。operator_id 必须与 operator_id_type 配合使用。根据operator_id_type的值，operator_id 代表不同类型。 (required)
    :type operator_id: str

    :param body:
    :type body: object
    """  # noqa: E501

    def __init__(
        self,
        meeting_id: Optional[str] = None,
        record_file_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        operator_id: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.meeting_id = meeting_id
        self.record_file_id = record_file_id
        self.operator_id_type = operator_id_type
        self.operator_id = operator_id
        self.body = body


class ApiV1RecordsTranscriptsParagraphsGetResponse(ApiResponse):
    data: Optional[V1RecordsTranscriptsParagraphsGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1RecordsTranscriptsParagraphsGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1RecordsTranscriptsSearchGetRequest(object):
    """查询会议纪要搜索结果

    根据指定内容搜索会议纪要。支持 OAuth2\\.0 鉴权调用，仅支持授权用户为商业版、企业版、教育版。  所需权限点为：查看会议录制（VIEW\\_VIDEO） 或 管理会议录制（MANAGE\\_VIDEO）。
    
    :param meeting_id: 会议ID (required)
    :type meeting_id: str

    :param record_file_id: 录制文件id (required)
    :type record_file_id: str

    :param text: 搜索的文本, 如果是中文, 需要urlencode一下 (required)
    :type text: str

    :param operator_id_type: id类型: 1: 常规用户 2：open_id 3:rooms (required)
    :type operator_id_type: str

    :param operator_id: 用户名 (required)
    :type operator_id: str

    :param transcripts_type: 转写类型，默认是0。 0：原文版 1：智能优化版
    :type transcripts_type: str

    :param body:
    :type body: object
    """  # noqa: E501

    def __init__(
        self,
        meeting_id: Optional[str] = None,
        record_file_id: Optional[str] = None,
        text: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        operator_id: Optional[str] = None,
        transcripts_type: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.meeting_id = meeting_id
        self.record_file_id = record_file_id
        self.text = text
        self.operator_id_type = operator_id_type
        self.operator_id = operator_id
        self.transcripts_type = transcripts_type
        self.body = body


class ApiV1RecordsTranscriptsSearchGetResponse(ApiResponse):
    data: Optional[V1RecordsTranscriptsSearchGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1RecordsTranscriptsSearchGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1RecordsTransferRecordingPutRequest(object):
    """设置专网会议录制是否转存

    描述：设置指定会议的录制文件是否转存 企业 secret 鉴权用户和OAuth2.0 鉴权用户并且有录制访问权限可指定会议录制设置。 设置仅支持对专网会议录制生效，如果会议为公网会议则返回失败 通过会议录制ID设置录制是否转存， 根据混合云集群是否开启转存： 如果混合云集群已开启录制转存功能 对指定的会议录制可通过API设置转存，和转存完成后的删除策略 如果录制未加入转存任务或转存失败， 则将录制加入转存任务 如果录制已加入转存任务， 或转存已完成， 则返回失败 如果混合云集群未开启专网会议录制转存 不支持通过API设置会议录制的转存， 返回失败
    
    :param meeting_id: 会议ID (required)
    :type meeting_id: str

    :param meeting_record_id: 会议录制ID (required)
    :type meeting_record_id: str

    :param body:
    :type body: V1RecordsTransferRecordingPutRequest
    """  # noqa: E501

    def __init__(
        self,
        meeting_id: Optional[str] = None,
        meeting_record_id: Optional[str] = None,
        body: Optional[V1RecordsTransferRecordingPutRequest] = None
    ):
        self.meeting_id = meeting_id
        self.meeting_record_id = meeting_record_id
        self.body = body


class ApiV1RecordsTransferRecordingPutResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1RecordsViewDetailsGetRequest(object):
    """查询录制文件观看流水记录

    查询会议云录制在一段时间内的观看记录，每次播放都会有一条记录。 支持 JWT 和 OAuth，OAuth 2.0鉴权用户只能获取该企业下 OAuth 2.0应用创建的会议记录 权限点：查看会议录制或管理会议录制。
    
    :param record_file_id: 录制文件 ID。 (required)
    :type record_file_id: str

    :param operator_id_type: 操作者 ID 的类型： 1：userid 2：open_id (required)
    :type operator_id_type: str

    :param operator_id: 操作者 ID。operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 (required)
    :type operator_id: str

    :param page_size: 分页大小，默认20，最大50
    :type page_size: str

    :param page: 页码，从1开始，默认1
    :type page: str

    :param start_time: 查询起始时间戳，UNIX 时间戳（单位毫秒）。 说明：仅存储最近31天的数据，默认展示最近31天的数据。
    :type start_time: str

    :param end_time: 查询结束时间戳，UNIX 时间戳（单位毫秒）。 说明：仅存储最近31天的数据，默认展示最近31天的数据
    :type end_time: str

    :param body:
    :type body: object
    """  # noqa: E501

    def __init__(
        self,
        record_file_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        operator_id: Optional[str] = None,
        page_size: Optional[str] = None,
        page: Optional[str] = None,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.record_file_id = record_file_id
        self.operator_id_type = operator_id_type
        self.operator_id = operator_id
        self.page_size = page_size
        self.page = page
        self.start_time = start_time
        self.end_time = end_time
        self.body = body


class ApiV1RecordsViewDetailsGetResponse(ApiResponse):
    data: Optional[V1RecordsViewDetailsGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1RecordsViewDetailsGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class RecordsApi:
    def __init__(self, config: Config):
        self.__config = config

    def v1_addresses_get(
        self,
        request: ApiV1AddressesGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1AddressesGetResponse:
        """v1_addresses_get 查询会议录制地址[/v1/addresses - GET]

            **描述：**  * 查询会议录制地址，可获取会议云录制的播放地址和下载地址。 * 企业 secret 鉴权用户可获取该用户所属企业下的会议录制地址，OAuth2.0 鉴权用户只能获取该企业下 OAuth2.0 应用的会议录制地址。 * 当您想实时监测会议录制相关状况时，您可以通过订阅 [录制管理](https://cloud.tencent.com/document/product/1095/53226) 中的相关事件，接收事件通知。 * 当前同一场会议的不同录制文件共用分享链接。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/addresses",
                                 authenticators=authenticators,
                                 header=header, 
                                 serializer=serializer)

            # verify the required parameter 'meeting_record_id' is set
            if request.meeting_record_id is None:
                raise Exception("meeting_record_id is required and must be specified")
            # path 参数
            # query 参数
            if request.meeting_record_id is not None:
                api_req.query_params.append(('meeting_record_id', request.meeting_record_id))
            if request.userid is not None:
                api_req.query_params.append(('userid', request.userid))
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            if request.page is not None:
                api_req.query_params.append(('page', request.page))
            if request.page_size is not None:
                api_req.query_params.append(('page_size', request.page_size))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1AddressesGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1AddressesGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_addresses_record_file_id_get(
        self,
        request: ApiV1AddressesRecordFileIdGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1AddressesRecordFileIdGetResponse:
        """v1_addresses_record_file_id_get 查询单个录制文件详情（文件、纪要）[/v1/addresses/{record_file_id} - GET]

            查询单个云录制的详情信息，包括录制文件和会议纪要，并可获取播放地址和下载地址。企业 secert 鉴权用户可获取该用户所属企业下的单个录制列表，OAuth2.0 鉴权用户只能获取该企业下 OAuth2.0 应用的单个录制列表。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/addresses/{record_file_id}",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'record_file_id' is set
            if request.record_file_id is None:
                raise Exception("record_file_id is required and must be specified")
            # path 参数
            if request.record_file_id is not None:
                api_req.path_params['record_file_id'] = request.record_file_id
            # query 参数
            if request.userid is not None:
                api_req.query_params.append(('userid', request.userid))
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1AddressesRecordFileIdGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1AddressesRecordFileIdGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_metrics_records_get(
        self,
        request: ApiV1MetricsRecordsGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1MetricsRecordsGetResponse:
        """v1_metrics_records_get 查询录制文件访问数据[/v1/metrics/records - GET]

            \\*\\*描述：\\*\\*查询会议录制 ID 对应的访问数据，按照天维度返回，支持 OAuth2\\.0 鉴权调用。  * \\*\\*所需权限点为：\\*\\*查看会议录制（VIEW\\_VIDEO） 或 管理会议录制（MANAGE\\_VIDEO）。 * \\*\\*接口请求方法：\\*\\*GET
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/metrics/records",
                                 authenticators=authenticators,
                                 header=header, 
                                 serializer=serializer)

            # verify the required parameter 'meeting_record_id' is set
            if request.meeting_record_id is None:
                raise Exception("meeting_record_id is required and must be specified")
            # path 参数
            # query 参数
            if request.meeting_record_id is not None:
                api_req.query_params.append(('meeting_record_id', request.meeting_record_id))
            if request.start_time is not None:
                api_req.query_params.append(('start_time', request.start_time))
            if request.end_time is not None:
                api_req.query_params.append(('end_time', request.end_time))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1MetricsRecordsGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1MetricsRecordsGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_records_approvals_meeting_record_id_put(
        self,
        request: ApiV1RecordsApprovalsMeetingRecordIdPutRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1RecordsApprovalsMeetingRecordIdPutResponse:
        """v1_records_approvals_meeting_record_id_put 云录制权限审批[/v1/records/approvals/{meeting_record_id} - PUT]

            会议创建者，企业超级管理员，有企业录制管理权限的用户，可以对云录制观看申请进行审批操作。OAuth权限点录制管理
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/records/approvals/{meeting_record_id}",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'meeting_record_id' is set
            if request.meeting_record_id is None:
                raise Exception("meeting_record_id is required and must be specified")
            # path 参数
            if request.meeting_record_id is not None:
                api_req.path_params['meeting_record_id'] = request.meeting_record_id
            # query 参数
            # 发送请求
            api_resp = self.__config.clt.put(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1RecordsApprovalsMeetingRecordIdPutResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_records_delete(
        self,
        request: ApiV1RecordsDeleteRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1RecordsDeleteResponse:
        """v1_records_delete 删除会议的所有录制文件[/v1/records - DELETE]

            删除会议的所有录制文件，该接口会删除会议录制 ID 里对应的所有云录制文件。企业 secret 鉴权用户可删除该用户所属企业下的会议录制，OAuth2.0 鉴权用户只能删除该企业下 OAuth2.0 应用的会议录制。 <span class=\"colour\" style=\"color:rgb(51, 51, 51)\">当您想实时监测会议录制删除状况时，您可以通过订阅 </span>[删除云录制](https://cloud.tencent.com/document/product/1095/53232)<span class=\"colour\" style=\"color:rgb(51, 51, 51)\"> 的事件，接收事件通知。</span>
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/records",
                                 authenticators=authenticators,
                                 header=header, 
                                 serializer=serializer)

            # verify the required parameter 'meeting_id' is set
            if request.meeting_id is None:
                raise Exception("meeting_id is required and must be specified")
            # verify the required parameter 'meeting_record_id' is set
            if request.meeting_record_id is None:
                raise Exception("meeting_record_id is required and must be specified")
            # path 参数
            # query 参数
            if request.meeting_id is not None:
                api_req.query_params.append(('meeting_id', request.meeting_id))
            if request.meeting_record_id is not None:
                api_req.query_params.append(('meeting_record_id', request.meeting_record_id))
            if request.userid is not None:
                api_req.query_params.append(('userid', request.userid))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            # 发送请求
            api_resp = self.__config.clt.delete(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1RecordsDeleteResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_records_events_get(
        self,
        request: ApiV1RecordsEventsGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1RecordsEventsGetResponse:
        """v1_records_events_get 获取会议录制操作（查看、下载）记录[/v1/records/events - GET]

            \\*\\*描述：\\*\\*查询会议录制 ID 对应的操作记录，包括用户查看和下载，支持 OAuth2\\.0 鉴权调用。  * \\*\\*所需权限点为：\\*\\*查看会议录制（VIEW\\_VIDEO） 或 管理会议录制（MANAGE\\_VIDEO）。 * \\*\\*接口请求方法：\\*\\*GET
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/records/events",
                                 authenticators=authenticators,
                                 header=header, 
                                 serializer=serializer)

            # verify the required parameter 'meeting_record_id' is set
            if request.meeting_record_id is None:
                raise Exception("meeting_record_id is required and must be specified")
            # verify the required parameter 'event_type' is set
            if request.event_type is None:
                raise Exception("event_type is required and must be specified")
            # path 参数
            # query 参数
            if request.meeting_record_id is not None:
                api_req.query_params.append(('meeting_record_id', request.meeting_record_id))
            if request.event_type is not None:
                api_req.query_params.append(('event_type', request.event_type))
            if request.page is not None:
                api_req.query_params.append(('page', request.page))
            if request.page_size is not None:
                api_req.query_params.append(('page_size', request.page_size))
            if request.start_time is not None:
                api_req.query_params.append(('start_time', request.start_time))
            if request.end_time is not None:
                api_req.query_params.append(('end_time', request.end_time))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1RecordsEventsGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1RecordsEventsGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_records_get(
        self,
        request: ApiV1RecordsGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1RecordsGetResponse:
        """v1_records_get 查询会议录制列表[/v1/records - GET]

            获取用户云录制记录，根据用户 ID、会议 ID、会议 code 进行查询，支持根据时间区间分页获取。 企业 secret 鉴权用户可获取该用户所属企业下的会议录制列表，OAuth2.0 鉴权用户只能获取该企业下 OAuth2.0 应用的会议录制列表。 当您想实时监测会议录制相关状况时，您可以通过订阅 [录制管理](https://cloud.tencent.com/document/product/1095/53226) 中的相关事件，接收事件通知。 当前同一场会议的不同录制文件共用分享链接。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/records",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'start_time' is set
            if request.start_time is None:
                raise Exception("start_time is required and must be specified")
            # verify the required parameter 'end_time' is set
            if request.end_time is None:
                raise Exception("end_time is required and must be specified")
            # path 参数
            # query 参数
            if request.userid is not None:
                api_req.query_params.append(('userid', request.userid))
            if request.start_time is not None:
                api_req.query_params.append(('start_time', request.start_time))
            if request.end_time is not None:
                api_req.query_params.append(('end_time', request.end_time))
            if request.meeting_id is not None:
                api_req.query_params.append(('meeting_id', request.meeting_id))
            if request.meeting_code is not None:
                api_req.query_params.append(('meeting_code', request.meeting_code))
            if request.page is not None:
                api_req.query_params.append(('page', request.page))
            if request.page_size is not None:
                api_req.query_params.append(('page_size', request.page_size))
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            if request.media_set_type is not None:
                api_req.query_params.append(('media_set_type', request.media_set_type))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1RecordsGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1RecordsGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_records_record_file_id_delete(
        self,
        request: ApiV1RecordsRecordFileIdDeleteRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1RecordsRecordFileIdDeleteResponse:
        """v1_records_record_file_id_delete 删除单个录制文件[/v1/records/{record_file_id} - DELETE]

            删除单个录制文件，该接口支持从会议中删除指定的某个录制文件。企业 secret 鉴权用户可删除该用户所属企业下的单个录制文件，OAuth2.0 鉴权用户只能删除该企业下 OAuth2.0 应用的单个录制文件。 <span class=\"colour\" style=\"color:rgb(51, 51, 51)\">当您想实时监测会议录制删除状况时，您可以通过订阅 </span>[删除云录制](https://cloud.tencent.com/document/product/1095/53232)<span class=\"colour\" style=\"color:rgb(51, 51, 51)\"> 的事件，接收事件通知。</span>
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/records/{record_file_id}",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'record_file_id' is set
            if request.record_file_id is None:
                raise Exception("record_file_id is required and must be specified")
            # verify the required parameter 'meeting_id' is set
            if request.meeting_id is None:
                raise Exception("meeting_id is required and must be specified")
            # path 参数
            if request.record_file_id is not None:
                api_req.path_params['record_file_id'] = request.record_file_id
            # query 参数
            if request.meeting_id is not None:
                api_req.query_params.append(('meeting_id', request.meeting_id))
            if request.userid is not None:
                api_req.query_params.append(('userid', request.userid))
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            # 发送请求
            api_resp = self.__config.clt.delete(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1RecordsRecordFileIdDeleteResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_records_settings_meeting_record_id_put(
        self,
        request: ApiV1RecordsSettingsMeetingRecordIdPutRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1RecordsSettingsMeetingRecordIdPutResponse:
        """v1_records_settings_meeting_record_id_put 修改会议录制共享设置[/v1/records/settings/{meeting_record_id} - PUT]

            根据会议录制 ID 修改共享等配置，支持修改共享权限、共享密码、共享有效期等信息，支持 OAuth2.0 鉴权调用。 所需权限点为：管理会议录制（MANAGE\\_VIDEO）。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/records/settings/{meeting_record_id}",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'meeting_record_id' is set
            if request.meeting_record_id is None:
                raise Exception("meeting_record_id is required and must be specified")
            # path 参数
            if request.meeting_record_id is not None:
                api_req.path_params['meeting_record_id'] = request.meeting_record_id
            # query 参数
            # 发送请求
            api_resp = self.__config.clt.put(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1RecordsSettingsMeetingRecordIdPutResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_records_transcripts_details_get(
        self,
        request: ApiV1RecordsTranscriptsDetailsGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1RecordsTranscriptsDetailsGetResponse:
        """v1_records_transcripts_details_get 查询会议纪要详情[/v1/records/transcripts/details - GET]

            获取云录制会议纪要的详情，包含时间戳、文本等内容。支持 OAuth2.0 鉴权调用，仅支持授权用户为商业版、企业版、教育版。  所需权限点为：查看会议录制（VIEW\\_VIDEO） 或 管理会议录制（MANAGE\\_VIDEO）。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/records/transcripts/details",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'meeting_id' is set
            if request.meeting_id is None:
                raise Exception("meeting_id is required and must be specified")
            # verify the required parameter 'record_file_id' is set
            if request.record_file_id is None:
                raise Exception("record_file_id is required and must be specified")
            # verify the required parameter 'operator_id' is set
            if request.operator_id is None:
                raise Exception("operator_id is required and must be specified")
            # verify the required parameter 'operator_id_type' is set
            if request.operator_id_type is None:
                raise Exception("operator_id_type is required and must be specified")
            # path 参数
            # query 参数
            if request.meeting_id is not None:
                api_req.query_params.append(('meeting_id', request.meeting_id))
            if request.record_file_id is not None:
                api_req.query_params.append(('record_file_id', request.record_file_id))
            if request.pid is not None:
                api_req.query_params.append(('pid', request.pid))
            if request.limit is not None:
                api_req.query_params.append(('limit', request.limit))
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            if request.transcripts_type is not None:
                api_req.query_params.append(('transcripts_type', request.transcripts_type))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1RecordsTranscriptsDetailsGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1RecordsTranscriptsDetailsGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_records_transcripts_paragraphs_get(
        self,
        request: ApiV1RecordsTranscriptsParagraphsGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1RecordsTranscriptsParagraphsGetResponse:
        """v1_records_transcripts_paragraphs_get 查询会议纪要段落信息[/v1/records/transcripts/paragraphs - GET]

            获取云录制会议纪要的段落信息（段落总数、段落 ID）。支持 OAuth2\\.0 鉴权调用，仅支持授权用户为商业版、企业版、教育版。  所需权限点为：查看会议录制（VIEW\\_VIDEO） 或 管理会议录制（MANAGE\\_VIDEO）。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/records/transcripts/paragraphs",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'meeting_id' is set
            if request.meeting_id is None:
                raise Exception("meeting_id is required and must be specified")
            # verify the required parameter 'record_file_id' is set
            if request.record_file_id is None:
                raise Exception("record_file_id is required and must be specified")
            # verify the required parameter 'operator_id_type' is set
            if request.operator_id_type is None:
                raise Exception("operator_id_type is required and must be specified")
            # verify the required parameter 'operator_id' is set
            if request.operator_id is None:
                raise Exception("operator_id is required and must be specified")
            # path 参数
            # query 参数
            if request.meeting_id is not None:
                api_req.query_params.append(('meeting_id', request.meeting_id))
            if request.record_file_id is not None:
                api_req.query_params.append(('record_file_id', request.record_file_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1RecordsTranscriptsParagraphsGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1RecordsTranscriptsParagraphsGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_records_transcripts_search_get(
        self,
        request: ApiV1RecordsTranscriptsSearchGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1RecordsTranscriptsSearchGetResponse:
        """v1_records_transcripts_search_get 查询会议纪要搜索结果[/v1/records/transcripts/search - GET]

            根据指定内容搜索会议纪要。支持 OAuth2\\.0 鉴权调用，仅支持授权用户为商业版、企业版、教育版。  所需权限点为：查看会议录制（VIEW\\_VIDEO） 或 管理会议录制（MANAGE\\_VIDEO）。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/records/transcripts/search",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'meeting_id' is set
            if request.meeting_id is None:
                raise Exception("meeting_id is required and must be specified")
            # verify the required parameter 'record_file_id' is set
            if request.record_file_id is None:
                raise Exception("record_file_id is required and must be specified")
            # verify the required parameter 'text' is set
            if request.text is None:
                raise Exception("text is required and must be specified")
            # verify the required parameter 'operator_id_type' is set
            if request.operator_id_type is None:
                raise Exception("operator_id_type is required and must be specified")
            # verify the required parameter 'operator_id' is set
            if request.operator_id is None:
                raise Exception("operator_id is required and must be specified")
            # path 参数
            # query 参数
            if request.meeting_id is not None:
                api_req.query_params.append(('meeting_id', request.meeting_id))
            if request.record_file_id is not None:
                api_req.query_params.append(('record_file_id', request.record_file_id))
            if request.text is not None:
                api_req.query_params.append(('text', request.text))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.transcripts_type is not None:
                api_req.query_params.append(('transcripts_type', request.transcripts_type))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1RecordsTranscriptsSearchGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1RecordsTranscriptsSearchGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_records_transfer_recording_put(
        self,
        request: ApiV1RecordsTransferRecordingPutRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1RecordsTransferRecordingPutResponse:
        """v1_records_transfer_recording_put 设置专网会议录制是否转存[/v1/records/transfer-recording - PUT]

            描述：设置指定会议的录制文件是否转存 企业 secret 鉴权用户和OAuth2.0 鉴权用户并且有录制访问权限可指定会议录制设置。 设置仅支持对专网会议录制生效，如果会议为公网会议则返回失败 通过会议录制ID设置录制是否转存， 根据混合云集群是否开启转存： 如果混合云集群已开启录制转存功能 对指定的会议录制可通过API设置转存，和转存完成后的删除策略 如果录制未加入转存任务或转存失败， 则将录制加入转存任务 如果录制已加入转存任务， 或转存已完成， 则返回失败 如果混合云集群未开启专网会议录制转存 不支持通过API设置会议录制的转存， 返回失败
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/records/transfer-recording",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'meeting_id' is set
            if request.meeting_id is None:
                raise Exception("meeting_id is required and must be specified")
            # verify the required parameter 'meeting_record_id' is set
            if request.meeting_record_id is None:
                raise Exception("meeting_record_id is required and must be specified")
            # path 参数
            # query 参数
            if request.meeting_id is not None:
                api_req.query_params.append(('meeting_id', request.meeting_id))
            if request.meeting_record_id is not None:
                api_req.query_params.append(('meeting_record_id', request.meeting_record_id))
            # 发送请求
            api_resp = self.__config.clt.put(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1RecordsTransferRecordingPutResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_records_view_details_get(
        self,
        request: ApiV1RecordsViewDetailsGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1RecordsViewDetailsGetResponse:
        """v1_records_view_details_get 查询录制文件观看流水记录[/v1/records/view-details - GET]

            查询会议云录制在一段时间内的观看记录，每次播放都会有一条记录。 支持 JWT 和 OAuth，OAuth 2.0鉴权用户只能获取该企业下 OAuth 2.0应用创建的会议记录 权限点：查看会议录制或管理会议录制。
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/records/view-details",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'record_file_id' is set
            if request.record_file_id is None:
                raise Exception("record_file_id is required and must be specified")
            # verify the required parameter 'operator_id_type' is set
            if request.operator_id_type is None:
                raise Exception("operator_id_type is required and must be specified")
            # verify the required parameter 'operator_id' is set
            if request.operator_id is None:
                raise Exception("operator_id is required and must be specified")
            # path 参数
            # query 参数
            if request.record_file_id is not None:
                api_req.query_params.append(('record_file_id', request.record_file_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.page_size is not None:
                api_req.query_params.append(('page_size', request.page_size))
            if request.page is not None:
                api_req.query_params.append(('page', request.page))
            if request.start_time is not None:
                api_req.query_params.append(('start_time', request.start_time))
            if request.end_time is not None:
                api_req.query_params.append(('end_time', request.end_time))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1RecordsViewDetailsGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1RecordsViewDetailsGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

