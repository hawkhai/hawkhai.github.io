---
layout: post
title: "编程 C++ -- std::&lt;sstream&gt; istringstream、ostringstream、stringstream"
author:
location: "珠海"
categories: ["编程"]
tags: ["编程", "C++"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---

包含 &lt;sstream&gt;，顺便加个使用名字空间 std 的声明，可以开始了。sstream 里包括 istringstream、ostringstream、stringstream、stringbuf 和各宽字符版本的对象类型。更方便的格式化字符串处理，更安全的类型转换。

{% include image.html url="/assets/images/210326-use-sstream/08cppios01_pconline2009.gif" %}


## stringstream

你可以使用 C++11 标准库里的 stringstream，它可以实现字符串和所有各种数字的转换，包括 int, float, double，简单粗暴，不用考虑缓冲区溢出的问题。自从知道这个神器之后，我就没有用过 sscanf 和 sprintf 函数了。

当要进行多次数据类型转换时，需要先使用 clear() 清空流，不然之前的数据会影响下一次数据类型转换。

```cpp
#include <string>
#include <sstream> // 包含头文件

int main()
{
    std::stringstream str2digit;
    std::string sint='1', sfloat='1.1', sdouble='1.2';
    int dint;
    float dfloat;
    double ddouble;

    str2digit << sint; str2digit >> dint;  // string to int
    str2digit.clear();
    str2digit << sfloat; str2digit >> dfloat;  // string to float
    str2digit.clear();
    str2digit << sdouble; str2digit >> ddouble;  // string to double

    std::cout << dint << ", " << dfloat << ", " << ddouble << std::endl;

    return 0;
}
```

```cpp
string str = "123";
int n = atoi(str.c_str());

int stringToInt(const string &s) {
    int v;
    stringstream ss;
    ss << s;
    ss >> v;
    return v;
}
```


## Input & Output

```cpp
ifstream infile;
infile.open(filename, ios::in);

    int DATA1;
    float DATA2, DATA3, DATA4;

    stringstream sem;
    sem << infile.rdbuf();

    while (true)
    {
        sem >> DATA1;
        if(sem.eof())break;

        sem >> DATA2;
        sem >> DATA3;
        sem >> DATA4;

        DATA1list.push_back(DATA1);
        DATA2list.push_back(DATA2);
        DATA3list.push_back(DATA3);
        DATA4list.push_back(DATA4);
    }
infile.close();
```

1. fstream 对象的 rdbuf() 成员函数返回的是一个 std::filebuf\*指针，用以重定向流，结果就是文件的内容全部作为一个 C++ 流，
    流向我们的 stringstream 对象里。
2. 我们从该 stringstream 对象里从头取出各个数据到中间变量 DATAi 中，这可不是一个一个字符取哦，
    因为它是以空格或者 \n,\t 之类字符为分隔的，所以很方便；
3. 同时，这里取出到 DATA 的也不是字符串，而确实就是连续一个 int 三个 float 哦，因为内部有安全的转换机制，
    所以不要再担心 C 那种格式化的问题了，无论是 INT 还是 DOUBLE 还是 CHAR\*都能做到。这是 stringstream 最强大之处。
4. 判断“取”的动作结束的 eof() 为什么要在最后做了一次“无用功”后才判断呢？因为只有这样能判断。
    stringstream 这时候扮演着一个乐施者，他不会去数自己包包里还剩下多少块波板糖，只会不停伸手入包里取出糖，
    而只有最后一次伸手入包包发现已经没糖了 —— 所以才叫最后一次 —— 才会醒觉：哦，原来我一贫如洗了。

基本上太强了。再举例，这次是保存数据到文件，虽是简单，但如果按我以前用 fstream 文件流的方法，效果比 C 的 fwrite 要糟糕：

```cpp
ofstream fileSave;
fileSave.open(filename, ios::ate);

    ostringstream strStream;

    strStream.setf(ios::showpoint);
    strStream << std::setprecision(4);

    for(int i = 0 ; i < Num; i++)
    {
        strStream<<DATA1[i]<< "  " <<DATA2[i]<< "  " <<DATA3[i]<< "  " <<DATA4[i]<<endl;
        fileSave.write( strStream.str().c_str(), strStream.str().size() );
    }
fileSave.close;
```

清空一个 stringstream 对象 (stringstream strs) 里的内容时，单 strs.clear() 是不行的，要用 strs.str("") 这句才行哦。

```cpp
// 把整个文件内容存储到单独一个字符串里：
ofstream dfileSave;
stringstream outstream;

dfileSave.open("tResult.txt", ios::in | ios::app);

std::filebuf *pFileBuffer =  dfileSave.rdbuf();
outstream << pFileBuffer;
int filesize = pFileBuffer->pubseekoff(0, ios::end, ios::in);

std::string sre = outstream.str(); // 1
const char *de = sre.c_str(); // 2

dfileSave.close();
```


## Refs

- [1] [不要犹豫了，用 sstream 吧](http://www.zwqxin.com/archives/cpp/use-sstream.html)

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-03-26-use-sstream.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [http://www.zwqxin.com/archives/cpp/use-sstream.html]({% include relref.html url="/backup/2021-03-26-use-sstream.md/www.zwqxin.com/b833d53a.html" %})
