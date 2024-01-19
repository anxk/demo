# Keepalived

Keepalived 主要依靠 VRRP 协议（虚拟路由冗余协议）实现 VIP 和 VMAC 的自动漂移，当 Master 发生故障后，会刷新 ARP 表，从而实现高可用。

## 常见使用场景
用来配置 Nginx 的高可用，实现热备。
