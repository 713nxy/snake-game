# 🐍 贪吃蛇 (Snake Game)

这是一个使用 Python 和 Pygame 库编写的经典贪吃蛇小游戏。代码结构清晰，修复了常见的 180 度掉头自杀、食物生成死循环等潜在 Bug。

## ✨ 功能特性
- 🎮 **流畅控制**：支持方向键和 WASD 控制。
- ⚡ **动态难度**：随着分数增加，蛇的移动速度会逐渐加快。
- 🛡️ **防自杀机制**：加入了方向输入队列，完美解决快速连续按键导致 180 度掉头撞死自己的问题。
- 🏆 **通关判定**：蛇填满整个棋盘时会触发通关提示，而不是卡死。
- 🌍 **跨平台中文支持**：优化了字体加载逻辑，Windows/Mac/Linux 均可正常显示中文。

## 📸 游戏截图
*(建议在 GitHub 上点击 Edit 上传一张游戏运行截图，然后替换下面的图片链接)*
![游戏运行截图](<img width="451" height="325" alt="image" src="https://github.com/user-attachments/assets/0e7ab7e0-bc13-42bd-85ad-58e24e72e292" /><img width="452" height="323" alt="屏幕截图 2026-10-26 171147" src="https://github.com/user-attachments/assets/b1066897-cef7-4853-bc12-1efe4918258c" />

)

## 🛠️ 环境要求
- Python 3.8 或更高版本
- Pygame 2.0 或更高版本（因为使用了 `border_radius` 等新特性）

## 🚀 安装与运行
 ##安装依赖
pip install pygame

##启动游戏
python snake.py  # 请替换为你实际的主程序文件名
