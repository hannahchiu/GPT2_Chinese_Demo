from flask import Flask, render_template, request
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tokenizer = AutoTokenizer.from_pretrained('bert-base-chinese')
model = AutoModelForCausalLM.from_pretrained('ckiplab/gpt2-base-chinese')
model2 = AutoModelForCausalLM.from_pretrained('output5/checkpoint-3000')
max_input_length = 50
max_output_length = 50

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", res="外界批評行政院逾期未開治安、食安等各項會報")


@app.route('/', methods=['POST'])
def upload():
    input_text = request.values['news']
    input_text = input_text.replace("，", ",")
    # input_ids = tokenizer.encode(input_text, return_tensors="pt")
    # no [CLS] & [SEP]
    tokenized_tokens = tokenizer.tokenize(input_text)
    input_ids = tokenizer.convert_tokens_to_ids(tokenized_tokens)
    input_ids = torch.tensor([input_ids])
    previous_input = input_ids[:, :max(len(input_ids[0]) - max_input_length, 0)]
    input_ids = input_ids[:, -max_input_length:]
    output = model.generate(input_ids, max_length=len(input_ids[0]) + max_output_length, repetition_penalty=1.2)
    output = tokenizer.decode(torch.cat([previous_input[0], output[0]]))
    output = output.replace(" ", "").replace("[CLS]", "").replace("[SEP]", "").replace("[UNK]", "").replace(",", "，")
    return render_template("index.html", res=output)


@app.route('/three')
def index2():
    return render_template("index.html", res="話說天下大勢，分久必合，合久必分。")


@app.route('/three', methods=['POST'])
def upload2():
    input_text = request.values['news']
    input_text = input_text.replace("，", ",")
    # input_ids = tokenizer.encode(input_text, return_tensors="pt")
    # no [CLS] & [SEP]
    tokenized_tokens = tokenizer.tokenize(input_text)
    input_ids = tokenizer.convert_tokens_to_ids(tokenized_tokens)
    input_ids = torch.tensor([input_ids])
    previous_input = input_ids[:, :max(len(input_ids[0]) - max_input_length, 0)]
    input_ids = input_ids[:, -max_input_length:]
    output = model2.generate(input_ids, max_length=len(input_ids[0]) + max_output_length, repetition_penalty=1.2)
    output = tokenizer.decode(torch.cat([previous_input[0], output[0]]))
    output = output.replace(" ", "").replace("[CLS]", "").replace("[SEP]", "").replace("[UNK]", "").replace(",", "，")
    return render_template("index.html", res=output)


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.jinja_env.auto_reload = True
    app.run(host='0.0.0.0', port=8000, threaded=True, debug=True)
