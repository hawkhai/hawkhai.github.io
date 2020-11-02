---
layout: post
title: "编程 Prog -- QT 内存泄露研究"
location: "珠海"
categories: ["编程"]
tags: [Prog Note, QT, Memory, C++]
toc: true
---


## 简介

Qt 内存管理机制：Qt 在内部能够维护对象的层次结构。对于可视元素，这种层次结构就是子组件与父组件的关系；对于非可视元素，则是一个对象与另一个对象的从属关系。在 Qt 中，删除父对象会将其子对象一起删除。

C++ 中 delete 和 new 必须配对使用（一一对应）：delete 少了，则内存泄露，多了麻烦更大。Qt 中使用了 new 却很少 delete，因为 QObject 的类及其继承的类，设置了 parent（也可在构造时使用 setParent 函数或 parent 的 addChild）故 parent 被 delete 时，这个 parent 的相关所有 child 都会自动 delete，不用用户手动处理。但 parent 是不区分它的 child 是 new 出来的还是在栈上分配的。这体现 delete 的强大，可以释放掉任何的对象，而 delete 栈上对象就会导致内存出错，这需要了解 Qt 的半自动的内存管理。另一个问题：child 不知道它自己是否被 delete 掉了，故可能会出现野指针。那就要了解 Qt 的智能指针 QPointer。


## 关联图

（1）Linux 内存图，主要了解堆栈上分配内存的不同方式。

{% include image.html url="/images/qtmemory/20140612095754296.jpg" %}
{% include image.html url="/images/qtmemory/20140612095928078.jpg" %}

（2）在 Qt 中，最基础和核心的类是：QObject，QObject 内部有一个 list，会保存 children，还有一个指针保存 parent，当自己析构时，会自己从 parent 列表中删除并且析构所有的 children。

{% include image.html url="/images/qtmemory/20140612112758250.png" %}


## 详解


### Qt 的半自动化的内存管理

（1）QObject 及其派生类的对象，如果其 parent 非 0，那么其 parent 析构时会析构该对象。

（2）QWidget 及其派生类的对象，可以设置 Qt::WA_DeleteOnClose 标志位（当 close 时会析构该对象）。

（3）QAbstractAnimation 派生类的对象，可以设置 QAbstractAnimation::DeleteWhenStopped。

（4）QRunnable::setAutoDelete()、MediaSource::setAutoDelete()。

（5）父子关系：父对象、子对象、父子关系。这是 Qt 中所特有的，与类的继承关系无关，传递参数是与 parent 有关（基类、派生类，或父类、子类，这是对于派生体系来说的，与 parent 无关）。


### 内存问题例子

#### 例子一

{% highlight cpp %}
#include <QApplication>
#include <QLabel>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    QLabel *label = new QLabel("Hello Qt!");
    label->show();
    return a.exec();
}
{% endhighlight %}

**分析：**

label 既没有指定 parent，也没有对其调用 delete，所以会造成内存泄漏。书中的这种小例子也会出现指针内存的问题。

**改进方式：**

（1）分配对象到栈上而不是堆上

{% highlight cpp %}
#include <QApplication>
#include <QLabel>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    QLabel label("Hello Qt!");
    label.show();
    return a.exec();
}
{% endhighlight %}

（2）设置标志位，close() 后会 delete label。

{% highlight cpp %}
label->setAttribute(Qt::WA_DeleteOnClose);
{% endhighlight %}

（3）new 后手动 delete

{% highlight cpp %}
#include <QApplication>
#include <QLabel>

int main(int argc, char *argv[])
{
    int ret = 0;
    QApplication a(argc, argv);
    QLabel *label = new QLabel("Hello Qt!");
    label->show();
    ret = a.exec();
    delete label;
    return ret;
}
{% endhighlight %}

#### 例子二

{% highlight cpp %}
#include <QApplication>
#include <QLabel>
int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    QLabel label("Hello Qt!");
    label.show();
    label.setAttribute(Qt::WA_DeleteOnClose);
    return app.exec();
}
{% endhighlight %}

**运行：**

{% include image.html url="/images/qtmemory/20140611221500421.png" %}

**分析：**

程序崩溃，因为 label 被 close 时，delete &label; 但 label 对象是在栈上分配的内存空间，delete 栈上的地址会出错。

有些朋友理解为 label 被 delete 两次而错误，可以测试 QLabel label("Hello Qt!"); label.show(); delete &label; 第一次 delete 就会出错。

#### 例子三

{% highlight cpp %}
#include <QApplication>
#include <QLabel>
int main(int argc, char* argv[])
{
    QApplication app(argc, argv);
    QLabel label("Hello Qt!");
    QWidget w;
    label.setParent(&w);
    w.show();
    return app.exec();
}
{% endhighlight %}

**分析：**

Object 内部有一个 list，会保存 children，还有一个指针保存 parent，当自己析构时，会自己从 parent 列表中删除并且析构所有的 children。

