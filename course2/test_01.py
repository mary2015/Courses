import allure

from course2.api_key import APIKey


@allure.title("Test Login")
def test_01():
    with allure.step("login to mall"):
        api_key = APIKey()
        url = "http://shop-xo.hctestedu.com/index.php?s=api/user/login"
        params = {
            "application": "app",
            "application_client_type": "weixin",
        }
        json = {
            "accounts": "zz",
            "pwd": "123456",
            "type": "username",
        }
        resp = api_key.request(url=url, method="GET", params=params, json=json)
        msg = api_key.get_resp(resp.json(), "$.msg")
        assert msg == "登录成功"
