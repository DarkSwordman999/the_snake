<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20&height=180&section=header&text=the_snake&fontSize=70&fontAlignY=35&desc=Python%20Game%20%7C%20Yandex%20Practicum&descAlignY=55&descSize=18" alt="the_snake banner" width="100%">

<br>

<img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Pygame-2.5.2-00A86B?style=for-the-badge&logo=python&logoColor=white" alt="Pygame">
<img src="https://img.shields.io/badge/Pytest-7.1.3-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" alt="Pytest">
<img src="https://img.shields.io/badge/Flake8-5.0.4-FFD43B?style=for-the-badge&logo=python&logoColor=black" alt="Flake8">
<img src="https://img.shields.io/badge/Yandex_Practicum-FF0000?style=for-the-badge&logo=yandex&logoColor=white" alt="Yandex Practicum">

<br><br>

### 🐍 Классическая «Змейка» на Python + Pygame

**Учебный проект в рамках курса «Python-разработчик» от Яндекс Практикума**

</div>

---

## 📖 О проекте

**the_snake** — классическая аркада «Змейка», реализованная на Python с использованием библиотеки **Pygame**.

Проект создан в рамках курса **«Python-разработчик»** от **Яндекс Практикума** и предназначен для практики:

* 🧩 объектно-ориентированного программирования;
* 🎮 построения игрового цикла и обработки событий;
* 🧪 написания и запуска unit-тестов с помощью `pytest`;
* 📐 соблюдения стандартов **PEP 8**;
* 🧹 статического анализа кода с помощью `flake8` и `pycodestyle`.

---

## 🎮 Игровой процесс

<table>
<tr>
<td align="center" width="33%">

### 🕹️ Управление

Стрелки клавиатуры

`↑` `↓` `←` `→`

</td>

<td align="center" width="33%">

### 🍎 Цель

Собирать яблоки

**+1 сегмент** за яблоко

</td>

<td align="center" width="33%">

### 💀 Проигрыш

Столкновение с собственным хвостом

Змейка сбрасывается

</td>
</tr>
</table>

### ✨ Особенности

| Возможность                | Описание                                                                                                                          |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| 🌀 **Телепортация**        | При выходе за границу экрана змейка появляется с противоположной стороны. Реализовано через `% SCREEN_WIDTH` и `% SCREEN_HEIGHT`. |
| 🔄 **Защита от разворота** | Нельзя мгновенно изменить направление на противоположное — например, `UP → DOWN`.                                                 |
| 🎲 **Случайный старт**     | После проигрыша змейка начинает движение в случайном направлении.                                                                 |
| 🎨 **Обводка объектов**    | Сегменты змейки и яблоко имеют границу `BORDER_COLOR` для лучшей видимости.                                                       |

---

## ⚙️ Константы игры

| Константа                |     Значение     | Описание                         |
| :----------------------- | :--------------: | :------------------------------- |
| `SCREEN_WIDTH`           |       `640`      | Ширина игрового поля, px         |
| `SCREEN_HEIGHT`          |       `480`      | Высота игрового поля, px         |
| `GRID_SIZE`              |       `20`       | Размер клетки сетки, px          |
| `GRID_WIDTH`             |       `32`       | Количество клеток по горизонтали |
| `GRID_HEIGHT`            |       `24`       | Количество клеток по вертикали   |
| `SPEED`                  |       `20`       | Скорость игры, FPS               |
| `SNAKE_COLOR`            |   `(0, 255, 0)`  | Цвет змейки                      |
| `APPLE_COLOR`            |   `(255, 0, 0)`  | Цвет яблока                      |
| `BOARD_BACKGROUND_COLOR` |    `(0, 0, 0)`   | Цвет игрового поля               |
| `BORDER_COLOR`           | `(93, 216, 228)` | Цвет границы объектов            |

---

## 🏗️ Архитектура

Проект построен с использованием **ООП** и включает три основных класса:

| Класс        | Родитель     | Назначение                                                              |
| :----------- | :----------- | :---------------------------------------------------------------------- |
| `GameObject` | —            | Базовый класс с полями `position`, `body_color` и методом `draw()`.     |
| `Apple`      | `GameObject` | Яблоко со случайной позицией на сетке и методом `randomize_position()`. |
| `Snake`      | `GameObject` | Управляет сегментами змейки, направлением движения, ростом и сбросом.   |

### 🔑 Основные методы `Snake`

* `get_head_position()` — возвращает координаты головы.
* `update_direction()` — применяет направление из `next_direction`.
* `move()` — перемещает змейку, проверяет столкновения и обновляет `last`.
* `reset()` — возвращает змейку в начальное состояние после проигрыша.

---

<details>
<summary><h2>🚀 Установка и запуск</h2></summary>

### 📋 Требования

* **Python 3.8+**
* **pip**
* Git

### 1. Клонирование репозитория

