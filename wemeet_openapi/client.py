from typing import Optional

from wemeet_openapi.core import xhttp, constants, config
from wemeet_openapi.service import *


class Client(object):
    def __init__(
        self,
        app_id: Optional[str] = None,
        sdk_id: Optional[str] = None,
        secret_id: Optional[str] = None,
        secret_key: Optional[str] = None,
        app_version: Optional[str] = None,
        clt: Optional[xhttp.AbstractClient] = None,
    ) -> None:
        self.__config: Optional[config.Config] = config.Config(
            clt=clt,
            version=app_version,
            app_id=app_id,
            sdk_id=sdk_id,
            secret_id=secret_id,
            secret_key=secret_key
        )

        if self.__config.clt is None:
            self.__config.clt = xhttp.Client(
                host=constants.OPEN_API_DOMAIN,
                protocol=constants.DEFAULT_PROTOCOL,
                serializer=constants.DEFAULT_SERIALIZER
            )

        # 注册服务
        self.meetings_api = MeetingsApi(self.__config)
        self.application_group_api = ApplicationGroupApi(self.__config)
        self.meeting_control_api = MeetingControlApi(self.__config)
        self.user_manager_api = UserManagerApi(self.__config)
        self.records_api = RecordsApi(self.__config)
        self.record_intelligence_api = RecordIntelligenceApi(self.__config)
        self.meeting_guest_api = MeetingGuestApi(self.__config)
        self.meeting_room_api = MeetingRoomApi(self.__config)
        self.layout_api = LayoutApi(self.__config)
