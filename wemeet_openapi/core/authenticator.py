import base64
import hmac
import random
import time

import requests

from typing import *

import wemeet_openapi.core.constants as constants
from wemeet_openapi.core.xhttp.authenticator import Authenticator
from wemeet_openapi.core.version import VERSION
from wemeet_openapi.core.config import Config


class VersionAuthenticator(Authenticator):
    """
    VersionAuthenticator SDK 版本鉴权器
    """

    def auth_header(self, http_req: requests.PreparedRequest) -> None:
        http_req.headers[constants.HTTP_HEADER_USER_AGENT] = VERSION


class JWTAuthenticator(Authenticator):
    """ JWTAuthenticator JWT 鉴权器

    封装了 JWT 鉴权需要的请求头参数。

    :param nonce: 此参数参与签名计算。随机正整数。SDK 默认自动随机生成。
    :param timestamp: 此参数参与签名计算。当前 UNIX 时间戳，可记录发起 API 请求的时间。SDK 默认当前时间戳。例如1529223702，单位为秒。
        注意：如果与服务器时间相差超过5分钟，会引起签名过期错误。
    :param action: 操作的接口名称。注意：某些接口不需要传递该参数，接口文档中会对此特别说明，此时即使传递该参数也不会生效。
    :param region: 地域参数，用来标识希望操作哪个地域的数据。
        注意：某些接口不需要传递该参数，接口文档中会对此特别说明，此时即使传递该参数也不会生效。
    :param signature: 放置由官网的签名方法产生的签名。SDK 默认自动生成，也可替换为自己生成符合标准的签名。
    :param registered: 启用账户通讯录，传入值必须为1，创建的会议可出现在用户的会议列表中。
        启用账户通讯录说明：
            1. 通过 SSO 接入腾讯会议账号体系。
            2. 通过调用接口创建企业用户。
            3. 通过企业管理后台添加或批量导入企业用户。
    """

    __config: Optional[Config] = None

    def __init__(
            self,
            nonce: Optional[int] = None,
            timestamp: Optional[str] = None,
            action: Optional[str] = None,
            region: Optional[str] = None,
            signature: Optional[str] = None,
            registered: str = "1",
    ):
        self.nonce: Optional[int] = nonce
        self.timestamp: Optional[str] = timestamp
        self.action: Optional[str] = action
        self.region: Optional[str] = region
        self.signature: Optional[str] = signature
        self.registered: str = registered

    def auth_header(self, http_req: requests.PreparedRequest) -> None:
        if self.__config is None:
            raise Exception("JWT authenticator is not available")

        if http_req.headers.get(constants.HTTP_HEADER_CONTENT_TYPE) is None:
            http_req.headers[constants.HTTP_HEADER_CONTENT_TYPE] = constants.DEFAULT_CONTENT_TYPE

        if self.__config.secret_id is None or self.__config.secret_id == "":
            raise Exception("JWT authenticator SecretId can't be empty")
        http_req.headers[constants.XTC_HEADER_KEY] = self.__config.secret_id

        if self.__config.app_id is None or self.__config.app_id == "":
            raise Exception("JWT authenticator AppId can't be empty")
        http_req.headers[constants.HEADER_APPID] = self.__config.app_id
        http_req.headers[constants.HEADER_SDKID] = self.__config.sdk_id

        if self.nonce is None or self.nonce == 0:
            ts = int(time.time() * 1000)
            rs = f"{random.randint(0, 999999):06d}"
            ri = int(rs)
            self.nonce = (ts * 1000000) + ri
        http_req.headers[constants.XTC_HEADER_NONCE] = str(self.nonce)

        if self.registered is not None or self.registered != "":
            http_req.headers[constants.XTC_HEADER_REGISTERED] = self.registered
        else:
            http_req.headers[constants.XTC_HEADER_REGISTERED] = "1"

        if self.__config.version is not None and self.__config.version != "":
            http_req.headers[constants.XTC_HEADER_VERSION] = self.__config.version

        if self.action is not None and self.action != "":
            http_req.headers[constants.XTC_HEADER_ACTION] = self.action

        if self.region is not None and self.region != "":
            http_req.headers[constants.XTC_HEADER_REGION] = self.region

        if self.timestamp is None or self.timestamp == "":
            self.timestamp = str(int(time.time()))
        http_req.headers[constants.XTC_HEADER_TIMESTAMP] = self.timestamp

        if self.signature is None or self.signature == "":
            self.signature = self.__signature__(req=http_req)
        http_req.headers[constants.XTC_HEADER_SIGNATURE] = self.signature

    def __signature__(self, req: requests.PreparedRequest) -> str:
        """
           生成签名
        :return: 签名，需要设置在请求头X-TC-Signature中
        """

        if isinstance(req.body, (bytes, str)):
            req_body = req.body.decode("utf-8")
        else:
            req_body = ""

        sign_str = "{0}\nX-TC-Key={1}&X-TC-Nonce={2}&X-TC-Timestamp={3}\n{4}\n{5}".format(
            req.method, self.__config.secret_id, self.nonce, self.timestamp, req.path_url, req_body)
        signer = hmac.new(key=self.__config.secret_key.encode('utf-8'),
                          msg=sign_str.encode('utf-8'), digestmod='sha256')
        sign = signer.hexdigest()
        return base64.b64encode(sign.encode('utf-8')).decode('utf-8')

    def options_build(self) -> Callable[[Config], Authenticator]:
        """
        构造 authenticator_option 函数，用于设置请求的 authenticators
        :param self: jwt 鉴权器对象
        :return: authenticator_option: Callable[[Config], Authenticator]
        """

        def authenticator_option(cfg: Config) -> Authenticator:
            self.__config = cfg
            return self

        return authenticator_option