w 比 label 先被析构，当 w 被析构时，会删除 chilren 列表中的对象 label，但 label 是分配到栈上的，因 delete 栈上的对象而出错。

**改进方式：**

（1）调整一下顺序，确保 label 先于其 parent 被析构，label 析构时将自己从父对象的列表中移除自己，w 析构时，children 列表中就不会有分配在 stack 中的对象了。

{% highlight cpp %}
#include <QApplication>
#include <QLabel>
int main(int argc, char* argv[])
{
    QApplication app(argc, argv);
    QWidget w;
    QLabel label("Hello Qt!");
    label.setParent(&w);
    w.show();
    return app.exec();
}
{% endhighlight %}

（2）将 label 分配到堆上

{% highlight cpp %}
QLabel *label = new QLabel("Hello Qt!");
label->setParent(&w);
{% endhighlight %}

或者

{% highlight cpp %}
QLabel *label = new QLabel("Hello Qt!", this);
{% endhighlight %}

#### 例子四：野指针

{% highlight cpp %}
#include <QApplication>
#include <QLabel>
int main(int argc, char* argv[])
{
    QApplication app(argc, argv);
    QWidget *w = new QWidget;
    QLabel *label = new QLabel("Hello Qt!");
    label->setParent(w);
    w->show();
    delete w;
    label->setText("go"); // 野指针
    return app.exec();
}
{% endhighlight %}

（上述程序不显示 Label，仅作测试）

**分析：**

程序异常结束，delete w 时会 delete label，label 成为野指针，调用 label->setText("go"); 出错。

**改进方式：**

QPointer 智能指针

{% highlight cpp %}
#include <QApplication>
#include <QLabel>
#include <QPointer>
int main(int argc, char* argv[])
{
    QApplication app(argc, argv);
    QWidget *w = new QWidget;
    QLabel *label = new QLabel("Hello Qt!");
    label->setParent(w);
    QPointer<QLabel> p = label;
    w->show();
    delete w;
    if (!p.isNull()) {
        label->setText("go");
    }
    return app.exec();
}
{% endhighlight %}

#### 例子五：deleteLater

当一个 QObject 正在接受事件队列时如果中途被你销毁掉了，就是出现问题了，所以 QT 中建大家不要直接 Delete 掉一个 QObject，如果一定要这样做，要使用 QObject 的 deleteLater() 函数，它会让所有事件都发送完一切处理好后马上清除这片内存，而且就算调用多次的 deletelater 也不会有问题。

发送一个删除事件到事件系统：

{% highlight cpp %}
void QObject::deleteLater()
{
    QCoreApplication::postEvent(this, new QEvent(QEvent::DeferredDelete));
}
{% endhighlight %}


### 智能指针

如果没有智能指针，程序员必须保证 new 对象能在正确的时机 delete，四处编写异常捕获代码以释放资源，而智能指针则可以在退出作用域时（不管是正常流程离开或是因异常离开）总调用 delete 来析构在堆上动态分配的对象。

Qt 家族的智能指针：

<table class="tablestyle" ntablew="35:55:15"></table>

| 智能指针 |  | 引入 |
| --- | --- | --- |
| QPointer | Qt Object 模型的特性（之一）<br/>注意：析构时不会 delete 它管理的资源 |  |
| QSharedPointer | 带引用计数 | Qt 4.5 |
| QWeakPointer |  | Qt 4.5 |
| QScopedPointer |  | Qt 4.6 |
| QScopedArrayPointer | QScopedPointer 的派生类 | Qt 4.6 |
| QSharedDataPointer | 用来实现 Qt 的隐式共享（Implicit Sharing） | Qt 4.0 |
| QExplicitlySharedDataPointer | 显式共享 | Qt 4.4 |
| std::auto_ptr |  |  |
| std::shared_ptr | std::tr1::shared_ptr | C++0x |
| std::weak_ptr | std::tr1::weak_ptr | C++0x |
| std::unique_ptr | boost::scoped_ptr | C++0x |

（1）QPointer

QPointer 是一个模板类。它很类似一个普通的指针，不同之处在于，QPointer 可以监视动态分配空间的对象，并且在对象被 delete 的时候及时更新。

QPointer 的现实原理：在 QPointer 保存了一个 QObject 的指针，并把这个指针的指针（双指针）交给全局变量管理，而 QObject 在销毁时（析构函数，QWidget 是通过自己的析构函数的，而不是依赖 QObject 的）会调用 QObjectPrivate::clearGuards 函数来把全局 GuardHash 的那个双指针置为*零，因为是双指针的问题，所以 QPointer 中指针当然也为零了。用 isNull 判断就为空了。

{% highlight cpp %}
// QPointer 表现类似普通指针
QDate *mydate = new QDate(QDate::currentDate());
QPointer mypointer = mydata;
mydate->year();    // -> 2005
mypointer->year(); // -> 2005

// 当对象 delete 之后，QPointer 会有不同的表现
delete mydate;

if(mydate == NULL)
    printf("clean pointer");
else
    printf("dangling pointer");
