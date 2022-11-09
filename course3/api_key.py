import allure
import jsonpath
import pymysql
import yaml
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

    @allure.step("Get data from DB")
    def get_data_from_database(self, sql):
        conn = pymysql.connect(
            host="shop-xo.hctestedu.com",
            port=3306,
            user="api_test",
            password="Aa9999!",
            database="shopxo_hctested"
        )
        cursor = conn.cursor()
        cursor.execute(query=sql)
        results = cursor.fetchall()[0][0]
        conn.close()
        return results


if __name__ == "__main__":
    sql = f"select status from sxo_order where id = 1"

    result = APIKey().get_data_from_database(sql)
    print(result)