class OAuth2Authenticator(Authenticator):
    """ OAuth2Authenticator OAuth2.0 鉴权器

    封装了 OAuth2.0 鉴权需要的请求头参数。

    :param nonce: 此参数参与签名计算。随机正整数。SDK 默认自动随机生成。
    :param timestamp: 此参数参与签名计算。当前 UNIX 时间戳，可记录发起 API 请求的时间。SDK 默认当前时间戳。例如1529223702，单位为秒。
        注意：如果与服务器时间相差超过5分钟，会引起签名过期错误。
    :param action: 操作的接口名称。注意：某些接口不需要传递该参数，接口文档中会对此特别说明，此时即使传递该参数也不会生效。
    :param region: 地域参数，用来标识希望操作哪个地域的数据。
        注意：某些接口不需要传递该参数，接口文档中会对此特别说明，此时即使传递该参数也不会生效。
    :param access_token: OAuth2.0 鉴权成功后返回的 token 信息。
    :param open_id: OAuth2.0 鉴权成功后的用户信息。
    """

    __config: Optional[Config] = None

    def __init__(
        self,
        open_id: str,
        access_token: str,
        nonce: Optional[int] = None,
        timestamp: Optional[str] = None,
        action: Optional[str] = None,
        region: Optional[str] = None,
    ):
        self.nonce: Optional[int] = nonce
        self.timestamp: Optional[str] = timestamp
        self.action: Optional[str] = action
        self.region: Optional[str] = region
        self.access_token: str = access_token
        self.open_id: str = open_id

    def auth_header(self, http_req: requests.PreparedRequest) -> None:
        if self.__config is None:
            raise Exception("OAuth2 authenticator is not available")

        if http_req.headers.get(constants.HTTP_HEADER_CONTENT_TYPE) is None:
            http_req.headers[constants.HTTP_HEADER_CONTENT_TYPE] = constants.DEFAULT_CONTENT_TYPE

        if self.access_token is None or self.access_token == "":
            raise Exception("OAuth2 authenticator AccessToken can't be empty")
        http_req.headers[constants.HEADER_ACCESSTOKEN] = self.access_token

        if self.open_id is None or self.open_id == "":
            raise Exception("OAuth2 authenticator OpenId can't be empty")
        http_req.headers[constants.HEADER_OPENID] = self.open_id

        if self.nonce is None or self.nonce == 0:
            ts = int(time.time() * 1000)
            rs = f"{random.randint(0, 999999):06d}"
            ri = int(rs)
            self.nonce = (ts * 1000000) + ri
        http_req.headers[constants.XTC_HEADER_NONCE] = str(self.nonce)

        if self.__config.version is not None and self.__config.version != "":
            http_req.headers[constants.XTC_HEADER_VERSION] = self.__config.version

        if self.action is not None and self.action != "":
            http_req.headers[constants.XTC_HEADER_ACTION] = self.action

        if self.region is not None and self.region != "":
            http_req.headers[constants.XTC_HEADER_REGION] = self.region

        if self.timestamp is None or self.timestamp == "":
            self.timestamp = str(int(time.time()))
        http_req.headers[constants.XTC_HEADER_TIMESTAMP] = self.timestamp

    def options_build(self) -> Callable[[Config], Authenticator]:
        """
        构造 authenticator_option 函数，用于设置请求的 authenticators
        :param self: oauth2 鉴权器对象
        :return: authenticator_option: Callable[[Config], Authenticator]
        """

        def authenticator_option(cfg: Config) -> Authenticator:
            self.__config = cfg
            return self

        return authenticator_option
