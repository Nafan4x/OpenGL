import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Координаты вершин куба
cube_vertices = [
    (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),  # Задняя грань
    (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)       # Передняя грань
]

# Определяем 12 треугольников для куба
cube_triangles = [
    (0, 1, 2), (0, 2, 3),  # Задняя грань
    (4, 5, 6), (4, 6, 7),  # Передняя грань
    (0, 1, 5), (0, 5, 4),  # Нижняя грань
    (3, 2, 6), (3, 6, 7),  # Верхняя грань
    (0, 3, 7), (0, 7, 4),  # Левая грань
    (1, 2, 6), (1, 6, 5)   # Правая грань
]

# Функция для инициализации OpenGL с параллельной проекцией
def init():
    glClearColor(0.1, 0.1, 0.1, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-0.85, 0.85, -0.7, 0.7, 6, 12)  # Параллельная проекция
    glMatrixMode(GL_MODELVIEW)
    #glTranslatef(0.0, 0.0, -13)  # Перемещаем куб ближе к центру видового объема

# Функция для отрисовки куба
def draw_cube():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBegin(GL_TRIANGLES)
    glColor3f(0.5, 0.5, 1)  # Цвет куба

    # Отрисовка каждого треугольника
    for triangle in cube_triangles:
        for vertex in triangle:
            glVertex3fv(cube_vertices[vertex])

    glEnd()

# Главная функция для запуска визуализации
def main():
    pygame.init()
    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    init()
    glEnable(GL_DEPTH_TEST)  # Включение буфера глубины

    # Основной цикл для отрисовки и взаимодействия
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Поворот для лучшего обзора
        #glRotatef(1, 1, 1, 0)
        draw_cube()
        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()
