import pygame
from pygame.locals import *
from OpenGL.GL import *
from math import cos, sin, pi


def clear_draw():
    pass

# Функция для вычисления координат вершин правильного n-угольника
def compute_polygon_vertices(n, radius):
    vertices = []
    for i in range(n):
        # Угол для каждой вершины
        angle = 2 * pi * i / n  # равномерное распределение углов
        print(angle)
        x = radius * cos(angle)
        y = radius * sin(angle)
        vertices.append((x, y))
    print(vertices)
    return vertices

# Инициализация OpenGL и Pygame
def init_pygame_opengl():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(0, 0, 0, 1)  # Устанавливаем белый фон
    glPointSize(10)  # Размер точки по умолчанию (можно менять для эксперимента)

    # Включаем сглаживание точек
    glEnable(GL_POINT_SMOOTH)
    glHint(GL_POINT_SMOOTH_HINT, GL_NICEST)

    # Устанавливаем режим проекции
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.5, 1.5, -1.5, 1.5, -1, 1)
    glMatrixMode(GL_MODELVIEW)


def draw_task3():
    glBegin(GL_LINE_STRIP)  # Начинаем рисовать замкнутую ломаную линию
    glVertex2f(-0.7, 1)  # Первая вершина
    glVertex2f(-0.7, -1)  # Вторая вершина
    glVertex2f(-0.2, -1)  # Третья вершина
    glVertex2f(-0.5, -0.6)  # Четвертая вершина (автоматически замкнется на первую)
    glVertex2f(0.1, 0.6)
    glVertex2f(0.6, -0.2)
    glVertex2f(0.1, -1)
    glVertex2f(1, -1)
    glEnd()

def draw_task4():
    glBegin(GL_LINE_LOOP)  # Начинаем рисовать замкнутую ломаную линию
    glVertex2f(0, 0)  # Первая вершина
    glVertex2f(1, 0)  # Вторая вершина
    glVertex2f(1, 0.7)  # Третья вершина
    glVertex2f(0.3, 0.3)  # Четвертая вершина (автоматически замкнется на первую)
    glVertex2f(-0.4, 0.7)
    glVertex2f(-1, 0.2)
    glVertex2f(-0.7, -0.7)
    glVertex2f(0.2, -1)


    glEnd()

def draw_points(vertices, point_size):
    glPointSize(point_size)
    glBegin(GL_POINTS)
    glColor3f(1.0, 1.0, 1.0)  # Красный цвет точек
    for vertex in vertices:
        glVertex2f(vertex[0], vertex[1])
    glEnd()

# Функция для рисования многоугольника с помощью линий
def draw_polygon(vertices):
    glBegin(GL_LINE_LOOP)  # Рисуем замкнутую ломаную линию
    glColor3f(1.0, 1.0, 1.0)  # Красный цвет линий
    for vertex in vertices:
        glVertex2f(vertex[0], vertex[1])
    glEnd()

def main():
    n = 6 # Количество вершин n-угольника
    radius = 0.5  # Радиус многоугольника
    point_size = 10  # Начальный размер точек
    max_point_size = 50  # Максимальный размер точек для эксперимента

    init_pygame_opengl()
    vertices = compute_polygon_vertices(n, radius)

    task = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    task = 1
                if event.key == pygame.K_2:
                    task = 2
                if event.key == pygame.K_0:
                    task = 0
                if event.key == pygame.K_3:
                    task = 3
                if event.key == pygame.K_4:
                    task = 4

                elif event.key == pygame.K_UP:
                    point_size += 1  # Увеличиваем размер точек
                elif event.key == pygame.K_DOWN:
                    point_size = max(1, point_size - 1)  # Уменьшаем размер точек

        # Очистка экрана
        if task == 0:
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        elif task == 1:
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            draw_points(vertices, point_size)
        elif task == 2:
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            draw_polygon(vertices)
        elif task == 3:
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            draw_task3()
        elif task == 4:
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            draw_task4()



        # Обновляем экран
        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()


if __name__ == "__main__":
    main()
