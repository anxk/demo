# Java

## Java 

* JUnit5, TestNG, Selenide, Allure Report, Selenium Grid2
* Maven / Gradle
* Servlet / Stapler
* Guava / Apache Commons / caffeine
* Free Marker
* Agent / JDK 动态代理 / CGLIB 代理 / 字节码技术 / Javaassist / ASM
* javac / javap / scripting / java / javaprof / javah
* JMX / jconsole / CRaSH
* 性能优化
* SPI / 插件机制
* 容器

## Spring

* Spring Cloud Config
* Spring Cloud Bus
* Spring Cloud Eureka
* Spring Boot Actuator
* Spring Security
* Spring Boot
* Spring MVC
* Spring Retry
* AOP
* Feign

## 八股文

### JDK和JRE有什么区别
JDK：Java Development Kit的简称，Java开发工具包，提供了Java的开发环境和运行环境，JRE：Java Runtime Environment的简称，
Java运行环境，为Java的运行提供了所需环境。具体来说 JDK 其实包含了 JRE，同时还包含了编译 Java 源码的编译器 Javac，还包含了很多 
Java 程序调试和分析的工具，简单来说：如果你需要运行 Java 程序，只需安装 JRE 就可以了，如果你需要编写 Java 程序，需要安装 JDK

### ==和equals的区别
对于基本类型和引用类型 == 的作用效果是不同的，基本类型比较的是值是否相同，引用类型比较的是引用是否相同。equals 本质上就是 ==，
只不过 String 和 Integer 等重写了 equals 方法，把它变成了值比较，Object中equals的定义为：
```java
public boolean equals(Object obj) {
    return (this == obj);
}
```

### 两个对象的hashCode()相同，则equals()也一定为true，对吗
不对，两个对象的hashCode()相同，equals()不一定true

### final在Java中有什么作用
final修饰的类叫最终类，该类不能被继承
final修饰的方法不能被重写
final修饰的变量叫常量，常量必须初始化，初始化之后值就不能被修改

### Java中的Math. round(-1.5)等于多少
等于-1，因为在数轴上取值时，中间值（0.5）向右取整，所以正0.5是往上取整，负0.5是直接舍弃

### String属于基础的数据类型吗
不属于基础类型，基础类型有8种：byte、boolean、char、short、int、float、long、double，而String属于对象

### Java中操作字符串都有哪些类？它们之间有什么区别
操作字符串的类有：String、StringBuffer、StringBuilder。
String和StringBuffer、StringBuilder的区别在于String声明的是不可变的对象，每次操作都会生成新的String对象，
然后将指针指向新的String对象，而StringBuffer、StringBuilder可以在原有对象的基础上进行操作，
所以在经常改变字符串内容的情况下最好不要使用String。StringBuffer和StringBuilder最大的区别在于，StringBuffer是线程安全的，
而StringBuilder是非线程安全的，但 StringBuilder的性能高于StringBuffer，所以在单线程环境下推荐使用StringBuilder，
多线程环境下推荐使用StringBuffer

### String str="i"与String str=new String("i")一样吗
不一样，因为内存的分配方式不一样，String str="i"，Java虚拟机会将其分配到常量池中，而String str=new String("i")则会被分到堆内存中
```java
String a = "xx";
String b = "xx";
String c = new String("xx"); // 堆上分配
System.out.println(a == b); // true
System.out.println(a == c); // false
```

### 如何将字符串反转
使用StringBuilder或者StringBuffer的reverse()方法

###	String类的常用方法都有那些
indexOf()：返回指定字符的索引
charAt()：返回指定索引处的字符
replace()：字符串替换
trim()：去除字符串两端空白
split()：分割字符串，返回一个分割后的字符串数组
getBytes()：返回字符串的byte类型数组
length()：返回字符串长度
toLowerCase()：将字符串转成小写字母
toUpperCase()：将字符串转成大写字符
substring()：截取字符串
equals()：字符串比较

###	抽象类必须要有抽象方法吗
不需要，抽象类不一定非要有抽象方法

###	普通类和抽象类有哪些区别
普通类不能包含抽象方法，抽象类可以包含抽象方法
抽象类不能直接实例化，普通类可以直接实例化

