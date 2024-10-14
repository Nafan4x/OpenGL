import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Параметры для задания 2
kx, ky = -0.5, 1.5
p = (1, -0.5)
alpha = 45
x, y = -10, 3
beta = -30

# Количество сторон n-угольника
N = 6


# Конвертация градусов в радианы
def deg_to_rad(deg):
    return deg * math.pi / 180


# Генерация вершин правильного N-угольника
def generate_polygon_vertices(n, radius=1):
    vertices = []
    for i in range(n):
        angle = 2 * math.pi * i / n
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        vertices.append((x, y))
    return vertices


# Рисование n-угольника
def draw_polygon(vertices):
    glBegin(GL_LINE_LOOP)
    for v in vertices:
        glVertex2f(v[0], v[1])
    glEnd()


colors = [(1, 0, 0), (1, 1, 1), (1, 0, 1), (1, 1, 0), (0, 0, 1),(0, 1, 0)]
# Рисование треугольников по вершинам n-угольника
def draw_triangles(vertices):
    glBegin(GL_TRIANGLES)
    n = len(vertices)
    for i in range(n):
        glColor3f(*colors[i])
        glVertex2f(vertices[i][0], vertices[i][1])
        glVertex2f(vertices[(i + 1) % n][0], vertices[(i + 1) % n][1])
        glVertex2f(0, 0)  # Треугольники соединяются с центром
    glEnd()


# Рисование пересекающихся линий
def draw_intersecting_lines(vertices):
    glBegin(GL_LINES)
    n = len(vertices)
    for i in range(n):
        for j in range(i + 1, n):
            glVertex2f(vertices[i][0], vertices[i][1])
            glVertex2f(vertices[j][0], vertices[j][1])
    glEnd()


# Рисование линий, соединяющих четные вершины
def draw_even_lines(vertices):
    glBegin(GL_LINES)
    for i in range(0, len(vertices), 2):
        glVertex2f(vertices[i][0], vertices[i][1])
        glVertex2f(vertices[(i + 2) % len(vertices)][0], vertices[(i + 2) % len(vertices)][1])
    glEnd()


# Функция для трансформаций и рисования фигур для задания 2
def draw_task_2():
    # Оригинальный треугольник
    glColor3f(1, 0, 0)  # Красный
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0, 0.5)
    glEnd()

    # Масштабированный и сдвинутый треугольник
    glColor3f(0, 1, 0)  # Зеленый
    glPushMatrix()
    glTranslatef(p[0], p[1], 0)
    glScalef(kx, ky, 1)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0, 0.5)
    glEnd()
    glPopMatrix()

    # Оригинальный прямоугольник
    glColor3f(0, 0, 1)  # Синий
    glBegin(GL_QUADS)
    glVertex2f(-0.5, -0.3)
    glVertex2f(0.5, -0.3)
    glVertex2f(0.5, 0.3)
    glVertex2f(-0.5, 0.3)
    glEnd()

    
    glPushMatrix()
    glTranslatef(x, y, 0)
    glRotatef(beta, 0, 0, 1)
    glTranslatef(-x, -y, 0)
    glBegin(GL_QUADS)
    glVertex2f(-0.5, -0.3)
    glVertex2f(0.5, -0.3)
    glVertex2f(0.5, 0.3)
    glVertex2f(-0.5, 0.3)
    glEnd()
    glPopMatrix()

    # Оригинальная линия
    glColor3f(1, 1, 0)  # Желтая
    glBegin(GL_LINES)
    glVertex2f(-1, -1)
    glVertex2f(1, 1)
    glEnd()

    # Повернутая линия
    glPushMatrix()
    glRotatef(alpha, 0, 0, 1)
    glBegin(GL_LINES)
    glVertex2f(-1, -1)
    glVertex2f(1, 1)
    glEnd()
    glPopMatrix()


# Функция для рисования креста (задание 3)
def draw_cross():
    glBegin(GL_TRIANGLES)

    # Первый треугольник (верхний)
    glVertex2f(0.0, 0.0)  # Вершина в центре
    glVertex2f(1.0, 0)  # Правая вершина
    glVertex2f(1.0, 0.5)  # Левая вершина

    # Второй треугольник (правый)
    glVertex2f(0.0, 0.0)  # Вершина в центре
    glVertex2f(-1, 0)  # Правая вершина
    glVertex2f(-1, 0.5)  # Левая вершина

    # Третий треугольник (нижний)
    glVertex2f(0.0, 0.0)  # Вершина в центре
    glVertex2f(0.5, -0.5)  # Правая вершина
    glVertex2f(0.3, -0.8)  # Левая вершина


    glVertex2f(0.0, 0.0)
    glVertex2f(-0.5, -0.5)
    glVertex2f(-0.3, -0.8)

    glEnd()

# Основная функция отображения
def display(current_task):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    if current_task == 1:
        # Задание 1: Рисуем n-угольник
        vertices = generate_polygon_vertices(N, radius=1)
        glColor3f(0, 1, 1)
        draw_polygon(vertices)

    elif current_task == 2:
        # Задание 1a: Рисуем треугольники
        vertices = generate_polygon_vertices(N, radius=1)

        glColor3f(1, 0, 0)
        draw_triangles(vertices)

    elif current_task == 3:
        # Задание 1б: Рисуем пересекающиеся линии
        vertices = generate_polygon_vertices(N, radius=1)
        glColor3f(0, 1, 0)
        draw_intersecting_lines(vertices)

    elif current_task == 4:
        # Задание 1в: Рисуем линии для четных вершин
        vertices = generate_polygon_vertices(N, radius=1)
        glColor3f(1, 1, 0)
        draw_even_lines(vertices)

    elif current_task == 5:
        # Задание 2: Применяем трансформации и рисуем фигуры
        draw_task_2()

    elif current_task == 6:
        # Задание 3: Рисуем крест
        glColor3f(1, 0, 1)
        draw_cross()

    pygame.display.flip()


# Инициализация OpenGL
def init_opengl():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-5, 5, -5, 5)


# Основная функция программы
def main():
    # Инициализация Pygame
    pygame.init()
    screen = pygame.display.set_mode((800, 800), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Pygame + OpenGL")

    # Инициализация OpenGL
    init_opengl()

    # Переменная для хранения текущего задания
    current_task = 1

    # Основной цикл
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Обработка нажатий клавиш
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    current_task = 2  # Задание 1 - n-угольник
                elif event.key == pygame.K_2:
                    current_task = 3  # Задание 1a - треугольники
                elif event.key == pygame.K_3:
                    current_task = 1  # Задание 1б - пересекающиеся линии
                elif event.key == pygame.K_4:
                    current_task = 4  # Задание 1в - четные вершины
                elif event.key == pygame.K_5:
                    current_task = 5  # Задание 2 - трансформации
                elif event.key == pygame.K_6:
                    current_task = 6  # Задание 3 - крест

        # Вызов функции отображения текущего задания
        display(current_task)

    pygame.quit()


if __name__ == "__main__":
    main()
