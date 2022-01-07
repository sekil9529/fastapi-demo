# fastapi-demo

# 环境
- Python == 3.9
- fastapi == 0.70 
- tortoise-orm == 0.17
- aiomysql
- httpx == 0.21

# 启动方式

1. 命令行
```shell
# 本地
python manage.py

# 测试
python -m gunicorn manage:app -b 0.0.0.0:8000 -w 2 -k uvicorn.workers.UvicornWorker --max-requests 10000
```