###	抽象类能使用 final 修饰吗
不能，定义抽象类就是让其他类继承的，如果定义为final该类就不能被继承，这样彼此就会产生矛盾，所以final不能修饰抽象类

###	接口和抽象类有什么区别
实现：抽象类的子类使用 extends 来继承；接口必须使用 implements 来实现接口
构造函数：抽象类可以有构造函数；接口不能有
实现数量：类可以实现很多个接口；但是只能继承一个抽象类
访问修饰符：接口中的方法默认使用 public 修饰；抽象类中的方法可以是任意访问修饰符

###	Java 中 IO 流分为几种
按功能来分：输入流（input）、输出流（output）
按类型来分：字节流和字符流
字节流和字符流的区别是：字节流按8位传输以字节为单位输入输出数据，字符流按 16 位传输以字符为单位输入输出数据

###	BIO、NIO、AIO 有什么区别
BIO：Block IO同步阻塞式IO，就是我们平常使用的传统IO，它的特点是模式简单使用方便，并发处理能力低
NIO：Non IO同步非阻塞IO，是传统IO的升级，客户端和服务器端通过Channel（通道）通讯，实现了多路复用
AIO：Asynchronous IO是NIO的升级，也叫NIO2，实现了异步非堵塞IO，异步IO的操作基于事件和回调机制

###	Files的常用方法都有哪些
Files. exists()：检测文件路径是否存在
Files. createFile()：创建文件
Files. createDirectory()：创建文件夹
Files. delete()：删除一个文件或目录
Files. copy()：复制文件
Files. move()：移动文件
Files. size()：查看文件个数
Files. read()：读取文件
Files. write()：写入文件

###	Java容器都有哪些
Java容器分为Collection和Map两大类，其下又有很多子类，如下所示
Collection
List
ArrayList
LinkedList
Vector
Stack
Set
HashSet
LinkedHashSet
TreeSet
Map
HashMap
LinkedHashMap
TreeMap
ConcurrentHashMap
Hashtable

###	Collection和Collections有什么区别
Collection 是一个集合接口，它提供了对集合对象进行基本操作的通用接口方法，所有集合都是它的子类，比如 List、Set 等
Collections 是一个包装类，包含了很多静态方法，不能被实例化，就像一个工具类，比如提供的排序方法： Collections. sort(list)

###	HashMap 和 Hashtable 有什么区别
存储：HashMap 运行 key 和 value 为 null，而 Hashtable 不允许。
线程安全：Hashtable 是线程安全的，而 HashMap 是非线程安全的。
推荐使用：在 Hashtable 的类注释可以看到，Hashtable 是保留类不建议使用，推荐在单线程环境下使用 HashMap 替代，如果需要多线程使用则用 ConcurrentHashMap 替代

###	如何决定使用 HashMap 还是 TreeMap
对于在 Map 中插入、删除、定位一个元素这类操作，HashMap 是最好的选择，因为相对而言 HashMap 的插入会更快，但如果你要对一个 key 集合进行有序的遍历，那 TreeMap 是更好的选择

###	说一下 HashMap 的实现原理
HashMap 基于 Hash 算法实现的，我们通过 put(key,value)存储，get(key)来获取。当传入 key 时，HashMap 会根据 key.hashCode() 计算出 
hash 值，根据 hash 值将 value 保存在 bucket 里。当计算出的 hash 值相同时，我们称之为 hash 冲突，HashMap 的做法是用链表和红黑树存
储相同 hash 值的 value。当 hash 冲突的个数比较少时，使用链表否则使用红黑树

###	说一下 HashSet 的实现原理
HashSet 是基于 HashMap 实现的，HashSet 底层使用 HashMap 来保存所有元素，因此 HashSet 的实现比较简单，相关 HashSet 的操作，
基本上都是直接调用底层 HashMap 的相关方法来完成，HashSet 不允许重复的值

