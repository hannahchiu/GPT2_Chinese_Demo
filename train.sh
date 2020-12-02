#!/bin/bash
set -x

MODEL=gpt2
TASK=sanguoyanyi

DATA_DIR=./data
TRAIN_DIR=${DATA_DIR}/train.txt
TEST_DIR=${DATA_DIR}/test.txt

DATETIME=$(date '+%Y:%m:%d-%H:%M:%S')
WANDB_PROJECT=${MODEL}-${TASK}
WANDB_NAME=ckip-${MODEL}-${TASK}-lm-${DATETIME}

BATCH_SIZE=6
EPOCH=5
STEP=100000
LENGTH=512

export WANDB_PROJECT

ARGS=(
	--seed 42
	--model_name_or_path ckiplab/gpt2-base-chinese
	--tokenizer_name bert-base-chinese
	--model_type ${MODEL}
	--fp16
	--fp16_opt_level O1
	--output_dir output5
	--run_name ${WANDB_NAME}
	--do_train
	--train_data_file ${TRAIN_DIR}
	--do_eval
	--eval_data_file ${TEST_DIR}
	--per_device_train_batch_size ${BATCH_SIZE}
	--per_device_eval_batch_size ${BATCH_SIZE}
#	--num_train_epochs ${EPOCH}
  --max_steps ${STEP}
	--block_size ${LENGTH}
	--evaluate_during_training
)

python run_language_modeling.py ${ARGS[*]}
