import requests
import pytest
import json
import allure
from config import BASE_URL

with open("test_data.json","r",encoding="utf-8") as f:
    test_cases=json.load(f)

@allure.feature('接口测试')
@allure.story('POST接口')
@allure.title('登录接口测试')
@pytest.mark.parametrize('case',test_cases)
def test_post_username(case):
    payload=case['payload']
    expected_name=case['expected_name']
    with allure.step("发送 POST 请求"):
        resp=requests.post(f'{BASE_URL}/post',data=payload)
    with allure.step("断言状态码"):
        assert resp.status_code==200
    with allure.step("断言用户名"):
        data=resp.json()
        assert data['form']['username']==expected_name

@allure.feature("接口测试")
@allure.story("GET 接口")
@allure.title("GET 状态码检查")
def test_get_status():
    resp=requests.get(f'{BASE_URL}/get')
    assert resp.status_code==200