###	ArrayList 和 LinkedList 的区别是什么
数据结构实现：ArrayList 是动态数组的数据结构实现，而 LinkedList 是双向链表的数据结构实现
随机访问效率：ArrayList 比 LinkedList 在随机访问的时候效率要高，因为 LinkedList 是线性的数据存储方式，所以需要移动指针从前往后依次查找
增加和删除效率：在非首尾的增加和删除操作，LinkedList 要比 ArrayList 效率要高，因为 ArrayList 增删操作要影响数组内的其他数据的下标
综合来说，在需要频繁读取集合中的元素时，更推荐使用 ArrayList，而在插入和删除操作较多时，更推荐使用 LinkedList

###	如何实现数组和 List 之间的转换
数组转 List：使用 Arrays. asList(array) 进行转换
List 转数组：使用 List 自带的 toArray() 方法

###	ArrayList 和 Vector 的区别是什么
线程安全：Vector 使用了 Synchronized 来实现线程同步，是线程安全的，而 ArrayList 是非线程安全的
性能：ArrayList 在性能方面要优于 Vector
扩容：ArrayList 和 Vector 都会根据实际的需要动态的调整容量，只不过在 Vector 扩容每次会增加 1 倍，而 ArrayList 只会增加 50%

###	Array 和 ArrayList 有何区别
Array 可以存储基本数据类型和对象，ArrayList 只能存储对象
Array 是指定固定大小的，而 ArrayList 大小是自动扩展的
Array 内置方法没有 ArrayList 多，比如 addAll、removeAll、iteration 等方法只有 ArrayList 有

###	在 Queue 中 poll()和 remove()有什么区别
相同点：都是返回第一个元素，并在队列中删除返回的对象
不同点：如果没有元素 poll()会返回 null，而 remove()会直接抛出 NoSuchElementException 异常

###	哪些集合类是线程安全的
Vector、Hashtable、Stack 都是线程安全的，而像 HashMap 则是非线程安全的，不过在 JDK 1.5 之后随着 Java.util.concurrent 并发包的出现，
它们也有了自己对应的线程安全类，比如 HashMap 对应的线程安全类就是 ConcurrentHashMap

###	迭代器 Iterator 是什么
Iterator 接口提供遍历任何 Collection 的接口。我们可以从一个 Collection 中使用迭代器方法来获取迭代器实例。迭代器取代了 Java 
集合框架中的 Enumeration，迭代器允许调用者在迭代过程中移除元素

###	Iterator 怎么使用？有什么特点
Iterator 使用代码如下：
List<String> list = new ArrayList<>();
Iterator<String> it = list. iterator();
while(it. hasNext()){
  String obj = it. next();
  System. out. println(obj);
}
Iterator 的特点是更加安全，因为它可以确保，在当前遍历的集合元素被更改的时候，就会抛出 ConcurrentModificationException 异常

###	Iterator 和 ListIterator 有什么区别
Iterator 可以遍历 Set 和 List 集合，而 ListIterator 只能遍历 List。
Iterator 只能单向遍历，而 ListIterator 可以双向遍历（向前/后遍历）。
ListIterator 从 Iterator 接口继承，然后添加了一些额外的功能，比如添加一个元素、替换一个元素、获取前面或后面元素的索引位置。

###	怎么确保一个集合不能被修改
可以使用 Collections. unmodifiableCollection(Collection c) 方法来创建一个只读集合，这样改变集合的任何操作都会抛出
Java.lang.UnsupportedOperationException 异常。示例代码如下：
List<String> list = new ArrayList<>();
list. add("x");
Collection<String> clist = Collections. unmodifiableCollection(list);
clist. add("y"); // 运行时此行报错
System. out. println(list. size());

###	并行和并发有什么区别
并行：多个处理器或多核处理器同时处理多个任务
并发：多个任务在同一个 CPU 核上，按细分的时间片轮流(交替)执行，从逻辑上来看那些任务是同时执行

###	线程和进程的区别
一个程序下至少有一个进程，一个进程下至少有一个线程，一个进程下也可以有多个线程来增加程序的执行速度

###	守护线程是什么
守护线程是运行在后台的一种特殊进程。它独立于控制终端并且周期性地执行某种任务或等待处理某些发生的事件。在 Java 中垃圾回收线程就是特殊的守护线程。

