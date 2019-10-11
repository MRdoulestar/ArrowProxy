#!/usr/bin/env python
# coding=utf-8

# 请求超时时间（秒）
REQUEST_TIMEOUT = 10
# 请求延迟时间（秒）
REQUEST_DELAY = 0

# redis 地址
REDIS_HOST = "localhost"
# redis 端口
REDIS_PORT = 6379
# redis 密码
#REDIS_PASSWORD = None
REDIS_PASSWORD = ""
# redis set key
REDIS_KEY = "proxies:ranking"
# redis 连接池最大连接量
REDIS_MAX_CONNECTION = 20

# REDIS SCORE 最大分数
MAX_SCORE = 10
# REDIS SCORE 最小分数
MIN_SCORE = 0
# REDIS SCORE 初始分数
INIT_SCORE = 9

# server web host
SERVER_HOST = "localhost"
# server web port
SERVER_PORT = 2333
# 是否开启日志记录
SERVER_ACCESS_LOG = True

# 代理池URL
PROXY_POOL_URL = "http://"+SERVER_HOST+":"+str(SERVER_PORT)+"/"

# 批量测试数量
VALIDATOR_BATCH_COUNT = 256
# 校验器测试网站，可以定向改为自己想爬取的网站，如新浪，知乎等
VALIDATOR_BASE_URL = "http://baidu.com"
# 校验器循环周期（分钟）
VALIDATOR_RUN_CYCLE = 15


# 爬取器循环周期（分钟）
CRAWLER_RUN_CYCLE = 30
# 请求 headers
HEADERS = {
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/6.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
}
