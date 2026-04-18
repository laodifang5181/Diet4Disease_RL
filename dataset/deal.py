import json
import sys
import os
import time
sys.path.append(R"")
import GPT_4o

a = 0

f = open(R"", 'r', encoding="utf-8")
lines = f.readlines()
f.close()


for line in lines[:]:
    a = a + 1
    print(a) 
    l = json.loads(line)
    image_name = l["image"]
    disease = l["disease"]
    dish = l["dish"]

    image = ""
    prompt = f"我会给你提供一个二元组,包括一道菜的菜名和一个疾病的名称,你需要:\n\
1:从一名厨师的角度分析,这道菜所包含的主要食材.\n\
2:从一名医生的角度分析,这个疾病的忌口有哪些.\n\
接下来我会给你输出的例子,这个例子用于规定你回答的整体格式.\n\
例子1:从厨师的角度分析，红烧肉主要食材包括五花肉等。从医生的角度分析，甲亢患者需要忌口高碘和高脂肪的食物。\n\
例子2:从厨师的角度分析，北京烤鸭主要食材包括鸭肉等。从医生的角度分析，扁桃体炎患者需要忌口油腻、辛辣、过于咸、热的食物，以及容易刺激喉咙的食物。\n\
接下来回答:{dish}, {disease}:"
    print(prompt)

    result = GPT_4o.callAPI_meta(prompt, image)

    t = {}
    t["dish"] = l["dish"]
    t["image"] = l["image"]
    t["disease"] = l["disease"]
    t["result"] = l["result"]
    t["model_result"] = result
    print(t)

    temp = json.dumps(t, ensure_ascii=False)
    f = open(R"", "a", encoding="utf-8")
    f.write(temp + "\n")
    f.close()