import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random

# Вершины 2D фигуры (например, 4 вершины)
vertices = [
    [-1, -1, 0],
    [1, -1, 0],
    [1, 1, 0],
    [-1, 1, 0]
]

# Треугольники (каждая грань)
triangles = [
    [0, 1, 2],
    [2, 3, 0]
]

# Случайные цвета для треугольников
colors = [
    [random.random(), random.random(), random.random()] for _ in range(len(triangles))
]

# Функция для отображения треугольников

def draw_tr():
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(1, -1)
    glVertex2f(0.3, -1)
    glVertex2f(0.8, 1)

    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0.3, -1)
    glVertex2f(0.8, 1)
    glVertex2f(0.3, 0)


    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.3, 0)
    glVertex2f(-0.1, 0.3)
    glVertex2f(0.8, 1)

    glColor3f(0.5, 0.5, 0.0)
    glVertex2f(0.3, 0)
    glVertex2f(-0.1, 0.3)
    glVertex2f(0.0, 0)

    glColor3f(0.471263322161369, 0.2974430471189735, 0.8830779091187262)
    glVertex2f(-0.1, 0.3)
    glVertex2f(0.0, 0)
    glVertex2f(-1, 0.7)

    glColor3f(0, 0.5, 0.5)
    glVertex2f(-1, 0.7)
    glVertex2f(-0.6, -0.5)
    glVertex2f(0.0, 0)

    glColor3f(0.5, 0, 0.5)
    glVertex2f(-1, 0.7)
    glVertex2f(-0.6, -0.5)
    glVertex2f(-1, -1)

    glColor3f(1, 1, 1)
    glVertex2f(0, -1)
    glVertex2f(-0.6, -0.5)
    glVertex2f(-1, -1)

    # glColor3f(0.2, 0.7, 0.4)
    # glVertex2f(-0.6, -0.5)
    # glVertex2f(0, 0)
    # glVertex2f(-1, 0.2)

    glEnd()
def draw_triangles(mode):
    if mode == "points":  # Отображение только вершин
        glPointSize(5)
        glPolygonMode(GL_FRONT, GL_POINT)
        draw_tr()

    elif mode == "face_vs_wireframe":  # Лицевые грани закрашены, обратные - линиями
        glPolygonMode(GL_FRONT, GL_FILL)  # вернем режим к стандартному
        glPolygonMode(GL_BACK, GL_LINE)  # вернем режим к стандартному
        draw_tr()
    elif mode == "wireframe":  # Каркасное отображение для обеих сторон
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        draw_tr()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # Настройка перспективы
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, display[0] / display[1], 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    glMatrixMode(GL_MODELVIEW)

    # Основной цикл
    mode = "face_vs_wireframe"  # Начальный режим
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_1:
                    mode = "points"
                elif event.key == K_2:
                    mode = "face_vs_wireframe"
                elif event.key == K_3:
                    mode = "wireframe"

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        #print(mode)
        draw_triangles(mode)  # Отрисовка треугольников в выбранном режиме

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
