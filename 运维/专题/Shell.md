# Shell

## shell 脚本备注

如果要在 shell 脚本 A 中调用另一个 shell 脚本 B 的内容，可以在 A 中对 B 进行source，然后就可以使用 B 中的内容了。

环境变量添加 export key=value。

在父 shell 脚本中加入某一环境变量后，在子 shell 脚本中可以成功获取到该变量。

进行删除文件(夹)操作时要注意检查路径中包含的变量是否会为空，因为这样的话可能会删除根目录。移动文件操作尽量使用 mv，而不是 cp + rm，对于有风险的操作一定先要进行备份。

shell 脚本中赋值等号两端不能有空格。

设置只读变量使用 readonly var。

删除变量 unset var （这种方法不能删除只读变量），删除环境变量也用 unset。

一行内如果只有一个表达式，那么结尾的分号是选择的；如果有多句，句之间分号必须要有，但是最后一句结尾的分号是选择的。

if 语句：if...then..fi / if...then...else...fi / if...then...else if...then...else...fi / if...then...elif...then...fi。

while 语句：while...do...done。

for 语句：for $var in...do...done。

read var 用于读取用户输入。

return 返回值或者 exit 值都只能是整数，不能是字符串等。

shell 中流程控制语句不能有空，如果需要可以使用 : 表示(类似 python 中的 pass 语句)。

$(expression) 或 `expression` 是在子 shell 中执行，执行完后返回。

shell 脚本退出状态最大只能为 255，若超出则取模(除以 256 的余数)。

直接 ./script 形式执行脚本需要有执行权限，但是 sh ./script 形式执行不需要脚本有执行权限。

在赋值的时候值中如果没有空格等字符是不要求必须有引号的，如果有空格等需要引号(单引号中的 $var 不会被解释，双引号中的 $var 会被解释)。

除了在变量赋值或者 for 循环句头中不需要加 $，其它都要加 $。

使用变量用 $var (不必须要用 "$var")，在可能歧义的情况下使用 ${var}。

shell 中变量有环境(全局)变量和局部变量。

单引号中不能用转移字符，双引号中能用转义字符。

单引号中不能再有单引号(无法采用转义字符来添加单引号)。

获取变量值(字符串)长度 ${#var}。

提取变量值(字符串)子串 ${var:start_index:end_index}。

查找变量值(字符串)字符位置 str=hello;echo `expr index $str eh`，会查找 e,h,o 中最先出现的一个的位置，位置从 1 开始计算。

shell 中变量类型都是字符串类型，或者说 shell 中没有变量类型。

数组定义 array=(val1 val2 ...)，也可单独指定 array[1]=var，变量之间分隔符可以是空格或换行符。

访问数组元素 ${array[index]}，数组长度 ${#array[@]} 或 ${#array[*]}，数组中元素的长度 ${#array[index]}。

循环访问数组中元素 for i in ${array[@]};do echo $i;done。

let 用于计算整数运算，变量计算中不需要加上 $ 来表示变量，如果表达式中包含了空格或其他特殊字符，则必须引起来，例如 let 'x = x + 1'，let 中可以使用自增增减或 +-*/%。

test命令。

函数定义可以使用关键字 function，如：function fun() 定义，也可以直接 fun() 或 fun 定义，不带任何参数，函数体的大括号要换行。参数返回，可以 return 返回，如果不加，将以最后一条命令的运行结果作为返回值。

在函数中使用和外部重名变量使要加 local 关键字。

可以认为 shell 中变量定义和赋值是一起的。

shell 中没有浮点，算术运算要通过 let 或 expr 命令实现。

`:(){ :: & };:` Fork Bomb。
