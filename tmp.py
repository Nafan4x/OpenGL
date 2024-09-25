import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random


# Функция для генерации случайного цвета
def random_color():
    #print([random.random() for _ in range(3)])
    a = [0.471263322161369, 0.2974430471189735, 0.8830779091187262]
    return a


# Функция для отрисовки через отдельные треугольники
def draw_triangles():
    glBegin(GL_TRIANGLES)
    glColor3fv(random_color())
    glVertex2f(-0.5, -1)
    glVertex2f(0, 1)
    glVertex2f(-1, -1)

    glColor3fv(random_color())
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(-0.5, 0.5)
    glEnd()


# Функция для отрисовки через ленту треугольников
def draw_triangle_strip():
    glBegin(GL_TRIANGLE_STRIP)
    glColor3fv(random_color())
    glVertex2f(-0.5, -0.5)

    glColor3fv(random_color())
    glVertex2f(0.5, -0.5)

    glColor3fv(random_color())
    glVertex2f(-0.5, 0.5)

    glColor3fv(random_color())
    glVertex2f(0.5, 0.5)
    glEnd()


# Функция для отрисовки через веер треугольников
def draw_triangle_fan():
    glBegin(GL_TRIANGLE_FAN)
    glColor3fv(random_color())
    glVertex2f(0.0, 0.0)  # Центральная вершина веера

    glColor3fv(random_color())
    glVertex2f(1, 0)  # Вторая вершина

    glColor3fv(random_color())
    glVertex2f(1, 0.7)  # Третья вершина

    glColor3fv(random_color())
    glVertex2f(0.3, 0.3)  # Четвертая вершина (автоматически замкнется на первую)

    glColor3fv(random_color())
    glVertex2f(-0.4, 0.7)

    glColor3fv(random_color())
    glVertex2f(-1, 0.2)

    glColor3fv(random_color())
    glVertex2f(-0.7, -0.7)

    glColor3fv(random_color())
    glVertex2f(0.2, -1)
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluOrtho2D(-1, 1, -1, 1)

    mode = 0  # 0: треугольники, 1: лента, 2: веер

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_1:
                    mode = 0
                elif event.key == K_2:
                    mode = 1
                elif event.key == K_3:
                    mode = 2

        glClear(GL_COLOR_BUFFER_BIT)

        if mode == 0:
            glClear(GL_COLOR_BUFFER_BIT)
            draw_triangles()
        elif mode == 1:
            glClear(GL_COLOR_BUFFER_BIT)
            draw_triangle_strip()
        elif mode == 2:
            glClear(GL_COLOR_BUFFER_BIT)
            draw_triangle_fan()

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
