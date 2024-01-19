# Nginx

## nginx 涉及的几个文件？
nginx 可执行文件，nginx.conf 配置文件，access.log 访问日志，error.log 错误日志。

## 介绍一下 nginx？
nginx，是一个 Web 服务器和反向代理服务器，用于 HTTP、HTTPS、SMTP、POP3、IMAP 等协议，nginx 的主要功能有 Web 服务器、反向代理、实现负载均衡、虚拟主机。

## nginx 日志格式中的 $time_local 表示的是什么时间？请求开始的时间？请求结束的时间？
$time_local 指的是请求开始的服务器本地时间。

## nginx 优点有哪些？
跨平台、配置简单、非阻塞、内存消耗小、稳定性高。

## nginx 和 haproxy 有什么区别？
haproxy 是基于四层和七层的转发，是专业的代理服务器，nginx 是 WEB 服务器，缓存服务器，又是反向代理服务器，可以做七层的转发，引入TCP插件之后，也可以支持四层的转发。

## nginx 的负载均衡策略？

**轮询（默认）round_robin：**每个请求按时间顺序逐一分配到不同的后端服务器，如果后端服务器 down 掉，能自动剔除。

**IP 哈希 ip_hash：**每个请求按访问 ip 的 hash 结果分配，这样每个访客固定访问一个后端服务器，可以解决 session 共享的问题。当然，实际场景下，一般不考虑使用 ip_hash 解决 session 共享。

**最少连接 least_conn：**下一个请求将被分派到活动连接数量最少的服务器。

通过 nginx 插件，我们还可以引入 fair、url_hash 等负载均衡策略。

## 请解释什么是 C10K 问题？
C10K 问题是指无法同时处理大量客户端(10,000)的网络套接字。

## 解释如何在 nginx 服务器上添加模块？
在编译过程中，必须选择 nginx 模块，因为 nginx 不支持模块的运行时选择。

## 在 nginx 中，如何在 URL 中保留双斜线？
要在 URL 中保留双斜线，就必须使用 merge_slashes_off;
语法：merge_slashes [on/off]
默认值：merge_slashes on

## 请解释 nginx 服务器上的 master 和 worker 进程分别是什么？
master 进程读取及评估配置和维持，worker 进程处理请求。

## 配置上传文件大小限制？
在 server_name 下面添加 client_max_body_size 8M; client_body_buffer_size 8M。
