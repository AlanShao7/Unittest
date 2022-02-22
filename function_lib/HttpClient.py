import requests
import json

class HttpClient(object):
  def __init__(self):
    pass

  def request(self, requestMethod, requestUrl, paramsType,requestData, headers =None, **kwargs):
    if requestMethod == "post":
      print("---", requestData, type(requestData))
      if paramsType == "form":
        response = self.__post(url = requestUrl, data = json.dumps(eval(requestData)),
                 headers = headers, **kwargs)
        return response
      elif paramsType == "json":
        response = self.__post(url = requestUrl, json = json.dumps(eval(requestData)),
                 headers = headers, **kwargs)
        return response
    elif requestMethod == "get":
      request_url = requestUrl
      if paramsType == "url":
        request_url = "%s%s" %(requestUrl, requestData)
      response = self.__get(url = request_url, params = requestData, **kwargs)
      return response

  def __post(self, url, data = None, json = None, headers=None,**kwargs):
    print("----")
    response = requests.post(url=url, data = data, json=json, headers=headers)
    return response

  def __get(self, url, params = None, **kwargs):
    response = requests.get(url, params = params, **kwargs)
    return response

if __name__ == "__main__":
    hc = HttpClient()
    res = hc.request("get", "http://kefu-test.weiwenjia.com/css/questionnaire/qstates", "url",'')
    print(res.json())