---
layout: post
title: "编程与调试 C++ -- 模板编程"
author:
location: "珠海"
categories: ["编程与调试"]
tags: ["编程", "C/C++"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---

模板是泛型编程的基础，泛型编程即以一种独立于任何特定类型的方式编写代码。

模板是创建泛型类（结构体）、函数以及模板常量（C++11）的蓝图或公式。库容器，比如迭代器和算法，都是泛型编程的例子，它们都使用了模板的概念。

每个容器都有一个单一的定义，比如 **向量** ，我们可以定义许多不同类型的向量，比如 `vector <int>` 或 `vector <string>` 。

这里着重声明一下，模板是在编译期完成的，想要熟悉模板编程，一定要不厌其烦的学会代入，只有将模板参数代码，
才能更好的去理解模板编程，尤其是标准库中模板。

接下来让我们一起来看看如何使用。


## 模板常用关键字

模板编程常用用到的关键字：
```
template、typename、class、constexpr、static_assert、auto、decltype、using
template、typename、class 自不用说，模板编程最常用的东西，后面部分 C++ 新提出来的，
又或者是相对比较有深度的东西，其中 using 其实和 typedef 差不多，
区别在于 using 更方便，且可以在类外进行模板类型定义，后续具体阐述。
```


## 模板参数

不管是模板函数还是模板类，都有模板参数，看似简单还是有些道道在里面的。
```cpp
template<typename Type = int>
Type func()
{
}

template<typename _Ty, typename _Alloc = std::allocator<_Ty>>
class vector
{
    ...
}
```

模板参数的写法如下：
```cpp
typename[class] Type = DefaultType
```

其中 DefaultType 是缺省模板参数，它与函数的缺省参数类似，可以写，也可以不写。
另外 Type 也是可以缺省的。
例如：
```cpp
template<typename Type, typename = std::enable_if_t<std::is_pod<Type>>>
Type func() {}
```
这种写法通常是为验证前一个参数，在 C++11 以前是用其它方法验证的，如下所示：
```cpp
template<typename Type>
std::enable_if_t<std::is_pod<Type, Type>> func(){}
```
两种写法意思都是差不多。其中
```cpp
std::enalbe_if_t<std::is_pod<Type>>
```
当 Type 是 pod 类型是 \<==\> void 否则是空的。代入原函数就变成（假定 A 不是 POD 类型），
```cpp
template<typename Type = A, typename = >
Type func(){}
```
可以看出语法根本不对。
同样返回值也是类似，你可以返回 void，但是至少需要写返回值，类型不匹配时，连返回值都没有
自然编译器会报错，报错之前，因为模板重载的缘故，会在编译器尝试寻找别的可替代函数。


## 模板模板参数（Template Template）

模板模板参数，就是模板参数仍然是模板，例如：
```cpp
template<typename T, template<typename> typename container = std::vector>
void func(const container<T>& con)
{
}
```

模板模板参数定义比较简单，只需要在 typename 之间加上 `template<typename...>`
这里说明两点：
1. 上述写法是错误的。
2. 如果是函数的定义，还有其它写法，也能达到实际的效果。

错误的原因是：std::vector 并不只有一个模板参数，上诉申明会报错。
应该写成：
```cpp
template<typename T, template<typename, typename> container = std::vector>
void func(const container<T, std::allocator<T> >& con)
{
}
```

其它写法如下：
```cpp
template<typename T, typename container>
void func(const container& t)
{
}
```

好吧，上诉写法仍然是错的。
`func(std::list<int>())` 显然会报错，因为无法推导出 T。
所以可以写成：
```cpp
template<typename container, typename T = typename Container::value_type>
void func(const Container& con)
{
}
```

这里是假定 Container 中定义了 value_type 这个类型，
事实上标准库的容器，都在内部定义了 value_type，因为是假定，所以需要写成
`typename Container::value_type`

当然这是建立在标准库的容器下，如果是第三方库实现的容器，例如 Qt 库中的容器。
容器类，并没有定义 value_type，同样模板参数也没有 \_Alloc 这个参数，显然这个模板函数
就不适用了，那么该如下实现呢？

可以使用重载
```cpp
template<typename T, template<typename> typename Container>
void func(const Container<T>& con)
{
    // dosomething weith con.
}

template<typename T, typename Alloc,
    template<typename, typename> typename Container>
void func(const Container<T, Alloc>& con)
{
    // dosomething weith con.
}
```

暂没有什么好的方式，让这两份代码，变成一份。


## 模板函数

```cpp
template<typename Type>
void func(Type type)
{
}
```

上面是模板函数简单用法，需要注意的是模板函数其实跟函数重载有很大关系，函数重载有一个概念叫做自动推导，
就是根据输入参数自动推导参数类型，找关联性最强的的函数，同样模板函数也可以完成自动推导，且不要写模板参数。例如上诉函数，可以直接写成：
```cpp
func(1);
func(1.3);
func('a');
// ...
```


## 模板类（结构体）

```cpp
template<typename Type>
struct TempClass
{
};
```

类没有重载的概念，但是类有特化与偏特化的概念。


## 模板变量

```cpp
// only function types and reference types can't be const qualified
template <class _Ty>
constexpr bool is_function_v = !is_const_v<const _Ty> && !is_reference_v<_Ty>;
```

这里有一个知识点，就是只有引用类型和函数类型不能加 const 修饰，也不是说不能加，是加了没用。
可是仔细琢磨这句话，总感觉哪里不对，引用类型不能加 const 修饰？
我们经常写函数成：
```cpp
void func(const A& a);
```
这不是 const 引用吗？

其实这就又要说到运算符归并优先级（这里不是运算符，但同样有一个归并优先级）。
实际上 `const A& a` \<==\> `(const A)& a`  而不是 `const (A&) a` ，实际不能这样加括号哈。
我们可以这样验证。
```cpp
typedef (const A) constA;
constA& a = 3;
typedef (A&) ARef;
const ARef a = 3; // 报错， a 是 A& 类型，无法用常量赋值。
```

简单的说 ARef 用 const 修饰是没有用的， 修饰了也是 ARef，右值引用也是同样的。
这里的函数，仅仅是指类成员函数和全局函数，跟其它仿函数无关。


## 模板特化

其中模板函数没有偏特化，只有全特化，且全特化也是多余的，因为函数重载的原因，全特化和偏特化基本没什么用处。例如：
```cpp
template<typename T>
void func(const T& t)
{
}

// 重载版本
void func(const int&)
{
}

// 特化版本
template<>
void func<int>(const int&)
{
}
```

总感觉特化版本是多余的，个人不清楚他们有啥区别。
模板函数之所以没有偏特化，个人感觉完全就是因为函数有重载的概念。
不需要偏特化。
例如：
```cpp
template<typename Func>
static void bind(typename QtPrivate::FunctionPointer<Func>::Object* receiver,
    Func func)
{
}

template<typename Func>
static void bind(QObject* receiver, Func func)
{
}
```

这里表示，如果第二个参数是类成员函数，且第一个参数是该类的成员对象指针，则适配第一个函数
否则会适配第二个。

所以后续说的全特化和偏特化都是针对类的讲解。


## 全特化与偏特化

先上例子：
```cpp
template<typename T, typename U>
class TempA
{
};

// 偏特化
template<typename T>
class TempA<T, int>
{
};

// 全特化
template<>
class TempA<int, double>
{
};
```

其实类的特化处理，大部分用在 Traits 上，能见到的其它例子，只有 std::atomic，其实类的特化压根也不需要区分偏特化和全特化，
意思差不多，只是区分有没有全部参数进行特化。
上述中，可以看到，特化一个参数，少一个模板参数，特化一定会减少参数吗？并不是哈，特化还是有可能增加参数的。
例如：
```cpp
template<typename T>
class TempB
{
};

template<typename T, typename U>
class TempB<std::pair<T, U>>
{
};
```


## 模板参数包

模板参数包就是 ...，省略号在 C++ 中，分别应用在函数的不定参数，宏的不定参数，以及模板参数包。
例如：
```cpp
template<int eType, typename ...Args>
class KCustomEvent : public QEvent
{
public:

    enum { ArgumentCount = sizeof...(Args) };
    using Arguments = QtPrivate::List<Args...>;
    using TupleData = std::tuple<Args...>;
    using Function = std::function<void(Args...)>;

    template<typename Object>
    using MemberFunction = void(Object::*)(Args...);

    using IndexesList = typename QtPrivate::Indexes<sizeof...(Args)>::Value;
    static constexpr QEvent::Type EventType = (QEvent::Type)eType;
};
```

模板参数包是 C++11 新推出的玩意，模板参数和 sizeof 之间的配合为：
```cpp
sizeof...(Args) // <==> Args 参数的个数。
```

模板参数包与特化组合有一定的特殊性，直接上例子：
```cpp
template <bool _First_value, class _First, class... _Rest>
struct _Conjunction
{ // handle false trait or last trait
    using type = _First;
};

template <class _True, class _Next, class... _Rest>
struct _Conjunction<true, _True, _Next, _Rest...>
{ // the first trait is true, try the next one
    using type = typename _Conjunction<_Next::value, _Next, _Rest...>::type;
};
```

所有的特化版本，为优先匹配版本，如果参数个数，或者类型匹配不上时，才会使用默认版本。
那么这里有一个问题，就是是模板参数在类中的省略号如何使用？参考如下代码：
```cpp
template<int ...Indexes, typename ...Args>
inline void KDataPack::_pack(IndexTuple<Indexes...>, const Args & ...args)
{
    int a[] = { (_packOne<Indexes>(args), 0)... }; // 不赋值会被优化
    Q_UNUSED(a);
}
```

这个函数的意思，挨个打包参数。

```cpp
int a = (void, 0); // a == 0, 逗号运算符就是取最后一个表达式值为返回结果
int b[] = { (void, 0), (void, 0)} // b <==> {0, 1}
因此下面声明一个数组 a, 目的在于执行前一个表达式。
对于 _pack(IndexTupe, "abc", 1, 2.5} 的函数体为
{
    int a[] = { (_packOne<0>("abc"), 0),
                (_packOne<1>(1), 0),
                (_packOne<2>(2.5), 0)};
}
```

可以看出类中的省略号就是逗号运算符的省略，我暂没有用到使用省略号错误的情况，且用且注意吧，除了在函数中或者类中使用省略号，
还可以使用递归的方案，但既然有方便的使用手法，那还是使用方便的手法。


## std::tuple 和 std::index_sequence

这两货都是模板参数包的衍生产物。
`std::tuple<double, int>` \<==\> `std::pair<double, int>` 类似
区别在于 `std::tuple` 支持任意模板参数个数。
而 `std::index_sequence` 是真正在编译期才需要的东西，而且和模板参数包高度结合。

那么 `std::tuple` 和 `std::index_sequence` 如何和模板参数包联合进行应用呢？参考如下代码：
现在我们要封装一个如下的类：
这个类的意义了将函数调用反过来，众所周知，函数有入参和返回值，入参不同，返回值不同，也就是可理解入参为函数的可变参数，
随着参数变化，返回值进行变化，但实际上，函数本身也已作为可变参之一，例如：
```cpp
int func1(int x)
{
    return x;
}
int func2(int x)
{
    return 2 * x;
}
int func3(int x)
{
    return x * x;
}
```

现在要实现一个类，先固定参数，然后传入函数，获得返回值。函数声明如下：
```cpp
template<typename ...Args>
class Argments
{
public:

    Argments(const Args& ...args)
        :m_args(std::make_tuple(args...))
    {
    }

    template<typename Func>
    void call(Func func)
    {
        func(std::get<Args>(args)...);
    }

private:
    std::tuple<Args...>  m_args;
}
```

从上面可以看出，可以使用 std::tuple 用于存储模板参数包中的参数，使用 std::get<Args>(args) 提取 std::tuple
中的数据，但实际上上诉代码是有问题的。例如：
```cpp
Argments<int, int> arg(3, 4);
arg.call([](int a, int b)
{
    std::cout << a + b << std::endl;
});
// 输出的结果是 6，这是因为 std::tuple<int, int> a = {3, 4};
// std::get<int>(a) === 3
```

tuple 中如果有相同类型，根据类型获取参数，是不可行的，但是 std::tuple 还提供另外一种方法获取参数，就是根据下标获取。
```cpp
std::get<0>(a); == 3
std::get<1>(a); == 4
```

那现在问题又来了，怎么将 Args... 转换为 0,1,2... 呢？
这就是 std::index_sequence 的作用了。
```cpp
index_sequence_for<Args...>  <==> std::index_sequence<0...>
```
举例说明：
```cpp
index_sequence_for<int, double, int, char> <==> std::index_sequence<0, 1, 2, 3>
```

基于这个原理，重新实现 Argments 如下：
```cpp
template<typename ...Args>
class Argments
{
public:

    using IndexS = std::index_sequence_for<Args...>;
    Argments(const Args& ...args)
        :m_args(std::make_tuple(args...))
    {

    }

    // 更优化的版本应该要推导函数的返回值，这里只是简化版本
    template<typename Func>
    void call(Func func)
    {
        _call(IndexS(), func);
    }

    template<typename Func, int...Indexes>
    void _call(std::index_sequence<Indexes...>, Func func)
    {
        func(std::get<Indexes>(m_args)...);
    }

private:
    std::tuple<Args...>  m_args;
}
```

至于 std::index_sequence 的实现，标准库没有给出完整定义。下面我给出 Qt 库定义的 index_sequence
```cpp
template<class T> using InvokeGenSeq = typename T::Type;

template<int...> struct IndexesList { using Type = IndexesList; };

template<int N, class S1, class S2> struct ConcatSeqImpl;

template<int N, int... I1, int... I2>
struct ConcatSeqImpl<N, IndexesList<I1...>, IndexesList<I2...>>
    : IndexesList<I1..., (N + I2)...>{};

template<int N, class S1, class S2>
using ConcatSeq = InvokeGenSeq<ConcatSeqImpl<N, S1, S2>>;

template<int N> struct GenSeq;
template<int N> using makeIndexSequence = InvokeGenSeq<GenSeq<N>>;

template<int N>
struct GenSeq : ConcatSeq<N/2, makeIndexSequence<N/2>,
    makeIndexSequence<N - N/2>>{};

template<> struct GenSeq<0> : IndexesList<>{};
template<> struct GenSeq<1> : IndexesList<0>{};

template<int N>
struct Indexes { using Value = makeIndexSequence<N>; };

// 理解难度非常大，自行代入拆解，还是很好理解的。
```


## 优先级


### 函数

全局函数和成员函数因为有重载和自动推导的缘故，因此函数是无所谓特化的，即便是全特化版本，
它和普通的函数是没啥太大区别的，目前仅仅知道，全特化版本一定写在模板函数的后面，普通函数随便写在哪儿，
那么函数调用优先级如何呢？先参考例子。
```cpp
template<typename T>
void func(const T&)                 // ----(1)
{
    std::cout << "const T&" << std::endl;
}

template<typename T>
void func(const std::vector<T>&)    // ----(2)
{
    std::cout << "vector<T>" << std::endl;
}

template<>
void func<int>(const int&)          // ----(3)
{
    std::cout << "int<>" << std::endl;
}

void func(const int)                // ----(4)
{
    std::cout << "int" << std::endl;
}

template<typename T>
void func(T t)                      // ----(5)
{
    std::cout << "T" << std::endl;
}
```

首先需要弄清楚，函数重载的优先级，如果两个函数形成重载，那么编译器会优先考虑最准确的版本，如果有两个版本准确度一样，
那么，不好意思，编译会报错：
```
error C2668: "func": 对重载函数的调用不明确。
```

所以上述定义的 5 个函数中，其中第一个和第五个会冲突，第三个和第四个冲突，那么函数重载的调用优先级不管是不是模板，
优先级仍然是按照重载的优先级，找最匹配的版本，剔除版本（3）和（5）。
1. 普通函数（非模板函数，参数类型一致时，无隐式转换的那种精确匹配）
    func(3) 调用的是（4），func(3.1) 调用的（1）。
2. 模板函数，参数匹配度最高的那种
    func(std::vector\<int\>()) 调用是（2）。
3. 如果匹配度一致，则会报错，当然匹配度一致，不仅仅只是上面说到的这两种情况。其它情况这里不罗列。


## 类（结构体）

类没有重载，但是有特化版本，其实类的特化版本与函数重载有点类似，仍然是找最合适的特化版本（匹配度最高的版本），
如果匹配度一致，仍然会报错。仍然是上例子：
```cpp
template<typename T>        //----(1)
struct TempA : std::integral_constant<int, 1> {};

template<typename C, typename T> //----(2)
struct TempA<std::pair<C, T>> : std::integral_constant<int, 2> {};

template<typename T>        //----(3)
struct TempA<std::pair<T, T>> : std::integral_constant<int, 3> {};

template<typename T>        //----(4)
struct TempA<std::pair<T, int>> : std::integral_constant<int, 4> {};
```

如下调用：
```cpp
TempA<int>::value;                          // 1)
TempA<std::pair<int, double>>::value;       // 2)
TempA<std::pair<double, double>>::value;    // 3)
TempA<std::pair<double, int>>::value;       // 4)
TempA<std::pair<int, int>>::value;          //Error, 3 和 4 无法抉择
```

类的优先级，仍然只有一个原则，仍然是匹配度最高的那个。
1. 特化版本中，找匹配度最高的
2. 如果特化版本中，一个都没匹配上，就使用非特化版本。


## 模板元编程

说着说着模板编程，这里变成模板元编程，这是因为模板元编程是模板编程的进阶版本，据说已证明模板元编程是图灵完备的，自行 Google **图灵完备** 。

模版元编程（template metaprogram）是 C++ 中最复杂也是威力最强大的编程范式，它是一种可以创建和操纵程序的程序。
模版元编程完全不同于普通的运行期程序，它很独特，因为模版元程序的执行完全是在编译期，并且模版元程序操纵的数据不能是运行时变量，
只能是编译期常量，不可修改，另外它用到的语法元素也是相当有限，不能使用运行期的一些语法，比如 if-else，for 等语句都不能用。
因此，模版元编程需要很多技巧，常常需要类型重定义、枚举常量、继承、模板偏特化等方法来配合，因此编写模版元编程比较复杂也比较困难。

可以参考标准库的 type_traits，它的手法非常单一，就是通过类特化，对类型进行重定义或者定义编译器常量等等。例如：
```cpp
template<typename T>
struct IsDouble
{
    static constexpr bool value = false;
};

template<>
struct IsDouble<double>
{
    static constexpr bool value = true;
};

// 又或者
template<typename T>
struct remove_reference
{
    using type = T;
};

template<typename T>
struct remove_reference<T&>
{
    using type = T;
};

template<typename T>
struct remove_reference<T&&>
{
    using type = T;
};
```

基本手法就是通过偏特化，进行组合、继承等，下面介绍标准库的几个模板元函数和类。


## integral_constant

具体实现如下：
```cpp
template<class _Ty, _Ty _Val>
struct integral_constant
{
    static constexpr _Ty value = _Val;

    // 下面这些代码都是多余，核心就上面这一行代码
    // 一行代码就是很特性表述的核心
    using value_type = _Ty;
    using type = integral_constant;

    constexpr operator value_type() const noexcept{
        return value;
    }
    _NODISCARD constexpr value_type operator()()const noexcept{
        return value;
    }
}
```

例如：
```cpp
integral_constant<size_t, 0>;
integral_constant<int, 2>;

integral_constant<bool, true>;
integral_constant<bool, false>;

// 上面都是类型，不要把他们理解为变量，bool 是最常用的，标准库给出如下定义：
using true_type = integral_constant<bool, true>;
using false_type = integral_constant<bool, false>;

// 那么上面提到的 IsDouble 的实现可以改为：
template<typename _Ty>
struct IsDouble : false_type;
template<>
struct IsDouble<double> : true_type;

// 标准库还有一个 is_same 的定义：
template<class, class>
struct is_same : false_type;

template<class _Ty>
struct is_same<_Ty, _Ty> : true_type;

// 基于 is_same 实现 IsDouble 如下：
template<typename _Ty>
using IsDouble = is_same<_Ty, double>;
```

那么总结而言，这是在结构体（类）中定义编译器常量的方式，结合模板特化，组合不一样编译器常量：
```cpp
is_same<double, int>::value;     // false
is_same<int, int>::value;        // true
IsDouble<int>::value;            // false
// 核心仍然里面的编译器常量值，C++11 多出一个模板常量的概念，其实就是为了方便取值。
// 因此定义如下：

template <typename _Ty1, typename _Ty2>
const bool is_same_v<_Ty1, _Ty2> = is_same<_Ty1, _Ty2>::value;

// 当然我们还可以反过来，先定义模板常量，再定义模板类：
template <typename, typename>
constexpr bool is_same_v = false;

template <typename _Ty>
constexpr bool is_same_v<_Ty, _Ty> = true;

// 然后在定义 is_same
template<typename _Ty1, typename _Ty2>
struct is_same : integral_constant<bool, is_same_v<_Ty1, _Ty2>>;
```


## enable_if

先看定义：
```cpp
template<bool _Test, class _Ty = void>
struct enable_if{};

template<class _Ty>
struct enable_if<true, _Ty>{
    using type = Ty;
};
// 这是定义类型，和定义编译器常量走的两条路线，这里可以看出
// 特化版本定义 type 类型， 那么：
enable_if<false, void>::type; // error, 没有定义 type
enable_if<true, void>::type;  // <==> void
// 虽然用了第一个，会报错，但是用在模板函数重载时，未必会报错
// 因为模板函数重载，检验不正确，会尝试用其它的，例如 :

template<typename Ty>
enalbe_if<IsDouble<Ty>::value, void>::type func()
{
};

func<double>(); // 正确
func<int>(); // 错误

// 但是如果再定义下面的函数
template<typename Ty>
std::enable_if<is_same<Ty, int>::value, void>::type func()
{
}
func<int>(); // 正确，它再尝试第一个失败时，会尝试别的。

// 也可在模板参数中验证
template<typename Ty, typename = std::enable_if_t<is_same_v<Ty,int>>>
void func()
{
}

// 又或者写成，标准库基本是下面这种写法
template<typename Ty, std::enable_if_t<is_same_v<Ty, int>, int> = 0>
void func()
{
}
```


## conditional

先看实现：
```cpp
template<bool _Test, class _Ty1, class _Ty2>
struct conditional {
    using type = _Ty1;
}

template<class _Ty1, class _Ty2>
struct conditional<false, _Ty1, _Ty2>{
    using type = _Ty2;
}
// 这个是条件分支
std::conditional<true, int, double>::type;     // int
std::conditional<false, int, double>::type;    // double

// 这么一说，可能看出它的作用，参考以下代码：
template<int Index, typename T>
inline void KDataPack::_packOne(const T& arg)
{
    using DT = std::decay<T>::type; // 这个行代码的主要目的是将 char [] ==> char*
    std::conditional_t<std::is_enum<DT>::value, _Enum<Index, DT>,
        std::conditional_t<_CanConstruct<DT>::value, _Constuct<Index, DT>,
        std::conditional_t<std::is_pointer<DT>::value, _GuidAdpater<Index, DT>,
        std::conditional_t<has_member_kpack<DT, KDataPack>::value, _Convert_Inner<Index, DT>,
        std::conditional_t<has_overload_globalPack<DT,KDataPack>::value, _Convert<Index, DT>,
        std::conditional_t<has_overload_stream<DT>::value, _Convert_Stream<Index, DT>,
        _Error_Convert<Index, DT>>>>>>>::_pack((DT)arg, *this);
}

// 如果是枚举类型，使用 _Enum<Index, DT>::_pack 进行参数打包
// 如果是可以用 QVariant 构造的类型，则用 _Construct<Index, DT>::_pack 进行参数打包
// 如果是指针类型，则用 _GuidAdapter<Index,DT>::_pack 进行参数打包
// 如果 DT 有成员函数 kpack， 则用 _Convert_Inner<Index, DT>::_pack 进行参数打包
// 如果由重载 DT 全局函数 globalPack, 则用 _Convert<Index,DT>::_pack 进行参数打包
// 如果 Dt 有重载流运算 QDataStream.operator<<, 则用 _Convert_Stream<Index, DT>::_Pack 打包
// 否则用兜底的 _Error_Convert<index, DT>::_pack, 内部会直接报错。
```

那么问题来了，可否用模板函数重载完成上诉代码呢？ 可以，但是比较复杂，因为上面的这几个条件他们是交叉的，模板函数重载，
你还得想办法修复交叉的问题，那代码就很复杂了。


## 检测语法是否正确

毒霸有一个日志库，底层使用使用的是 std::wostream 的流运算符重载，现在的问题是基于 Qt 开发时，
有很多 Qt 的类型，因为没重载对应流运算符，没法直接进行日志输出，使得使用起来很麻烦，那么怎么进行重载。
1. 首先 Qt 的日志打印，用的 QDebug 这个类，虽然也是用到了流运算符，但确实 QDataStream 和 QTextStream。
2. 如果挨个重载一遍代码量重载有点大。

大致的重载写法如下：
```cpp
template<typename T>
std::wostream& operator<<(std::wostream& stream, const T& t)
{
    QString buffer;
    {
        QDebug debug(&buffer);
        debug << t;
    }
    return stream << (LPCWSTR)buffer.utf16();
}
```

直接这么写，是很多问题的，至少需要保证 T 是支持 debug 的流运算，同时需要排除掉已经重载被 std::wostream
重载过的流运算（否则会报冲突）。这样需要验证 T 类型是否已经重载了 std::wostream 的运算以及是否可以被 QDebug 进行流运算。
```cpp
template<typename T>
struct CheckDebug
{
    template<typename U> static auto Check(int)
             ->decltype(std::declval<QDebug>() << std::declval<U>(),
                 std::true_type());
    template<typename U> static std::false_type Check(...);
    static constexpr auto value = decltype(Check<T>(0))::value;
}
```

这里需要解释点是，这里的 ... 是不定参数，跟模板参数包没啥关系，跟不定参数宏也没啥关系。
这里是利用 check(int) 和 check(...) 的匹配优先级，优先使用 check(int)，但是如果第一个的语法检测不成立，
则会使用第二个，但是第一个和第二个返回值不一样。

通过这个方法，可以用于检测语法是否成立。

这里需要备注的点是：std::declval\<QDebug\>()，为什么不直接写成 QDebug()，首先这里写成 QDebug() 是可以的，
但是后面的 std::decalval\<U\>() 是不能写成 U()。
这是因为 U 未必有默认构造函数，QDebug 是确定有的，U 是模板参数，可以任意指定的。
这里只是为了验证 QDebug() \<\< U 类型的对象 是否语法成立，并不强求 U 有无参构造函数。
那么怎么构造 U 的对象出来用于检验了？这就需要用到以下函数：
```cpp
Template <typename T>
T declval();
// 它就是这么简单，没有实现，也没法实现，因为同样在这也不知道怎么构造一个 T 的对象。
// 因为上述代码是在编译器完成，压根就没打算真正的调用 declval 函数，不会出现链接错误。
```

这个检验语法正确方案，有很多变种，大致的写法都是类似的。至于有没有完全另类的写法，我暂时不知道，目前见到的几种版本，大体雷同。


## 错误示例

错误示例 1：
```cpp
struct A {
    void funcA() {}
}

struct B {
    void funcB() {}
}

template<typename T>
void myFunc(T t)
{
    if (is_same<A, T>::value)
    {
        t.funcA();
    } else if (is_same<B, T>::value)
    {
        t.funcB();
    }
}
```

错误示例 2：
```cpp
template<typename ...Args>
class Argments
{
    void callFunc(const std::function<Args...>& func)
    {
    };
};

Argments.call([](int, double)
{
});
```


## Refs

* <https://cheetahfun.feishu.cn/docs/doccnMJnXaHGq9raQCrtCiQpfjf>



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2022-01-25-C++-template.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://cheetahfun.feishu.cn/docs/doccnMJnXaHGq9raQCrtCiQpfjf]({% include relrefx.html url="/backup/2022-01-25-C++-template.md/cheetahfun.feishu.cn/1969e84b.html" %})
