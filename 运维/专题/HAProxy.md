# HAProxy

HAProxy 可以做四层和七层的转发，是专业的代理服务器

## HAProxy 负载均衡策略非常多，常见的有如下8种
- roundrobin，表示简单的轮询
- static-rr，表示根据权重
- leastconn，表示最少连接者先处理
- source，表示根据请求的源 IP，类似 Nginx 的 IP_hash 机制
- ri，表示根据请求的 URI
- rl_param，表示根据 HTTP 请求头来锁定每一次 HTTP 请求
- rdp-cookie(name)，表示根据据 cookie(name) 来锁定并哈希每一次 TCP 请求