###	创建线程有哪几种方式
创建线程有三种方式：
继承 Thread 重写 run 方法；
实现 Runnable 接口；
实现 Callable 接口。

###	说一下 runnable 和 callable 有什么区别
runnable 没有返回值，callable 可以拿到有返回值，callable 可以看作是 runnable 的补充。

###	线程有哪些状态
线程的状态：
NEW 尚未启动
RUNNABLE 正在执行中
BLOCKED 阻塞的（被同步锁或者IO锁阻塞）
WAITING 永久等待状态
TIMED_WAITING 等待指定的时间重新被唤醒的状态
TERMINATED 执行完成

###	sleep() 和 wait() 有什么区别
类的不同：sleep() 来自 Thread，wait() 来自 Object
释放锁：sleep() 不释放锁；wait() 释放锁
用法不同：sleep() 时间到会自动恢复；wait() 可以使用 notify()/notifyAll()直接唤醒

###	notify()和 notifyAll()有什么区别
notifyAll()会唤醒所有的线程，notify()之后唤醒一个线程。notifyAll() 调用后，会将全部线程由等待池移到锁池，然后参与锁的竞争，
竞争成功则继续执行，如果不成功则留在锁池等待锁被释放后再次参与竞争。而 notify()只会唤醒一个线程，具体唤醒哪一个线程由虚拟机控制

###	线程的 run() 和 start() 有什么区别
start() 方法用于启动线程，run() 方法用于执行线程的运行时代码。run() 可以重复调用，而 start() 只能调用一次

###	创建线程池有哪几种方式
线程池创建有七种方式，最核心的是最后一种：
newSingleThreadExecutor()：它的特点在于工作线程数目被限制为 1，操作一个无界的工作队列，所以它保证了所有任务的都是被顺序执行，最多会有一个任务处于活动状态，并且不允许使用者改动线程池实例，因此可以避免其改变线程数目；
newCachedThreadPool()：它是一种用来处理大量短时间工作任务的线程池，具有几个鲜明特点：它会试图缓存线程并重用，当无缓存线程可用时，就会创建新的工作线程；如果线程闲置的时间超过 60 秒，则被终止并移出缓存；长时间闲置时，这种线程池，不会消耗什么资源。其内部使用 SynchronousQueue 作为工作队列；
newFixedThreadPool(int nThreads)：重用指定数目（nThreads）的线程，其背后使用的是无界的工作队列，任何时候最多有 nThreads 个工作线程是活动的。这意味着，如果任务数量超过了活动队列数目，将在工作队列中等待空闲线程出现；如果有工作线程退出，将会有新的工作线程被创建，以补足指定的数目 nThreads；
newSingleThreadScheduledExecutor()：创建单线程池，返回 ScheduledExecutorService，可以进行定时或周期性的工作调度；
newScheduledThreadPool(int corePoolSize)：和newSingleThreadScheduledExecutor()类似，创建的是个 ScheduledExecutorService，可以进行定时或周期性的工作调度，区别在于单一工作线程还是多个工作线程；
newWorkStealingPool(int parallelism)：这是一个经常被人忽略的线程池，Java 8 才加入这个创建方法，其内部会构建ForkJoinPool，利用Work-Stealing算法，并行地处理任务，不保证处理顺序；
ThreadPoolExecutor()：是最原始的线程池创建，上面1-3创建方式都是对ThreadPoolExecutor的封装。

###	线程池都有哪些状态
RUNNING：这是最正常的状态，接受新的任务，处理等待队列中的任务。
SHUTDOWN：不接受新的任务提交，但是会继续处理等待队列中的任务。
STOP：不接受新的任务提交，不再处理等待队列中的任务，中断正在执行任务的线程。
TIDYING：所有的任务都销毁了，workCount 为 0，线程池的状态在转换为 TIDYING 状态时，会执行钩子方法 terminated()。
TERMINATED：terminated()方法结束后，线程池的状态就会变成这个。

###	线程池中 submit() 和 execute() 方法有什么区别
execute()：只能执行 Runnable 类型的任务。
submit()：可以执行 Runnable 和 Callable 类型的任务。
Callable 类型的任务可以获取执行的返回值，而 Runnable 执行无返回值。

