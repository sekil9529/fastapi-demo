# fastapi-demo

# 目录结构
```shell
- app: app目录
  - xxx/: 具体某个业务场景如 user/
    - param/: 参数相关
      - request: 请求参数
      - response: 响应参数
      - router.py: 子路由
    - view/: 视图
  - application.py: app的工厂方法
  - router.py: 总路由
- config/: 配置文件目录
  - gunicorn.conf.py: gunicorn运行时载入
  - config.yaml: 应用配置
  - config.test.yaml: 测试配置留档
- event/: 事件
- exception_handler/: 异常处理
- middleware/: 请求中间件
- model/: 数据库模型
- util/: 通用工具集目录（不限制当前项目）
- helper/: 通用工具集目录（当前业务强相关）
- extra/: 对框架级别的扩展的目录
- log/: 日志目录
- tmp/: 临时目录，存储 gunicorn pid文件
- tests/: 测试文件目录
- setting.py: 配置
- manage.py: 启动入口
```

# 启动方式

1. 命令行
```shell
# 本地
python manage.py

# 测试
python -m gunicorn -c config/gunicorn.conf.py manage:app
```
