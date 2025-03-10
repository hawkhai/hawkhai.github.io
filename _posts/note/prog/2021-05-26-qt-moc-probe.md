---
layout: post
title: "编程与调试 C++ -- Qt MOC 信号槽 剖解"
author:
location: "珠海"
categories: ["编程与调试"]
tags: ["编程", "QT", "C/C++"]
toc: true
toclistyle:
comments:
visibility: hidden
mathjax:
mermaid:
glslcanvas:
codeprint:
archived: true
---

moc & rcc & uic
QT uic rcc moc 命令行使用
```
cd %PROJ_PATH%
# 资源文件生成
rcc.exe --name mainwindow .\mainwindow.qrc -o .\GeneratedFiles\qrc_mainwindow.cpp
# 界面代码生成
uic.exe .\mainwindow.ui -o .\GeneratedFiles\ui_mainwindow.h
# 信号槽
moc.exe -I.\ .\mainwindow.h -o .\GeneratedFiles\Debug\moc_mainwindow.cpp
```

需要 c++17，QT 文件路径转 windows 实际文件路径：

```cpp
#include <filesystem>
QFileInfo fileInfo(defaultFile);
QString tmp = fileInfo.absoluteFilePath();
tmp = tmp.replace("/", "\\");
std::wstring path = tmp.toStdWString();
defaultFile = QString::fromStdWString(std::filesystem::canonical(path));
```

* 信号槽问题。新式语法是使用模板来实现的。由于模板的实例化是编译期完成的，所以如果有问题编译时直接就可以暴露出来，这比老式用法（问题要在运行时才能反应出来）是的巨大的改进。
    * [信号与槽的新语法 (Qt5) {% include relref_csdn.html %}](https://blog.csdn.net/dbzhang800/article/details/6547196)
    * [深入 qt 信号与槽实现原理 {% include relref_csdn.html %}](https://blog.csdn.net/iEearth/article/details/74025072)


## 初探

对于每一个 QObject 类的派生类，qt 都会使用 moc 命令之生成附加的 moc_xxx.cpp 文件。[from](https://my.oschina.net/hevakelcj/blog/4667809)
在 moc_xxx.cpp 文件中，包含了 QObject 派生类的附加信息。

在 sender.h 头文件中定义一个 Sender 的类：
{% include image.html url="/assets/images/210526-qt-moc-probe/up-fc2e91ba2e43cf65d7703c4022fd6e2835d.png" %}

它分别有三个信号与四个槽函数。

在生成的 moc_sender.cpp 中：

qt_meta_stringdata_Sender 是一个字面量表，也是可称之为符号表。
{% include image.html url="/assets/images/210526-qt-moc-probe/up-8e4d8d571b5a11c0cef43ffd4c964f486e5.png" %}

它的存在是为了能够以 idx 就能获取对应的字符串。比如 idx = 4，对应的字串在则为 (const char \*)(qt_meta_stringdata_Sender.stringdata0+29)

另一个则是 qt_meta_data_Sender ，其生成的内容如下：
{% include image.html url="/assets/images/210526-qt-moc-probe/up-48a71610128f37ae0fb533e672b763350c7.png" %}

从上可以看出，通过上面的这个数据，足于描述 Sender 类中有几个信号与槽函数，并描述了它们的参数与返回值类型。
值得注意的是：标识信号与槽的方式都是字符串。因此为引发个别问题： Qt signal 函数使用类内部类型作为参数导致 connect 不成功问题分析
这也是 Qt 反射机制的基础。


## 实验

定义信号槽：
```cpp
class Test : public QObject {
    Q_OBJECT

public:
    explicit Test(QObject* parent = nullptr) : QObject(parent) {
    }

signals:
    void signalfunc(const MyString& str, int tid);

public slots:
    void slotfunc(const MyString& str, int tid);
};
```

* Q_OBJECT 在哪个线程创建的，其对应的信号槽消息循环就挂在了哪个线程上。
* 发送对象，会拷贝构造一个，发过去后，用完了在槽函数结束后销毁。
    * 信号函数：<span imgid="signalfunc.Construct" />
  ```cpp
// 生成的信号函数
// SIGNAL 0
void Test::signalfunc(const MyString & _t1, int _t2)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))), const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t2))) };
    // 这个会调用对象的拷贝构造函数，然后再把指针传过去。
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}
```
    * 槽函数：<span imgid="signalfunc.callback" />
    * 槽函数用完后通过 QScopedPointer 销毁对象。<span imgid="signalfunc.Destruct" />

{% include image.html url="/assets/images/210526-qt-moc-probe/20210604172601.png" relocate="signalfunc.Construct" %}
{% include image.html url="/assets/images/210526-qt-moc-probe/20210604172944.png" relocate="signalfunc.Destruct" %}
{% include image.html url="/assets/images/210526-qt-moc-probe/20210604173330.png" relocate="signalfunc.callback" %}


## QT 信号槽机制


## CSS & QSS 的几个原则

1. 限制条件尽量写多写完整一点。最好使用独一无二的 objectname。
    * 写的时候不留意，出问题了反向排查非常浪费时间。
2. 最小作用域原则，拆分 QSS 成为多个文件。
    * 比如对话框的某个文件：QWidget::setStyleSheet。
    * 出问题了，排查范围更小一些，只用排查当前 QSS。
3. 尽量避免全局一个 QSS 文件，效率也是一个问题。
    * 文件越来越大，上万行，基本没法维护，更不敢改动了。
4. 关于 QSS 的优先级。
    * 具体的高于一般的。
    * 后定义的高于前面的。
    * 样式表不考虑类的继承关系。
    * 对象的样式表高于父类或 qApp 的样式表。



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-05-26-qt-moc-probe.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://blog.csdn.net/dbzhang800/article/details/6547196]({% include relrefx.html url="/backup/2021-05-26-qt-moc-probe.md/blog.csdn.net/15a76a30.html" %})
- [https://blog.csdn.net/iEearth/article/details/74025072]({% include relrefx.html url="/backup/2021-05-26-qt-moc-probe.md/blog.csdn.net/05aaf4ef.html" %})
- [https://my.oschina.net/hevakelcj/blog/4667809]({% include relrefx.html url="/backup/2021-05-26-qt-moc-probe.md/my.oschina.net/d1164837.html" %})
