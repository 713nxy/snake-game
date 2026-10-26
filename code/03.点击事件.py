"""
点击事件把原先的静态网页变成动态网页
click => 点击
    就是当点击之后,触发一个函数的执行
语法 =>
    组件.click(fn=函数,inputs=输入函数的参数,outputs=输出函数的参数)
"""
# 导包
import gradio as gr
# 先定义一个函数,传入一个年龄,返回年龄的两倍
def click_fn(age):
    """
    这个函数的作用就是传入一个年龄进来,然后把年龄乘以2,再返回出去
    """
    return age * 2

# 搭建UI组件
with gr.Blocks() as demo:
    # 定义一个数值输入组件 gr.Number
    age = gr.Number(label='年龄',placeholder="请输入您的年龄")
    # 按钮
    btn = gr.Button("提交")
    # 显示的组件
    show = gr.Textbox(label="年龄的两倍")

    """
    当我们点击按钮的时候,获取年龄,然后调用函数,把年龄给我传入进去
    在函数里面,让年龄乘以2,然后返回这个年龄
    最后将返回出来的年龄 在show 组件当中显示出来
    """
    # 组件.click(fn=函数,inputs=输入函数的参数,outputs=输出函数的参数)
    btn.click(fn=click_fn,inputs=age,outputs=show)

if __name__ == '__main__':
    demo.launch()