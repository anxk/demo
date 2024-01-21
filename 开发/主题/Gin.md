# Gin

## 路由

### 路由原理

Gin 框架中的路由使用的是 [httprouer](https://github.com/julienschmidt/httprouter) 这个库，其基本原理就是构造一个路由地址的前缀树。

### 路由种类

普通路由和分组路由。

## 中间件

### 简单描述一下中间件？

Gin 框架允许开发者在处理请求的过程中，加入用户自己的钩子（Hook）函数。这个钩子函数就叫中间件，中间件适合处理一些公共的业务逻辑，比如登录校验、日志打印、耗时统计等。（责任链模式）

### 中间件分为哪几种？

中间件可以注册为全局的，也可以注册为单个路由或者路由组的。

## 使用细节

### Gin 框架中怎么实现参数校验？

在 `struct` 结构体 添加 `binding` 标签，然后调用 `ShouldBind` 方法解析参数。

### Gin 框架响应请求方式有哪几种？

- 字符串:  `c.String(http.StatusOK, "hello world")` 
- JSON 格式:  `c.JSON(http.StatusOK, gin.H{})`

### Gin 框架中 `Gin.H` 代表什么意思？

`gin.H` 实际上就是 `map[string]interface{}`，引入 `gin.H` 可以简化生成 JSON 的方式，`gin.H` 可以嵌套使用。

