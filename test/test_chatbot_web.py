from flask import Flask, request, jsonify
from transformers import pipeline
import logging
# https://www.zhihu.com/tardis/bd/art/613895056?source_id=1001
# 初始化 Flask 应用
app = Flask(__name__)

# 设置日志记录
logging.basicConfig(level=logging.INFO)

# 加载对话生成模型
chatbot = pipeline("text-generation", model="gpt2-medium", truncation=True)


@app.route('/chat', methods=['POST'])
def chat():
    try:
        # 获取用户输入
        user_input = request.json.get('message')

        if not user_input:
            return jsonify({"error": "No message provided"}), 400

        # 生成响应
        response = chatbot(user_input, max_length=100, num_return_sequences=1)

        # 返回生成的文本
        return jsonify({"response":  response[0]['generated_text']})

    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return jsonify({"error": "An error occurred while processing your request."}), 500


if __name__ == '__main__':
    app.run(port=5000)