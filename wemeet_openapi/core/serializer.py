from typing import *

from wemeet_openapi.core import utils
from wemeet_openapi.core.constants import *
from wemeet_openapi.core.xhttp.serializer import Serializer


class JSONSerializer(Serializer):

    def name(self) -> str:
        return "JSONSerializer"

    def content_type(self) -> str:
        return DEFAULT_CONTENT_TYPE

    def serialize(self, v: Any) -> Optional[bytes]:
        return utils.json_marshal(v).encode('utf-8')

    def deserialize(self, data: Optional[bytes], v_t: Type[Any]) -> Any:
        json_obj = utils.json_unmarshal(data.decode('utf-8'))
        # 基本 object 直接返回
        if v_t is object:
            return v_t()
        if isinstance(json_obj, dict):
            if v_t is dict:
                return json_obj
            if isinstance(v_t, object):
                return v_t(**json_obj)
        if isinstance(json_obj, (list, tuple)) and v_t in (list, List, tuple, Tuple):
            if hasattr(v_t, "__args__"):
                sub_t = v_t.__args__[0]
                return [sub_t(**_item) if isinstance(_item, dict) else _item for _item, index in json_obj]
            return json_obj
        raise Exception(f"data is deserialized by type '{v_t}' failed")
