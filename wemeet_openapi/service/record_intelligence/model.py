# coding: utf-8

"""
    腾讯会议OpenAPI

    SAAS版RESTFUL风格API

    API version: v1.0.4

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

from typing import *


class V1SmartChaptersGet200Response(object):
    """V1SmartChaptersGet200Response

    :param chapter_list: ChapterList对象数组 
    :type chapter_list: Optional[List[V1SmartChaptersGet200ResponseChapterListInner]]
    """  # noqa: E501

    chapter_list: Optional[List[V1SmartChaptersGet200ResponseChapterListInner]] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        chapter_list: Optional[List[V1SmartChaptersGet200ResponseChapterListInner] | List[Dict[str, Any]]] = None,
        **kwargs
    ):
        
        if chapter_list and isinstance(chapter_list, (list, List)):
            self.chapter_list = [V1SmartChaptersGet200ResponseChapterListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in chapter_list]
        


class V1SmartChaptersGet200ResponseChapterListInner(object):
    """V1SmartChaptersGet200ResponseChapterListInner

    :param chapter_id: 章节唯一ID 
    :type chapter_id: Optional[str]

    :param chapter_name: 章节主题，返回base64编码后的结果 
    :type chapter_name: Optional[str]

    :param pic_url: 章节封面图片url 
    :type pic_url: Optional[str]

    :param start_time: 开始时间戳（单位毫秒） 
    :type start_time: Optional[str]
    """  # noqa: E501

    chapter_id: Optional[str] = None
    chapter_name: Optional[str] = None
    pic_url: Optional[str] = None
    start_time: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        chapter_id: Optional[str] = None,
        chapter_name: Optional[str] = None,
        pic_url: Optional[str] = None,
        start_time: Optional[str] = None,
        **kwargs
    ):
        self.chapter_id = chapter_id
        self.chapter_name = chapter_name
        self.pic_url = pic_url
        self.start_time = start_time


class V1SmartFullsummaryGet200Response(object):
    """V1SmartFullsummaryGet200Response

    :param ai_summary: 智能总结内容 
    :type ai_summary: Optional[str]
    """  # noqa: E501

    ai_summary: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        ai_summary: Optional[str] = None,
        **kwargs
    ):
        self.ai_summary = ai_summary


class V1SmartSpeakersGet200Response(object):
    """V1SmartSpeakersGet200Response

    :param speaker_list: 本录制文件的发言人列表，以对象数组形式返回 
    :type speaker_list: Optional[List[V1SmartSpeakersGet200ResponseSpeakerListInner]]

    :param total_count: 发言人总数 
    :type total_count: Optional[int]
    """  # noqa: E501

    speaker_list: Optional[List[V1SmartSpeakersGet200ResponseSpeakerListInner]] = None
    total_count: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        speaker_list: Optional[List[V1SmartSpeakersGet200ResponseSpeakerListInner] | List[Dict[str, Any]]] = None,
        total_count: Optional[int] = None,
        **kwargs
    ):
        
        if speaker_list and isinstance(speaker_list, (list, List)):
            self.speaker_list = [V1SmartSpeakersGet200ResponseSpeakerListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in speaker_list]
        
        self.total_count = total_count


class V1SmartSpeakersGet200ResponseSpeakerListInner(object):
    """V1SmartSpeakersGet200ResponseSpeakerListInner

    :param ms_open_id: 会议中为每个参会成员授予的临时 ID，以会议为维度，表示同一场会议内用户的唯一标识，不同会议间 ms_open_id 隔离。 
    :type ms_open_id: Optional[str]

    :param speaker_id: 发言人ID。speaker_id 必须与 speaker_id_type 配合使用。根据 speaker_id_type 的值，speaker_id 代表不同类型。 
    :type speaker_id: Optional[str]

    :param speaker_id_type: 发言人ID类型： 1：userid 2：openid 6：temp_id（临时 ID，上传的文件无法映射到 userid，故仅在当前录制发言人中代表唯一标识） 
    :type speaker_id_type: Optional[int]

    :param speaker_name: 发言人名称，base64编码 
    :type speaker_name: Optional[str]

    :param speaker_time: 本录制文件某个具体发言人的发言时间段，以对象数组形式返回 
    :type speaker_time: Optional[List[V1SmartSpeakersGet200ResponseSpeakerListInnerSpeakerTimeInner]]

    :param total_time: 发言总时长 
    :type total_time: Optional[int]
    """  # noqa: E501

    ms_open_id: Optional[str] = None
    speaker_id: Optional[str] = None
    speaker_id_type: Optional[int] = None
    speaker_name: Optional[str] = None
    speaker_time: Optional[List[V1SmartSpeakersGet200ResponseSpeakerListInnerSpeakerTimeInner]] = None
    total_time: Optional[int] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        ms_open_id: Optional[str] = None,
        speaker_id: Optional[str] = None,
        speaker_id_type: Optional[int] = None,
        speaker_name: Optional[str] = None,
        speaker_time: Optional[List[V1SmartSpeakersGet200ResponseSpeakerListInnerSpeakerTimeInner] | List[Dict[str, Any]]] = None,
        total_time: Optional[int] = None,
        **kwargs
    ):
        self.ms_open_id = ms_open_id
        self.speaker_id = speaker_id
        self.speaker_id_type = speaker_id_type
        self.speaker_name = speaker_name
        
        if speaker_time and isinstance(speaker_time, (list, List)):
            self.speaker_time = [V1SmartSpeakersGet200ResponseSpeakerListInnerSpeakerTimeInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in speaker_time]
        
        self.total_time = total_time


class V1SmartSpeakersGet200ResponseSpeakerListInnerSpeakerTimeInner(object):
    """V1SmartSpeakersGet200ResponseSpeakerListInnerSpeakerTimeInner

    :param end_time: 结束时间戳（单位毫秒） 
    :type end_time: Optional[str]

    :param sid: 发言语句id 
    :type sid: Optional[str]

    :param start_time: 开始时间戳（单位毫秒） 
    :type start_time: Optional[str]
    """  # noqa: E501

    end_time: Optional[str] = None
    sid: Optional[str] = None
    start_time: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        end_time: Optional[str] = None,
        sid: Optional[str] = None,
        start_time: Optional[str] = None,
        **kwargs
    ):
        self.end_time = end_time
        self.sid = sid
        self.start_time = start_time


class V1SmartTopicsGet200Response(object):
    """V1SmartTopicsGet200Response

    :param ai_topic_list: 本录制文件的智能话题列表，以对象数组形式返回 
    :type ai_topic_list: Optional[List[V1SmartTopicsGet200ResponseAiTopicListInner]]
    """  # noqa: E501

    ai_topic_list: Optional[List[V1SmartTopicsGet200ResponseAiTopicListInner]] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        ai_topic_list: Optional[List[V1SmartTopicsGet200ResponseAiTopicListInner] | List[Dict[str, Any]]] = None,
        **kwargs
    ):
        
        if ai_topic_list and isinstance(ai_topic_list, (list, List)):
            self.ai_topic_list = [V1SmartTopicsGet200ResponseAiTopicListInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in ai_topic_list]
        


class V1SmartTopicsGet200ResponseAiTopicListInner(object):
    """V1SmartTopicsGet200ResponseAiTopicListInner

    :param topic_id: 话题唯一ID 
    :type topic_id: Optional[str]

    :param topic_name: 话题主题，base6编码 
    :type topic_name: Optional[str]

    :param topic_time: 本话题的发言段落及时间段，以对象数组形式返回 
    :type topic_time: Optional[List[V1SmartTopicsGet200ResponseAiTopicListInnerTopicTimeInner]]
    """  # noqa: E501

    topic_id: Optional[str] = None
    topic_name: Optional[str] = None
    topic_time: Optional[List[V1SmartTopicsGet200ResponseAiTopicListInnerTopicTimeInner]] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        topic_id: Optional[str] = None,
        topic_name: Optional[str] = None,
        topic_time: Optional[List[V1SmartTopicsGet200ResponseAiTopicListInnerTopicTimeInner] | List[Dict[str, Any]]] = None,
        **kwargs
    ):
        self.topic_id = topic_id
        self.topic_name = topic_name
        
        if topic_time and isinstance(topic_time, (list, List)):
            self.topic_time = [V1SmartTopicsGet200ResponseAiTopicListInnerTopicTimeInner(**_item) if isinstance(_item, (dict, Dict)) else _item for _item in topic_time]
        


class V1SmartTopicsGet200ResponseAiTopicListInnerTopicTimeInner(object):
    """V1SmartTopicsGet200ResponseAiTopicListInnerTopicTimeInner

    :param end_time: 结束时间戳（单位毫秒） 
    :type end_time: Optional[str]

    :param pid: 段落ID 
    :type pid: Optional[str]

    :param start_time: 开始时间戳（单位毫秒） 
    :type start_time: Optional[str]
    """  # noqa: E501

    end_time: Optional[str] = None
    pid: Optional[str] = None
    start_time: Optional[str] = None
    additional_properties: Dict[str, Any] = {}

    def __init__(
        self,
        end_time: Optional[str] = None,
        pid: Optional[str] = None,
        start_time: Optional[str] = None,
        **kwargs
    ):
        self.end_time = end_time
        self.pid = pid
        self.start_time = start_time

