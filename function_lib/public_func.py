import requests


class Gettoken:
    def __init__(self):
        self.login_url = 'https://lxcrm-test.weiwenjia.com/api/v2/auth/login'
        self.data = {'login': 15868718273,
                     'password': 'Ik123456',
                     'corp_id': 'wwjg8aoKBzsWlkMGCHYG'}

    def token(self):
        req = requests.post(url=self.login_url, params=self.data)
        user_token = req.json()['data']['user_token']
        return user_token


class HttpRequest:

    def __init__(self):
        token = Gettoken()
        user_token = token.token()
        token = 'Token token=' + user_token
        self.url = 'https://lxcrm-test.weiwenjia.com'
        self.header = {
            "Authorization": token,
        }

    def send_request(self, api_name, method, params=None, content_type='application/json', data=None, json=None, timeout=10):
        """
        request封装
        :param self:
        :param api_name: 请求地址
        :param method: 请求方式
        :param params: get的请求参数
        :param content_type: 传参方式
        :param data: 字典格式传参
        :param json: json格式传参
        :param timeout: 超时时间
        :return: 请求返回值
        """
        self.header['content-type'] = content_type
        new_method = method.lower()
        if new_method == 'get':
            print("正在请求接口，请求地址{},请求参数{},".format(self.url + api_name, params))
            res = requests.get(url=self.url + api_name, params=params, headers=self.header, timeout=timeout)
            return res
        elif new_method == 'post':
            if json:
                print("正在请求接口，请求地址{},请求参数{},".format(self.url + api_name, json))
                res = requests.post(url=self.url+api_name, json=json, headers=self.header, timeout=timeout)
                return res
            else:
                print("正在请求接口，请求地址{},请求参数{},".format(self.url + api_name, data))
                res = requests.post(url=self.url+api_name, data=data, headers=self.header, timeout=timeout)
                return res
        elif new_method == 'put':
            print("正在请求接口，请求地址{},请求参数{},".format(self.url + api_name, data))
            res = requests.put(url=self.url+api_name, data=data, headers=self.header, timeout=timeout)
            return res



    # def get(self, data='', api_name=''):
    #     print('self.url + api_name', self.url + api_name)
    #     response = requests.get(self.url + api_name, params=data, headers=self.header)
    #     return response
    #
    # def post(self, data='', api_name=''):
    #     print('self.url + api_name', self.url + api_name)
    #     response = requests.post(self.url + api_name, data=data, headers=self.header)
    #     return response
    #
    # def put(self, data='', api_name=''):
    #     print('self.url + api_name', self.url + api_name)
    #     response = requests.post(self.url + api_name, data=data, headers=self.header)
    #     return response
