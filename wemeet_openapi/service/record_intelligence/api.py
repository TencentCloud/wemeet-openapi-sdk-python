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
from wemeet_openapi.service.record_intelligence.model import *

from requests_toolbelt import MultipartEncoder


class ApiV1SmartChaptersGetRequest(object):
    """智能章节

    查询单个云录制的智能章节，支持OAuth2.0鉴权调用，仅支持授权用户为商业版、企业版、教育版。 当该录制文件未开启相关智能化功能或内容处于生成中状态时，结果返回错误码
    
    :param operator_id: 操作者ID。operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 (required)
    :type operator_id: str

    :param operator_id_type: 操作者ID类型： 1：userid 2:openid (required)
    :type operator_id_type: str

    :param record_file_id: 录制文件ID，列表接口返回的 record_file_id。 (required)
    :type record_file_id: str

    :param lang: 翻译类型，默认原文展示 \"default\" ：原文（不翻译） \"zh\" ：简体中文 \"en\" ：英文 \"ja\"： 日语
    :type lang: str

    :param pwd:
    :type pwd: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        record_file_id: Optional[str] = None,
        lang: Optional[str] = None,
        pwd: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.record_file_id = record_file_id
        self.lang = lang
        self.pwd = pwd
        self.body = body

class ApiV1SmartChaptersGetResponse(ApiResponse):
    data: Optional[V1SmartChaptersGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1SmartChaptersGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1SmartFullsummaryGetRequest(object):
    """智能总结

    查询单个云录制的智能总结。支持OAuth2.0鉴权调用，仅支持授权用户为商业版、企业版、教育版。 当该录制文件未开启相关智能化功能或内容处于生成中状态时，结果返回错误码
    
    :param operator_id: 操作者ID。operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 (required)
    :type operator_id: str

    :param operator_id_type: 操作者ID类型： 1：userid 2:openid (required)
    :type operator_id_type: str

    :param record_file_id: 录制文件ID，列表接口返回的 record_file_id。 (required)
    :type record_file_id: str

    :param lang: 翻译类型，默认原文展示 \"default\" 原文（不翻译） \"zh\" 简体中文 \"en\" 英文 \"ja\" 日语
    :type lang: str

    :param pwd: 录制文件的访问密码，非必填
    :type pwd: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        record_file_id: Optional[str] = None,
        lang: Optional[str] = None,
        pwd: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.record_file_id = record_file_id
        self.lang = lang
        self.pwd = pwd
        self.body = body

