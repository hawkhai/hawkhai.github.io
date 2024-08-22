#encoding=utf8
import os
import clip
import torch
#from torchvision.datasets import CIFAR100
import cv2
from PIL import Image

# Load the model
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load('ViT-B/32', device)

def test():
    from torchvision.datasets import CIFAR100

    # Download the dataset
    cifar100 = CIFAR100(root=os.path.expanduser("~/.cache"), download=True, train=False)

    # Prepare the inputs
    image, class_id = cifar100[3637]
    print(type(image), class_id)
    image_input = preprocess(image).unsqueeze(0).to(device)
    text_inputs = torch.cat([clip.tokenize(f"a photo of a {c}") for c in cifar100.classes]).to(device)

    # Calculate features
    with torch.no_grad():
        image_features = model.encode_image(image_input)
        text_features = model.encode_text(text_inputs)

    # Pick the top 5 most similar labels for the image
    image_features /= image_features.norm(dim=-1, keepdim=True)
    text_features /= text_features.norm(dim=-1, keepdim=True)
    similarity = (100.0 * image_features @ text_features.T).softmax(dim=-1)
    values, indices = similarity[0].topk(5)

    # Print the result
    print("\nTop predictions:\n")
    for value, index in zip(values, indices):
        print(f"{cifar100.classes[index]:>16s}: {100 * value.item():.2f}%")

# Download the dataset
#cifar100 = CIFAR100(root=os.path.expanduser("~/.cache"), download=True, train=False)
def cateclip(image, classes):
    # Prepare the inputs
    #image, class_id = cifar100[3637]
    image_input = preprocess(image).unsqueeze(0).to(device)
    
    classe_ids = [c.split(":")[-1].strip() for c in classes]
    classes = [c.split(":")[0].strip() for c in classes]
    text_inputs = torch.cat([clip.tokenize(f"a photo of a {c}") for c in classes]).to(device)

    # Calculate features
    with torch.no_grad():
        image_features = model.encode_image(image_input)
        text_features = model.encode_text(text_inputs)

    # Pick the top 5 most similar labels for the image
    image_features /= image_features.norm(dim=-1, keepdim=True)
    text_features /= text_features.norm(dim=-1, keepdim=True)
    similarity = (100.0 * image_features @ text_features.T).softmax(dim=-1)
    values, indices = similarity[0].topk(5)

    # Print the result
    print("\nTop predictions:\n")
    for value, index in zip(values, indices):
        print(f"{classes[index]:>16s}: {100 * value.item():.2f}%")
        return classe_ids[index]

def main():
    classes = r"""
animal
anime
cartoon:anime
building
architecture:building
food
goods
product:goods
indoor
night view:night
people
figure:people
plant
scenery
landscape:scenery
text
scanned document:text
vehicle
transportation:vehicle
    """.strip().split("\n")
    classes = [i.strip() for i in classes]
    cnclasses = r"""
动物:animal
动漫:anime
卡通:anime
建筑:building
食物:food
商品:goods
室内:indoor
夜景:night
人物:people
植物:plant
风景:scenery
文本:text
扫描件:text
交通工具:vehicle
    """.strip().split("\n")
    cnclasses = [i.strip() for i in cnclasses]
    for dir in os.listdir("dataset"):
        subdir = os.path.join("dataset", dir)
        if not os.path.isdir(subdir):
            continue
        for idir in os.listdir(subdir):
            ifile = os.path.join(subdir, idir)
            if ifile.endswith(".txt"):
                continue
            
            print("***" * 30)
            print(ifile)
            image = Image.open(ifile)
            print(cateclip(image, classes))
            break

if __name__ == "__main__":
    #test()
    main()
    print("ok")
