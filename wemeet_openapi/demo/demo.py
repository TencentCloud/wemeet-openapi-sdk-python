import random
import time

import wemeet_openapi


# 请求demo
def demo():
    # 1.构造 client 客户端(jwt 鉴权需要配置 appId sdkId secretID 和 secretKey)
    client = wemeet_openapi.Client(app_id="2****46", sdk_id="2****50",
                                   secret_id="Zk*****J8h",
                                   secret_key="Y2z*****WRsVksn")

    endTime = str(int(time.time()) + 3600)
    instanceid = 1
    startTime = str(int(time.time()))
    subject = "测试会议"
    type = 1
    userid = "userid"
    # 2.构造请求体
    bodyReq = wemeet_openapi.V1MeetingsPostRequest(
        end_time=endTime,
        instanceid=instanceid,
        subject=subject,
        type=type,
        userid=userid,
        start_time=startTime,
    )

    request = wemeet_openapi.ApiV1MeetingsPostRequest(
        body=bodyReq  # V1MeetingsPostRequest ｜
    )

    # 3.构造 JWT 鉴权器
    authenticator_builder = wemeet_openapi.JWTAuthenticator(
        nonce=random.randrange(0, 2 ** 64),
        timestamp=str(int(time.time()))
    ).options_build()

    # 4.发送对应的请求
    try:
        response = client.meetings_api.v1_meetings_post(
            request=request,
            authenticator_options=[authenticator_builder])

        print(f"Response from `MeetingsApi.V1MeetingsPost`: {vars(response)}\n")
    except wemeet_openapi.ClientException as e:
        print(f"Error when calling `MeetingsApi.V1MeetingsPost`: {e}\n")

    except wemeet_openapi.ServiceException as svrErr:
        print(f"Error when calling `MeetingsApi.V1MeetingsPost`: {svrErr}\n")
        print(f"Full HTTP response: {str(svrErr.api_resp.raw_body)}\n")


# 调用入口点函数
if __name__ == "__main__":
    demo()