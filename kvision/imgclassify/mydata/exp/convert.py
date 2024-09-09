import os, sys
import torch
sys.path.append(r"D:\kSource\pythonx\note\infai\fastocr\image_classification")
#os.system("D:\kSource\pythonx\note\infai\fastocr\image_classification\pnnx.exe best.pt inputshape=[1,3,224,224]")
#os.system("python3 -m onnxsim mobilenet_v2.onnx sim.onnx")

import torch
import torchvision.models as models

# 定义模型结构（这里直接使用 torchvision 中的 MobileNetV2）
model = models.mobilenet_v2(pretrained=False)  # 注意这里pretrained=False，因为我们要加载自己的权重

# 加载微调后的模型权重
model_path = 'best.pt'  # 替换为你的模型文件路径
checkpoint = torch.load(model_path, map_location=torch.device('cpu'))

# 将权重加载到模型中
#model.load_state_dict(checkpoint['state_dict'])  # 注意可能需要根据你的checkpoint结构进行调整

# 如果checkpoint中还包含优化器等其他信息，可以在这里加载它们
# optimizer.load_state_dict(checkpoint['optimizer'])

# 设置为评估模式
model.eval()

x = torch.randn(1, 3, 224, 224)
traced_script_module = torch.jit.trace(model, x, strict=False)
traced_script_module.save("ts.pt")
os.system(r"D:\kSource\pythonx\note\infai\fastocr\image_classification\pnnx.exe ts.pt inputshape=[1,3,224,224]")

torch_out = torch.onnx._export(model, x, "mobilenet_v2.onnx", export_params=True)
os.system("python3 -m onnxsim mobilenet_v2.onnx sim.onnx")

# # 3. onnx --> ncnn
# os.system("D:\kSource\pythonx\note\infai\ncnn\ncnn-20240410-windows-vs2019-shared\x64\bin\onnx2ncnn.exe sim.onnx ncnn.param ncnn.bin")

# # 4. ncnn --> optmize ---> ncnn
# os.system("D:\kSource\pythonx\note\infai\ncnn\ncnn-20220729-windows-vs2019-md-debug\windows-x64\bin\ncnnoptimize.exe ncnn.param ncnn.bin opt.param opt.bin 1")  # 数字0 代表fp32 ；1代表fp16
