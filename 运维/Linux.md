# Linux

## Linux
Linux 是 Unix 的一种版本
第一个 Linux 内核 0.0.1 版本于 1991 年 5 月 14 日发布，可以运行在 80386 处理器上，在与 Intel 公司的 PC 兼容的 CPU 系列中，
80386 是第一个真正的 32 位处理器，小版本号是奇数的内核是开发内核，小版本号是偶数的内核是产品内核（major:minor:patch）。
Linux 2.6 版本的进程调度器提供了 O(1) 的调度算法。Linux 遵循 GPL 协议，并不是公共域软件，公共域意味着作者放弃了软件的版权，
但是 Linux 代码的版权仍为代码的各位作者所有。

## 进程状态
D: uninterruptible sleep (usually IO)
R: running or runnable (on run queue)
S: interruptible sleep (waiting for an event to complete)
T: stopped by job control signal
t: stopped by debugger during the tracing
W: paging (not valid since the 2.6.xx kernel)
X: dead (should never be seen)
Z: defunct ("zombie") process, terminated but not - reaped by its parent

## 扩展
- ebpf（bcc-tool/cilium），在拦截的时候通常会使用 readelf 查看库符号
- lfs 从零开始制作Linux
- grub
- device-driver https://lwn.net/Kernel/LDD3/
- 内核模块

## 常用的诊断工具
- hcache 查看cache 
- atopd, bcc, ftrace, trace-cmd, iostat, dstat, iotop, netstat, sar, iftop, htop, top
- dig/nslookup
- ls*命令
- nsenter
- strace
- strings
- nmap
- dmesg

## 工具
- SystemTap
- qemu/kvm/vitualbox/libvirt/openstack
- lvm
- chaosblade
- atop
- rsyslogd
- chronyd
- ntp
- auditd
- sshd
- journald
- systemd
- make
- openssh/openssl

## 性能调优
- sysctl (/etc/sysctl.d/)
- ulimit (系统层面/进程层面cat /proc/PID/limits)
- https://github.com/zeushammer/Preformance-Tune-Linux
- nfs tune
- http://www.admin-magazine.com/HPC/Articles/Useful-NFS-Options-for-Tuning-and-Management
- https://www.slashroot.in/how-do-linux-nfs-performance-tuning-and-optimization
- https://www.slashroot.in/linux-nfs-network-file-system-client-and-server-complete-guide
- https://www.slashroot.in/linux-file-system-read-write-performance-test
- https://www.cyberciti.biz/faq/linux-unix-tuning-nfs-server-client-performance/
- https://docs.microsoft.com/en-us/windows-server/administration/performance-tuning/role/file-server/nfs-file-server
- https://docs.oracle.com/cd/E19620-01/805-4448/index.html
- https://www.ibm.com/support/knowledgecenter/en/ssw_aix_71/com.ibm.aix.performance/nfs_tuning_client.htm
- http://blog.chinaunix.net/uid-70565-id-2070512.html

## 一些技巧
- 清理cache /proc/sys/vm/drop_caches
- 查看/proc/net/nf_conntrack
- 查看进程内存 /proc/PID/maps
- 使用gdb可以讲进程某段地址内存dump出来 
- 利用 {} 的 expand 特性建文件夹，mkdir -pv /tmp/test_mkdir/{boot,root,etc,bin,sbin,lib,var,tmp,usr/{bin,etc,include,lib,local,sbin,share,share,src}}
- ll /dev 可看主次设备号
- mount -o loop 挂载环回设备
- sr0 是 CD-ROM 设备
- :(){ :: & };: Fork Bomb
- 查看 selinux 状态，sestatus 或 getenforce，临时关闭 setenforce 0，恢复 setenforce 1，永久修改 selinux 要配置 /etc/selinux/config
