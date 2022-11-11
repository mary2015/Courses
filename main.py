# This is a sample Python script.
import os

import pytest


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    pytest.main(['-v', '--alluredir', './allure-results', './course3/cases', '--clean-alluredir'])
    os.system('/opt/homebrew/bin/allure generate ./allure-results/ -o ./allure-report/ --clean')



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
