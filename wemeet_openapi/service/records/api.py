# coding: utf-8

"""
    腾讯会议OpenAPI

    SAAS版RESTFUL风格API

    API version: v1.0.4

    Do not edit the class manually.
"""  # noqa: E501


from typing import Dict, List, Optional, Callable, BinaryIO

from wemeet_openapi.core import Config, DEFAULT_AUTHENTICATOR, DEFAULT_SERIALIZER
from wemeet_openapi.core.xhttp import ApiRequest, ApiResponse
from wemeet_openapi.core.authenticator import Authenticator
from wemeet_openapi.core.serializer import Serializer
from wemeet_openapi.core.exception import ServiceException, ClientException
from wemeet_openapi.service.records.model import *

from requests_toolbelt import MultipartEncoder


class ApiV1AddressesGetRequest(object):
    """查询会议录制地址

    **描述：**  * 查询会议录制地址，可获取会议云录制的播放地址和下载地址。 * 企业 secret 鉴权用户可获取该用户所属企业下的会议录制地址，OAuth2.0 鉴权用户只能获取该企业下 OAuth2.0 应用的会议录制地址。 * 当您想实时监测会议录制相关状况时，您可以通过订阅 [录制管理](https://cloud.tencent.com/document/product/1095/53226) 中的相关事件，接收事件通知。 * 当前同一场会议的不同录制文件共用分享链接。
    
    :param meeting_record_id: 会议录制 ID。 (required)
    :type meeting_record_id: str

    :param operator_id: 操作者ID 必须与operator_id_type 同时提供
    :type operator_id: str

    :param operator_id_type: 操作者ID的类型 3为rooms_id 必须与operator_id_type 同时提供
    :type operator_id_type: str

    :param userid: 用户 ID（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId）。
    :type userid: str

    :param page_size: 分页size
    :type page_size: str

    :param page: 分页page
    :type page: str

    :param address_type:
    :type address_type: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        meeting_record_id: Optional[str] = None,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        userid: Optional[str] = None,
        page_size: Optional[str] = None,
        page: Optional[str] = None,
        address_type: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.meeting_record_id = meeting_record_id
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.userid = userid
        self.page_size = page_size
        self.page = page
        self.address_type = address_type
        self.body = body

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
    """查询单个录制详情（文件、转写、纪要）

    查询单个云录制的详情信息，包括录制文件和会议纪要，并可获取播放地址和下载地址。企业 secert 鉴权用户可获取该用户所属企业下的单个录制列表，OAuth2.0 鉴权用户只能获取该企业下 OAuth2.0 应用的单个录制列表。
    
    :param record_file_id: (required)
    :type record_file_id: str

    :param operator_id: 操作者ID，必须与operator_id_type同时出现。
    :type operator_id: str

    :param operator_id_type: 操作者ID的类型 rooms_Id是3，必须与operator_id同时出现。
    :type operator_id_type: str

    :param userid: 用户 ID（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId）。
    :type userid: str

    :param address_type:
    :type address_type: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        record_file_id: str,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        userid: Optional[str] = None,
        address_type: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.record_file_id = record_file_id
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.userid = userid
        self.address_type = address_type
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


class ApiV1FilesRecordsUploadAllPostRequest(object):
    """上传录制文件

    

    :param operator_id: (required)
    :type operator_id: str

    :param operator_id_type: (required)
    :type operator_id_type: int

    :param file_name: (required)
    :type file_name: str

    :param file_type: (required)
    :type file_type: str

    :param file_size: (required)
    :type file_size: int

    :param file_checksum: (required)
    :type file_checksum: str

    :param file_content: (required)
    :type file_content: bytearray

    :param speak_number: (required)
    :type speak_number: int

    :param ai_record:
    :type ai_record: bool
    """  # noqa: E501


    def __init__(
        self,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[int] = None,
        file_name: Optional[str] = None,
        file_type: Optional[str] = None,
        file_size: Optional[int] = None,
        file_checksum: Optional[str] = None,
        file_content: Optional[BinaryIO] = None,
        speak_number: Optional[int] = None,
        ai_record: Optional[bool] = None
    ):
        
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.file_name = file_name
        self.file_type = file_type
        self.file_size = file_size
        self.file_checksum = file_checksum
        self.file_content = file_content
        self.speak_number = speak_number
        self.ai_record = ai_record

