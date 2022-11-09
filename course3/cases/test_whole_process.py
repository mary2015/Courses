import allure
import pytest
from deepdiff import DeepDiff

from course3.api_key import APIKey
from course3.constants import Constants
from course3.yaml_driver import read_yaml


@allure.step("the whole process")
@pytest.mark.parametrize("expected_data", read_yaml.get_yaml_data(
    "/Users/marongyao/PycharmProjects/Assignment/course3/expected_data/cart_details.yaml"))
def test_whole_process(get_token, expected_data):
    with allure.step("add goods into cart"):
        api_key = APIKey()
        url = Constants.BASE_URL + "/index.php?s=api/cart/save"
        json = {
            "goods_id": "10",
            "spec": "",
            "stock": 1
        }

        params = {
            "application": "app",
            "application_client_type": "weixin",
            "token": get_token
        }

        resp = api_key.request(method="POST", url=url, params=params, json=json)
        print(resp.json())
        msg = api_key.get_resp(resp.json(), "$.msg")
        assert msg == "加入成功"
        code = api_key.get_resp(resp.json(), "$.code")
        assert code == 0

    with allure.step("query the cart"):
        url = Constants.BASE_URL + "/index.php?s=api/cart/index"
        resp = api_key.request(method="GET", url=url, params=params)
        print(resp.json())
        result = DeepDiff(expected_data, resp.json(), view='tree',
                          exclude_paths={"root['data']['data'][0]['id']", "root['data']['data'][0]['add_time']",
                                         "root['data']['data'][0]['upd_time']"}).pretty()
        print(expected_data)
        print(result)
        cart_id = api_key.get_resp(resp.json(), "$..id")
        # assert result == ''

    with allure.step("Checkout"):
        url = Constants.BASE_URL + "/index.php?s=api/buy/add"
        data = {
            "goods_id": 10,
            "buy_type": "cart",
            "stock": 1,
            "spec": "",
            "ids": cart_id,
            "address_id": 921,
            "payment_id": 4,
            "user_note": "",
            "site_model": 0
        }
        resp = api_key.request(method="POST", url=url, params=params, json=data)
        order_id = api_key.get_resp(resp.json(), "$..order_ids")[0]
        order_status = api_key.get_resp(resp.json(), "$..order_status")
        with allure.step("check order_Status in DB"):
            sql = f"select status from sxo_order where id = {order_id}"
            order_status_db = api_key.get_data_from_database(sql)
            assert order_status_db == order_status

    with allure.step("payment"):
        url = Constants.BASE_URL + "/index.php?s=api/order/pay"
        data = {
            "ids": 12,
            "payment_id": 4  # 1 alipay,2 wechatpay,4 cash on delivery
        }
        resp = api_key.request(method="POST", url=url, params=params, json=data)
        print(resp)
