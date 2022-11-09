import jsonpath
import pytest

from course3.api_key import APIKey


@pytest.fixture(scope="session")
def get_token():
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
    return jsonpath.jsonpath(resp.json(), "$..token")
