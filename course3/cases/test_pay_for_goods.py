import allure
import pytest

from course3.api_key import APIKey
from course3.constants import Constants


@pytest.mark.parametrize("goods_id,payment_id", [(10, 2), (11, 3), (12, 4)])
@allure.step("buy goods")
def test_pay_for_goods(get_token, goods_id, payment_id):
    with allure.step("buy goods directly without adding to cart"):
        api_key = APIKey()
        url = Constants.BASE_URL+"/index.php?s=api/buy/add"
        params = {
            "application": "app",
            "application_client_type": "weixin",
            "token": get_token
        }
        json = {
            "buy_type": "goods",  # 类型（cart购物车、goods直接购买），不需要添加购物车
            "goods_id": goods_id,
            "stock": "1",
            "spec": [],
            "address_id": 921,
            "payment_id": payment_id,
            "site_model": 0,
            "is_points": 0,
            "user_note": ""
        }

        resp = api_key.request(method="POST", url=url, params=params, json=json)
        print(resp.json())
        msg = api_key.get_resp(resp.json(), "$.msg")
        assert msg == "提交成功"
        code = api_key.get_resp(resp.json(), "$.code")
        assert code == 0
        order_status = api_key.get_resp(resp.json(), "$.data.order_status")
        assert order_status == 1