###	在 Java 程序中怎么保证多线程的运行安全
方法一：使用安全类，比如 Java. util. concurrent 下的类。
方法二：使用自动锁 synchronized。
方法三：使用手动锁 Lock。
手动锁 Java 示例代码如下：

###	多线程中 synchronized 锁升级的原理是什么
synchronized 锁升级原理：在锁对象的对象头里面有一个 threadid 字段，在第一次访问的时候 threadid 为空，jvm 让其持有偏向锁，并将 threadid 设置为其线程 id，再次进入的时候会先判断 threadid 是否与其线程 id 一致，如果一致则可以直接使用此对象，如果不一致，则升级偏向锁为轻量级锁，通过自旋循环一定次数来获取锁，执行一定次数之后，如果还没有正常获取到要使用的对象，此时就会把锁从轻量级升级为重量级锁，此过程就构成了 synchronized 锁的升级。
锁的升级的目的：锁升级是为了减低了锁带来的性能消耗。在 Java 6 之后优化 synchronized 的实现方式，使用了偏向锁升级为轻量级锁再升级到重量级锁的方式，从而减低了锁带来的性能消耗。

###	什么是死锁
当线程 A 持有独占锁a，并尝试去获取独占锁 b 的同时，线程 B 持有独占锁 b，并尝试获取独占锁 a 的情况下，就会发生 AB 两个线程由于互相持有对方需要的锁，而发生的阻塞现象，我们称为死锁。

###	怎么防止死锁
尽量使用 tryLock(long timeout, TimeUnit unit)的方法(ReentrantLock、ReentrantReadWriteLock)，设置超时时间，超时可以退出防止死锁。尽量使用 Java. util. concurrent 并发类代替自己手写锁。尽量降低锁的使用粒度，尽量不要几个功能用同一把锁。尽量减少同步的代码块。

###	ThreadLocal 是什么？有哪些使用场景
ThreadLocal 为每个使用该变量的线程提供独立的变量副本，所以每一个线程都可以独立地改变自己的副本，而不会影响其它线程所对应的副本。ThreadLocal 的经典使用场景是数据库连接和 session 管理等。

###	说一下 synchronized 底层实现原理
synchronized 是由一对 monitorenter/monitorexit 指令实现的，monitor 对象是同步的基本实现单元。在 Java 6 之前，monitor 的实现完全是依靠操作系统内部的互斥锁，因为需要进行用户态到内核态的切换，所以同步操作是一个无差别的重量级操作，性能也很低。但在 Java 6 的时候，Java 虚拟机 对此进行了大刀阔斧地改进，提供了三种不同的 monitor 实现，也就是常说的三种不同的锁：偏向锁（Biased Locking）、轻量级锁和重量级锁，大大改进了其性能。

###	synchronized 和 volatile 的区别是什么
volatile 是变量修饰符；synchronized 是修饰类、方法、代码段。
volatile 仅能实现变量的修改可见性，不能保证原子性；而 synchronized 则可以保证变量的修改可见性和原子性。
volatile 不会造成线程的阻塞；synchronized 可能会造成线程的阻塞。

###	synchronized和Lock有什么区别
synchronized 可以给类、方法、代码块加锁；而 lock 只能给代码块加锁。
synchronized 不需要手动获取锁和释放锁，使用简单，发生异常会自动释放锁，不会造成死锁；而 lock 需要自己加锁和释放锁，如果使用不当没有 unLock()去释放锁就会造成死锁。
通过 Lock 可以知道有没有成功获取锁，而 synchronized 却无法办到。

###	synchronized和ReentrantLock区别是什么
synchronized早期的实现比较低效，对比ReentrantLock，大多数场景性能都相差较大，但是在Java 6中对synchronized进行了非常多的改进。
主要区别如下：
ReentrantLock使用起来比较灵活，但是必须有释放锁的配合动作；
ReentrantLock必须手动获取与释放锁，而synchronized不需要手动释放和开启锁；
ReentrantLock只适用于代码块锁，而synchronized可用于修饰方法、代码块等。
volatile标记的变量不会被编译器优化，synchronized标记的变量可以被编译器优化。

