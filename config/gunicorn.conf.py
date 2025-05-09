# coding: utf-8

"""
文档地址: https://docs.gunicorn.org/en/latest/settings.html
"""

import os

_base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

'''gunicorn'''

# 守护Gunicorn进程，默认False
daemon = False

# 要写入的访问日志格式
# access_log_format = " - ".join(["%(t)s", "[%(h)s]", "[%(a)s]", "[%(m)s]", "[%(U)s]", "[%(L)s]"])

# app dir
chdir = _base_dir

# socket bind
bind = f'0.0.0.0:{os.environ.get("GUNICORN_PORT", 8000)}'

# worker推荐的数量为当前的CPU个数*2 + 1。
workers = int(os.environ.get("GUNICORN_WORKERS", 3))

# 工作模式
worker_class = "uvicorn.workers.UvicornWorker"

# 设置pid文件的文件名，如果不设置将不会创建pid文件
pidfile = os.path.join(_base_dir, "tmp", "gunicorn.pid")

# 超过这么多秒后工作将被杀掉，并重新启动。一般设定为30秒
timeout = int(os.environ.get("GUNICORN_TIMEOUT", 30))

# 最大客户端并发数量，默认情况下这个值为1000。此设置将影响gevent和eventlet工作模式
worker_connections = int(os.environ.get("GUNICORN_WORKER_CONNECTIONS", 500))

# 达到worker最大处理次数之后，自动重启worker，防止内存溢出
max_requests = int(os.environ.get("GUNICORN_MAX_REQUESTS", 20000))
'''
max_requests的最大抖动
每个worker在处理请求次数随机达到 max_requests ~ max_requests + max_requests_jitter 时重启
避免所有worker同时被重启
'''
max_requests_jitter = int(os.environ.get("GUNICORN_MAX_REQUESTS_JITTER", 1000))

# 要写入的访问日志目录（gunicorn的日志记录模块也是logging，项目启动时,logging会禁用已经存在的handler，因此记录到的东西会为空。）
# 服务器日志已经集成到项目之中
# accesslog = "../log/gunicorn.info.log"
#
# # 要写入错误日志的文件目录。
# errorlog = "../log/gunicorn.error.log"

# loglevel
loglevel = "info"

# 开启访问日志
accesslog = "-"
