import allure
import pytest

from course3.api_key import APIKey
from course3.constants import Constants
from course3.yaml_driver import read_yaml


@pytest.mark.parametrize("data", read_yaml.get_yaml_data('./course3/test_data/payment_data.yaml'))
def test_payment(get_token, data):
    api_key = APIKey()
    params = {
        "application": "app",
        "application_client_type": "weixin",
        "token": get_token
    }
    url = Constants.BASE_URL+"/index.php?s=api/order/pay"
    resp = api_key.request(method="POST", url=url, params=params, json=data)
    print(resp.json())
