# coding: utf-8

from helper.error_code import ECEnum

_URL = "/api/demo/test/hello"


def test(client, logger):

    resp = client.get(f"{_URL}?keyword=200")
    assert resp.status_code == 200
    result = resp.json()
    assert result["code"] == "0"
    assert result["data"]["keyword"] == "200"


def test_now_allowed_method(client, logger):

    resp = client.post(f"{_URL}?keyword=200")
    assert resp.status_code == 200

    result = resp.json()
    logger.info(result)
    assert result["code"] == ECEnum.ClientError.code
    assert result["message"] == ECEnum.ClientError.message
    assert result["desc"] == "Method Not Allowed"
