# 这个例子在运行时报错
import torch
from transformers import BertTokenizer, BertForSequenceClassification

# 加载预训练模型和分词器
model_name = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)

# 准备输入数据
text = "This is a sample text for classification."
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)

# 将模型设置为评估模式
model.eval()

# 推理
with torch.no_grad():
    outputs = model(**inputs)

# 获取预测结果
logits = outputs.logits
predicted_class = torch.argmax(logits, dim=1)

print(f"Predicted class: {predicted_class.item()}")