###	说一下 atomic 的原理
atomic主要利用CAS (Compare And Wwap)和volatile和native法来保证原子操作，从而避免synchronized的高开销，执行效率大为提升。

###	什么是反射
反射是在运行状态中，对于任意一个类，都能够知道这个类的所有属性和方法；对于任意一个对象，都能够调用它的任意一个方法和属性；这种动态获取的信息以及动态调用对象的方法的功能称为Java语言的反射机制。

###	什么是Java序列化？什么情况下需要序列化
Java序列化是为了保存各种对象在内存中的状态，并且可以把保存的对象状态再读出来。
以下情况需要使用 Java 序列化：
想把的内存中的对象状态保存到一个文件中或者数据库中时候；
想用套接字在网络上传送对象的时候；
想通过RMI（远程方法调用）传输对象的时候；

###	动态代理是什么？有哪些应用
动态代理是运行时动态生成代理类。

###	怎么实现动态代理
JDK原生动态代理和cglib动态代理，JDK原生动态代理是基于接口实现的，而cglib是基于继承当前类的子类实现的。

###	为什么要使用克隆
克隆的对象可能包含一些已经修改过的属性，而new出来的对象的属性都还是初始化时候的值，所以当需要一个新的对象来保存当前对象的“状态”就靠克隆方法了。

###		如何实现对象克隆
实现Cloneable接口并重写Object 类中的clone()方法。
实现Serializable接口，通过对象的序列化和反序列化实现克隆，可以实现真正的深度克隆。

###	深拷贝和浅拷贝区别是什么
浅克隆：当对象被复制时只复制它本身和其中包含的值类型的成员变量，而引用类型的成员对象并没有复制；
深克隆：除了对象本身被复制外，对象所包含的所有成员变量也将复制；

###	如何避免SQL注入
使用预处理PreparedStatement或使用正则表达式过滤掉字符中的特殊字符。

###	throw和throws的区别
throw：是真实抛出一个异常。
throws：是声明可能会抛出一个异常。

###	final、finally、finalize 有什么区别
final：是修饰符，如果修饰类，此类不能被继承；如果修饰方法和变量，则表示此方法和此变量不能在被改变，只能使用；
finally：是try{} catch{} finally{}最后一部分，表示不论发生任何情况都会执行，finally部分可以省略，但如果finally部分存在，则一定会执行finally里面的代码；
finalize：是Object类的一个方法，在垃圾收集器执行的时候会调用被回收对象的此方法；

###	try-catch-finally 中哪个部分可以省略
try-catch-finally其中catch和finally都可以被省略，但是不能同时省略，也就是说有try的时候，必须后面跟一个catch或者finally。

###	try-catch-finally中，如果catch中return了，finally还会执行吗
finally一定会执行，即使是catch中return了，catch中的return会等finally中的代码执行完之后，才会执行。

###	常见的异常类有哪些
NullPointerException 空指针异常
ClassNotFoundException 指定类不存在
NumberFormatException 字符串转换为数字异常
IndexOutOfBoundsException 数组下标越界异常
ClassCastException 数据类型转换异常
FileNotFoundException 文件未找到异常
NoSuchMethodException 方法不存在异常
IOException IO异常
SocketException Socket 异常
JVM

###	说一下 JVM 的主要组成部分？及其作用
类加载器（ClassLoader）
运行时数据区（Runtime Data Area）
执行引擎（Execution Engine）
本地库接口（Native Interface）
组件的作用： 首先通过类加载器（ClassLoader）会把 Java 代码转换成字节码，运行时数据区（Runtime Data Area）再把字节码加载到内存中，而字节码文件只是 JVM 的一套指令集规范，并不能直接交给底层操作系统去执行，因此需要特定的命令解析器执行引擎（Execution Engine），将字节码翻译成底层系统指令，再交由 CPU 去执行，而这个过程中需要调用其他语言的本地库接口（Native Interface）来实现整个程序的功能。

