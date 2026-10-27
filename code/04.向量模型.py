"""
向量模型又叫做嵌入模型,也叫做embedding model
"""
# 导包
from zhipuai import ZhipuAI

# client = ZhipuAI(api_key="YOUR_API_KEY")
# 把 api_key="YOUR_API_KEY" 给删除掉,原因我们把api_key已经配置到环境当中了,可以省略不写
# 创建客户端
client = ZhipuAI()

# 和向量模型进行交互
response = client.embeddings.create(
    # embedding-2 => 1024维度
    # embedding-3 => 2048维度
    model="embedding-3", # 就是你的向量,智谱AI提供了两个向量模型
    input=[ # 这个就是你要向量化的内容
        "美食非常美味，服务员也很友好。这部电影既刺激又令人兴奋。阅读书籍是扩展知识的好方法",
        "我是宁欣怡",
        "你好"
    ],
)
# 获取第一个数据的维度(有多少个小数的集合,那么就是多少的维度)
# 第一条数据的向量数据和维度
print(response.data[0].embedding)
print(len(response.data[0].embedding))

print(response.data[1].embedding)
print(len(response.data[1].embedding))

print(response.data[2].embedding)
print(len(response.data[2].embedding))

# print(response.data[3].embedding)
# print(len(response.data[3].embedding))