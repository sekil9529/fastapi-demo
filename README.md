# fastapi-demo

# 环境
- Python == 3.9
- fastapi == 0.70 
- tortoise-orm == 0.17
- aiomysql

# 启动方式
```shell
python -m gunicorn manage:app -b 0.0.0.0:8000 -w 2 -k uvicorn.workers.UvicornWorker --max-requests 10000
```
