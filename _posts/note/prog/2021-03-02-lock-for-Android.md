---
layout: post
title: "编程 C++ -- 多平台 lock（include Android）"
author:
location: "珠海"
categories: ["编程"]
tags: ["编程", "C++", "Android"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---


## pthread_mutex_lock

[from](https://pubs.opengroup.org/onlinepubs/7908799/xsh/pthread_mutex_lock.html)

```cpp
#include <pthread.h>

int pthread_mutex_lock(pthread_mutex_t *mutex);
int pthread_mutex_trylock(pthread_mutex_t *mutex);
int pthread_mutex_unlock(pthread_mutex_t *mutex);
```

* 如果互斥锁类型为 **PTHREAD_MUTEX_NORMAL**，则不提供死锁检测。尝试重新锁定互斥锁会导致死锁。
    如果某个线程尝试解除锁定的互斥锁不是由该线程锁定或未锁定，则将产生不确定的行为。
* 如果互斥锁类型为 **PTHREAD_MUTEX_ERRORCHECK**，则会提供错误检查。
    如果某个线程尝试重新锁定的互斥锁已经由该线程锁定，则将返回错误。
    如果某个线程尝试解除锁定的互斥锁不是由该线程锁定或者未锁定，则将返回错误。
* 如果互斥锁类型为 **PTHREAD_MUTEX_RECURSIVE**，则该互斥锁会保留锁定计数这一概念。
    线程首次成功获取互斥锁时，锁定计数会设置为 1。线程每重新锁定该互斥锁一次，锁定计数就增加 1。
    线程每解除锁定该互斥锁一次，锁定计数就减小 1。
    锁定计数达到 0 时，该互斥锁即可供其他线程获取。
    如果某个线程尝试解除锁定的互斥锁不是由该线程锁定或者未锁定，则将返回错误。
* 如果互斥锁类型是 **PTHREAD_MUTEX_DEFAULT**，则尝试以递归方式锁定该互斥锁将产生不确定的行为。
    对于不是由调用线程锁定的互斥锁，如果尝试解除对它的锁定，则会产生不确定的行为。
    如果尝试解除锁定尚未锁定的互斥锁，则会产生不确定的行为。

* 描述 pthread_mutex_lock() 函数锁住由 mutex 指定的 mutex 对象。
    如果 mutex 已经被锁住，调用这个函数的线程阻塞直到 mutex 可用为止。
    这跟函数返回的时候参数 mutex 指定的 mutex 对象变成锁住状态，同时该函数的调用线程成为该 mutex 对象的拥有者。

    * 如果 mutex 对象的 type 是 PTHREAD_MUTEX_NORMAL，不进行 deadlock detection（死锁检测）。
        企图进行 relock 这个 mutex 会导致 deadlock。
        如果一个线程对未加锁的或已经 unlock 的 mutex 对象进行 unlock 操作，结果是不未知的。
    * 如果 mutex 类型是 PTHREAD_MUTEX_ERRORCHECK，那么将进行错误检查。
        如果一个线程企图对一个已经锁住的 mutex 进行 relock，将返回一个错误。
        如果一个线程对未加锁的或已经 unlock 的 mutex 对象进行 unlock 操作，将返回一个错误。
    * 如果 mutex 类型是 PTHREAD_MUTEX_RECURSIVE，mutex 会有一个锁住次数（lock count）的概念。
        当一个线程成功地第一次锁住一个 mutex 的时候，锁住次数（lock count）被设置为 1，
        每一次一个线程 unlock 这个 mutex 的时候，锁住次数（lock count）就减 1。
        当锁住次数（lock count）减少为 0 的时候，其他线程就能获得该 mutex 锁了。
        如果一个线程对未加锁的或已经 unlock 的 mutex 对象进行 unlock 操作，将返回一个错误。
    * 如果 mutex 类型是 PTHREAD_MUTEX_DEFAULT，企图递归的获取这个 mutex 的锁的结果是不确定的。
        unlock 一个不是被调用线程锁住的 mutex 的结果也是不确定的。
        企图 unlock 一个未被锁住的 mutex 导致不确定的结果。

* pthread_mutex_trylock() 调用在参数 mutex 指定的 mutex 对象当前被锁住的时候立即返回，
    除此之外，pthread_mutex_trylock() 跟 pthread_mutex_lock() 功能完全一样。

* pthread_mutex_unlock() 函数释放有参数 mutex 指定的 mutex 对象的锁。如果被释放取决于该 Mutex 对象的类型属性。
    如果有多个线程为了获得该 mutex 锁阻塞，调用 pthread_mutex_unlock() 将是该 mutex 可用，
    一定的调度策略将被用来决定哪个线程可以获得该 mutex 锁。
    （在 mutex 类型为 PTHREAD_MUTEX_RECURSIVE 的情况下，只有当 lock count 减为 0 并且调用线程在该 mutex 上已经没有锁的时候）
    （翻译到这里，才觉得我的这个锁概念是多么模糊）
    如果一个线程在等待一个 mutex 锁得时候收到了一个 signal，那么在从 signal handler 返回的时候，
    该线程继续等待该 mutex 锁，就像这个线程没有被中断一样。
    返回值成功

* pthread_mutex_lock() 和 pthread_mutex_unlock() 返回 0，否则返回一个错误的提示码。
* pthread_mutex_trylock() 在成功获得了一个 mutex 的锁后返回 0，否则返回一个错误提示码错误。
* pthread_mutex_lock() 和 pthread_mutex_unlock() 失败的时候
    * [EINVAL] mutex 在生成的时候，它的 protocol 属性的值是 PTHREAD_PRIO_PROTECT，
        同时调用线程的优先级 (priority) 比该 mutex 的当前 prority 上限高。

* pthread_mutex_trylock() 函数在一下情况会失败：
    * [EBUSY] The mutex could not be acquired because it was already locked. mutex 已经被锁住的时候无法再获取锁。

* The pthread_mutex_lock(), pthread_mutex_trylock() and pthread_mutex_unlock() functions may fail if:
    * [EINVAL] mutex 指向的 mutex 未被初始化。
    * [EAGAIN] Mutex 的 lock count( 锁数量 ) 已经超过 递归索的最大值，无法再获得该 mutex 锁。

* pthread_mutex_lock() 函数在一下情况下会失败：
    * [EDEADLK] 当前线程已经获得该 mutex 锁。

* pthread_mutex_unlock() 函数在以下情况下会失败：
    * [EPERM] 当前线程不是该 mutex 锁的拥有者 所有的这些函数的错误返回值都不会是 [EINTR]。


## 互斥锁

互斥锁用来保证一段时间内只有一个线程在执行一段代码。必要性显而易见：假设各个线程向同一个文件顺序写入数据，最后得到的结果一定是灾难性的。

我们先看下面一段代码。这是一个读 / 写程序，它们公用一个缓冲区，并且我们假定一个缓冲区只能保存一条信息。
即缓冲区只有两个状态：有信息或没有信息。

```cpp
void reader_function ( void );
void writer_function ( void );
pthread_mutex_lock(&android_app->mutex);
pthread_mutex_unlock(&android_app->mutex);
```

```cpp
char buffer;
int buffer_has_item = 0;
pthread_mutex_t mutex;
struct timespec delay;

void main ( void ) {
    pthread_t reader;
    /* 定义延迟时间 */
    delay.tv_sec = 2;
    delay.tv_nec = 0;
    /* 用默认属性初始化一个互斥锁对象 */
    pthread_mutex_init (&mutex,NULL);
    pthread_create(&reader, pthread_attr_default, (void *)&reader_function), NULL);
    writer_function( );
}

void writer_function (void) {
    while (1) {
        /* 锁定互斥锁*/
        pthread_mutex_lock (&mutex);
        if (buffer_has_item == 0) {
            buffer = make_new_item( );
            buffer_has_item = 1;
        }
        /* 打开互斥锁 */
        pthread_mutex_unlock(&mutex);
        pthread_delay_np(&delay);
    }
}

void reader_function(void) {
    while(1) {
        pthread_mutex_lock(&mutex);
        if (buffer_has_item == 1) {
            consume_item(buffer);
            buffer_has_item = 0;
        }
        pthread_mutex_unlock(&mutex);
        pthread_delay_np(&delay);
    }
}
```

这里声明了互斥锁变量 mutex，结构 pthread_mutex_t 为不公开的数据类型，其中包含一个系统分配的属性对象。
函数 pthread_mutex_init 用来生成一个互斥锁。NULL 参数表明使用默认属性。如果需要声明特定属性的互斥锁，须调用函数 pthread_mutexattr_init。
函数 pthread_mutexattr_setpshared 和函数 pthread_mutexattr_settype 用来设置互斥锁属性。
前一个函数设置属性 pshared，它有两个取值，PTHREAD_PROCESS_PRIVATE 和 PTHREAD_PROCESS_SHARED。
前者用来不同进程中的线程同步，后者用于同步本进 程的不同线程。
在上面的例子中，我们使用的是默认属性 PTHREAD_PROCESS_ PRIVATE。
后者用来设置互斥锁类型，可选的类型有 PTHREAD_MUTEX_NORMAL、PTHREAD_MUTEX_ERRORCHECK、PTHREAD_MUTEX_RECURSIVE 和 PTHREAD _MUTEX_DEFAULT。
它们分别定义了不同的上所、解锁机制，一般情况下，选用最后一个默认属性。

pthread_mutex_lock 声明开始用互斥锁上锁，此后的代码直至调用 pthread_mutex_unlock 为止，均被上锁，即同一时间只能被一个线程调用执行。
当一个线程执行到 pthread_mutex_lock 处时，如果该锁此时被另一个线程使用，那此线程被阻塞，即程序将等待到另一个线程释放此互斥锁。
在上面的例子中，我们使用了 pthread_delay_np 函数，让线程睡眠一段时间，就是为了防止一个线程始终占据此函数。

上面的例子非常简单，就不再介绍了，需要提出的是在使用互斥锁的过程中很有可能会出现死锁：
两个线程试图同时占用两个资源，并按不同的次序锁定相应的互 斥锁，
例如两个线程都需要锁定互斥锁 1 和互斥锁 2，a 线程先锁定互斥锁 1，b 线程先锁定互斥锁 2，这时就出现了死锁。
此时我们可以使用函数 pthread_mutex_trylock，它是函数 pthread_mutex_lock 的非阻塞版本，当它发现死锁不可避免时，
它会返回相应的信 息，程序员可以针对死锁做出相应的处理。另外不同的互斥锁类型对死锁的处理不一样，
但最主要的还是要程序员自己在程序设计注意这一点。


## android 自旋锁 spin_lock

```cpp
#include <linux/spinlock.h>

spinlock_t lock;
spin_lock_init(&lock);
spin_lock(&lock);
spin_unlock(&lock);
```


## C++11 mutex 方便的自解锁 lock_guard

[Thread support library](https://en.cppreference.com/w/cpp/thread)

```cpp
std::lock_guard<std::mutex> Lock(SignalMutex);
std::lock_guard<std::mutex> Lock;
lock_guard_type<mutex_type> lock(m_mutex);

#if defined(BOTAN_TARGET_OS_HAS_THREADS)

namespace Botan {

template<typename T> using lock_guard_type = std::lock_guard<T>;
typedef std::mutex mutex_type;

}

#else

// No threads
namespace Botan {

template<typename Mutex>
class lock_guard final
   {
   public:
      explicit lock_guard(Mutex& m) : m_mutex(m)
         { m_mutex.lock(); }

      ~lock_guard() { m_mutex.unlock(); }

      lock_guard(const lock_guard& other) = delete;
      lock_guard& operator=(const lock_guard& other) = delete;
   private:
      Mutex& m_mutex;
   };

class noop_mutex final
   {
   public:
      void lock() {}
      void unlock() {}
   };

typedef noop_mutex mutex_type;
template<typename T> using lock_guard_type = lock_guard<T>;

}

#endif
```


## MutexLock(Mutex& m)

json-3.9.1\benchmarks\thirdparty\benchmark\src 里面的一个实现 mutex.h。

```cpp
MutexLock(Mutex& m) ACQUIRE(m) : ml_(m.native_handle()) {}
```


## std::mutex synopsis

```cpp
namespace std
{

class mutex
{
public:
     constexpr mutex() noexcept;
     ~mutex();

    mutex(const mutex&) = delete;
    mutex& operator=(const mutex&) = delete;

    void lock();
    bool try_lock();
    void unlock();

    typedef pthread_mutex_t* native_handle_type;
    native_handle_type native_handle();
};

class recursive_mutex
{
public:
     recursive_mutex();
     ~recursive_mutex();

    recursive_mutex(const recursive_mutex&) = delete;
    recursive_mutex& operator=(const recursive_mutex&) = delete;

    void lock();
    bool try_lock() noexcept;
    void unlock();

    typedef pthread_mutex_t* native_handle_type;
    native_handle_type native_handle();
};

class timed_mutex
{
public:
     timed_mutex();
     ~timed_mutex();

    timed_mutex(const timed_mutex&) = delete;
    timed_mutex& operator=(const timed_mutex&) = delete;

    void lock();
    bool try_lock();
    template <class Rep, class Period>
        bool try_lock_for(const chrono::duration<Rep, Period>& rel_time);
    template <class Clock, class Duration>
        bool try_lock_until(const chrono::time_point<Clock, Duration>& abs_time);
    void unlock();
};

class recursive_timed_mutex
{
public:
     recursive_timed_mutex();
     ~recursive_timed_mutex();

    recursive_timed_mutex(const recursive_timed_mutex&) = delete;
    recursive_timed_mutex& operator=(const recursive_timed_mutex&) = delete;

    void lock();
    bool try_lock() noexcept;
    template <class Rep, class Period>
        bool try_lock_for(const chrono::duration<Rep, Period>& rel_time);
    template <class Clock, class Duration>
        bool try_lock_until(const chrono::time_point<Clock, Duration>& abs_time);
    void unlock();
};

struct defer_lock_t {};
struct try_to_lock_t {};
struct adopt_lock_t {};

inline constexpr defer_lock_t  defer_lock{};
inline constexpr try_to_lock_t try_to_lock{};
inline constexpr adopt_lock_t  adopt_lock{};

template <class Mutex>
class lock_guard
{
public:
    typedef Mutex mutex_type;

    explicit lock_guard(mutex_type& m);
    lock_guard(mutex_type& m, adopt_lock_t);
    ~lock_guard();

    lock_guard(lock_guard const&) = delete;
    lock_guard& operator=(lock_guard const&) = delete;
};

template <class... MutexTypes>
class scoped_lock // C++17
{
public:
    using mutex_type = Mutex;  // If MutexTypes... consists of the single type Mutex

    explicit scoped_lock(MutexTypes&... m);
    scoped_lock(adopt_lock_t, MutexTypes&... m);
    ~scoped_lock();
    scoped_lock(scoped_lock const&) = delete;
    scoped_lock& operator=(scoped_lock const&) = delete;
private:
    tuple<MutexTypes&...> pm; // exposition only
};

template <class Mutex>
class unique_lock
{
public:
    typedef Mutex mutex_type;
    unique_lock() noexcept;
    explicit unique_lock(mutex_type& m);
    unique_lock(mutex_type& m, defer_lock_t) noexcept;
    unique_lock(mutex_type& m, try_to_lock_t);
    unique_lock(mutex_type& m, adopt_lock_t);
    template <class Clock, class Duration>
        unique_lock(mutex_type& m, const chrono::time_point<Clock, Duration>& abs_time);
    template <class Rep, class Period>
        unique_lock(mutex_type& m, const chrono::duration<Rep, Period>& rel_time);
    ~unique_lock();

    unique_lock(unique_lock const&) = delete;
    unique_lock& operator=(unique_lock const&) = delete;

    unique_lock(unique_lock&& u) noexcept;
    unique_lock& operator=(unique_lock&& u) noexcept;

    void lock();
    bool try_lock();

    template <class Rep, class Period>
        bool try_lock_for(const chrono::duration<Rep, Period>& rel_time);
    template <class Clock, class Duration>
        bool try_lock_until(const chrono::time_point<Clock, Duration>& abs_time);

    void unlock();

    void swap(unique_lock& u) noexcept;
    mutex_type* release() noexcept;

    bool owns_lock() const noexcept;
    explicit operator bool () const noexcept;
    mutex_type* mutex() const noexcept;
};

template <class Mutex>
  void swap(unique_lock<Mutex>& x, unique_lock<Mutex>& y) noexcept;

template <class L1, class L2, class... L3>
  int try_lock(L1&, L2&, L3&...);
template <class L1, class L2, class... L3>
  void lock(L1&, L2&, L3&...);

struct once_flag
{
    constexpr once_flag() noexcept;

    once_flag(const once_flag&) = delete;
    once_flag& operator=(const once_flag&) = delete;
};

template<class Callable, class ...Args>
  void call_once(once_flag& flag, Callable&& func, Args&&... args);

}  // std
```

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relrefx.html url="/assets/reviewjs/blogs/2021-03-02-lock-for-Android.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://pubs.opengroup.org/onlinepubs/7908799/xsh/pthread_mutex_lock.html]({% include relrefx.html url="/backup/2021-03-02-lock-for-Android.md/pubs.opengroup.org/717c42d5.html" %})
- [https://en.cppreference.com/w/cpp/thread]({% include relrefx.html url="/backup/2021-03-02-lock-for-Android.md/en.cppreference.com/1f71b663.html" %})