###	说一下 JVM 运行时数据区
不同虚拟机的运行时数据区可能略微有所不同，但都会遵从 Java 虚拟机规范， Java 虚拟机规范规定的区域分为以下 5 个部分：
程序计数器（Program Counter Register）：当前线程所执行的字节码的行号指示器，字节码解析器的工作是通过改变这个计数器的值，来选取下一条需要执行的字节码指令，分支、循环、跳转、异常处理、线程恢复等基础功能，都需要依赖这个计数器来完成；
Java 虚拟机栈（Java Virtual Machine Stacks）：用于存储局部变量表、操作数栈、动态链接、方法出口等信息；
本地方法栈（Native Method Stack）：与虚拟机栈的作用是一样的，只不过虚拟机栈是服务 Java 方法的，而本地方法栈是为虚拟机调用 Native 方法服务的；
Java 堆（Java Heap）：Java 虚拟机中内存最大的一块，是被所有线程共享的，几乎所有的对象实例都在这里分配内存；
方法区（Methed Area）：用于存储已被虚拟机加载的类信息、常量、静态变量、即时编译后的代码等数据。

###	说一下堆栈的区别
功能方面：堆是用来存放对象的，栈是用来执行程序的；
共享性：堆是线程共享的，栈是线程私有的；
空间大小：堆大小远远大于栈；

###	什么是双亲委派模型
在介绍双亲委派模型之前先说下类加载器。对于任意一个类，都需要由加载它的类加载器和这个类本身一同确立在JVM中的唯一性，每一个类加载器，都有一个独立的类名称空间。类加载器就是根据指定全限定名称将class文件加载到JVM内存，然后再转化为class对象。
启动类加载器（Bootstrap ClassLoader）：是虚拟机自身的一部分，用来加载JAVA_HOME/lib/目录，或者被-Xbootclasspath参数所指定的路径中并且被虚拟机识别的类库；
扩展类加载器（Extension ClassLoader）：负责加载JAVA_HOME\lib\ext目录或Java.ext.dirs系统变量指定的路径中的所有类库；
应用程序类加载器（Application ClassLoader）：负责加载用户类路径（classpath）上的指定类库，我们可以直接使用这个类加载器，一般情况，如果我们没有自定义类加载器默认就是用这个加载器。
双亲委派模型：如果一个类加载器收到了类加载的请求，它首先不会自己去加载这个类，而是把这个请求委派给父类加载器去完成，每一层的类加载器都是如此，这样所有的加载请求都会被传送到顶层的启动类加载器中，只有当父加载无法完成加载请求（它的搜索范围中没找到所需的类）时，子加载器才会尝试去加载类。

###	说一下类装载的执行过程
类装载分为以下5个步骤：
加载：根据查找路径找到相应的class文件然后导入；
检查：检查加载的class文件的正确性；
准备：给类中的静态变量分配内存空间；
解析：虚拟机将常量池中的符号引用替换成直接引用的过程，符号引用就理解为一个标示，而在直接引用直接指向内存中的地址；
初始化：对静态变量和静态代码块执行初始化工作。

###	怎么判断对象是否可以被回收
引用计数器：为每个对象创建一个引用计数，有对象引用时计数器+1，引用被释放时计数-1，当计数器为0时就可以被回收，它有一个缺点不能解决循环引用的问题；
可达性分析：从GC Roots开始向下搜索，搜索所走过的路径称为引用链，当一个对象到GC Roots没有任何引用链相连时，则证明此对象是可以被回收的；

###	Java中都有哪些引用类型
强引用：发生gc的时候不会被回收；
软引用：有用但不是必须的对象，在发生内存溢出之前会被回收；
弱引用：有用但不是必须的对象，在下一次GC时会被回收；
虚引用（幽灵引用/幻影引用）：无法通过虚引用获得对象，用PhantomReference实现虚引用，虚引用的用途是在gc时返回一个通知；

###	说一下JVM有哪些垃圾回收算法
标记-清除算法：标记无用对象，然后进行清除回收，缺点：效率不高，无法清除垃圾碎片；
标记-整理算法：标记无用对象，让所有存活的对象都向一端移动，然后直接清除掉端边界以外的内存；
复制算法：按照容量划分二个大小相等的内存区域，当一块用完的时候将活着的对象复制到另一块上，然后再把已使用的内存空间一次清理掉，缺点：内存使用率不高，只有原来的一半；
分代算法：根据对象存活周期的不同将内存划分为几块，一般是新生代和老年代，新生代基本采用复制算法，老年代采用标记整理算法；

