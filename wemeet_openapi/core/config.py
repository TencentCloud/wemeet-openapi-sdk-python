from typing import Optional

from wemeet_openapi.core.xhttp.client import AbstractClient


class Config(object):
    """ Config 通用配置
    :param version: 应用 App 的版本号，建议设置，以便灰度和查找问题。
        通过设置该字段，API 会把该版本信息传递给会议后台，以控制一些和 App 版本有关的特性。
    :param app_id:  腾讯会议分配给企业的企业 ID。
        企业管理员可以登录 腾讯会议官网，单击右上角用户中心，在左侧菜单栏中的企业管理 > 账户管理 > 账户信息中进行查看。
        开发者可以单击右上角用户中心，在左侧菜单栏中的企业管理 > 高级  > REST API 应用信息中查看。
    :param sdk_id: 用户子账号或开发的应用 ID。
        企业管理员可以登录 腾讯会议官网，单击右上角用户中心，在左侧菜单栏中的企业管理 > 高级 > REST API 中进行查看（JWT 鉴权中如存在 SdkId 则必须填写，早期申请 API 且未分配 SdkId 的客户可不填写）。
    :param secret_id: 应用生成的 Secret ID。JWT 鉴权用。
    :param secret_key: 应用生成的 Secret Key。JWT 鉴权用。
     """
    def __init__(
            self,
            clt: Optional[AbstractClient] = None,
            version: Optional[str] = None,
            app_id: Optional[str] = None,
            sdk_id: Optional[str] = None,
            secret_id: Optional[str] = None,
            secret_key: Optional[str] = None):
        self.clt: Optional[AbstractClient] = clt
        self.version: Optional[str] = version
        self.app_id: Optional[str] = app_id
        self.sdk_id: Optional[str] = sdk_id
        self.secret_id: Optional[str] = secret_id
        self.secret_key: Optional[str] = secret_key
