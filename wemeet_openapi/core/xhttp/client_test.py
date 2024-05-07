import unittest

from wemeet_openapi.core.xhttp.client import Client
from wemeet_openapi.core.xhttp.request import ApiRequest


# wemeet_openapi 单元测试
class TestClient(unittest.TestCase):

    def test_init_client(self):
        try:
            clt = Client("www.baidu.com", protocol="https")
            resp = clt.get(req=ApiRequest(api_uri="/", body=None))
            data = resp.raw_body.decode("UTF-8")
            print(f"new client success, \nresp body: {data}\n", )
        except Exception as e:
            self.assertIsNone(e, f"new client error, \nerr: {e}\n")
