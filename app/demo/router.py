from fastapi import APIRouter

from .views.hello import test_hello
from .views.error import test_error_code
from .pyd_models.response.hello import Model as HelloResModel
from utils.pyd_model import res_model_factory

router: APIRouter = APIRouter(prefix="/demo", tags=["demo"])


# 测试hello
router.add_api_route("/test/hello", test_hello, methods=["GET"], response_model=res_model_factory(HelloResModel))
router.add_api_route("/test/error", test_error_code, methods=["GET"], response_model=None)
