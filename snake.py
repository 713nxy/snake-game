
import random
import sys
from collections import deque
import pygame



# ========== 基础配置 ==========
pygame.display.init()
pygame.font.init()

CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20

SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT

# 颜色
BLACK = (15, 15, 15)
WHITE = (240, 240, 240)
RED = (220, 60, 60)
GREEN = (60, 200, 80)
DARK_GREEN = (40, 150, 60)
GRAY = (40, 40, 40)

# 方向
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("贪吃蛇 Snake")
clock = pygame.time.Clock()



def load_font(size):
    """加载字体，优先使用 Windows 中文字体。"""
    import os

    font_paths = [
        r"C:\Windows\Fonts\msyh.ttc",   # 微软雅黑
        r"C:\Windows\Fonts\simhei.ttf", # 黑体
        r"C:\Windows\Fonts\simsun.ttc", # 宋体
        r"C:\Windows\Fonts\arial.ttf",  # Arial
    ]

    for path in font_paths:
        if os.path.isfile(path):
            try:
                return pygame.font.Font(path, size)
            except (pygame.error, OSError):
                continue

    # 如果没有找到指定字体，使用 Pygame 默认字体
    return pygame.font.Font(None, size)


font = load_font(26)
small_font = load_font(20)


class Snake:
    """贪吃蛇类，蛇头位于 body[0]。"""

    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = RIGHT
        self.turn_queue = deque()

    def queue_direction(self, new_dir):
        """缓存转向，防止连续输入造成直接反向。"""
        last_dir = (
            self.turn_queue[-1]
            if self.turn_queue
            else self.direction
        )

        # 忽略相同方向和反方向
        if new_dir == last_dir:
            return

        if new_dir == (-last_dir[0], -last_dir[1]):
            return

        # 最多缓存两个转向
        if len(self.turn_queue) < 2:
            self.turn_queue.append(new_dir)

    def update_direction(self):
        """每次移动最多处理一个转向。"""
        if self.turn_queue:
            self.direction = self.turn_queue.popleft()

    def next_head(self):
        """计算下一步蛇头位置，不修改蛇身。"""
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        return head_x + dx, head_y + dy

    def check_collision(self, new_head, will_grow):
        """检查下一步是否撞墙或撞到自身。"""

        x, y = new_head

        # 撞墙
        if not (0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT):
            return True

        # 如果不增长，尾巴本次会移走，因此不检查最后一节
        body_to_check = self.body if will_grow else self.body[:-1]

        # 撞到身体
        if new_head in body_to_check:
            return True

        return False

    def move(self, new_head, will_grow):
        """执行移动；吃到食物时保留尾巴，实现增长。"""
        self.body.insert(0, new_head)

        if not will_grow:
            self.body.pop()


def spawn_food(snake):
    """在空格中随机生成食物；棋盘填满时返回 None。"""
    occupied = set(snake.body)
    empty_cells = [
        (x, y)
        for x in range(GRID_WIDTH)
        for y in range(GRID_HEIGHT)
        if (x, y) not in occupied
    ]

    return random.choice(empty_cells) if empty_cells else None


def draw_game(snake, food, score, fps):
    """绘制游戏画面。"""
    screen.fill(BLACK)

    # 网格线
    for x in range(0, SCREEN_WIDTH, CELL_SIZE):
        pygame.draw.line(
            screen, GRAY, (x, 0), (x, SCREEN_HEIGHT)
        )

    for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
        pygame.draw.line(
            screen, GRAY, (0, y), (SCREEN_WIDTH, y)
        )

    # 食物
    if food is not None:
        center = (
            food[0] * CELL_SIZE + CELL_SIZE // 2,
            food[1] * CELL_SIZE + CELL_SIZE // 2,
        )
        pygame.draw.circle(
            screen, RED, center, CELL_SIZE // 2 - 2
        )

    # 蛇身
    for i, (x, y) in enumerate(snake.body):
        color = WHITE if i == 0 else (
            GREEN if i % 2 else DARK_GREEN
        )

        rect = pygame.Rect(
            x * CELL_SIZE,
            y * CELL_SIZE,
            CELL_SIZE - 1,
            CELL_SIZE - 1,
        )

        pygame.draw.rect(
            screen, color, rect, border_radius=4
        )

    # 分数和速度
    text = font.render(
        f"分数: {score}   速度: {fps}",
        True,
        WHITE,
    )
    screen.blit(text, (10, 8))

    pygame.display.flip()


def game_over_screen(score, win):
    """显示结束界面，返回 True 表示重开，False 表示退出。"""
    screen.fill(BLACK)

    if win:
        title_text = f"通关！最终分数: {score}"
        title_color = GREEN
    else:
        title_text = f"游戏结束！最终分数: {score}"
        title_color = RED

    title = font.render(title_text, True, title_color)
    tip = small_font.render(
        "按 R 重新开始，按 Q 退出",
        True,
        WHITE,
    )

    screen.blit(
        title,
        (
            (SCREEN_WIDTH - title.get_width()) // 2,
            SCREEN_HEIGHT // 2 - 40,
        ),
    )

    screen.blit(
        tip,
        (
            (SCREEN_WIDTH - tip.get_width()) // 2,
            SCREEN_HEIGHT // 2 + 20,
        ),
    )

    pygame.display.flip()

    while True:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True

                if event.key in (pygame.K_q, pygame.K_ESCAPE):
                    return False


def main():
    key_map = {
        pygame.K_UP: UP,
        pygame.K_w: UP,
        pygame.K_DOWN: DOWN,
        pygame.K_s: DOWN,
        pygame.K_LEFT: LEFT,
        pygame.K_a: LEFT,
        pygame.K_RIGHT: RIGHT,
        pygame.K_d: RIGHT,
    }

    try:
        # 外层循环：支持重新开始
        while True:
            snake = Snake()
            food = spawn_food(snake)
            score = 0
            base_fps = 8

            alive = True
            win = False

            while alive:
                # 事件处理
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            return

                        if event.key in key_map:
                            snake.queue_direction(key_map[event.key])

                # 每次移动只消费一个转向
                snake.update_direction()

                # 先计算下一步，再判断是否吃到食物
                new_head = snake.next_head()
                will_grow = new_head == food

                # 移动前进行碰撞检查
                if snake.check_collision(new_head, will_grow):
                    alive = False
                    break

                # 执行移动
                snake.move(new_head, will_grow)

                # 吃到食物
                if will_grow:
                    score += 10
                    food = spawn_food(snake)

                    # 棋盘填满，游戏胜利
                    if food is None:
                        win = True
                        alive = False

                # 分数越高，移动越快，最高 20 FPS
                fps = min(base_fps + score // 50, 20)

                draw_game(snake, food, score, fps)
                clock.tick(fps)

            # 游戏结束后等待玩家选择
            if not game_over_screen(score, win):
                break

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
