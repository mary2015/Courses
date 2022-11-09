import allure
import yaml


# Encapsulation reading data from yaml file
@allure.step("Read data from Yaml file")
def get_yaml_data(path):
    file = open(path, 'r', encoding='utf-8')
    data = yaml.safe_load_all(file)
    return data
