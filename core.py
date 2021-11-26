# api请求内核
# Powered by Kl1nge5
# 2021/11/24 晚上，过完一天，有点累

import requests
import os


class Config:
    from_lang = 'en'
    to_lang = 'zh'
    app_id = ''
    app_key = ''
    cuid = 'APICUID'
    mac = 'MAC'
    version = 3

    def setAppInfo(self, app_id: str, app_key: str):
        self.app_id = app_id
        self.app_key = app_key

    def setLanguage(self, f: str, t: str):
        self.from_lang = f
        self.to_lang = t


class RequestSender:
    def __init__(self):
        self.url = f'https://aip.baidubce.com/file/2.0/mt/pictrans/v1'
        self.tokenURL = 'https://aip.baidubce.com/oauth/2.0/token'
        self.token_parameter = {'grant_type': 'client_credentials', 'client_id': Config.app_id, 'client_secret': Config.app_key}

        self.token = ''
        self.payload = ''
        self.image = ''
        self.response = ''
        self.result = ''

    def getResult(self, image: str):
        try:
            self.token = requests.post(self.tokenURL, params=self.token_parameter).json()['access_token']
            self.payload = {'from': Config.from_lang, 'to': Config.to_lang, 'v': Config.version, 'access_token': self.token}
            self.image = {'image': (os.path.basename(image), open(image, 'rb'), "multipart/form-data")}
            self.response = requests.post(self.url, params=self.payload, files=self.image)
            self.result = self.response.json()
            return self.result['data']['sumDst']
        except Exception as e:
            return e
