# 傅里叶“海螺图”复现

完整的公式、四种绘图结果、参数解释与数值检查见 [fourier.md](fourier.md)。所有图片由 NumPy 与 Matplotlib 从公式生成，运行时不读取参考截图。

## 运行

在仓库根目录执行：

```powershell
python -m pip install -r scripts/fourier_shell/requirements.txt
python scripts/fourier_shell/redraw_conch.py
python scripts/fourier_shell/reproduce_single.py
python scripts/fourier_shell/reproduce_reference.py
python scripts/fourier_shell/reproduce.py
```

本工作区已有隔离环境，可将上述命令中的 `python` 换成 `.\tempdir\fourier-shell-venv\Scripts\python.exe`。

| 脚本 | 默认结果 |
| --- | --- |
| [redraw_conch.py](redraw_conch.py) | [独立海螺图](output/conch.png)，支持 `--show` 交互旋转 |
| [reproduce_single.py](reproduce_single.py) | [独立海螺图](output/single/fourier_shell_single.png)与参数 JSON |
| [reproduce_reference.py](reproduce_reference.py) | [贴近参考排版的三层图](output/reference/fourier_reference.png)与参数 JSON |
| [reproduce.py](reproduce.py) | [带公式和积分曲线的三层图](output/fourier_shell.png)、[频谱验证图](output/fourier_validation.png)与数值 JSON |

四个脚本的海螺曲面默认参数与 `redraw_conch.py` 一致：矩形脉冲宽度 `--width 2`，最大显示半径 `--amplitude 0.05`，曲面范围 `--fmax 8 --tmax 5`，采样 `--nf 1201 --nt 101`，视角 `--elev 8 --azim -135`，输出 `--dpi 200`。曲面坐标统一为 `(-Re C, Im C, t)`，三维框比例为 `(1, 1, 0.78)`。

例如，改变单图的海螺参数：

```powershell
python scripts/fourier_shell/redraw_conch.py --width 3 --amplitude 0.05 --fmax 6 --tmax 4 --nf 1201 --nt 101 --elev 8 --azim -135
```

`reproduce_single.py` 与 `reproduce_reference.py` 还接受原有 `--duration` 和 `--scale`：前者等同 `--tmax`，后者按 `amplitude = scale × width` 换算。`redraw_conch.py` 的 `--output` 是 PNG 文件路径，其他三个脚本的 `--output` 是目录。三层图的数值积分截止频率默认是 `--cutoff 40`，不受曲面振幅缩放影响。

这里的数值与视角是根据参考图调校的数学复现，不代表原作者代码或精确绘图参数。
