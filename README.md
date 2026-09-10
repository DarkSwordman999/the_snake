<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20&height=180&section=header&text=the_snake&fontSize=70&fontAlignY=35&desc=Python%20game%20%7C%20Yandex%20Practicum&descAlignY=55&descSize=18" alt="Banner" width="100%">

<img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Pygame-2.5.2-green?style=for-the-badge&logo=python&logoColor=white" alt="Pygame">
<img src="https://img.shields.io/badge/Pytest-7.1.3-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" alt="Pytest">
<img src="https://img.shields.io/badge/Flake8-5.0.4-yellow?style=for-the-badge&logo=python&logoColor=white" alt="Flake8">
<img src="https://img.shields.io/badge/Yandex-Practicum-red?style=for-the-badge&logo=yandex&logoColor=white" alt="Yandex Practicum">

<br><br>

<b>🐍 Классическая «Змейка» на Python с использованием Pygame</b>

</div>

<hr>

<h2>📖 О проекте</h2>
<p>
<b>the_snake</b> — это реализация популярной аркады «Змейка» на языке Python с графическим интерфейсом на базе библиотеки <b>Pygame</b>. Проект создан в рамках курса <b>«Python-разработчик»</b> от <b>Яндекс Практикума</b> для отработки навыков:
</p>
<ul>
  <li>Объектно-ориентированного программирования (ООП).</li>
  <li>Работы с игровым циклом и обработкой событий.</li>
  <li>Покрытия кода юнит-тестами с помощью <code>pytest</code>.</li>
  <li>Соблюдения стандартов <b>PEP 8</b> через линтеры <code>flake8</code> и <code>pycodestyle</code>.</li>
</ul>

<hr>

<h2>🎮 Игровой процесс</h2>

<table>
  <tr>
    <td align="center" width="33%">
      <h3>🕹️ Управление</h3>
      <p>Стрелки на клавиатуре</p>
      <p><code>↑ ↓ ← →</code></p>
    </td>
    <td align="center" width="33%">
      <h3>🍎 Цель</h3>
      <p>Собирать яблоки и расти</p>
      <p>+1 сегмент за яблоко</p>
    </td>
    <td align="center" width="33%">
      <h3>💀 Проигрыш</h3>
      <p>Столкновение с хвостом</p>
      <p>Змейка сбрасывается</p>
    </td>
  </tr>
</table>

<h3>Особенности реализации</h3>
<ul>
  <li><b>Телепортация через стены:</b> змейка не умирает при выходе за границы экрана — она появляется с противоположной стороны (реализовано через операцию <code>% SCREEN_WIDTH</code> и <code>% SCREEN_HEIGHT</code>).</li>
  <li><b>Защита от разворота на 180°:</b> нельзя мгновенно повернуть в противоположную сторону (например, из <code>UP</code> в <code>DOWN</code>).</li>
  <li><b>Случайный старт:</b> при сбросе после проигрыша змейка начинает движение в случайном направлении.</li>
  <li><b>Отрисовка с границей:</b> каждый сегмент змейки и яблоко обведены цветом <code>BORDER_COLOR</code> для четкости на черном фоне.</li>
</ul>

<hr>

<h2>⚙️ Константы игры</h2>

<table>
  <thead>
    <tr>
      <th align="left">Константа</th>
      <th align="left">Значение</th>
      <th align="left">Описание</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><code>SCREEN_WIDTH</code></td><td><code>640</code></td><td>Ширина игрового поля (px)</td></tr>
    <tr><td><code>SCREEN_HEIGHT</code></td><td><code>480</code></td><td>Высота игрового поля (px)</td></tr>
    <tr><td><code>GRID_SIZE</code></td><td><code>20</code></td><td>Размер одной клетки сетки (px)</td></tr>
    <tr><td><code>GRID_WIDTH</code></td><td><code>32</code></td><td>Кол-во клеток по горизонтали</td></tr>
    <tr><td><code>GRID_HEIGHT</code></td><td><code>24</code></td><td>Кол-во клеток по вертикали</td></tr>
    <tr><td><code>SPEED</code></td><td><code>20</code></td><td>Скорость движения (FPS)</td></tr>
    <tr><td><code>SNAKE_COLOR</code></td><td><code>(0, 255, 0)</code></td><td>Цвет змейки (зеленый)</td></tr>
    <tr><td><code>APPLE_COLOR</code></td><td><code>(255, 0, 0)</code></td><td>Цвет яблока (красный)</td></tr>
    <tr><td><code>BOARD_BACKGROUND_COLOR</code></td><td><code>(0, 0, 0)</code></td><td>Цвет фона (черный)</td></tr>
    <tr><td><code>BORDER_COLOR</code></td><td><code>(93, 216, 228)</code></td><td>Цвет обводки (голубой)</td></tr>
  </tbody>
