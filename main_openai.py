from openai import OpenAI
import os


def get_response():
    client = OpenAI(
        api_key="sk-8461d57af4954b3f82e20b589b7c58c7",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    completion = client.chat.completions.create(
        model="qwen-plus",
        messages=[{'role': 'system', 'content': 'You are a helpful assistant.'},
                  {'role': 'user', 'content': '你是谁？'}],
        stream=True,
        # 可选，配置以后会在流式输出的最后一行展示token使用信息
        stream_options={"include_usage": True}
        )
    for chunk in completion:
        print(chunk.model_dump_json())


if __name__ == '__main__':
    get_response()