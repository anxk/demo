## Spring

## 为什么要使用spring？
spring提供ioc技术，容器会帮你管理依赖的对象，从而不需要自己创建和管理依赖对象了，更轻松的实现了程序的解耦。spring提供了事务支持，使得事务操作变的更加方便。spring提供了面向切片编程，这样可以更方便的处理某一类的问题。更方便的框架集成，spring可以很方便的集成其他框架，比如MyBatis等。

## 解释一下什么是aop？
aop是面向切面编程，通过预编译方式和运行期动态代理实现程序功能的统一维护的一种技术。简单来说就是统一处理某一“切面”问题的编程思想，比如统一处理日志、异常等。

## 解释一下什么是 ioc？
ioc：Inversionof Control（中文：控制反转）是spring的核心，对于spring框架来说，就是由spring来负责控制对象的生命周期和对象间的关系。简单来说，控制指的是当前对象对内部成员的控制权；控制反转指的是，这种控制权不由当前对象管理了，由其他（类，第三方容器）来管理。

## spring 有哪些主要模块？
spring core：框架的最基础部分，提供ioc和依赖注入特性；
spring context：构建于core封装包基础上的context封装包，提供了一种框架式的对象访问方法；
spring dao：Data Access Object 提供JDBC的抽象层；
spring aop：提供了面向切面的编程实现，让你可以自定义拦截器、切点等；
spring Web：提供了针对Web开发的集成特性，例如文件上传，利用servlet listeners进行ioc容器初始化和针对Web的 ApplicationContext；
spring Web mvc：spring中的mvc封装包提供了Web应用的Model-View-Controller（MVC）的实现；

## spring实现aop的方式？
主要是基于动态代理，CGLIB和Java原生的动态代理。

## spring 常用的注入方式有哪些？
setter属性注入，构造方法注入，注解方式注入。

## spring中的bean是线程安全的吗？
spring中的bean默认是单例模式，spring框架并没有对单例bean进行多线程的封装处理。实际上大部分时候spring bean无状态的（比如dao类），所以某种程度上来说bean也是安全的，但如果bean有状态的话（比如view model对象），那就要开发者自己去保证线程安全了，最简单的就是改变bean的作用域，把“singleton”变更为“prototype”，这样请求bean相当于new Bean()了，所以就可以保证线程安全了。有状态就是有数据存储功能，无状态就是不会保存数据。

## spring支持几种bean的作用域？
spring支持5种作用域，如下：
singleton：spring ioc容器中只存在一个bean实例，bean以单例模式存在，是系统默认值（使用 prototype 作用域需要慎重的思考，因为频繁创建和销毁 bean 会带来很大的性能开销。）；
prototype：每次从容器调用bean时都会创建一个新的示例，既每次getBean()相当于执行new bean()操作；
Web环境下的作用域：
request：每次http请求都会创建一个bean；
session：同一个http session共享一个bean实例；
global-session：用于portlet容器，因为每个portlet有单独的session，globalsession提供一个全局性的http session；

## spring自动装配bean有哪些方式？
no：默认值，表示没有自动装配，应使用显式bean引用进行装配；
byName：它根据bean的名称注入对象依赖项；
byType：它根据类型注入对象依赖项；
构造函数：通过构造函数来注入依赖项，需要设置大量的参数；
autodetect：容器首先通过构造函数使用autowire装配，如果不能，则通过byType自动装配；

## spring事务实现方式有哪些？
声明式事务：声明式事务也有两种实现方式，基于xml配置文件的方式和注解方式（在类上添加@Transaction注解）；
编码方式：提供编码的形式管理和维护事务；

## 说一下 spring mvc 运行流程？
spring mvc 先将请求发送给 DispatcherServlet；
DispatcherServlet 查询一个或多个 HandlerMapping，找到处理请求的 Controller；
DispatcherServlet 再把请求提交到对应的 Controller；
Controller 进行业务逻辑处理后，会返回一个ModelAndView；
Dispathcher 查询一个或多个 ViewResolver 视图解析器，找到 ModelAndView 对象指定的视图对象；
视图对象负责渲染返回给客户端；

## spring mvc 有哪些组件？
前置控制器 DispatcherServlet；
映射控制器 HandlerMapping；
处理器 Controller；
模型和视图 ModelAndView；
视图解析器 ViewResolver；

## @RequestMapping 的作用是什么？
将http请求映射到相应的类/方法上。

## @Autowired 的作用是什么？
@Autowired它可以对类成员变量、方法及构造函数进行标注，完成自动装配的工作，通过@Autowired的使用来消除set/get方法。

## 什么是 spring boot？
spring boot是为spring服务的，是用来简化新spring应用的初始搭建以及开发过程的。

## 为什么要用spring boot？
配置简单，独立运行，自动装配，无代码生成和xml配置，提供应用监控，易上手，提升开发效率。

## spring boot核心配置文件是什么？
spring boot核心的两个配置文件：
bootstrap (. yml 或者 . properties)：boostrap由父ApplicationContext加载的，比applicaton优先加载，且boostrap里面的属性不能被覆盖；
application (. yml 或者 . properties)：用于 spring boot 项目的自动化配置。

## spring boot 配置文件有哪几种类型？它们有什么区别？
配置文件有 . properties 格式和 . yml 格式，它们主要的区别是书法风格不同。. yml 格式不支持 @PropertySource 注解导入。

## spring boot有哪些方式可以实现热部署？
使用devtools启动热部署，添加devtools库，在配置文件中把spring. devtools. restart. enabled设置为true；
使用Intellij Idea编辑器，勾上自动编译或手动重新编译。

## jpa和hibernate有什么区别？
jpa全称Java Persistence API，是Java持久化接口规范，hibernate属于jpa的具体实现。

## 什么是 spring cloud？
spring cloud是一系列框架的集合，它利用spring boot的开发便利性巧妙地简化了分布式系统基础设施的开发，如服务发现注册、配置中心、消息总线、负载均衡、断路器、数据监控等，都可以用spring boot的开发风格做到一键启动和部署。

## spring cloud 断路器的作用是什么？
在分布式架构中，断路器模式的作用也是类似的，当某个服务单元发生故障（类似用电器发生短路）之后，通过断路器的故障监控（类似熔断保险丝），向调用方返回一个错误响应，而不是长时间的等待。这样就不会使得线程因调用故障服务被长时间占用不释放，避免了故障在分布式系统中的蔓延。

## spring cloud 的核心组件有哪些？
Eureka：服务注册于发现。
Feign：基于动态代理机制，根据注解和选择的机器，拼接请求 url 地址，发起请求。
Ribbon：实现负载均衡，从一个服务的多台机器中选择一台。
Hystrix：提供线程池，不同的服务走不同的线程池，实现了不同服务调用的隔离，避免了服务雪崩的问题。
Zuul：网关管理，由 Zuul 网关转发请求给对应的服务。
