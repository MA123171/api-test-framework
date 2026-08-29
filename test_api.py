import requests
import pytest
import json
from config import BASE_URL

with open("test_data.json","r",encoding="utf-8") as f:
    test_cases=json.load(f)


@pytest.mark.parametrize('case',test_cases)
def test_post_username(case):
    payload=case['payload']
    expected_name=case['expected_name']
    resp=requests.post(f'{BASE_URL}/post',data=payload)
    assert resp.status_code==200
    data=resp.json()
    assert data['form']['username']==expected_name


def test_get_status():
    resp=requests.get(f'{BASE_URL}/get')
    assert resp.status_code==200

