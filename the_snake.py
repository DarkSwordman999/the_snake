from random import choice
import pygame

# Константы для размеров поля и сетки
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвета
BOARD_BACKGROUND_COLOR = (0, 0, 0)
BORDER_COLOR = (93, 216, 228)
APPLE_COLOR = (255, 0, 0)
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки
SPEED = 10

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Змейка')
clock = pygame.time.Clock()


class GameObject:
    """Базовый класс для объектов на игровом поле."""

    def __init__(self, position=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2),
                 body_color=(255, 255, 255)):
        """Инициализация объекта.

        Args:
            position (tuple): Координаты объекта на экране.
            body_color (tuple): Цвет объекта в формате RGB.
        """
        self.position = position
        self.body_color = body_color

    def draw(self):
        """Метод для отрисовки объекта."""
        pass


class Apple(GameObject):
    """Класс яблока."""

    def __init__(self, snake_positions=None):
        """Инициализация яблока с случайной позицией."""
        super().__init__(body_color=APPLE_COLOR)
        self.snake_positions = snake_positions or []
        self.randomize_position()

    def randomize_position(self):
        """Устанавливает случайную позицию яблока на игровом поле."""
        while True:
            x = choice(range(GRID_WIDTH)) * GRID_SIZE
            y = choice(range(GRID_HEIGHT)) * GRID_SIZE
            new_position = (x, y)
            
            # Проверяем, чтобы яблоко не появилось на змейке
            if new_position not in self.snake_positions:
                self.position = new_position
                break

    def draw(self):
        """Отрисовывает яблоко на игровом поле."""
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Snake(GameObject):
    """Класс змейки."""

    def __init__(self):
        """Инициализация змейки."""
        super().__init__(
            position=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2),
            body_color=SNAKE_COLOR
        )
        self.length = 1
        self.positions = [self.position]
        self.direction = RIGHT
        self.next_direction = None
        self.last = None
        self.score = 0

    def get_head_position(self):
        """Возвращает координаты головы змейки."""
        return self.positions[0]

    def update_direction(self):
        """Обновляет направление движения после нажатия клавиши."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self):
        """Передвигает змейку на одну ячейку в текущем направлении."""
        cur = self.get_head_position()
        dx, dy = self.direction
        new_x = (cur[0] + dx * GRID_SIZE) % SCREEN_WIDTH
        new_y = (cur[1] + dy * GRID_SIZE) % SCREEN_HEIGHT
        new = (new_x, new_y)

        # Проверка столкновения с собой
        if new in self.positions[1:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.last = self.positions.pop()
            else:
                self.last = None

    def reset(self):
        """Сбрасывает змейку в начальное состояние."""
        self.length = 1
        self.positions = [self.position]
        self.direction = choice([UP, DOWN, LEFT, RIGHT])
        self.next_direction = None
        self.last = None
        self.score = 0

    def grow(self):
        """Увеличивает длину змейки."""
        self.length += 1
        self.score += 10

    def draw(self):
        """Отрисовывает змейку на экране."""
        # Отрисовка тела
        for position in self.positions[1:]:
            rect = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

        # Отрисовка головы (немного темнее для отличия)
        head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, head_rect)
        pygame.draw.rect(screen, BORDER_COLOR, head_rect, 2)

        # Затирание последнего сегмента
        if self.last:
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)


def handle_keys(snake_obj):
    """Обрабатывает нажатия клавиш для управления змейкой.

    Args:
        snake_obj (Snake): Объект змейки.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP and 
                    snake_obj.direction != DOWN):
                snake_obj.next_direction = UP
            elif (event.key == pygame.K_DOWN and 
                    snake_obj.direction != UP):
                snake_obj.next_direction = DOWN
            elif (event.key == pygame.K_LEFT and 
                    snake_obj.direction != RIGHT):
                snake_obj.next_direction = LEFT
            elif (event.key == pygame.K_RIGHT and 
                    snake_obj.direction != LEFT):
                snake_obj.next_direction = RIGHT


def draw_score(score):
    """Отрисовывает счет на экране."""
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))


def main():
    """Основной игровой цикл."""
    snake = Snake()
    apple = Apple(snake.positions)

    while True:
        clock.tick(SPEED)
        handle_keys(snake)
        snake.update_direction()
        snake.move()

        # Проверка, съела ли змейка яблоко
        if snake.get_head_position() == apple.position:
            snake.grow()
            apple = Apple(snake.positions)

        screen.fill(BOARD_BACKGROUND_COLOR)
        snake.draw()
        apple.draw()
        draw_score(snake.score)
        pygame.display.update()


if __name__ == '__main__':
    main()
