import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Координаты вершин куба
cube_vertices = [
    (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),  # Задняя грань
    (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)       # Передняя грань
]

# Ребра куба (индексы вершин, соединяющие каждую пару)
cube_edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # Задняя грань
    (4, 5), (5, 6), (6, 7), (7, 4),  # Передняя грань
    (0, 4), (1, 5), (2, 6), (3, 7)   # Соединение передней и задней граней
]

# Функция для инициализации OpenGL с перспективной проекцией
def init():
    glClearColor(0.1, 0.1, 0.1, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (800 / 600), 0.1, 50.0)  # Установка перспективной проекции
    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0.0, 0.0, -5)  # Перемещаем куб ближе к центру видового объема

# Функция для отрисовки каркасного изображения куба
def draw_wireframe_cube():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1, 1, 1)  # Белый цвет для каркаса куба
    glBegin(GL_LINES)

    # Рисуем ребра куба
    for edge in cube_edges:
        for vertex in edge:
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

        # Поворот куба для лучшего обзора
        #glRotatef(1, 3, 1, 1)
        draw_wireframe_cube()
        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()
