# Improving Loss Function for Deep CNN-based AIA
This is the official PyTorch implementation of the paper "[Improving loss function for deep convolutional neural network applied in automatic image annotation](https://doi.org/10.1007/s00371-023-02873-3)"

## Abstract
<div align="justify"> Automatic image annotation (AIA) is a mechanism for describing the visual content of an image with a list of semantic labels. Typically, there is a massive imbalance between positive and negative tags in a picture—in other words, an image includes much fewer positive labels than negative ones. This imbalance can negatively affect the optimization process and diminish the emphasis on gradients from positive labels during training. Although traditional annotation models mainly focus on model structure design, we propose a novel unsymmetrical loss function for a deep convolutional neural network (CNN) that performs differently on positives and negatives, which leads to a reduction in the loss contribution from negative labels and also highlights the contribution of positive ones. During the annotation process, we specify a threshold for each label separately based on the Matthews correlation coefficient (MCC). Extensive experiments on high-vocabulary datasets like Corel 5 k, IAPR TC-12, and Esp Game reveal that despite ignoring the semantic relationships between labels, our suggested approach achieves remarkable results compared to the state-of-the-art automatic image annotation models. </div>

## Datasets
There are three well-known datasets that are mostly used in AIA tasks. The table below provides details about these datasets. It is also possible to download them by the given links. (After downloading each dataset, replace its 'images' folder with the corresponding 'images' folder in the 'datasets' folder).

| *Dataset* | *Num of images* | *Num of training images* | *Num of testing images*  | *Num of vocabularies*  | *Labels per image*  | *Image per label* |
| :------------: | :-------------: | :-------------: | :-------------: | :------------: | :-------------: | :-------------: |
| [Corel 5k](https://www.kaggle.com/datasets/parhamsalar/corel5k) | 5,000 | 4,500 | 500 | 260 | 3.4 | 58.6 |
| [IAPR TC-12](https://www.kaggle.com/datasets/parhamsalar/iaprtc12) | 19,627 | 17,665 | 1962 | 291 | 5.7 | 347.7 |
| [ESP Game](https://www.kaggle.com/datasets/parhamsalar/espgame) | 20,770 | 18,689 | 2081 | 268 | 4.7 | 362.7 |

## Convolutional model
**TResNet-M**
![TResNet-M](https://user-images.githubusercontent.com/85555218/198952123-391fdfe0-4bd2-4129-982c-c1074279b099.png)

## Train and Evaluation
To train the model in Spyder IDE use the code below:
```python
run main.py --data {select training dataset} --loss-function {select loss function}
```
Please note that:
1) You should put **Corel-5k**, **ESP-Game** or **IAPR-TC-12** in {select training dataset}.

2) You should put the **proposedLoss** in {select loss function}.

To evaluate the model in Spyder IDE use the code below:
```python
run main.py --data {select training dataset} --loss-function {select loss function} --evaluate
```

## Results
Proposed method:
| data | precision | recall | f1-score | N+ |
| :------------: | :------------: | :------------: | :------------: | :------------: |
Corel 5k | 0.466 | 0.554 | **0.506** | **189** |
IAPR TC-12 | 0.503 | 0.562 | **0.531** | **285** |
ESP Game | 0.423 | 0.484 | **0.452** | **261** |

Proposed method + MCC:
| data | precision | recall | f1-score | N+ |
| :------------: | :------------: | :------------: | :------------: | :------------: |
Corel 5k | 0.484 | 0.563 | **0.520** | **191** |
IAPR TC-12 | 0.562 | 0.515 | **0.537** | **277** |
ESP Game | 0.508 | 0.421 | **0.461** | **255** |

## Citation
Please consider citing our paper in your publications if the project helps your research. BibTeX reference is as follows:
```
@article{salar2023improving,
  title={Improving loss function for deep convolutional neural network applied in automatic image annotation},
  author={Salar, Ali and Ahmadi, Ali},
  journal={The Visual Computer},
  pages={1--13},
  year={2023},
  publisher={Springer}
}
```
## Contact
I would be happy to answer any questions you may have - Ali Salar (parham1998resume@gmail.com)
