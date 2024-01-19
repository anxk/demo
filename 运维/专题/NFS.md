# NFS

## 一次 NFS 的过程？
- 本地用户要访问 NFS 服务器中文件，先向内核发起请求，内核处理调用 NFS 模块及 rpc client。
- rpc client 向 rpc server 发起连接。
- 在连接之前，NFS 服务除了启动 nfsd 本身监听的端口 2049/tcp 和 2049/udp，还会启动其它进程（如mountd，statd，rquotad等）以完成文件共享，这些进程的端口是不固定的，是每次 NFS 服务启动时向 RPC 服务注册的，RPC 服务会随机分配未使用的端口。
- 完成连接，接受访问请求。
- NFS 应用程序向内核发起请求。
- 内核调用文件系统，然后 client 端通过获取的 NFS 端口来建立和 server 端的 NFS 连接并进行数据的传输。

## 有哪些方法可以提升 NFS 吞吐量？
采用 ext4 文件系统，NFS 的吞吐量会更高。