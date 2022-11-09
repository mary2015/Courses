from requests import request
import jsonpath
import allure


class Test:
    @allure.step("login")
    def test_01(self):
        url = "http://shop-xo.hctestedu.com/index.php?s=api/user/login"
        params = {
            "application": "app",
            "application_client_type": "weixin",
        }
        json = {
            "accounts": "zz",
            "pwd": "123456",
            "type": "username"
        }
        response = request(method="get", url=url, params=params, json=json)
        print(response.status_code)
        print(response.content)
        print(response.json())
        print(response.url)
        print(response.cookies)
        print(response.headers)
        print(response.encoding)
        print(jsonpath.jsonpath(response.json(), "$..id")[0])
