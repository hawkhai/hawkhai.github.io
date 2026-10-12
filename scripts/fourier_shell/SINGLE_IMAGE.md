# 单张傅里叶“海螺图”

[reproduce_single.py](reproduce_single.py) 根据傅里叶分量公式单独生成曲面。当前默认参数与 [redraw_conch.py](redraw_conch.py) 对齐；两张默认 PNG 使用相同曲面、视角、网格和画布。

![单张海螺图的运行结果](output/single/fourier_shell_single.png)

在仓库根目录运行：

```powershell
python -m pip install -r scripts/fourier_shell/requirements.txt
python scripts/fourier_shell/reproduce_single.py
```

输出目录为 `scripts/fourier_shell/output/single/` ，包含 1600 × 1130 的 PNG、SVG 和记录本次参数的 JSON。脚本不读取截图，也不需要中文字体。

默认曲面采用：

```text
C(f,t) = 0.05 sinc(2f) exp(i2πft)
sinc(u) = sin(πu)/(πu), sinc(0) = 1
(x,y,z) = (-Re C, Im C, t)
f ∈ [0,8], t ∈ [0,5]
```

对固定频率 $f$，复数 $C(f,t)$ 随时间旋转；频率越高，旋转越快。 `sinc` 包络使不同频率的半径不同。连接相邻频率和时间的采样点，就得到海螺曲面。颜色按时间从蓝到红，细黑线表示网格。曲面是各个正频率的分量，还没有对频率积分。要还原单位高度的矩形脉冲，需要加上负频率，并撤销显示振幅缩放。

与 `redraw_conch.py` 相同的参数有 `--width 2 --amplitude 0.05 --fmax 8 --tmax 5 --nf 1201 --nt 101 --elev 8 --azim -135 --dpi 200` 。 `--labels` 显示坐标名称， `--output` 指定输出目录。旧参数 `--scale` 仍可使用，换算关系为 `amplitude = scale × width` ； `--duration` 等同 `--tmax` 。

更完整的数学推导与三层示意图见 [fourier.md](fourier.md)。