</table>

<hr>

<h2>🏗️ Архитектура</h2>

<p>Проект построен на <b>ООП</b> и включает три класса:</p>

<table>
  <thead>
    <tr>
      <th align="left">Класс</th>
      <th align="left">Родитель</th>
      <th align="left">Назначение</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>GameObject</code></td>
      <td>—</td>
      <td>Базовый класс с полями <code>position</code> и <code>body_color</code>, а также методом <code>draw()</code></td>
    </tr>
    <tr>
      <td><code>Apple</code></td>
      <td><code>GameObject</code></td>
      <td>Яблоко со случайной позицией на сетке и методом <code>randomize_position()</code></td>
    </tr>
    <tr>
      <td><code>Snake</code></td>
      <td><code>GameObject</code></td>
      <td>Змейка: хранит список сегментов, направление, длину, обрабатывает движение и сброс</td>
    </tr>
  </tbody>
</table>

<h3>Ключевые методы Snake</h3>
<ul>
  <li><code>get_head_position()</code> — возвращает координаты головы.</li>
  <li><code>update_direction()</code> — применяет отложенное направление из <code>next_direction</code>.</li>
  <li><code>move()</code> — двигает змейку, проверяет столкновение с хвостом, обновляет <code>last</code> для стирания.</li>
  <li><code>reset()</code> — сбрасывает змейку в начальное состояние при проигрыше.</li>
</ul>

<hr>

<details>
<summary><b>🚀 Установка и запуск (нажмите, чтобы развернуть)</b></summary>

<br>

<h3>Требования</h3>
<ul>
  <li><b>Python</b> версии 3.8 или выше.</li>
  <li><b>pip</b> для установки зависимостей.</li>
</ul>

<h3>Шаги</h3>
<ol>
  <li>
    <b>Клонируйте репозиторий:</b>
    <pre><code>git clone https://github.com/DarkSwordman999/the_snake.git
cd the_snake</code></pre>
  </li>
  <li>
    <b>Создайте виртуальное окружение:</b>
    <pre><code>python -m venv venv</code></pre>
  </li>
  <li>
    <b>Активируйте его:</b>
    <pre><code># Windows:
venv\Scripts\activate

# macOS / Linux:
source venv/bin/activate</code></pre>
  </li>
  <li>
    <b>Установите зависимости:</b>
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>
    <b>Запустите игру:</b>
    <pre><code>python the_snake.py</code></pre>
  </li>
</ol>

</details>

<hr>

<details>
<summary><b>🧪 Тестирование (нажмите, чтобы развернуть)</b></summary>

<br>

<p>Проект покрыт тестами с использованием <b>pytest</b>. Конфигурация находится в <code>pytest.ini</code>.</p>

<h3>Запуск тестов</h3>
<pre><code>pytest</code></pre>

<h3>Структура тестов</h3>
<ul>
  <li><b><code>conftest.py</code></b> — общие фикстуры для тестов.</li>
  <li><b><code>test_code_structure.py</code></b> — проверка структуры кода и соответствия PEP 8.</li>
  <li><b><code>test_main.py</code></b> — тестирование игровой логики (движение змейки, столкновения, рост).</li>
</ul>