###	说一下 JVM 有哪些垃圾回收器
Serial：最早的单线程串行垃圾回收器；
Serial Old：Serial垃圾回收器的老年版本，同样也是单线程的，可以作为CMS垃圾回收器的备选预案；
ParNew：是Serial的多线程版本；
Parallel：和ParNew收集器类似，是多线程的，但Parallel是吞吐量优先的收集器，可以牺牲等待时间换取系统的吞吐量；
Parallel Old：是Parallel老生代版本，Parallel使用的是复制的内存回收算法，Parallel Old使用的是标记-整理的内存回收算法；
CMS：一种以获得最短停顿时间为目标的收集器，非常适用B/S系统；
G1：一种兼顾吞吐量和停顿时间的GC实现，是JDK 9以后的默认GC选项；

###	详细介绍一下 CMS 垃圾回收器
CMS是英文Concurrent Mark-Sweep的简称，是以牺牲吞吐量为代价来获得最短回收停顿时间的垃圾回收器。对于要求服务器响应速度的应用上，这种垃圾回收器非常适合。在启动JVM的参数加上“-XX:+UseConcMarkSweepGC”来指定使用CMS垃圾回收器。CMS使用的是标记-清除的算法实现的，所以在gc的时候回产生大量的内存碎片，当剩余内存不能满足程序运行要求时，系统将会出现Concurrent Mode Failure，临时CMS会采用Serial Old回收器进行垃圾清除，此时的性能将会被降低。

###	新生代垃圾回收器和老生代垃圾回收器都有哪些？有什么区别
新生代回收器：Serial、ParNew、Parallel Scavenge
老年代回收器：Serial Old、Parallel Old、CMS
整堆回收器：G1
新生代垃圾回收器一般采用的是复制算法，复制算法的优点是效率高，缺点是内存利用率低；老年代回收器一般采用的是标记-整理的算法进行垃圾回收。

###	简述分代垃圾回收器是怎么工作的
分代回收器有两个分区：老生代和新生代，新生代默认的空间占比总空间的 1/3，老生代的默认占比是 2/3。新生代使用的是复制算法，新生代里有 3 个分区：Eden、To Survivor、From Survivor，它们的默认占比是 8:1:1，它的执行流程如下：
把 Eden + From Survivor 存活的对象放入 To Survivor 区；
清空 Eden 和 From Survivor 分区；
From Survivor 和 To Survivor 分区交换，From Survivor 变 To Survivor，To Survivor 变 From Survivor。
每次在 From Survivor 到 To Survivor 移动时都存活的对象，年龄就 +1，当年龄到达 15（默认配置是 15）时，升级为老生代。大对象也会直接进入老生代。
老生代当空间占用到达某个值之后就会触发全局垃圾收回，一般使用标记整理的执行算法。以上这些循环往复就构成了整个分代垃圾回收的整体执行流程。

###	说一下 JVM 调优的工具
JDK 自带了很多监控工具，都位于 JDK 的 bin 目录下，其中最常用的是 jconsole 和 jvisualvm 这两款视图监控工具。
jconsole：用于对 JVM 中的内存、线程和类等进行监控；
jvisualvm：JDK 自带的全能分析工具，可以分析：内存快照、线程快照、程序死锁、监控内存的变化、gc 变化等。

###	常用的 JVM 调优的参数都有哪些
-Xms2g：初始化推大小为2g；
-Xmx2g：堆最大内存为2g；
-XX:NewRatio=4：设置年轻的和老年代的内存比例为1:4；
-XX:SurvivorRatio=8：设置新生代Eden和Survivor比例为 8:2；
-XX:+UseParNewGC：指定使用ParNew + Serial Old垃圾回收器组合；
-XX:+UseParallelOldGC：指定使用ParNew + ParNew Old垃圾回收器组合；
-XX:+UseConcMarkSweepGC：指定使用CMS + Serial Old垃圾回收器组合；
-XX:+PrintGC：开启打印gc信息；
-XX:+PrintGCDetails：打印gc详细信息；
