# 单张“海螺图”复现

对应本次提供的 Heinrich 傅里叶海螺截图。
运行 `reproduce_single.py` 可独立生成单图，不需要读取截图，也不需要运行目录里的三层示意脚本。

## 运行

在仓库根目录执行（Python 3.10 或更新版本）：

```powershell
python -m pip install -r scripts/fourier_shell/requirements.txt
python scripts/fourier_shell/reproduce_single.py
```

本工作区已经有可用环境，也可以直接执行：

```powershell
.\tempdir\fourier-shell-venv\Scripts\python.exe scripts/fourier_shell/reproduce_single.py
```

输出到 `scripts/fourier_shell/output/single/`：

- `fourier_shell_single.png`：1600 × 1240 图片。
- `fourier_shell_single.svg`：坐标文字为矢量，密集曲面嵌入位图。
- `parameters.json`：公式、坐标含义和本次运行的全部参数。

## 这张图如何构造

以宽度为 T、中心在零点、高度为 1 的矩形脉冲为例。采用 Hz 为频率单位：

```text
X(f) = ∫[-T/2,T/2] exp(-i 2πfτ) dτ
     = T sinc(Tf)

sinc(u) = sin(πu)/(πu)，sinc(0) = 1
C(f,t) = s X(f) exp(i 2πft)
```

`s` 只是把复平面坐标缩放到截图的约 ±0.05 范围。此图展示傅里叶逆变换中各个复指数分量的集合，尚未对频率积分。

脚本把虚部、实部、时间分别放到三条轴上：

```text
x(f,t) = s T sinc(Tf) sin(2πft)
y(f,t) = s T sinc(Tf) cos(2πft)
z(f,t) = t
```

先生成频率和时间的二维网格，再将这些坐标传给 Matplotlib `plot_surface`。交换实部和虚部所在的水平轴，是为了匹配截图的观察方向。

- 固定 f，沿 t 方向看：半径为 `s |X(f)|`、每秒转 f 圈的螺旋线。f=0 是竖直直线。
- 固定 t，沿 f 方向看：得到该高度处的截面；连续频率把不同螺旋线连成曲面。
- `sinc` 的主瓣形成外壳，逐渐衰减的旁瓣形成内部的小卷曲。必须保留其正负号；负号相当于额外的 π 相位。
- 颜色取决于高度 t，使用 `jet` 色图，从底部蓝色逐渐变为顶部红色。细黑线是曲面网格。

核心计算只有几行：

```python
f, t = np.meshgrid(np.linspace(0, 6, 601), np.linspace(0, 5, 361))
C = 0.025 * 2 * np.sinc(2 * f) * np.exp(2j * np.pi * f * t)
ax.plot_surface(C.imag, C.real, t, cmap="jet",
                rstride=3, cstride=1, edgecolor=(0, 0, 0, 0.38),
                linewidth=0.22, shade=False)
```

这里展示非负频率，包括 f=0 边界。如果要重建原来的矩形信号，需要把负频率也包含进积分；不能只把图中的螺旋线直接相加。在上述实偶频谱特例中，可以用 `2 Re ∫₀∞ X(f)exp(i2πft)df`。

## 参数与复现范围

默认采用 `T=2`、`s=0.025`、`t∈[0,5]`、`f∈[0,6]`，俯仰角 7°、方位角 135°。脉冲宽度与相机参数是根据截图轮廓选取的复现参数；不能仅凭一张截图唯一恢复原作者的数据和代码。原文网页在本次访问中未能成功读取。

例如修改视角，或添加坐标名称：

```powershell
python scripts/fourier_shell/reproduce_single.py --elev 20 --azim 150 --labels --output tempdir/shell-other-view
```

`--width` 调整脉冲宽度和频谱形状，`--scale` 调整水平坐标数值，`--duration` 调整时间范围，`--fmax` 调整最高显示频率，`--dpi` 调整输出分辨率。相机和绘图框比例也会明显影响外观。水平轴范围会随 `scale * width` 调整，因此单独修改 `scale` 会改变刻度，不改变画面中的相对大小。

图形由上述公式重新生成；未重绘原图的作者水印。参考图署名为 Heinrich（韩昊），原文为[《傅里叶分析之掐死教程》](https://zhuanlan.zhihu.com/p/19763358)。

数学和绘图接口参考：[MathWorks 矩形脉冲的傅里叶变换](https://www.mathworks.com/help/symbolic/sym.fourier.html)（该文档默认使用角频率 ω，换成 Hz 时令 ω=2πf）；[Matplotlib 三维曲面示例](https://matplotlib.org/stable/gallery/mplot3d/surface3d.html)。
