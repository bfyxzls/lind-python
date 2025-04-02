from transformers import pipeline

# 加载 gpt2-medium 模型，1.41G左右,./user/.cache/huggingface/models--gpt2-medium
chatbot = pipeline("text-generation", model="EleutherAI/gpt-neo-2.7B", truncation=True)

# 定义输入问题
input_question = "请帮我推荐一本好看的历史书，它可以在人与人沟通中帮到我的。"

# 生成响应
response = chatbot(input_question, max_length=100, num_return_sequences=1)

# 输出结果
print("输入问题:", input_question)
print("模型输出:", response[0]['generated_text'])
