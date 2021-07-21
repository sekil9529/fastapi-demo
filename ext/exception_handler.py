# coding: utf-8

from fastapi import Request
from starlette.responses import JSONResponse
from loguru import logger

Exc = Exception


async def exc_handler(request: Request, exc: Exception) -> JSONResponse:
    logger.exception(exc)
    return JSONResponse({'message': '服务异常'}, status_code=500)