class ApiV1FilesRecordsUploadAllPostResponse(ApiResponse):
    data: Optional[V1FilesRecordsUploadAllPost200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1FilesRecordsUploadAllPost200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1FilesRecordsUploadFinishPostRequest(object):
    """分块上传录制文件 - 上传完成

    
    :param body:
    :type body: V1FilesRecordsUploadFinishPostRequest
    """  # noqa: E501


    def __init__(
        self,
        body: Optional[V1FilesRecordsUploadFinishPostRequest] = None
    ):
        self.body = body

class ApiV1FilesRecordsUploadFinishPostResponse(ApiResponse):
    data: Optional[V1FilesRecordsUploadAllPost200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1FilesRecordsUploadAllPost200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1FilesRecordsUploadPartPostRequest(object):
    """分块上传录制文件 - 上传

    

    :param operator_id: String 操作者 ID。operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 (required)
    :type operator_id: str

    :param operator_id_type: 操作人 ID 类型： 1：userid (required)
    :type operator_id_type: int

    :param upload_id: 上传事务 ID。 (required)
    :type upload_id: str

    :param file_size: 文件大小（以字节为单位），需按预上传返回的 block_size 填写（最后一个文件块按照实际大小填写）。 (required)
    :type file_size: int

    :param file_seq: 文件块号，从1开始计数。最后一个文件块允许小于 block_size 的值。 (required)
    :type file_seq: int

    :param file_checksum: 文件校验和，文件内容 MD5 结果的十六进制表示。 (required)
    :type file_checksum: str

    :param file_content: 文件二进制内容。 (required)
    :type file_content: bytearray
    """  # noqa: E501


    def __init__(
        self,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[int] = None,
        upload_id: Optional[str] = None,
        file_size: Optional[int] = None,
        file_seq: Optional[int] = None,
        file_checksum: Optional[str] = None,
        file_content: Optional[BinaryIO] = None
    ):
        
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.upload_id = upload_id
        self.file_size = file_size
        self.file_seq = file_seq
        self.file_checksum = file_checksum
        self.file_content = file_content

class ApiV1FilesRecordsUploadPartPostResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1FilesRecordsUploadPreparePostRequest(object):
    """分块上传录制文件 - 预上传

    分块上传录制文件 - 预上传
    
    :param body:
    :type body: V1FilesRecordsUploadPreparePostRequest
    """  # noqa: E501


    def __init__(
        self,
        body: Optional[V1FilesRecordsUploadPreparePostRequest] = None
    ):
        self.body = body

class ApiV1FilesRecordsUploadPreparePostResponse(ApiResponse):
    data: Optional[V1FilesRecordsUploadPreparePost200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1FilesRecordsUploadPreparePost200Response] = None):
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

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        meeting_record_id: Optional[str] = None,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.meeting_record_id = meeting_record_id
        self.start_time = start_time
        self.end_time = end_time
        self.body = body

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


class ApiV1RecordsAccessMeetingRecordIdDeleteRequest(object):
    """移除录制访问成员

    仅会议创建者、企业超级管理员或有企业录制管理权限的用户可调用。 权限点：管理会议录制
    
    :param meeting_record_id: 会议录制ID (required)
    :type meeting_record_id: str

    :param body:
    :type body: V1RecordsAccessMeetingRecordIdDeleteRequest
    """  # noqa: E501


    def __init__(
        self,
        meeting_record_id: str,
        body: Optional[V1RecordsAccessMeetingRecordIdDeleteRequest] = None
    ):
        self.meeting_record_id = meeting_record_id
        self.body = body

class ApiV1RecordsAccessMeetingRecordIdDeleteResponse(ApiResponse):
    data: Optional[object] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[object] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1RecordsAccessMeetingRecordIdPostRequest(object):
    """添加录制访问成员

    仅会议创建者、企业超级管理员或有企业录制管理权限的用户可调用，可以添加参会成员或企业内成员为访问成员。 权限点：管理会议录制
    
    :param meeting_record_id: 会议录制ID (required)
    :type meeting_record_id: str

    :param body:
    :type body: V1RecordsAccessMeetingRecordIdPostRequest
    """  # noqa: E501


    def __init__(
        self,
        meeting_record_id: str,
        body: Optional[V1RecordsAccessMeetingRecordIdPostRequest] = None
    ):
        self.meeting_record_id = meeting_record_id
        self.body = body

class ApiV1RecordsAccessMeetingRecordIdPostResponse(ApiResponse):
    data: Optional[V1RecordsAccessMeetingRecordIdPost200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1RecordsAccessMeetingRecordIdPost200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1RecordsApprovalsMeetingRecordIdPutRequest(object):
    """审批云录制权限

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
    """删除会议录制

    删除会议的所有录制文件，该接口会删除会议录制 ID 里对应的所有云录制文件。企业 secret 鉴权用户可删除该用户所属企业下的会议录制，OAuth2.0 鉴权用户只能删除该企业下 OAuth2.0 应用的会议录制。 <span class=\"colour\" style=\"color:rgb(51, 51, 51)\">当您想实时监测会议录制删除状况时，您可以通过订阅 </span>[删除云录制](https://cloud.tencent.com/document/product/1095/53232)<span class=\"colour\" style=\"color:rgb(51, 51, 51)\"> 的事件，接收事件通知。</span>
    
    :param meeting_record_id: 会议录制 ID。 (required)
    :type meeting_record_id: str

    :param meeting_id: 会议 ID。
    :type meeting_id: str

    :param operator_id: 操作者ID，根据operator_id_type的值，使用不同的类型
    :type operator_id: str

    :param operator_id_type: 操作者ID的类型，必须与operator_id同时出现
    :type operator_id_type: str

    :param userid: 用户 ID（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId）。
    :type userid: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        meeting_record_id: Optional[str] = None,
        meeting_id: Optional[str] = None,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        userid: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.meeting_record_id = meeting_record_id
        self.meeting_id = meeting_id
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.userid = userid
        self.body = body

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

    :param page_size: 分页大小，默认值为20，最大为50。
    :type page_size: str

    :param page: 页码，从1开始，默认值为1。
    :type page: str

    :param start_time: 查询起始时间戳，UNIX 时间戳（单位秒）。说明：时间区间不允许超过31天。
    :type start_time: str

    :param end_time: 查询结束时间戳，UNIX 时间戳（单位秒）。说明：时间区间不允许超过31天。
    :type end_time: str
    """  # noqa: E501


    def __init__(
        self,
        meeting_record_id: Optional[str] = None,
        event_type: Optional[str] = None,
        page_size: Optional[str] = None,
        page: Optional[str] = None,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None
    ):
        self.meeting_record_id = meeting_record_id
        self.event_type = event_type
        self.page_size = page_size
        self.page = page
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

    :param operator_id: 操作者ID，必须与operator_id_type同时出现。
    :type operator_id: str

    :param operator_id_type: 操作者ID的类型，必须与operator_id同时出现。
    :type operator_id_type: str

    :param userid: 用户 ID（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId），当会议 ID 和会议 code 均为空时，表示查询用户所有会议的录制列表。
    :type userid: str

    :param meeting_id: 会议的唯一 ID，不为空时优先根据会议 ID 查询。
    :type meeting_id: str

    :param meeting_code: 会议 code，当 meeting_id 为空且 meeting_code 不为空时根据会议 code 查询。
    :type meeting_code: str

    :param page_size: 分页大小，默认值为10，最大为20。
    :type page_size: str

    :param page: 页码，从1开始，默认值为1。
    :type page: str

    :param media_set_type:
    :type media_set_type: str

    :param query_record_type: 录制文件类型： 0：全部、1：云录制、2：上传录制，默认为 1
    :type query_record_type: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        userid: Optional[str] = None,
        meeting_id: Optional[str] = None,
        meeting_code: Optional[str] = None,
        page_size: Optional[str] = None,
        page: Optional[str] = None,
        media_set_type: Optional[str] = None,
        query_record_type: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.userid = userid
        self.meeting_id = meeting_id
        self.meeting_code = meeting_code
        self.page_size = page_size
        self.page = page
        self.media_set_type = media_set_type
        self.query_record_type = query_record_type
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

    :param meeting_id: 会议 ID。
    :type meeting_id: str

    :param operator_id: 操作者ID，根据operator_id_type的值，使用不同的类型，必须与operator_id_type同时出现
    :type operator_id: str

    :param operator_id_type: 操作者ID的类型，必须与operator_id同时出现
    :type operator_id_type: str

    :param userid: 用户 ID（企业内部请使用企业唯一用户标识；OAuth2.0 鉴权用户请使用 openId）。
    :type userid: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        record_file_id: str,
        meeting_id: Optional[str] = None,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        userid: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.record_file_id = record_file_id
        self.meeting_id = meeting_id
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.userid = userid
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


class ApiV1RecordsSettingsMeetingRecordIdGetRequest(object):
    """查询会议录制共享设置

    根据会议录制 ID 查询共享等配置，支持修改共享权限、共享密码、共享有效期等信息，
    
    :param meeting_record_id: 会议录制ID (required)
    :type meeting_record_id: str

    :param operator_id: 操作人ID,录制管理者、企业超级管理员或有企业录制管理权限的用 (required)
    :type operator_id: str

    :param operator_id_type: 操作人ID 类型 1-userid，2-openid,3-rooms_id (required)
    :type operator_id_type: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        meeting_record_id: str,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.meeting_record_id = meeting_record_id
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.body = body

class ApiV1RecordsSettingsMeetingRecordIdGetResponse(ApiResponse):
    data: Optional[V1RecordsSettingsMeetingRecordIdGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1RecordsSettingsMeetingRecordIdGet200Response] = None):
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
    """查询录制转写详情

    获取云录制会议纪要的详情，包含时间戳、文本等内容。支持 OAuth2.0 鉴权调用，仅支持授权用户为商业版、企业版、教育版。  所需权限点为：查看会议录制（VIEW\\_VIDEO） 或 管理会议录制（MANAGE\\_VIDEO）。
    
    :param record_file_id: 录制id (required)
    :type record_file_id: str

    :param operator_id: 操作者ID。operator_id 必须与 operator_id_type 配合使用。根据operator_id_type的值，operator_id 代表不同类型。 (required)
    :type operator_id: str

    :param operator_id_type: 操作者ID的类型：  1. 企业用户userid 2：open_id 3. rooms设备rooms_id (required)
    :type operator_id_type: str

    :param meeting_id: 会议id
    :type meeting_id: str

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
        record_file_id: Optional[str] = None,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        meeting_id: Optional[str] = None,
        pid: Optional[str] = None,
        limit: Optional[str] = None,
        transcripts_type: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.record_file_id = record_file_id
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.meeting_id = meeting_id
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
    """查询录制转写段落信息

    获取云录制会议纪要的段落信息（段落总数、段落 ID）。支持 OAuth2\\.0 鉴权调用，仅支持授权用户为商业版、企业版、教育版。  所需权限点为：查看会议录制（VIEW\\_VIDEO） 或 管理会议录制（MANAGE\\_VIDEO）。
    
    :param record_file_id: 录制文件 ID。 (required)
    :type record_file_id: str

    :param operator_id_type: 操作者ID的类型：  1. 企业用户userid 2：open_id 3. rooms设备rooms_id (required)
    :type operator_id_type: str

    :param operator_id: 操作者ID。operator_id 必须与 operator_id_type 配合使用。根据operator_id_type的值，operator_id 代表不同类型。 (required)
    :type operator_id: str

    :param meeting_id: 会议 ID。
    :type meeting_id: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        record_file_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        operator_id: Optional[str] = None,
        meeting_id: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.record_file_id = record_file_id
        self.operator_id_type = operator_id_type
        self.operator_id = operator_id
        self.meeting_id = meeting_id
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
    """查询录制转写搜索结果

    根据指定内容搜索会议纪要。支持 OAuth2\\.0 鉴权调用，仅支持授权用户为商业版、企业版、教育版。  所需权限点为：查看会议录制（VIEW\\_VIDEO） 或 管理会议录制（MANAGE\\_VIDEO）。
    
    :param record_file_id: 录制文件id (required)
    :type record_file_id: str

    :param operator_id: 用户名 (required)
    :type operator_id: str

    :param operator_id_type: id类型: 1: 常规用户 2：open_id 3:rooms (required)
    :type operator_id_type: str

    :param text: 搜索的文本, 如果是中文, 需要urlencode一下 (required)
    :type text: str

    :param meeting_id: 会议ID
    :type meeting_id: str

    :param transcripts_type: 转写类型，默认是0。 0：原文版 1：智能优化版
    :type transcripts_type: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        record_file_id: Optional[str] = None,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        text: Optional[str] = None,
        meeting_id: Optional[str] = None,
        transcripts_type: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.record_file_id = record_file_id
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.text = text
        self.meeting_id = meeting_id
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
    """设置专网会议转存

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
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'meeting_record_id' is set
            if request.meeting_record_id is None:
                raise Exception("meeting_record_id is required and must be specified")
            # path 参数
            # query 参数
            if request.meeting_record_id is not None:
                api_req.query_params.append(('meeting_record_id', request.meeting_record_id))
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            if request.userid is not None:
                api_req.query_params.append(('userid', request.userid))
            if request.page_size is not None:
                api_req.query_params.append(('page_size', request.page_size))
            if request.page is not None:
                api_req.query_params.append(('page', request.page))
            if request.address_type is not None:
                api_req.query_params.append(('address_type', request.address_type))
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
        """v1_addresses_record_file_id_get 查询单个录制详情（文件、转写、纪要）[/v1/addresses/{record_file_id} - GET]

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
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            if request.userid is not None:
                api_req.query_params.append(('userid', request.userid))
            if request.address_type is not None:
                api_req.query_params.append(('address_type', request.address_type))
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

    def v1_files_records_upload_all_post(
        self,
        request: ApiV1FilesRecordsUploadAllPostRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1FilesRecordsUploadAllPostResponse:
        """v1_files_records_upload_all_post 上传录制文件[/v1/files/records/upload-all - POST]

        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 读取文件内容
            file_content_file_content = request.file_content.read()
            # 关闭文件
            request.file_content.close()
            # 设置请求头
            multipart_data = MultipartEncoder(
                fields={ 
                    # 封装表单字段
                    "operator_id": str(request.operator_id),
                    # 封装表单字段
                    "operator_id_type": str(request.operator_id_type),
                    # 封装表单字段
                    "file_name": str(request.file_name),
                    # 封装表单字段
                    "file_type": str(request.file_type),
                    # 封装表单字段
                    "file_size": str(request.file_size),
                    # 封装表单字段
                    "file_checksum": str(request.file_checksum),
                    # 添加文件到FormData
                    "file_content": (request.file_content.name, file_content_file_content, "application/octet-stream"),
                    # 封装表单字段
                    "speak_number": str(request.speak_number),
                    # 封装表单字段
                    "ai_record": str(request.ai_record),
                }
            )
            # 设置请求头
            if header is not None:
                header["Content-Type"] = multipart_data.content_type
            else:
                header = {
                    "Content-Type": multipart_data.content_type,
                }
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/files/records/upload-all",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=multipart_data,
                                 serializer=serializer)

            # verify the required parameter 'operator_id' is set
            if request.operator_id is None:
                raise Exception("operator_id is required and must be specified")
            # verify the required parameter 'operator_id_type' is set
            if request.operator_id_type is None:
                raise Exception("operator_id_type is required and must be specified")
            # verify the required parameter 'file_name' is set
            if request.file_name is None:
                raise Exception("file_name is required and must be specified")
            # verify the required parameter 'file_type' is set
            if request.file_type is None:
                raise Exception("file_type is required and must be specified")
            # verify the required parameter 'file_size' is set
            if request.file_size is None:
                raise Exception("file_size is required and must be specified")
            # verify the required parameter 'file_checksum' is set
            if request.file_checksum is None:
                raise Exception("file_checksum is required and must be specified")
            # verify the required parameter 'file_content' is set
            if request.file_content is None:
                raise Exception("file_content is required and must be specified")
            # verify the required parameter 'speak_number' is set
            if request.speak_number is None:
                raise Exception("speak_number is required and must be specified")
            # path 参数
            # query 参数
            # 发送请求
            api_resp = self.__config.clt.post(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1FilesRecordsUploadAllPostResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1FilesRecordsUploadAllPost200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_files_records_upload_finish_post(
        self,
        request: ApiV1FilesRecordsUploadFinishPostRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1FilesRecordsUploadFinishPostResponse:
        """v1_files_records_upload_finish_post 分块上传录制文件 - 上传完成[/v1/files/records/upload-finish - POST]

        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/files/records/upload-finish",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # path 参数
            # query 参数
            # 发送请求
            api_resp = self.__config.clt.post(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1FilesRecordsUploadFinishPostResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1FilesRecordsUploadAllPost200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_files_records_upload_part_post(
        self,
        request: ApiV1FilesRecordsUploadPartPostRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1FilesRecordsUploadPartPostResponse:
        """v1_files_records_upload_part_post 分块上传录制文件 - 上传[/v1/files/records/upload-part - POST]

        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 读取文件内容
            file_content_file_content = request.file_content.read()
            # 关闭文件
            request.file_content.close()
            # 设置请求头
            multipart_data = MultipartEncoder(
                fields={ 
                    # 封装表单字段
                    "operator_id": str(request.operator_id),
                    # 封装表单字段
                    "operator_id_type": str(request.operator_id_type),
                    # 封装表单字段
                    "upload_id": str(request.upload_id),
                    # 封装表单字段
                    "file_size": str(request.file_size),
                    # 封装表单字段
                    "file_seq": str(request.file_seq),
                    # 封装表单字段
                    "file_checksum": str(request.file_checksum),
                    # 添加文件到FormData
                    "file_content": (request.file_content.name, file_content_file_content, "application/octet-stream"),
                }
            )
            # 设置请求头
            if header is not None:
                header["Content-Type"] = multipart_data.content_type
            else:
                header = {
                    "Content-Type": multipart_data.content_type,
                }
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/files/records/upload-part",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=multipart_data,
                                 serializer=serializer)

            # verify the required parameter 'operator_id' is set
            if request.operator_id is None:
                raise Exception("operator_id is required and must be specified")
            # verify the required parameter 'operator_id_type' is set
            if request.operator_id_type is None:
                raise Exception("operator_id_type is required and must be specified")
            # verify the required parameter 'upload_id' is set
            if request.upload_id is None:
                raise Exception("upload_id is required and must be specified")
            # verify the required parameter 'file_size' is set
            if request.file_size is None:
                raise Exception("file_size is required and must be specified")
            # verify the required parameter 'file_seq' is set
            if request.file_seq is None:
                raise Exception("file_seq is required and must be specified")
            # verify the required parameter 'file_checksum' is set
            if request.file_checksum is None:
                raise Exception("file_checksum is required and must be specified")
            # verify the required parameter 'file_content' is set
            if request.file_content is None:
                raise Exception("file_content is required and must be specified")
            # path 参数
            # query 参数
            # 发送请求
            api_resp = self.__config.clt.post(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1FilesRecordsUploadPartPostResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_files_records_upload_prepare_post(
        self,
        request: ApiV1FilesRecordsUploadPreparePostRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1FilesRecordsUploadPreparePostResponse:
        """v1_files_records_upload_prepare_post 分块上传录制文件 - 预上传[/v1/files/records/upload-prepare - POST]

            分块上传录制文件 - 预上传
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/files/records/upload-prepare",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # path 参数
            # query 参数
            # 发送请求
            api_resp = self.__config.clt.post(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1FilesRecordsUploadPreparePostResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1FilesRecordsUploadPreparePost200Response)
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
                                 body=request.body,
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

    def v1_records_access_meeting_record_id_delete(
        self,
        request: ApiV1RecordsAccessMeetingRecordIdDeleteRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1RecordsAccessMeetingRecordIdDeleteResponse:
        """v1_records_access_meeting_record_id_delete 移除录制访问成员[/v1/records/access/{meeting_record_id} - DELETE]

            仅会议创建者、企业超级管理员或有企业录制管理权限的用户可调用。 权限点：管理会议录制
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/records/access/{meeting_record_id}",
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
            api_resp = self.__config.clt.delete(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1RecordsAccessMeetingRecordIdDeleteResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=object)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_records_access_meeting_record_id_post(
        self,
        request: ApiV1RecordsAccessMeetingRecordIdPostRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1RecordsAccessMeetingRecordIdPostResponse:
        """v1_records_access_meeting_record_id_post 添加录制访问成员[/v1/records/access/{meeting_record_id} - POST]

            仅会议创建者、企业超级管理员或有企业录制管理权限的用户可调用，可以添加参会成员或企业内成员为访问成员。 权限点：管理会议录制
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/records/access/{meeting_record_id}",
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
            api_resp = self.__config.clt.post(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1RecordsAccessMeetingRecordIdPostResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1RecordsAccessMeetingRecordIdPost200Response)
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
        """v1_records_approvals_meeting_record_id_put 审批云录制权限[/v1/records/approvals/{meeting_record_id} - PUT]

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
        """v1_records_delete 删除会议录制[/v1/records - DELETE]

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
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'meeting_record_id' is set
            if request.meeting_record_id is None:
                raise Exception("meeting_record_id is required and must be specified")
            # path 参数
            # query 参数
            if request.meeting_id is not None:
                api_req.query_params.append(('meeting_id', request.meeting_id))
            if request.meeting_record_id is not None:
                api_req.query_params.append(('meeting_record_id', request.meeting_record_id))
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            if request.userid is not None:
                api_req.query_params.append(('userid', request.userid))
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
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            if request.userid is not None:
                api_req.query_params.append(('userid', request.userid))
            if request.meeting_id is not None:
                api_req.query_params.append(('meeting_id', request.meeting_id))
            if request.meeting_code is not None:
                api_req.query_params.append(('meeting_code', request.meeting_code))
            if request.start_time is not None:
                api_req.query_params.append(('start_time', request.start_time))
            if request.end_time is not None:
                api_req.query_params.append(('end_time', request.end_time))
            if request.page_size is not None:
                api_req.query_params.append(('page_size', request.page_size))
            if request.page is not None:
                api_req.query_params.append(('page', request.page))
            if request.media_set_type is not None:
                api_req.query_params.append(('media_set_type', request.media_set_type))
            if request.query_record_type is not None:
                api_req.query_params.append(('query_record_type', request.query_record_type))
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
            # path 参数
            if request.record_file_id is not None:
                api_req.path_params['record_file_id'] = request.record_file_id
            # query 参数
            if request.meeting_id is not None:
                api_req.query_params.append(('meeting_id', request.meeting_id))
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            if request.userid is not None:
                api_req.query_params.append(('userid', request.userid))
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

    def v1_records_settings_meeting_record_id_get(
        self,
        request: ApiV1RecordsSettingsMeetingRecordIdGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1RecordsSettingsMeetingRecordIdGetResponse:
        """v1_records_settings_meeting_record_id_get 查询会议录制共享设置[/v1/records/settings/{meeting_record_id} - GET]

            根据会议录制 ID 查询共享等配置，支持修改共享权限、共享密码、共享有效期等信息，
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
            # verify the required parameter 'operator_id' is set
            if request.operator_id is None:
                raise Exception("operator_id is required and must be specified")
            # verify the required parameter 'operator_id_type' is set
            if request.operator_id_type is None:
                raise Exception("operator_id_type is required and must be specified")
            # path 参数
            if request.meeting_record_id is not None:
                api_req.path_params['meeting_record_id'] = request.meeting_record_id
            # query 参数
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1RecordsSettingsMeetingRecordIdGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1RecordsSettingsMeetingRecordIdGet200Response)
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
        """v1_records_transcripts_details_get 查询录制转写详情[/v1/records/transcripts/details - GET]

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
        """v1_records_transcripts_paragraphs_get 查询录制转写段落信息[/v1/records/transcripts/paragraphs - GET]

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
        """v1_records_transcripts_search_get 查询录制转写搜索结果[/v1/records/transcripts/search - GET]

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

            # verify the required parameter 'record_file_id' is set
            if request.record_file_id is None:
                raise Exception("record_file_id is required and must be specified")
            # verify the required parameter 'operator_id' is set
            if request.operator_id is None:
                raise Exception("operator_id is required and must be specified")
            # verify the required parameter 'operator_id_type' is set
            if request.operator_id_type is None:
                raise Exception("operator_id_type is required and must be specified")
            # verify the required parameter 'text' is set
            if request.text is None:
                raise Exception("text is required and must be specified")
            # path 参数
            # query 参数
            if request.meeting_id is not None:
                api_req.query_params.append(('meeting_id', request.meeting_id))
            if request.record_file_id is not None:
                api_req.query_params.append(('record_file_id', request.record_file_id))
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            if request.text is not None:
                api_req.query_params.append(('text', request.text))
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
        """v1_records_transfer_recording_put 设置专网会议转存[/v1/records/transfer-recording - PUT]

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

