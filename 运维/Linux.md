# Linux

## Linux
Linux是Unix的一种版本
第一个Linux内核0.0.1版本于1991年5月14日发布，可以运行在80386处理器上，在与Intel公司的PC兼容的CPU系列中，80386是第一个真正的32位处理器
小版本号是奇数的内核是开发内核，小版本号是偶数的内核是产品内核（major:minor:patch）
Linux 2.6版本的进程调度器提供了O(1)的调度算法
Linux遵循GPL协议，并不是公共域软件，公共域意味着作者放弃了软件的版权，但是Linux代码的版权仍为代码的各位作者所有

## 进程状态
D: uninterruptible sleep (usually IO)
R: running or runnable (on run queue)
S: interruptible sleep (waiting for an event to complete)
T: stopped by job control signal
t: stopped by debugger during the tracing
W: paging (not valid since the 2.6.xx kernel)
X: dead (should never be seen)
Z: defunct ("zombie") process, terminated but not - reaped by its parent

## 命令行工具
- hcache 查看cache 
- openssh/openssl

## 扩展
- ebpf（bcc-tool/cilium）
- lfs 从零开始制作Linux
- grub
- device-driver https://lwn.net/Kernel/LDD3/
- 内核模块

## 工具
- SystemTap

## 性能调优
- sysctl (/etc/sysctl.d/)
- ulimit (系统层面/进程层面cat /proc/PID/limits)

## 技巧
- 清理cache /proc/sys/vm/drop_caches
- 查看/proc/net/nf_conntrack
- 查看进程内存 /proc/PID/maps
- 使用gdb可以讲进程某段地址内存dump出来 