class ApiV1SmartFullsummaryGetResponse(ApiResponse):
    data: Optional[V1SmartFullsummaryGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1SmartFullsummaryGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1SmartSpeakersGetRequest(object):
    """智能发言人

    查询单个云录制的发言人列表。支持OAuth2.0鉴权调用，仅支持授权用户为商业版、企业版、教育版。 当该录制文件未开启相关智能化功能或内容处于生成中状态时，结果返回错误码
    
    :param operator_id: 操作者ID。operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 (required)
    :type operator_id: str

    :param operator_id_type: 操作者ID类型： 1：userid 2:openid (required)
    :type operator_id_type: str

    :param record_file_id: 录制文件ID，列表接口返回的 record_file_id。 (required)
    :type record_file_id: str

    :param page: 页码，从1开始 (required)
    :type page: str

    :param page_size: 返回数量，最大50 (required)
    :type page_size: str

    :param pwd: 录制文件的访问密码，非必填
    :type pwd: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        record_file_id: Optional[str] = None,
        page: Optional[str] = None,
        page_size: Optional[str] = None,
        pwd: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.record_file_id = record_file_id
        self.page = page
        self.page_size = page_size
        self.pwd = pwd
        self.body = body

class ApiV1SmartSpeakersGetResponse(ApiResponse):
    data: Optional[V1SmartSpeakersGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1SmartSpeakersGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class ApiV1SmartTopicsGetRequest(object):
    """智能话题

    查询单个云录制的智能话题。支持OAuth2.0鉴权调用，仅支持授权用户为商业版、企业版、教育版。 当该录制文件未开启相关智能化功能或内容处于生成中状态时，结果返回错误码
    
    :param operator_id: 操作者ID。operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。 (required)
    :type operator_id: str

    :param operator_id_type: 操作者ID类型： 1：userid 2:openid (required)
    :type operator_id_type: str

    :param record_file_id: 录制文件ID，列表接口返回的 record_file_id。 (required)
    :type record_file_id: str

    :param lang: 翻译类型，默认原文展示 \"default\" 原文（不翻译） \"zh\" 简体中文 \"en\" 英文 \"ja\" 日语
    :type lang: str

    :param pwd: 录制文件的访问密码，非必填
    :type pwd: str

    :param body:
    :type body: object
    """  # noqa: E501


    def __init__(
        self,
        operator_id: Optional[str] = None,
        operator_id_type: Optional[str] = None,
        record_file_id: Optional[str] = None,
        lang: Optional[str] = None,
        pwd: Optional[str] = None,
        body: Optional[object] = None
    ):
        self.operator_id = operator_id
        self.operator_id_type = operator_id_type
        self.record_file_id = record_file_id
        self.lang = lang
        self.pwd = pwd
        self.body = body

class ApiV1SmartTopicsGetResponse(ApiResponse):
    data: Optional[V1SmartTopicsGet200Response] = None

    def __init__(self, api_resp: ApiResponse, data: Optional[V1SmartTopicsGet200Response] = None):
        super().__init__(
            status_code=api_resp.status_code,
            raw_body=api_resp.raw_body,
            header=api_resp.header,
            serializer=api_resp.serializer()
        )
        self.data = data


class RecordIntelligenceApi:
    def __init__(self, config: Config):
        self.__config = config

    def v1_smart_chapters_get(
        self,
        request: ApiV1SmartChaptersGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1SmartChaptersGetResponse:
        """v1_smart_chapters_get 智能章节[/v1/smart/chapters - GET]

            查询单个云录制的智能章节，支持OAuth2.0鉴权调用，仅支持授权用户为商业版、企业版、教育版。 当该录制文件未开启相关智能化功能或内容处于生成中状态时，结果返回错误码
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/smart/chapters",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'operator_id' is set
            if request.operator_id is None:
                raise Exception("operator_id is required and must be specified")
            # verify the required parameter 'operator_id_type' is set
            if request.operator_id_type is None:
                raise Exception("operator_id_type is required and must be specified")
            # verify the required parameter 'record_file_id' is set
            if request.record_file_id is None:
                raise Exception("record_file_id is required and must be specified")
            # path 参数
            # query 参数
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            if request.record_file_id is not None:
                api_req.query_params.append(('record_file_id', request.record_file_id))
            if request.lang is not None:
                api_req.query_params.append(('lang', request.lang))
            if request.pwd is not None:
                api_req.query_params.append(('pwd', request.pwd))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1SmartChaptersGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1SmartChaptersGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_smart_fullsummary_get(
        self,
        request: ApiV1SmartFullsummaryGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1SmartFullsummaryGetResponse:
        """v1_smart_fullsummary_get 智能总结[/v1/smart/fullsummary - GET]

            查询单个云录制的智能总结。支持OAuth2.0鉴权调用，仅支持授权用户为商业版、企业版、教育版。 当该录制文件未开启相关智能化功能或内容处于生成中状态时，结果返回错误码
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/smart/fullsummary",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'operator_id' is set
            if request.operator_id is None:
                raise Exception("operator_id is required and must be specified")
            # verify the required parameter 'operator_id_type' is set
            if request.operator_id_type is None:
                raise Exception("operator_id_type is required and must be specified")
            # verify the required parameter 'record_file_id' is set
            if request.record_file_id is None:
                raise Exception("record_file_id is required and must be specified")
            # path 参数
            # query 参数
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            if request.record_file_id is not None:
                api_req.query_params.append(('record_file_id', request.record_file_id))
            if request.lang is not None:
                api_req.query_params.append(('lang', request.lang))
            if request.pwd is not None:
                api_req.query_params.append(('pwd', request.pwd))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1SmartFullsummaryGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1SmartFullsummaryGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_smart_speakers_get(
        self,
        request: ApiV1SmartSpeakersGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1SmartSpeakersGetResponse:
        """v1_smart_speakers_get 智能发言人[/v1/smart/speakers - GET]

            查询单个云录制的发言人列表。支持OAuth2.0鉴权调用，仅支持授权用户为商业版、企业版、教育版。 当该录制文件未开启相关智能化功能或内容处于生成中状态时，结果返回错误码
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/smart/speakers",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'operator_id' is set
            if request.operator_id is None:
                raise Exception("operator_id is required and must be specified")
            # verify the required parameter 'operator_id_type' is set
            if request.operator_id_type is None:
                raise Exception("operator_id_type is required and must be specified")
            # verify the required parameter 'record_file_id' is set
            if request.record_file_id is None:
                raise Exception("record_file_id is required and must be specified")
            # verify the required parameter 'page' is set
            if request.page is None:
                raise Exception("page is required and must be specified")
            # verify the required parameter 'page_size' is set
            if request.page_size is None:
                raise Exception("page_size is required and must be specified")
            # path 参数
            # query 参数
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            if request.record_file_id is not None:
                api_req.query_params.append(('record_file_id', request.record_file_id))
            if request.pwd is not None:
                api_req.query_params.append(('pwd', request.pwd))
            if request.page is not None:
                api_req.query_params.append(('page', request.page))
            if request.page_size is not None:
                api_req.query_params.append(('page_size', request.page_size))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1SmartSpeakersGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1SmartSpeakersGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

    def v1_smart_topics_get(
        self,
        request: ApiV1SmartTopicsGetRequest,
        serializer: Optional[Serializer] = None,
        authenticator_options: Optional[List[Callable[[Config], Authenticator]]] = None,
        header: Optional[Dict[str, str]] = None
    ) -> ApiV1SmartTopicsGetResponse:
        """v1_smart_topics_get 智能话题[/v1/smart/topics - GET]

            查询单个云录制的智能话题。支持OAuth2.0鉴权调用，仅支持授权用户为商业版、企业版、教育版。 当该录制文件未开启相关智能化功能或内容处于生成中状态时，结果返回错误码
        """
        try:
            # 生成鉴权器
            authenticators: List[Authenticator] = []
            for option in authenticator_options:
                authenticators.append(option(self.__config))

            # 增加 SDK Version 标识
            authenticators.append(DEFAULT_AUTHENTICATOR)
            
            # 构造请求
            api_req = ApiRequest(api_uri="/v1/smart/topics",
                                 authenticators=authenticators,
                                 header=header, 
                                 body=request.body,
                                 serializer=serializer)

            # verify the required parameter 'operator_id' is set
            if request.operator_id is None:
                raise Exception("operator_id is required and must be specified")
            # verify the required parameter 'operator_id_type' is set
            if request.operator_id_type is None:
                raise Exception("operator_id_type is required and must be specified")
            # verify the required parameter 'record_file_id' is set
            if request.record_file_id is None:
                raise Exception("record_file_id is required and must be specified")
            # path 参数
            # query 参数
            if request.operator_id is not None:
                api_req.query_params.append(('operator_id', request.operator_id))
            if request.operator_id_type is not None:
                api_req.query_params.append(('operator_id_type', request.operator_id_type))
            if request.record_file_id is not None:
                api_req.query_params.append(('record_file_id', request.record_file_id))
            if request.lang is not None:
                api_req.query_params.append(('lang', request.lang))
            if request.pwd is not None:
                api_req.query_params.append(('pwd', request.pwd))
            # 发送请求
            api_resp = self.__config.clt.get(api_req)

            if api_resp.status_code >= 300:
                raise ServiceException(api_resp=api_resp)
            try:
                response = ApiV1SmartTopicsGetResponse(api_resp=api_resp)
                response.data = api_resp.translate(dst_t=V1SmartTopicsGet200Response)
            except Exception as e:
                raise ClientException(Exception(f"http status code: {api_resp.status_code}, "
                                                f"response: {api_resp.raw_body}, err: {e.__str__()}"))
            return response
        except (ClientException, ServiceException):
            raise
        except Exception as e:
            raise ClientException(e)

