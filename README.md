# GPT2_Chinese_Demo

## Required packages
```
requests
bs4
tqdm
lxml

flask
torch
transformers (3.5.1)
```
## Link
https://ckip.iis.sinica.edu.tw/service/gpt2/

## Crawl
```
python crawler.py
```

## Train
Use first chapter as evaluation data
```
CUDA_VISIBLE_DEVICES=0 ./train.sh
```
