---
layout: post
title: "生活 -- Welcome to my blog"
author:
location: "Japan"
categories: ["生活"]
tags: ["生活"]
toc: true
toclistyle:
comments: true
visibility:
mathjax: true
mermaid: true
glslcanvas:
codeprint:
---

Hey, there! Welcome to my blog. I hope you enjoy reading the stuff in here. Nothing fancy, really. Just bits and bobs about tech and random topics.<br/><br/>
Enjoy!

[MathJax 总结](https://www.zybuluo.com/yangfch3/note/267947)


## Test MathJax $\require{mediawiki-texvc}$

[MathJax basic tutorial and quick reference](https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference)

[基本数学公式语法 (of MathJax) {% include relref_csdn.html %}](https://blog.csdn.net/ethmery/article/details/50670297)

[MathJax 总结](https://www.zybuluo.com/yangfch3/note/267947)


### Inline MathJax

Inline MathJax: $E = mc^2$.


### Display MathJax

[维基百科·麦克斯韦方程组 {% include relref_wiki.html %}](https://zh.wikipedia.org/wiki/%E9%A6%AC%E5%85%8B%E5%A3%AB%E5%A8%81%E6%96%B9%E7%A8%8B%E7%B5%84)。初等数学不是这个世界的真相，高等数学才是。麦克斯韦方程组有三种形式，表达的居然是同一个东西：积分形式、微分形式、复数形式。将电现象、磁现象与光的本质有机地统一在完整的电磁场理论中。

#### [麦克斯韦方程 {% include relref_csdn.html %}](https://blog.csdn.net/weixin_43318626/article/details/102329794)

##### 积分形式

$$
\begin{cases}
\oiint_{\partial V} \mathbf{E} \cdot d\mathbf{a} = \frac{Q_V}{\epsilon_0} \\
\oint_{\partial S} \mathbf{E} \cdot d\mathbf{l} = -\frac{d}{dt} \int_{S} \mathbf{B} \cdot d\mathbf{a} \\
\oiint_{\partial V} \mathbf{B} \cdot d\mathbf{a} = 0 \\
\oint_{\partial S} \mathbf{B} \cdot d\mathbf{l} = \mu_0 I_S + \mu_0 \epsilon_0 \frac{d}{dt} \int_{S} \mathbf{E} \cdot d\mathbf{a} \\
\end{cases}
$$

##### 微分形式

$$
\begin{cases}
\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0} \\
\nabla \times \mathbf{E} = -\frac{\partial}{\partial t} \mathbf{B} \\
\nabla \cdot \mathbf{B} = 0 \\
\nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0 \epsilon_0 \frac{\partial}{\partial t} \mathbf{E} \\
\end{cases}
$$

这里 $\mathbf{E}$ 表示电场，$\mathbf{B}$ 表示磁场，$\epsilon_0$ 和 $\mu_0$ 只是两个常数暂时可以忽略。积分形式中 $Q$ 是电荷，$I$ 是电流，$V$ 表示一块体积，$\partial V$ 表示它的表面，而 $S$ 表示一块曲面，$\partial S$ 表示它的边缘。微分形式中 $\rho$ 是电荷密度（$$电荷/体积$$），$\mathbf{J}$ 是电流密度（$$电流/面积$$），$\nabla\cdot$ 和 $\nabla\times$ 是两个不同的算符，基本可以理解为对向量的某种微分。

四个方程中，两个是关于电场 $\mathbf{E}$ 的，两个是关于磁场 $\mathbf{B}$ 的；两个是曲面积分 $\int \cdots d\mathbf{a}$ 或者散度 $\nabla\cdot$，两个是曲线积分 $\int \cdots d\mathbf{l}$ 或者旋度 $\nabla\times$。等式左边四个式子分别描述电场和磁场的两个东西，非常对称。

##### 复数形式

$$
\left\{\begin{array}{l}
{\nabla \times \boldsymbol{E}             = -\mathbf{i} \omega \mu \boldsymbol{H}} \\
{\nabla \times \boldsymbol{H}             = \boldsymbol{j}_{f}+\mathrm{i} \omega \varepsilon \boldsymbol{E}} \\
{\nabla \cdot \varepsilon \boldsymbol{E}  = \dot{\rho}_{f}} \\
{\nabla \cdot \mu \boldsymbol{H}          = 0} \\
{\nabla \cdot \boldsymbol{j}_{f}          = -\mathrm{i} \omega \dot{\rho}_{f}}
\end{array}\right.
$$


## 参考式 / 行内式

<https://www.imydl.tech/ty/70.html>


## 常见的希腊字母

<https://blog.csdn.net/qq_36148847/article/details/79419814>

<https://www.szdev.com/blog/Hexo/mathjax-config-and-tutorial/>

<table class="tablestyle" ntablew="1:1:1:1:1"></table>

<table>
<thead>
<tr><th>序号</th><th>大写</th><th>小写</th><th>LaTex 代码</th><th>汉语注音</th></tr>
</thead>
<tbody>
<tr><td>1</td><td>$\Alpha$</td><td>$\alpha$</td><td>\alpha</td><td>阿尔法</td></tr>
<tr><td>2</td><td>$\Beta$</td><td>$\beta$</td><td>\beta</td><td>贝塔</td></tr>
<tr><td>3</td><td>$\Gamma$</td><td>$\gamma$</td><td>\gamma</td><td>伽马</td></tr>
<tr><td>4</td><td>$\Delta$</td><td>$\delta$</td><td>\delta</td><td>德尔塔</td></tr>
<tr><td>5</td><td>$\Epsilon$</td><td>$\epsilon$</td><td>\epsilon</td><td>伊普西隆</td></tr>
<tr><td>6</td><td>$\Zeta$</td><td>$\zeta$</td><td>\zeta</td><td>泽塔</td></tr>
<tr><td>7</td><td>$\Eta$</td><td>$\eta$</td><td>\eta</td><td>伊塔</td></tr>
<tr><td>8</td><td>$\Theta$</td><td>$\theta$</td><td>\theta</td><td>西塔</td></tr>
<tr><td>9</td><td>$\Iota$</td><td>$\iota$</td><td>\iota</td><td>约塔</td></tr>
<tr><td>10</td><td>$\Kappa$</td><td>$\kappa$</td><td>\kappa</td><td>卡帕</td></tr>
<tr><td>11</td><td>$\Lambda$</td><td>$\lambda$</td><td>\lambda</td><td>兰姆达</td></tr>
<tr><td>12</td><td>$\Mu$</td><td>$\mu$</td><td>\mu</td><td>缪</td></tr>
<tr><td>13</td><td>$\Nu$</td><td>$\nu$</td><td>\nu</td><td>纽</td></tr>
<tr><td>14</td><td>$\Xi$</td><td>$\xi$</td><td>\xi</td><td>克西</td></tr>
<tr><td>15</td><td>$\Omicron$</td><td>$\omicron$</td><td>\omicron</td><td>欧米克隆</td></tr>
<tr><td>16</td><td>$\Pi$</td><td>$\pi$</td><td>\pi</td><td>派</td></tr>
<tr><td>17</td><td>$\Rho$</td><td>$\rho$</td><td>\rho</td><td>柔</td></tr>
<tr><td>18</td><td>$\Sigma$</td><td>$\sigma$</td><td>\sigma</td><td>西格玛</td></tr>
<tr><td>19</td><td>$\Tau$</td><td>$\tau$</td><td>\tau</td><td>陶</td></tr>
<tr><td>20</td><td>$\Upsilon$</td><td>$\upsilon$</td><td>\upsilon</td><td>宇普西隆</td></tr>
<tr><td>21</td><td>$\Phi$</td><td>$\phi$</td><td>\phi</td><td>弗爱</td></tr>
<tr><td>22</td><td>$\Chi$</td><td>$\chi$</td><td>\chi</td><td>卡</td></tr>
<tr><td>23</td><td>$\Psi$</td><td>$\psi$</td><td>\psi</td><td>普赛</td></tr>
<tr><td>24</td><td>$\Omega$</td><td>$\omega$</td><td>\omega</td><td>欧米伽</td></tr>
</tbody></table>

<table class="tablestyle" ntablew="1:1:1:1:1"></table>

<table>
<tbody>
<tr><td rowspan="7">斜体</td>
    <td>$\varEpsilon$</td><td>$\varepsilon$</td><td>\varepsilon</td><td>伊普西隆</td></tr>
<tr><td>$\varKappa$</td><td>$\varkappa$</td><td>\varkappa</td><td>卡帕</td></tr>
<tr><td>$\varTheta$</td><td>$\vartheta$</td><td>\vartheta</td><td>西塔</td></tr>
<tr><td>$\varPi$</td><td>$\varpi$</td><td>\varpi</td><td>派</td></tr>
<tr><td>$\varRho$</td><td>$\varrho$</td><td>\varrho</td><td>柔</td></tr>
<tr><td>$\varSigma$</td><td>$\varsigma$</td><td>\varsigma</td><td>西格玛</td></tr>
<tr><td>$\varPhi$</td><td>$\varphi$</td><td>\varphi</td><td>弗爱</td></tr>
</tbody></table>

$$
\bbox[border:2px solid red]
{
e^x=\lim_{n\to\infty} \left( 1+\frac{x}{n} \right)^n
}
$$


## quote demo

[Alexander Telea's inpainting algorithm][1]

[1]: <https://www.rug.nl/>

[![][im1_in_thumb]][im1_in]

[im1_in]: <https://sunocean.life/blog/assets/gitee.png>
[im1_in_thumb]: <https://sunocean.life/blog/assets/opengl.png>


## domain tag sample

[域名标记 {% include relref_bili.html %} 样例](bilibili.com)<br/>
[域名标记 {% include relref_github.html %} 样例](github.com)<br/>
[域名标记 {% include relref_cnblogs.html %} 样例](cnblogs.com)<br/>
[域名标记 {% include relref_jianshu.html %} 样例](jianshu.com)<br/>
[域名标记 {% include relref_csdn.html %} 样例](csdn.net)<br/>
[域名标记 {% include relref_zhihu.html %} 样例](zhihu.com)<br/>
[域名标记 {% include relref_wiki.html %} 样例](wikipedia.org)<br/>
[域名标记 {% include relref_weixin.html %} 样例](weixin.qq.com)<br/>
[域名标记 {% include relref_keqq.html %} 样例](ke.qq.com)<br/>

[域名标记 {% include relref_scriptol.html %} 样例](scriptol.com)<br/>
[域名标记 {% include relref_khronos.html %} 样例](khronos.org)<br/>
[域名标记 {% include relref_gluon.html %} 样例](gluon.ai)<br/>


## sequenceDiagram

[sequenceDiagram {% include relref_cnblogs.html %}](https://www.cnblogs.com/songjn/p/13552340.html)

<div class="mermaid">
sequenceDiagram

    # 通过设定参与者（participants）的顺序控制展示模块顺序。

    participant Alice
    participant Bob
    participant John
    Alice -> John: Hello John, how are you?
    loop Healthcheck
        John -> John: Fight against hypochondria
    end
    Note right of John: Rational thoughts <br/>prevail...
    John --> Alice: Great!
    John -> Bob: How about you?
    Bob --> John: good!
</div>


## log

```cpp
FILE *fp = NULL;
fp = fopen("D:\\camera.txt", "a");
if (fp)
{
    fprintf(fp, "%s %d \n", __FILE__, __LINE__);
    fclose(fp);
}

FILE* fp = NULL;
errno_t err = fopen_s(&fp, "E:\\irrlicht.txt", "a");
if (err == 0 && fp)
{
    fprintf(fp, "%s@x\n", lpcstr);
    fclose(fp);
}

char fpath[1024] = "";
_fullpath(fpath, fileLocation, 1024);
```

这个存在缺陷，如果转码失败会不可逆：

```cpp
#include "stdafx.h"
#include <assert.h>
#include <string>

std::wstring CharToWChar(const char* str, size_t encode = CP_ACP) {
    int srclen = strlen(str);
    int len = MultiByteToWideChar(encode, 0, str, srclen, NULL, 0);
    if (len <= 0) {
        return L"";
    }
    wchar_t* temp = new wchar_t[len + 1];
    MultiByteToWideChar(encode, 0, str, srclen, temp, len);
    temp[len] = '\0';
    std::wstring wstr = temp;
    delete[] temp;
    return wstr;
}

std::string WCharToChar(const wchar_t* wstr, size_t encode = CP_ACP) {
    int srclen = wcslen(wstr);
    int len = WideCharToMultiByte(encode, 0, wstr, srclen, NULL, 0, NULL, NULL);
    if (len <= 0) {
        return "";
    }
    char* temp = new char[len + 1];
    WideCharToMultiByte(encode, 0, wstr, srclen, temp, len, NULL, NULL);
    temp[len] = '\0';
    std::string str = temp;
    delete[] temp;
    return str;
}

wchar_t bkHexWChar(const wchar_t* buffer, int cntlen = 4) {
    wchar_t* num = new wchar_t[cntlen + 1];
    memcpy(num, buffer, cntlen * sizeof(wchar_t));
    num[cntlen] = 0;
    wchar_t ch = wcstol(num, NULL, 16);
    delete[] num;
    return ch;
}

int bkHexChar(const char* buffer, int cntlen = 2) {
    char* num = new char[cntlen + 1];
    memcpy(num, buffer, cntlen * sizeof(char));
    num[cntlen] = 0;
    int ch = strtol(num, NULL, 16);
    delete[] num;
    return ch;
}

CString toHexString(CString str) {
    std::string strk = WCharToChar(str.GetString());
    const int length = strk.length();
    const char* buffer = strk.c_str();
    assert(length >= 0 && length <= 0xffff);
    CString retv;
    retv.AppendFormat(L"%04x", length);
    for (int i = 0; i < length; i++) {
        // 宽字符型 wchar_t (unsigned short.)
        // wchar_t ch = buffer[i];
        // assert(ch >= 0 && ch <= 0xffff);
        unsigned char ch = buffer[i];
        assert(ch >= 0 && ch <= 0xff);
        retv.AppendFormat(L"%02x", ch);
    }
    return retv;
}

CString bkHexString(CString str) {
    std::string strk = WCharToChar(str.GetString());
    int srclen = strk.length();
    assert((srclen - 4) % 2 == 0 && srclen >= 4);
    if ((srclen - 4) % 2 != 0 || srclen < 4) {
        return L"";
    }
    const char* buffer = strk.c_str();
    const int length = bkHexChar(&buffer[0], 4);
    assert(length == (srclen - 4) / 2);
    if (length != (srclen - 4) / 2) {
        return L"";
    }
    CStringA retv;
    for (int i = 0; i < length; i++) {
        char ch = bkHexChar(&buffer[4 + i * 2]);
        retv.AppendChar(ch);
    }
    std::wstring temp = CharToWChar(retv.GetString());
    CString wstr = temp.c_str();
    return wstr;
}

int _tmain(int argc, _TCHAR* argv[])
{
    CString test = L"中文 123";

    test = toHexString(test);
    test = bkHexString(test);

    test = bkHexString(L"0004ffffff01");
    test = toHexString(test);
    return 0;
}
```

这个方案：

<div class="highlighter-rouge" foldctrl="1"></div>

```cpp
#include <assert.h>

#define ALG_TYPE 0x321

class b62 {
  public:
    static int ParseBase62(wchar_t ch) {
        if (ch >= L'0' && ch <= L'9') {
            return ch - L'0';
        }
        if (ch >= L'a' && ch <= L'z') {
            return ch - L'a' + 10;
        }
        if (ch >= L'A' && ch <= L'Z') {
            return ch - L'A' + 10 + 26;
        }
        return -1;
    }

    static int appendHex(CString& retv, unsigned long value) {
        int len = 0;
        for (unsigned long temp = value; len == 0 || temp; temp /= 62) {
            len++;
        }

        static wchar_t SZ_BASE62_TAB[] = L"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
        retv.AppendChar(SZ_BASE62_TAB[len]);
        for (int i = 0; i < len; i++) {
            int node = value % 62;
            retv.AppendChar(SZ_BASE62_TAB[node]);
            value /= 62;
        }
        return len;
    }

    static unsigned long eatupHex(const wchar_t* ptr, unsigned int& index) {
        int len = ParseBase62(ptr[index++]);
        unsigned long value = 0;
        unsigned long mulval = 1;
        for (int i = 0; i < len; i++) {
            int node = ParseBase62(ptr[index++]);
            value += node * mulval;
            mulval *= 62;
        }
        return value;
    }

    static CString toHexString(CString str) {
        const int length = str.GetLength();
        const wchar_t* buffer = str.GetString();

        CString retv;
        appendHex(retv, ALG_TYPE);
        appendHex(retv, length);
        wchar_t check = 0;
        for (int i = 0; i < length; i++) {
            wchar_t ch = buffer[i]; // <= 0xffff
            appendHex(retv, ch ^ ALG_TYPE);
            check ^= ch;
        }
        appendHex(retv, check);
        return retv;
    }

    static CString bkHexString(CString str) {
        unsigned int index = 0;

        const wchar_t* buffer = str.GetString();
        const int algType = eatupHex(buffer, index);
        if (algType != ALG_TYPE) {
            return L"??<unknow type>";
        }

        CString retv;
        wchar_t check = 0;
        const int length = eatupHex(buffer, index);
        for (int i = 0; i < length; i++) {
            wchar_t ch = eatupHex(buffer, index) ^ ALG_TYPE;
            retv.AppendChar(ch);
            check ^= ch;
        }

        wchar_t checkz = eatupHex(buffer, index);
        assert(checkz == check);
        if (checkz != check) {
            return L"??<check error>";
        }
        return retv;
    }

}; // namespace b62
```


## Tools

* 公式在线编辑 <https://kerzol.github.io/markdown-mathjax/editor.html>
* **公式在线编辑** <https://latex.codecogs.com/eqneditor/editor.php>
* 文档在线编辑 <http://www.mdeditor.com/>
* 文档在线编辑 <https://www.zybuluo.com/mdeditor>
* **图片转公式** <https://gongshi.wang/>
* <https://mathpix.com/><sup>图片转公式貌似要收钱</sup>

* **HTML 转 MarkDown** <http://domchristie.github.io/turndown/>
* [Html 转 MarkDown](http://www.fly63.com/tool/htmarkdown/)
* **[Html 转 Markdown](http://www.atoolbox.net/Tool.php?Id=715)**
* [Html 转换为 MarkDown 工具](https://www.bejson.com/convert/html2markdown/)



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2020-08-21-welcome-to-my-blog.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.zybuluo.com/yangfch3/note/267947]({% include relrefx.html url="/backup/2020-08-21-welcome-to-my-blog.md/www.zybuluo.com/b3ceed04.html" %})
- [https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference]({% include relrefx.html url="/backup/2020-08-21-welcome-to-my-blog.md/math.meta.stackexchange.com/77111110.html" %})
- [https://blog.csdn.net/ethmery/article/details/50670297]({% include relrefx.html url="/backup/2020-08-21-welcome-to-my-blog.md/blog.csdn.net/30eba2a7.html" %})
- [https://zh.wikipedia.org/wiki/%E9%A6%AC%E5%85%8B%E5%A3%AB%E5%A8%81%E6%96%B9%E7%A8%8B%E7%B5%84]({% include relrefx.html url="/backup/2020-08-21-welcome-to-my-blog.md/zh.wikipedia.org/07dc9777.html" %})
- [https://blog.csdn.net/weixin_43318626/article/details/102329794]({% include relrefx.html url="/backup/2020-08-21-welcome-to-my-blog.md/blog.csdn.net/2799a43b.html" %})
- [https://www.imydl.tech/ty/70.html]({% include relrefx.html url="/backup/2020-08-21-welcome-to-my-blog.md/www.imydl.tech/76d29f47.html" %})
- [https://blog.csdn.net/qq_36148847/article/details/79419814]({% include relrefx.html url="/backup/2020-08-21-welcome-to-my-blog.md/blog.csdn.net/b40f77e7.html" %})
- [https://www.szdev.com/blog/Hexo/mathjax-config-and-tutorial/]({% include relrefx.html url="/backup/2020-08-21-welcome-to-my-blog.md/www.szdev.com/c7cf6953.html" %})
- [https://www.rug.nl/]({% include relrefx.html url="/backup/2020-08-21-welcome-to-my-blog.md/www.rug.nl/739d4824.html" %})
- [https://www.cnblogs.com/songjn/p/13552340.html]({% include relrefx.html url="/backup/2020-08-21-welcome-to-my-blog.md/www.cnblogs.com/3fe970e2.html" %})
- [https://kerzol.github.io/markdown-mathjax/editor.html]({% include relrefx.html url="/backup/2020-08-21-welcome-to-my-blog.md/kerzol.github.io/554e5cc8.html" %})
- [https://latex.codecogs.com/eqneditor/editor.php]({% include relrefx.html url="/backup/2020-08-21-welcome-to-my-blog.md/latex.codecogs.com/eb52cd36.php" %})
- [http://www.mdeditor.com/]({% include relrefx.html url="/backup/2020-08-21-welcome-to-my-blog.md/www.mdeditor.com/1e2faf1f.html" %})
- [https://www.zybuluo.com/mdeditor]({% include relrefx.html url="/backup/2020-08-21-welcome-to-my-blog.md/www.zybuluo.com/eb3376cc.html" %})
- [https://gongshi.wang/]({% include relrefx.html url="/backup/2020-08-21-welcome-to-my-blog.md/gongshi.wang/d6fb7cac.html" %})
- [https://mathpix.com/]({% include relrefx.html url="/backup/2020-08-21-welcome-to-my-blog.md/mathpix.com/6a3d6789.html" %})
- [http://domchristie.github.io/turndown/]({% include relrefx.html url="/backup/2020-08-21-welcome-to-my-blog.md/domchristie.github.io/9cfffeb1.html" %})
- [http://www.fly63.com/tool/htmarkdown/]({% include relrefx.html url="/backup/2020-08-21-welcome-to-my-blog.md/www.fly63.com/488480ab.html" %})
- [http://www.atoolbox.net/Tool.php?Id=715]({% include relrefx.html url="/backup/2020-08-21-welcome-to-my-blog.md/www.atoolbox.net/ecf02067.php" %})
- [https://www.bejson.com/convert/html2markdown/]({% include relrefx.html url="/backup/2020-08-21-welcome-to-my-blog.md/www.bejson.com/0f492a91.html" %})
