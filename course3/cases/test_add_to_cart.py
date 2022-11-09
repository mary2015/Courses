import allure

from course3.api_key import APIKey
from course3.constants import Constants


@allure.step("add goods into cart")
def test_add_to_cart(get_token):
    with allure.step("add goods into the cart"):
        api_key = APIKey()
        token = get_token
        url = Constants.BASE_URL+"/index.php?s=api/cart/save"
        data = {
            "goods_id": "10",
            "spec": "",
            "stock": 1
        }
        params = {
            "application": "app",
            "application_client_type": "weixin",
            "token": token,
        }

        resp = api_key.request(method="POST", url=url, params=params, json=data)
        print(resp.json())
        msg = api_key.get_resp(resp.json(), "$.msg")
        assert msg == "加入成功"