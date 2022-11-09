import allure
import jsonpath
from requests import request


class APIKey:
    # Encapsulation GET, POST requests
    @allure.step("Send Request")
    def request(self, method, url, **kwargs):
        return request(method, url, **kwargs)

    # Encapsulation response data
    @allure.step("Get Specific Response Key-Value")
    def get_resp(self, data, key):
        value = jsonpath.jsonpath(data, key)
        return value[0]