# fastapi-demo

## 简介

基于 Python-3.7 + fastapi-0.65 + SQLAlchemy-1.4 + aiomysql + loguru

用于项目生成模板

##  项目文件组织结构

```
.fastapi-demo
├── app                                  # app主目录

│   ├── __init__.py                      # app创建及相关组件注册
│   ├── models.py                        # 数据库模型
│   ├── router.py                        # 包含全部模块的router元组

│   ├── demo                             # demo模块
│   │   ├── __init__.py  
│   │   ├── router.py                    # demo模块router配置
│   │   └── views.py                     # demo模块相关视图

│   └── user                             # user模块
│       ├── __init__.py
│       ├── router.py                    # user模块router配置
│       └── views.py                     # user模块相关视图

├── ext                                  # 扩展模块

│   ├── error_code.py                    # 错误码定义

│   ├── events                           # fastapi-事件
│   │   ├── __init__.py                  # 包含全部事件的元组
│   │   ├── base.py                      # 事件基类
│   │   └── sqlalchemy.py                # SQLAlchemy事件，启动时绑定Session类，关闭时清空连接池

│   ├── exception_handlers               # fastapi-异常处理类
│   │   ├── __init__.py                  # 包含全部异常处理类的元组
│   │   ├── base.py                      # 异常处理基类
│   │   ├── error_code.py                # 错误码异常处理类
│   │   ├── request_validation.py        # 请求校验异常处理类
│   │   └── unknown.py                   # 未知异常处理类
│   ├── __init__.py

│   ├── middlewares                      # fastapi-中间件
│   │   ├── __init__.py                  # 包含全部中间件的元组
│   │   ├── base.py                      # 中间件基类
│   │   ├── sqlalchemy.py                # SQLAlchemy中间件，参考Sanic实现，request绑定session，response释放session
│   │   └── timer.py                     # 超时中间件

│   └── response.py                      # response扩展

├── libs                                 # 通用模块
│   ├── config.py                        # 读取配置文件
│   ├── datetime.py                      # 日期相关函数
│   ├── dict.py                          # 扩展字典

│   ├── error_code                       # 错误码相关
│   │   ├── enum.py                      # 错误码枚举类
│   │   ├── exception.py                 # 错误码异常类
│   │   └── __init__.py
│   ├── __init__.py

│   ├── logger.py                        # loguru

│   └── sqlalchemy                       # SQLAlchemy相关
│       ├── __init__.py 
│       └── result.py                    # 结果格式化

├── manage.py                            # 项目启动文件
├── README.md
├── requirements.txt                     # 依赖包
├── .evn_bak                             # 配置文件模板，请改名为".env"

└── settings                             # 配置类
    ├── __init__.py                      # 获取对应配置类的方法
    ├── base.py                          # 配置基类
    ├── development.py                   # 开发环境配置类
    └── production.py                    # 生产环境配置类
```