## Go

## 25个关键字

> break, case, chan, const, continue, default, defer, else, fallthrough, for, func, go, goto, if, import, interface, 
> map, package, range, return, select, struct, switch, type, var

## GPM模型

## 注意事项
- 每个可独立运行的go程序都必须有且仅有一个main包，只有package名称为main的源码文件可以包含main函数
- main函数是每一个可执行程序所必须包含的，一般来说都是在启动后第一个执行的函数（如果有init函数则会先执行该函数）
- 块注释不可以嵌套
- 首字母大写的标识符是可导出的，否则是仅包内可见
- 符号{不能单独放在一行
- 文件名和包名没有直接关系，文件夹名和包名没有直接关系，同一个文件夹下的文件只能有一个包名，否则编译报错
- go mod使用本地包的方法，在go.mod文件中加入replace example.com/test/sub =\> ./sub
- 如果要将多条语句写在一行，需要用分号间隔
- v, ok := \<- ch可用于判断通道是否已经关闭
- go的通道底层实现？
- goroutine之间的内存共享程度？
- 关闭带缓冲的通道并不会丢失里面的数据，只是让读取通道数据的时候不会读完之后一直阻塞等待新数据写入
- go程序一般结构
```go
// 当前程序的包名
package main

// 导入其他包
import . "fmt"

// 包别名
import "fmt2" "fmt"

// 常量定义
const PI = 3.14

// 全局变量的声明和赋值
var name = "gopher"

// 一般类型声明
type newType int

// 结构的声明
type gopher struct{}

// 接口的声明
type golang interface{}

// 由main函数作为程序入口点启动
func main() {
    Println("Hello World!")
}
```
- 错误是一个接口，可以通过errors.New("a error")抛出
```go
type error interface {
    Error() string
}
```
- 类型转换，type_name(expression)
- 如果不初始化map，那么就会创建一个nil map，nil map不能用来存放键值对
- 当要将结构体对象转换为JSON时，对象中的属性首字母必须是大写，才能正常转换为JSON
- 跟for循环不一样的地方在于range循环中的x变量是临时变量，range循环只是将值拷贝到x变量中

## 命令行工具
- go run
- go build
- go fmt
- go mod vendor