```bash
git clone https://github.com/DarkSwordman999/the_snake.git
cd the_snake
```

### 2. Создание виртуального окружения

```bash
python -m venv venv
```

### 3. Активация окружения

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 4. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 5. Запуск игры

```bash
python the_snake.py
```

</details>

---

<details>
<summary><h2>🧪 Тестирование</h2></summary>

Проект содержит набор тестов на базе **pytest**.

Конфигурация тестирования находится в `pytest.ini`.

### ▶️ Запуск

```bash
pytest
```

### 📁 Структура тестов

| Файл                     | Назначение                                              |
| :----------------------- | :------------------------------------------------------ |
| `conftest.py`            | Общие фикстуры для тестов                               |
| `test_code_structure.py` | Проверка структуры кода и соответствия PEP 8            |
| `test_main.py`           | Проверка игровой логики, движения, столкновений и роста |

### ⚙️ Параметры `pytest`

```ini
norecursedirs = env/*
testpaths = tests/
filterwarnings = ignore::DeprecationWarning
addopts = --tb=short -vv -p no:cacheprovider
```

* `norecursedirs` — исключает виртуальное окружение из поиска тестов.
* `testpaths` — указывает директорию с тестами.
* `filterwarnings` — игнорирует `DeprecationWarning`.
* `addopts` — включает подробный вывод и сокращённые traceback.

</details>

---

<details>
<summary><h2>🧹 Линтинг и стиль кода</h2></summary>

Проект ориентирован на соблюдение стандартов **PEP 8**.

Настройки `flake8` находятся в `setup.cfg`.

### ▶️ Запуск линтера

```bash
flake8 .
```

### ⚙️ Основные настройки

| Параметр          |                              Значение                              | Назначение                             |
| :---------------- | :----------------------------------------------------------------: | :------------------------------------- |
| `max-line-lenght` |                                `79`                                | Максимальная длина строки              |
| `max-complexity`  |                                `10`                                | Максимальная цикломатическая сложность |
| `ignore`          | `W503, F811, D100, D107, D203, D205, D213, D400, D401, N806, N818` | Игнорируемые правила                   |
| `exclude`         |                        `tests/, venv/, env/`                       | Исключённые директории                 |

> **Примечание:** в конфигурации используется `max-line-lenght`. Если это не намеренная настройка, параметр следует проверить — стандартное написание: `max-line-length`.

### 🔧 Используемые инструменты

* `flake8==5.0.4`
* `flake8-docstrings==1.7.0`
* `pep8-naming==0.13.3`
* `pycodestyle==2.9.1`

</details>

---

## 📂 Структура проекта

```text
the_snake/
│
├── tests/
│   ├── conftest.py
│   ├── test_code_structure.py
│   └── test_main.py
│
├── .gitignore
├── README.md
├── pytest.ini
├── requirements.txt
├── setup.cfg
└── the_snake.py
```

### 🗂️ Назначение основных файлов

| Файл               | Назначение                     |
| :----------------- | :----------------------------- |
| `the_snake.py`     | Основная логика и игровой цикл |
| `tests/`           | Автоматические тесты           |
| `pytest.ini`       | Конфигурация pytest            |
| `setup.cfg`        | Настройки flake8               |
| `requirements.txt` | Зависимости проекта            |
| `README.md`        | Документация                   |

---

## 🛠️ Технологический стек

<div align="center">

| Технология               |  Версия  | Назначение                         |
| :----------------------- | :------: | :--------------------------------- |
| 🐍 **Python**            |  `3.8+`  | Основной язык программирования     |
| 🎮 **Pygame**            |  `2.5.2` | Графика и игровой цикл             |
| 🧪 **Pytest**            |  `7.1.3` | Unit-тестирование                  |
| ⏱️ **pytest-timeout**    |  `2.1.0` | Контроль времени выполнения тестов |
| 🧹 **Flake8**            |  `5.0.4` | Статический анализ                 |
| 📝 **flake8-docstrings** |  `1.7.0` | Проверка документации              |
| 📐 **pep8-naming**       | `0.13.3` | Проверка именования                |
| 🔍 **pycodestyle**       |  `2.9.1` | Проверка PEP 8                     |

</div>

---

## 👤 Автор

<div align="center">

### **DarkSwordman999**

<a href="https://github.com/DarkSwordman999">
<img src="https://img.shields.io/badge/GitHub-DarkSwordman999-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
</a>

<br><br>

[💻 GitHub Repository](https://github.com/DarkSwordman999/the_snake)

</div>

---

<div align="center">

### 🎓 Yandex Practicum

Проект создан в рамках курса
**«Python-разработчик» от Яндекс Практикума**

<br>

> 🐍 **the_snake** — небольшой учебный проект,
> созданный для практики Python, ООП, тестирования и работы с Pygame.

<br>

⭐ **Если проект оказался полезным — поставь звезду репозиторию!**

</div>

