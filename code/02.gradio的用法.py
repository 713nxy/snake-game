"""
gradio是一个快速搭建UI界面的python的库文件
步骤:
    下载包 =>
        pip install gradio
    搭建UI界面
        A. 导包
            import gradio as gr
        B. 搭建UI界面
            with gr.Blocks() as demo:
        C. 启动这个UI界面
            demo.launch()
"""
# 导入包
import gradio as gr
# 搭建UI界面
with gr.Blocks() as demo:
    """
    创建一个文本输入框
        Textbox => 文本输入框
            label = > 标题
            placeholder => 输入提示
    """
    gr.Textbox(label="姓名",placeholder="请输入您的姓名")


    """
    创建一个滑块
        Slider => 滑块
            label => 标题
            minimum => 滑块的最小值
            maximum => 滑块的最大值
            value => 滑块的默认值
            step => 滑块的步子
            interactive => 和滑块进行交互
    """
    gr.Slider(label="声音",minimum=0,maximum=100,value=50,step=10,interactive=True)
if __name__ == '__main__':
    # 启动这个UI界面
    demo.launch()