"""
这一次我们换一个模型来使用,使用智谱AI大模型
    1. 注册账号 => https://www.bigmodel.cn/invite?icode=BD1t%2FZ0paEIra%2Bdacfj9X3HEaazDlIZGj9HxftzTbt4%3D
    2. 申请key =>
        3b3fa69b51c3453d910fad6d3333edaa.KYY9bKZcSXa5r1tt
        我们把这个key存储到环境变量当中
                变量名                         变量值
           zhipuai_api_key          就是你刚刚从官网当中申请到的这个key
        注意: 你把这个key配置大环境当中的时候,需要你重启开发工具
    3. 下载包 =>
        pip install zhipuai
        注意: 你在下载包的时候,需要下载到你的虚拟环境里面
    4. 编写操作
        A. 导包
            from zhipuai import ZhipuAI
        B. 创建聊天客户端
            client = ZhipuAI()
        C. 和AI大模型进行交互工作
            res = client.chat.completions.create(
                model="glm-4-plus",
                messages = [
                    {"role":"system","content":"你是一个专业的语文老师!"},
                    {"role":"user","content":"请背诵出师表"}
                ]
            )
        D. 获取AI的回复结果
            print(res.choices[0].messages.content)

"""
# 导包
from zhipuai import ZhipuAI
# 创建聊天客户端
client = ZhipuAI()
# 和AI大模型进行交互工作
res = client.chat.completions.create(
    model="glm-5.3-flashx",     # 你和AI大模型交互的时候,你需要使用到的是那个模型
    messages=[              # 你和AI聊天的消息
        {"role":"system","content":"你是一个资深的编程大师"},
        {"role":"user","content":"用python写一个贪吃蛇小游戏"}
    ]
)
# 获取AI大模型的回复结果
print(res.choices[0].message.content)

"""
你在编写这个代码的时候,有可能会报错 => ModuleNotFoundError: No module named 'sniffio'
所以说: 我们需要去下载这个模型包 => 
    pip install sniffio
然后你再运行


"""