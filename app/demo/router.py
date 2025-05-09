# coding: utf-8

from fastapi import APIRouter

from .view.hello import test_hello
from .view.error import test_error_code
from .param.response.hello import Model as HelloResModel
from helper.response import res_model_factory, ResData

router: APIRouter = APIRouter(prefix="/demo", tags=["demo"])


# 测试hello
router.add_api_route("/test/hello", test_hello, methods=["GET"], response_model=res_model_factory(HelloResModel))
router.add_api_route("/test/error", test_error_code, methods=["GET"], response_model=ResData)
