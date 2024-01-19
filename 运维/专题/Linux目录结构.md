# Linux 目录结构

/boot 引导程序，内核等存放的目录。

/sbin 超级用户可以使用的命令的存放目录。

/bin 普通用户可以使用的命令的存放目录。

/lib 根目录下的所程序的共享库目录。

/dev 设备文件目录。

/home 普通用户的家目录。

/root 用户 root 的 HOME 目录。

/etc 全局的配置文件存放目录。
* /etc/rc 或 /etc/rc.d 或 /etc/rc?.d 启动、或改变运行级时运行的脚本或脚本的目录。
* /etc/passwd 用户数据库。
* /etc/fdprm 软盘参数表，用以说明不同的软盘格式。
* /etc/fstab 指定启动时需要自动安装的文件系统列表，也包括用swapon -a 启用的 swap 区的信息。
* /etc/group 类似 /etc/passwd，包括组的各种数据。
* /etc/inittab `init` 的配置文件。
* /etc/issue 包括用户在登录提示符前的输出信息，通常包括系统的一段短说明或欢迎信息。
* /etc/magic `file` 的配置文件，包含不同文件格式的说明，`file` 基于它猜测文件类型。
* /etc/motd motd 是 message of the day 的缩写，用户成功登录后自动输出，常用于通告信息，如计划关机时间的警告等。
* /etc/mtab 当前安装的文件系统列表，由脚本初始化，并由 mount 命令自动更新。
* /etc/shadow 影子口令文件。
* /etc/login.defs `login` 命令的配置文件。
* /etc/printcap 类似 /etc/termcap，但针对打印机。
* /etc/profile /etc/csh.login、/etc/csh.cshrc 登录或启动时 bourne 或 shells 执行的文件。
* /etc/securetty 确认安全终端，即哪个终端允许超级用户登录。
* /etc/shells 列出可以使用的 shell。
* /etc/termcap 说明不同的终端用什么转义序列控制。

/usr 这个目录中包含了命令库文件和在通常操作中不会修改的文件。

/usr/lib 目标库文件，包括动态连接库加上一些通常不是直接调用的可执行文件的存放位置。

/usr/bin 一般使用者使用并且不是系统自检等所必需可执行文件的目录。

/usr/sbin 管理员使用的非系统必须的可执行文件存放目录。

/usr/share 存放共享文件的目录。

/usr/include C 程序语言编译使用的头文件。

/usr/local 安装本地程序的一般默认路径。

/proc 这个目录采用一种特殊的文件系统格式（proc格式，内核支持这种格式，其中包含了全部虚拟文件。它们并不保存在磁盘中，也不占据磁盘空间(尽管命令ls -c 会显示它们的大小)。当查看它们时，实际上看到的是内存里的信息，这些文件助于我们了解系统内部信息。
