import gradio as gr
import spaces
from transformers import Qwen2VLForConditionalGeneration, AutoProcessor
from qwen_vl_utils import process_vision_info
import torch
from PIL import Image
import subprocess
from datetime import datetime
import numpy as np
import os

# subprocess.run('pip install flash-attn --no-build-isolation', env={'FLASH_ATTENTION_SKIP_CUDA_BUILD': "TRUE"}, shell=True)

# models = {
#     "Qwen/Qwen2-VL-7B-Instruct": AutoModelForCausalLM.from_pretrained("Qwen/Qwen2-VL-7B-Instruct", trust_remote_code=True, torch_dtype="auto", _attn_implementation="flash_attention_2").cuda().eval()

# }
def array_to_image_path(image_array):
    # Convert numpy array to PIL Image
    img = Image.fromarray(np.uint8(image_array))
    
    # Generate a unique filename using timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"image_{timestamp}.png"
    
    # Save the image
    img.save(filename)
    
    # Get the full path of the saved image
    full_path = os.path.abspath(filename)
    
    return full_path
    
models = {
    "Qwen/Qwen2-VL-7B-Instruct": Qwen2VLForConditionalGeneration.from_pretrained("Qwen/Qwen2-VL-7B-Instruct", trust_remote_code=True, torch_dtype="auto").cuda().eval()

}

processors = {
    "Qwen/Qwen2-VL-7B-Instruct": AutoProcessor.from_pretrained("Qwen/Qwen2-VL-7B-Instruct", trust_remote_code=True)
}

DESCRIPTION = "[Qwen2-VL-7B Demo](https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct)"

kwargs = {}
kwargs['torch_dtype'] = torch.bfloat16

user_prompt = '<|user|>\n'
assistant_prompt = '<|assistant|>\n'
prompt_suffix = "<|end|>\n"

@spaces.GPU
def run_example(image, text_input=None, model_id="Qwen/Qwen2-VL-7B-Instruct"):
    imgclear = False
    if type(image) == type(""):
        image = np.array(Image.open(image))
        imgclear = True
    
    image_path = array_to_image_path(image)
    
    print(image_path)
    model = models[model_id]
    processor = processors[model_id]

    prompt = f"{user_prompt}<|image_1|>\n{text_input}{prompt_suffix}{assistant_prompt}"
    image = Image.fromarray(image).convert("RGB")
    messages = [
    {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "image": image_path,
                },
                {"type": "text", "text": text_input},
            ],
        }
    ]
    
    # Preparation for inference
    text = processor.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    image_inputs, video_inputs = process_vision_info(messages)
    inputs = processor(
        text=[text],
        images=image_inputs,
        videos=video_inputs,
        padding=True,
        return_tensors="pt",
    )
    inputs = inputs.to("cuda")
    
    # Inference: Generation of the output
    generated_ids = model.generate(**inputs, max_new_tokens=1024)
    generated_ids_trimmed = [
        out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
    ]
    output_text = processor.batch_decode(
        generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
    )
    
    if imgclear and os.path.exists(image_path):
        os.remove(image_path)
    return output_text[0]

css = """
  #output {
    height: 500px; 
    overflow: auto; 
    border: 1px solid #ccc; 
  }
"""

if __name__ == "__main__":
    input_img = "test.jpg"
    text_input = r"""你是一个图片分类器。根据定义的图片分类及其提示词列表，请问这张图片属于哪个分类？{
    "animal": ["动物", "哺乳动物", "鸟类", "爬行动物", "鱼类", "昆虫", "野生动物", "宠物"],
    "cartoon": ["动漫", "卡通", "动画系列", "漫画", "日本漫画"], # animation
    "building": ["建筑", "建筑学", "摩天大楼", "历史建筑", "办公楼"], # architecture
    "food": ["食物", "菜肴", "餐点", "美食", "小吃", "饮料", "甜点"],
    "goods": ["商品", "产品", "货物", "消费品", "日常用品", "电视机", "电脑"], # products
    "nightscape": ["夜景", "城市灯光", "星空"],
    "people": ["人物", "肖像", "人类"],
    "plant": ["植物", "花卉", "树木", "灌木", "叶子", "植被", "灌木丛"],
    "landscape": ["风景", "自然景观", "地形", "乡村风光", "山脉", "湖泊", "海滩", "森林"], # nature
    "text": ["文本", "扫描件", "书写内容", "手稿", "屏幕截图"],
    "vehicle": ["车辆", "汽车", "自行车", "公交车", "火车", "飞机", "船", "摩托车"],
    "abstract": ["抽象艺术", "概念艺术", "现代艺术", "非具象艺术", "表现主义", "超现实主义", "极简主义"],
}"""
    model_selector = "Qwen/Qwen2-VL-7B-Instruct"
    output_text = run_example(input_img, text_input, model_selector)
    print(output_text)

if __name__ == "__main__z":
    with gr.Blocks(css=css) as demo:
        gr.Markdown(DESCRIPTION)
        with gr.Tab(label="Qwen2-VL-7B Input"):
            with gr.Row():
                with gr.Column():
                    input_img = gr.Image(label="Input Picture")
                    model_selector = gr.Dropdown(choices=list(models.keys()), label="Model", value="Qwen/Qwen2-VL-7B-Instruct")
                    text_input = gr.Textbox(label="Question")
                    submit_btn = gr.Button(value="Submit")
                with gr.Column():
                    output_text = gr.Textbox(label="Output Text")

            submit_btn.click(run_example, [input_img, text_input, model_selector], [output_text])

    demo.queue(api_open=False)
    demo.launch(debug=True)
