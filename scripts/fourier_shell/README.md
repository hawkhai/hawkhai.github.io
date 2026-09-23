# 傅里叶“海螺图”脚本复现

单独复现海螺截图请运行 `python scripts/fourier_shell/reproduce_single.py`，公式、参数和输出说明见 [SINGLE_IMAGE.md](SINGLE_IMAGE.md)。下面介绍的是原有三层示意图脚本。

## 单独重绘 CSDN 海螺图

`redraw_conch.py` 专门重绘 [这篇文章](https://blog.csdn.net/Ciellee/article/details/108304531) 中的彩虹海螺曲面。原文没有绘图代码和具体参数，下面的默认值是根据截图外形调整的数学复现，不是原作者的精确参数。运行时不读取截图，也不联网。

```powershell
python -m pip install -r scripts/fourier_shell/requirements.txt
python scripts/fourier_shell/redraw_conch.py
```

工作区已有环境，也可直接运行：

```powershell
.\tempdir\fourier-shell-venv\Scripts\python.exe scripts/fourier_shell/redraw_conch.py
```

输出为 `output/conch.png`（1600 × 1130）与 `output/conch.svg`。SVG 的坐标和文字为矢量，密集曲面为嵌入位图。加 `--show` 可打开窗口，用鼠标旋转；`--labels` 显示坐标含义。

核心公式：

```text
A(f) = 0.05 sinc(2f),     sinc(u) = sin(πu)/(πu)
C(f,t) = A(f) exp(i 2πft)
(x, y, z) = (-Re C, Im C, t)
f ∈ [0, 8], t ∈ [0, 5]
```

固定频率 f 时就是一条螺旋；相邻频率的螺旋连成曲面。A(f) 的负旁瓣保留符号，相当于增加 π 的相位，不能直接取绝对值。A(f) 对应宽度 2、高度 0.025 的中心矩形脉冲的频谱。这里展示的是逆变换的各个正频率分量，不是已经求和的结果。实部坐标反向显示，是为了匹配截图朝向；彩虹颜色随时间/高度变化。

常用调整：

```powershell
# 改变外形、视角和导出分辨率
python scripts/fourier_shell/redraw_conch.py --width 2.5 --elev 12 --azim -125 --dpi 250
# 较稀疏的网格，加快交互预览
python scripts/fourier_shell/redraw_conch.py --nf 601 --nt 81 --show --labels
# 指定输出文件，同时生成同名 SVG
python scripts/fourier_shell/redraw_conch.py --output tempdir/my_conch.png
```

`--width` 控制 sinc 包络宽度和卷曲外形；`--tmax` 控制显示时长；`--fmax` 控制中心小螺旋的频率范围；`--nf/--nt` 控制网格密度。增大频率或时间范围时应相应增加采样，避免网格欠采样。完整参数见 `--help`。

## 原有三层示意图

这是一份根据参考图构造的数学复现，不是原作者代码，也不声称恢复了原图的坐标、采样范围或相机参数。绘图完全由公式生成，不依赖截图。

## 接近原截图的排版版本

新增 `reproduce_reference.py`，复现白底竖排、海螺曲面、彩色频率分量、蓝色箭头、矩形脉冲和中文说明。参考为用户提供的[腾讯云文章](https://cloud.tencent.com/developer/article/1187502)及其截图，原图署名 Heinrich（韩昊）。此脚本可独立运行，仅依赖本目录 requirements 中的 NumPy、Matplotlib 和本机中文字体。

```powershell
python -m pip install -r scripts/fourier_shell/requirements.txt
python scripts/fourier_shell/reproduce_reference.py
```

本工作区可以直接使用已有环境：

```powershell
.\tempdir\fourier-shell-venv\Scripts\python.exe scripts/fourier_shell/reproduce_reference.py
```

默认输出：

- `output/reference/fourier_reference.png`：1800 × 2940 高清图片。
- `output/reference/fourier_reference.svg`：文字、箭头及脉冲为矢量，三维曲面为嵌入位图。
- `output/reference/reference_parameters.json`：公式、采样范围和数值积分检查结果。

参数包括 `--width 1 --duration 5 --fmax 6 --scale 0.05 --cutoff 40 --dpi 300 --output <目录>`。`width` 是脉冲宽度，`duration`、`fmax` 是曲面显示范围，`scale` 只缩放曲面振幅；`cutoff` 是数值积分截止频率。加上 `--show-reconstruction` 可在底部叠加橙色的有限带宽重建曲线，直观看到振铃。

此版上下曲面使用同一组 `C(f,t)` 数据。海螺的坐标依次为 `(Im C, Re C, t)`，中图为 `(f, t, Re C)`；调整坐标顺序是为了匹配截图中开口朝向。为保留原图外观，右侧沿用“复频域 / 频域 / 时域”文字；中图严格说是各频率的时间波形，不能当作单独的频谱。默认底部画的是无限带宽下的理想矩形，实际积分结果另存于 JSON，未将有限积分冒充精确矩形。

以下说明对应原有的带公式版本 `reproduce.py`。

## 运行

```powershell
python -m pip install -r scripts/fourier_shell/requirements.txt
python scripts/fourier_shell/reproduce.py
```

本工作区也已建立隔离环境，可直接运行：

```powershell
.\tempdir\fourier-shell-venv\Scripts\python.exe scripts/fourier_shell/reproduce.py
```

可调参数：`--width 1 --cutoff 40 --dpi 180 --output <目录>`。宽度决定脉冲宽度，截止频率决定重建精度，DPI 决定图片分辨率。需要中文字体，例如微软雅黑、黑体或 Noto Sans CJK SC。

## 图是怎样绘制的

设时域信号在 `|t| < T/2` 时为 1，在外部为 0，使用以 Hz 为单位的傅里叶变换约定：

```text
X(f) = ∫ x(t) exp(-i 2πft) dt = T sinc(Tf)
sinc(u) = sin(πu)/(πu)，sinc(0) = 1
C(f,t) = X(f) exp(i 2πft)
```

1. **上图**：以频率 `f` 和时间 `t` 为两个参数，把 `(Re C, Im C, t)` 作为三维坐标，交给 Matplotlib 的 `plot_surface`。固定频率得到一条复平面上的螺旋线；不同频率有不同半径与转速，连起来就是“海螺”。颜色按时间着色，使用 `jet` 色图；细黑线显示网格。
2. **中图**：同一批数据取实部，以 `(f, t, X(f) cos(2πft))` 为坐标绘制曲面。它同时含有时间与频率，严格说是**各频率分量的时域波形集合**，不是通常意义上只依赖频率的频谱 `X(f)`。原图“投影”这一步还包含把频率参数展开为坐标；单纯把上图压到实数平面不会自动得到中图。
3. **下图**：对频率数值积分。因为此例的频谱是实偶函数，使用 `x_F(t) = 2 ∫₀ᶠ X(f) cos(2πft) df`，其中积分上限为截止频率 F。乘 2 包含负频率的贡献；它不是任意比例调整。蓝线画理想矩形，橙线是实际积分结果。

上面两个曲面取 `t ∈ [0, 5T]`、`f ∈ [0, 8/T]`，便于重现参考图的单侧海螺外形。底图展示正负时间，默认积分到 40 Hz。可视化范围与积分范围不同，是为了分别看清曲面和重建结果。

有限频率截断会产生 Gibbs 振铃，不能如原图示意那样得到完全笔直的矩形边缘。增加截止频率会缩窄振铃区域，跳变处的超调比例不会趋于零；在 `t = ±T/2` 处，无限带宽重建的极限为 1/2。

## 输出

- `output/fourier_shell.png`：三层布局复现图。
- `output/fourier_shell.svg`：文字与坐标为矢量、密集三维曲面为嵌入位图，兼顾编辑与文件体积。
- `output/fourier_validation.png`：真正的频谱，以及不同截止频率的重建曲线。
- `output/numerical_check.json`：中心、内部、边缘、外部采样值，便于核对积分归一化。

矩形与 sinc 的傅里叶变换关系可参见 [MathWorks 文档](https://www.mathworks.com/help/symbolic/sym.fourier.html)。仓库原有相关文章为 `_posts/dip/2020-09-26-dip-fourier-transform.md`，本次没有修改文章。
