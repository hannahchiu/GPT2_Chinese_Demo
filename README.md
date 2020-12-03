# GPT2_Chinese_Demo

## Required packages
* Crawler:
```
requests
lxml
bs4
tqdm
```
* Training:
```
torch
transformers (3.5.1)
wandb
```
* Web:
```
flask
```

## Link
https://ckip.iis.sinica.edu.tw/service/gpt2/

## Crawl
Dataset: 三國演義

Source: [Wikisource](https://zh.wikisource.org/wiki/三國演義)
```
python crawler.py
```
Data will be saved to `./data`

## Train
We used first chapter as evaluation data
```
CUDA_VISIBLE_DEVICES=0 ./train.sh
```
Model will be saved to `./output`
