from wemeet_openapi.core.authenticator import VersionAuthenticator
from wemeet_openapi.core.serializer import JSONSerializer

# OPEN_API_DOMAIN 域名
OPEN_API_DOMAIN = "api.meeting.qq.com"

# DEFAULT_PROTOCOL 默认协议
DEFAULT_PROTOCOL = "https"

# SDK 使用的原生+自定义请求头
HTTP_HEADER_CONTENT_TYPE = "Content-Type"
HTTP_HEADER_USER_AGENT = "User-Agent"

XTC_HEADER_NONCE = "X-TC-Nonce"  # 随机正整数。
XTC_HEADER_KEY = "X-TC-Key"  # 应用安全凭证密钥对中的 SecretId。
XTC_HEADER_ACTION = "X-TC-Action"  # 操作的接口名称。
XTC_HEADER_REGION = "X-TC-Region"  # 地域参数，用来标识希望操作哪个地域的数据。
XTC_HEADER_TIMESTAMP = "X-TC-Timestamp"  # 当前 UNIX 时间戳，可记录发起 API 请求的时间。例如1529223702，单位为秒。
XTC_HEADER_VERSION = "X-TC-Version"  # 应用 App 的版本号，建议设置，以便灰度和查找问题。
XTC_HEADER_SIGNATURE = "X-TC-Signature"  # 签名方法产生的签名。
XTC_HEADER_REGISTERED = "X-TC-Registered"  # 启用账户通讯录，传入值必须为1，创建的会议可出现在用户的会议列表中。
HEADER_APPID = "AppId"  # 腾讯会议分配给企业的企业 ID。
HEADER_SDKID = "SdkId"  # 用户子账号或开发的应用 ID。
HEADER_ACCESSTOKEN = "AccessToken"  # OAuth2.0 鉴权成功后返回的 token 信息。
HEADER_OPENID = "OpenId"  # OAuth2.0 鉴权成功后的用户信息。

DEFAULT_CONTENT_TYPE = "application/json; charset=utf-8"

# JSON_SERIALIZER 全局 JSON 序列化器
JSON_SERIALIZER = JSONSerializer()
# DefaultSerializer 默认序列化器
DEFAULT_SERIALIZER = JSON_SERIALIZER
# DEFAULT_AUTHENTICATOR 默认鉴权器，用于增加 SDK 版本标识头
DEFAULT_AUTHENTICATOR = VersionAuthenticator()
