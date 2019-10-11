# ArrowProxy
针对红队&amp;渗透测试的代理池随机跳板(HTTP/HTTPS)

## 工具简介
对部分站点的一些测试和访问可能会导致IP被BAN或者触发其他奇奇怪怪的问题，以及为了一定程度上的保护自己，粗糙地拿各种轮子实现了HTTP/HTTPS流量随机代理出口，方便自己，方便大家。

```
1、基于各大免费代理IP站点的代理，动态维护高可用代理池
2、构建本地中间代理转发，随机选择代理池的二级代理继续转发流量
3、支持HTTP/HTTPS
```

## 工具使用
```
启动代理池服务: python server_sanic.py > server.log 2>&1 & OR python server_flask.py > server.log &
启动代理池维护: python check_validate.py > check.log 2>&1 &
启动本地随机转发: python proxy.py > localproxy.log 2>&1 &
```
#### HTTPS支持需要将证书导入Firefox的证书信任中


## 参考项目
[BaseProxy](https://github.com/qiyeboy/BaseProxy "BaseProxy")
[async-proxy-pool](https://github.com/chenjiandongx/async-proxy-pool "async-proxy-pool")