// 输出 dangling pointer

if(mypointer.isNull())
    printf("clean pointer");
else
    printf("dangling pointer");
// 输出 clean pointer
{% endhighlight %}

（2）std::auto_ptr

auto_ptr 被销毁时会自动删除它指向的对象。

{% highlight cpp %}
std::auto_ptr<QLabel> label(new QLabel("Hello Dbzhang800!"));
{% endhighlight %}

（3）其他的类参考相应文档。


### 自动垃圾回收机制

（1）QObjectCleanupHandler

Qt 对象清理器是实现自动垃圾回收的很重要的一部分。QObjectCleanupHandler 可以注册很多子对象，并在自己删除的时候自动删除所有子对象。同时，它也可以识别出是否有子对象被删除，从而将其从它的子对象列表中删除。这个类可以用于不在同一层次中的类的清理操作，例如，当按钮按下时需要关闭很多窗口，由于窗口的 parent 属性不可能设置为别的窗口的 button，此时使用这个类就会相当方便。

{% highlight cpp %}
#include <QApplication>
#include <QObjectCleanupHandler>
#include <QPushButton>

int main(int argc, char* argv[])
{
    QApplication app(argc, argv);
    // 创建实例
    QObjectCleanupHandler *cleaner = new QObjectCleanupHandler;
    // 创建窗口
    QPushButton *w = new QPushButton("Remove Me");
    w->show();
    // 注册第一个按钮
    cleaner->add(w);
    // 如果第一个按钮点击之后，删除自身
    QObject::connect(w, SIGNAL(clicked()), w, SLOT(deleteLater()));
    // 创建第二个按钮，注意，这个按钮没有任何动作
    w = new QPushButton("Nothing");
    cleaner->add(w);
    w->show();
    // 创建第三个按钮，删除所有
    w = new QPushButton("Remove All");
    cleaner->add(w);
    QObject::connect(w, SIGNAL(clicked()), cleaner, SLOT(deleteLater()));
    w->show();
    return app.exec();
}
{% endhighlight %}

{% include image.html url="/images/qtmemory/20140612145714109.png" %}

在上面的代码中，创建了三个仅有一个按钮的窗口。第一个按钮点击后，会删除掉自己（通过 deleteLater() 槽），此时，cleaner 会自动将其从自己的列表中清除。第三个按钮点击后会删除 cleaner，这样做会同时删除掉所有未关闭的窗口。

（2）引用计数

应用计数是最简单的垃圾回收实现：每创建一个对象，计数器加 1，每删除一个则减 1。

{% highlight cpp %}
class CountedObject : public QObject
{
    Q_OBJECT
public:
    CountedObject() {
        ctr = 0;
    }

    void attach(QObject *obj) {
        ctr++;
        connect(obj, SIGNAL(destroyed(QObject*)), this, SLOT(detach()));
    }

public slots:
    void detach() {
        ctr--;
        if(ctr <= 0)
            delete this;
    }

private:
    int ctr;
};
{% endhighlight %}

利用 Qt 的信号槽机制，在对象销毁的时候自动减少计数器的值。但是，我们的实现并不能防止对象创建的时候调用了两次 attach()。

（3）记录所有者

更合适的实现是，不仅仅记住有几个对象持有引用，而且要记住是哪些对象。例如：

{% highlight cpp %}
class CountedObject : public QObject
{
public:

    CountedObject() {}

    void attach(QObject *obj) {
        // 检查所有者
        if(obj == 0)
            return;
        // 检查是否已经添加过
        if(owners.contains(obj))
            return;
        // 注册
        owners.append(obj);
        connect(obj, SIGNAL(destroyed(QObject*)), this, SLOT(detach(QObject*)));
    }

public slots:

    void detach(QObject *obj) {
        // 删除
        owners.removeAll(obj);
        // 如果最后一个对象也被 delete，删除自身
        if(owners.size() == 0)
            delete this;
    }

private:
    QList owners;
};
{% endhighlight %}

现在我们的实现已经可以做到防止一个对象多次调用 attach() 和 detach() 了。然而，还有一个问题是，我们不能保证对象一定会调用 attach() 函数进行注册。毕竟，这不是 C++ 内置机制。有一个解决方案是，重定义 new 运算符（这一实现同样很复杂，不过可以避免出现有对象不调用 attach() 注册的情况）。


## 总结

Qt 简化了我们对内存的管理，但是，由于它会在不太注意的地方调用 delete，所以，使用时还是要当心。


## 参考

* <http://doc.qt.nokia.com/4.7/qobject.html>
* <http://www.cuteqt.com/blog/?p=824>
* <http://blog.csdn.net/dbzhang800/article/details/6300025>
* <http://blog.csdn.net/dbzhang800/article/details/6403285>
* <http://devbean.blog.51cto.com/448512/526734/>
* **<https://blog.csdn.net/taiyang1987912/article/details/29271549>**
* **<https://www.cnblogs.com/senior-engineer/p/10037920.html>**
