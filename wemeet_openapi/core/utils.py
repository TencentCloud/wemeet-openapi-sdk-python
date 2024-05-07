import copy
import datetime
import json
from typing import Any, Dict


def json_marshal(v: Any) -> str:
    return json.dumps(v, separators=(",", ":"), default=__marshal__, ensure_ascii=False)


def json_unmarshal(data: str) -> Any:
    return json.loads(s=data)


def __marshal__(o: Any) -> Any:
    if hasattr(o, "__dict__"):
        return __filter_null__(copy.deepcopy(vars(o)))
    if isinstance(o, datetime.datetime):
        return o.strftime("%Y-%m-%d %H:%M:%S")
    if isinstance(o, bytes):
        return str(o, encoding="utf-8")
    if isinstance(o, int):
        return int(o)
    if isinstance(o, float):
        return float(o)
    if isinstance(o, set):
        return list(o)
    if type(o) is object:
        return {}
    raise TypeError(f'Object of type {o.__class__.__name__} '
                    f'is not JSON serializable')


def __filter_null__(d: Dict) -> Dict:
    if isinstance(d, dict):
        for k, v in list(d.items()):
            if isinstance(v, dict):
                __filter_null__(v)
            elif v is None:
                del d[k]

    return d
