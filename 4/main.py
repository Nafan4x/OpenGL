import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *



# Задаем координаты вершин фигур
triangle_1_vertices = [
    [0.0, 0.3, 0.2],
    [0.3, 0.3, 0.0],
    [0.0, 0.0, 0.7]
]

square_vertices = [
    [-0.5, 0.5, 0.3],
    [-0.5, -0.5, 0.3],
    [0.5, -0.5, 0.3],
    [0.5, 0.5, 0.3]
]

triangle_2_vertices = [
    [0.0, 0.0, 0.3],
    [0.4, 0.0, 0.5],
    [-0.5, 0.5, -1.0]
]


# Функции отрисовки фигур
def draw_polygon(vertices, color):
    glColor3fv(color)  # Устанавливаем цвет
    glBegin(GL_POLYGON)  # Начинаем отрисовку полигона
    for vertex in vertices:
        glVertex3fv(vertex)  # Определяем вершины
    glEnd()  # Завершаем отрисовку полигона


def draw_figures():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Очищаем экран и буфер глубины
    glLoadIdentity()  # Сбрасываем текущее преобразование

    # Рисуем первый треугольник
    glPushMatrix()
    glTranslatef(-1.5, 0, -6)  # Позиционируем фигуру влево
    draw_polygon(triangle_1_vertices, (1, 0, 0))  # Красный цвет
    glPopMatrix()

    # Рисуем четырехугольник
    glPushMatrix()
    glTranslatef(0, 0, -6)  # Позиционируем фигуру в центре
    draw_polygon(square_vertices, (0, 1, 0))  # Зеленый цвет
    glPopMatrix()

    # Рисуем второй треугольник
    glPushMatrix()
    glTranslatef(1.5, 0, -6)  # Позиционируем фигуру вправо
    draw_polygon(triangle_2_vertices, (0, 0, 1))  # Синий цвет
    glPopMatrix()

    pygame.display.flip()  # Обновляем экран


def draw_line(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()


# Основной цикл программы
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # Настраиваем перспективу и включаем буфер глубины
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glEnable(GL_DEPTH_TEST)  # Включаем тест глубины

    # Главный цикл отрисовки
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Очищаем экран и буфер глубины

        glRotatef(1, 3, 1, 1)  # Добавляем вращение для лучшего обзора
        draw_figures()  # Отрисовываем фигуры
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
