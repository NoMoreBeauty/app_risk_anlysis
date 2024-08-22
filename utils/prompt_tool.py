import os

def get_prompt(prompt_path:str)->str:
    with open(prompt_path, 'r', encoding='utf-8') as fin:
        prompt = fin.read()
        # print(prompt)
        fin.close()
    return prompt


if __name__ == '__main__':
    # pass
    print(get_prompt('field_filter.txt'))