<h3>Параметры pytest</h3>
<ul>
  <li><code>norecursedirs = env/*</code> — игнорируется папка виртуального окружения.</li>
  <li><code>testpaths = tests/</code> — тесты ищутся только в папке <code>tests/</code>.</li>
  <li><code>filterwarnings = ignore::DeprecationWarning</code> — предупреждения о deprecated-функциях игнорируются.</li>
  <li><code>addopts = --tb=short -vv -p no:cacheprovider</code> — краткий вывод трейсбеков и подробный режим.</li>
</ul>

</details>

<hr>

<details>
<summary><b>🧹 Линтинг и стиль кода (нажмите, чтобы развернуть)</b></summary>

<br>

<p>Проект соответствует <b>PEP 8</b>. Настройки <code>flake8</code> находятся в <code>setup.cfg</code>.</p>

<h3>Запуск линтера</h3>
<pre><code>flake8 .</code></pre>

<h3>Настройки из <code>setup.cfg</code></h3>
<table>
  <thead>
    <tr>
      <th align="left">Параметр</th>
      <th align="left">Значение</th>
      <th align="left">Описание</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><code>max-line-lenght</code></td><td><code>79</code></td><td>Максимальная длина строки (в оригинале опечатка: <code>lenght</code> вместо <code>length</code>)</td></tr>
    <tr><td><code>max-complexity</code></td><td><code>10</code></td><td>Максимальная цикломатическая сложность</td></tr>
    <tr><td><code>ignore</code></td><td><code>W503, F811, D100, D107, D203, D205, D213, D400, D401, N806, N818</code></td><td>Игнорируемые правила</td></tr>
    <tr><td><code>exclude</code></td><td><code>tests/, venv/, env/</code></td><td>Исключенные директории</td></tr>
  </tbody>
</table>

<h3>Установленные линтеры</h3>
<ul>
  <li><code>flake8==5.0.4</code></li>
  <li><code>flake8-docstrings==1.7.0</code></li>
  <li><code>pep8-naming==0.13.3</code></li>
  <li><code>pycodestyle==2.9.1</code></li>
</ul>

</details>

<hr>

<h2>📂 Структура проекта</h2>

<pre><code>the_snake/
├── tests/
│   ├── conftest.py            # Общие фикстуры для тестов
│   ├── test_code_structure.py # Проверка структуры кода
│   └── test_main.py           # Тесты игровой логики
├── .gitignore                 # Исключения для Git
├── README.md                  # Документация проекта
├── pytest.ini                 # Конфигурация pytest
├── requirements.txt           # Зависимости проекта
├── setup.cfg                  # Конфигурация flake8
└── the_snake.py               # Основной файл игры</code></pre>

<hr>

<h2>🛠️ Технологии</h2>

<div align="center">

<table>
  <thead>
    <tr>
      <th align="left">Технология</th>
      <th align="left">Версия</th>
      <th align="left">Назначение</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><b>Python</b></td><td>3.8+</td><td>Язык программирования</td></tr>
    <tr><td><b>Pygame</b></td><td>2.5.2</td><td>Графика и игровой цикл</td></tr>
    <tr><td><b>Pytest</b></td><td>7.1.3</td><td>Тестирование</td></tr>
    <tr><td><b>pytest-timeout</b></td><td>2.1.0</td><td>Таймауты для тестов</td></tr>
    <tr><td><b>Flake8</b></td><td>5.0.4</td><td>Линтинг</td></tr>
    <tr><td><b>flake8-docstrings</b></td><td>1.7.0</td><td>Проверка docstring</td></tr>
    <tr><td><b>pep8-naming</b></td><td>0.13.3</td><td>Проверка именования по PEP 8</td></tr>
    <tr><td><b>pycodestyle</b></td><td>2.9.1</td><td>Стиль кода</td></tr>
  </tbody>
</table>

</div>

<hr>

<h2>👤 Автор</h2>

<div align="center">

<p><b>DarkSwordman999</b></p>

<a href="https://github.com/DarkSwordman999">
  <img src="https://img.shields.io/badge/GitHub-DarkSwordman999-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
</a>

</div>

<hr>

<div align="center">

<h3>🎓 Проект создан в рамках курса «Python-разработчик» от <a href="https://practicum.yandex.ru/">Яндекс Практикума</a></h3>

<p><i>Учебный проект. Создан в образовательных целях.</i></p>

</div>
