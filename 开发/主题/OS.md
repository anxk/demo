# OS

## 进程和线程的区别？

## 同步和异步的区别？

## 阻塞和非阻塞的区别？

## Linux 系统调用 fork？

## Linux 进程状态？

D: uninterruptible sleep (usually IO)
R: running or runnable (on run queue)
S: interruptible sleep (waiting for an event to complete)
T: stopped by job control signal
t: stopped by debugger during the tracing
W: paging (not valid since the 2.6.xx kernel)
X: dead (should never be seen)
Z: defunct ("zombie") process, terminated but not - reaped by its parent

## 操作系统常用调度方法?

先来先服务（FCFS, First Come First Service）、最短进程优先(SJF, Short Job First) 、优先级调度、时间片轮转、
高响应比优先调度（响应比=(等待时间+要求服务的时间)/要求服务的时间）、多级反馈队列调度算法。