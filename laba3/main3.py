import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Координаты фигур
triangle1 = [(1, 1, 0), (1, 0, 1), (0, 1, 1)]
quad = [(0.8, 0.7, 1), (-0.8, 0.7, 1), (-0.8, -0.7, -0.8), (0.8, -0.7, -0.8)]
triangle2 = [(0, 0.5, -0.5), (-0.5, 0, -0.5), (0.5, 0, 0.5)]

# Координаты вершин куба
cube_vertices = [
    (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),  # Задняя грань
    (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)       # Передняя грань
]

vertices = [
    [1, 1, -1],
    [1, -1, -1],
    [-1, -1, -1],
    [-1, 1, -1],
    [1, 1, 1],
    [1, -1, 1],
    [-1, -1, 1],
    [-1, 1, 1],
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


# Ребра куба (индексы вершин, соединяющие каждую пару)
cube_edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # Задняя грань
    (4, 5), (5, 6), (6, 7), (7, 4),  # Передняя грань
    (0, 4), (1, 5), (2, 6), (3, 7)   # Соединение передней и задней граней
]

# Грани куба (каждая грань состоит из 4 вершин)
cube_faces = [
    (0, 1, 2, 3),  # Задняя грань
    (4, 5, 6, 7),  # Передняя грань
    (0, 1, 5, 4),  # Нижняя грань
    (3, 2, 6, 7),  # Верхняя грань
    (0, 3, 7, 4),  # Левая грань
    (1, 2, 6, 5)   # Правая грань
]

# Цвета для каждой грани
face_colors = [
    (1, 0, 0),  # Красный
    (0, 1, 0),  # Зеленый
    (0, 0, 1),  # Синий
    (1, 1, 0),  # Желтый
    (1, 0, 1),  # Фиолетовый
    (0, 1, 1)   # Голубой
]

# Грани куба (каждая грань состоит из 4 вершин)
cube_faces = [
    (0, 1, 2, 3),  # Задняя грань
    (4, 5, 6, 7),  # Передняя грань
    (0, 1, 5, 4),  # Нижняя грань
    (3, 2, 6, 7),  # Верхняя грань
    (0, 3, 7, 4),  # Левая грань
    (1, 2, 6, 5)   # Правая грань
]

# Цвета для каждой грани
face_colors = [
    (1, 0, 0),  # Красный
    (0, 1, 0),  # Зеленый
    (0, 0, 1),  # Синий
    (1, 1, 0),  # Желтый
    (1, 0, 1),  # Фиолетовый
    (0, 1, 1)   # Голубой
]


# Функция для инициализации OpenGL
def init():
    glClearColor(0.1, 0.1, 0.1, 1)
    gluPerspective(45, (800/600), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)


# Функция для отрисовки фигур
def draw_shapes():
    glDisable(GL_DEPTH_TEST)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0)
    for vertex in triangle1:
        glVertex3fv(vertex)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0, 1, 0)
    for vertex in quad:
        glVertex3fv(vertex)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0, 0, 1)
    for vertex in triangle2:
        glVertex3fv(vertex)
    glEnd()

# Функция для отрисовки фигур
def draw_shapes2():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)

    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0)
    for vertex in triangle1:
        glVertex3fv(vertex)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0, 1, 0)
    for vertex in quad:
        glVertex3fv(vertex)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0, 0, 1)
    for vertex in triangle2:
        glVertex3fv(vertex)
    glEnd()

# Функция для отрисовки каркасного изображения куба
def draw_wireframe_cube():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)

    for edge in cube_edges:
        for vertex in edge:
            glVertex3fv(cube_vertices[vertex])

    glEnd()

def draw_cube():
    glClearColor(0.1, 0.1, 0.1, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-0.85, 0.85, -0.7, 0.7, 6, 12)  # Параллельная проекция
    glMatrixMode(GL_MODELVIEW)
    #glTranslatef(0.0, 0.0, -5)  # Перемещаем куб ближе к центру видового объема
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBegin(GL_TRIANGLES)
    glColor3f(0.5, 0.5, 1)  # Цвет куба

    # Отрисовка каждого треугольника
    for triangle in cube_triangles:
        for vertex in triangle:
            glVertex3fv(cube_vertices[vertex])

    glEnd()


def draw_tr_cube():
    glBegin(GL_TRIANGLES)
    glVertex3fv(vertices[0])
    glVertex3fv(vertices[1])
    glVertex3fv(vertices[2])

    glVertex3fv(vertices[0])
    glVertex3fv(vertices[2])
    glVertex3fv(vertices[3])

    glVertex3fv(vertices[4])
    glVertex3fv(vertices[5])
    glVertex3fv(vertices[6])

    glVertex3fv(vertices[4])
    glVertex3fv(vertices[6])
    glVertex3fv(vertices[7])

    glVertex3fv(vertices[3])
    glVertex3fv(vertices[7])
    glVertex3fv(vertices[0])

    glVertex3fv(vertices[0])
    glVertex3fv(vertices[7])
    glVertex3fv(vertices[4])

    glVertex3fv(vertices[1])
    glVertex3fv(vertices[5])
    glVertex3fv(vertices[6])

    glVertex3fv(vertices[1])
    glVertex3fv(vertices[6])
    glVertex3fv(vertices[2])

    glVertex3fv(vertices[3])
    glVertex3fv(vertices[7])
    glVertex3fv(vertices[6])

    glVertex3fv(vertices[3])
    glVertex3fv(vertices[6])
    glVertex3fv(vertices[2])

    glVertex3fv(vertices[0])
    glVertex3fv(vertices[1])
    glVertex3fv(vertices[5])

    glVertex3fv(vertices[0])
    glVertex3fv(vertices[5])
    glVertex3fv(vertices[4])

    glEnd()



def draw_colored_cube():
    glClearColor(0.1, 0.1, 0.1, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glBegin(GL_QUADS)
    for i, face in enumerate(cube_faces):
        glColor3fv(face_colors[i])
        for vertex in face:
            glVertex3fv(cube_vertices[vertex])
    glEnd()

# Главная функция для запуска визуализации
def main():
    pygame.init()
    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    #init()
    task = 0
    fill_mode = True

    # Основной цикл для отрисовки и взаимодействия
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key != pygame.K_SPACE:
                    glLoadIdentity()

                    glClearColor(0.1, 0.1, 0.1, 1)

                    gluPerspective(45, (800 / 600), 0.1, 50.0)
                    glTranslatef(0.0, 0.0, -5)
                if event.key == pygame.K_1:
                    task = 1
                if event.key == pygame.K_2:
                    task = 2
                if event.key == pygame.K_3:
                    glOrtho(-0.85, 0.85, -0.7, 0.7, 6, 12)
                    task = 3
                if event.key == pygame.K_4:
                    task = 4
                if event.key == pygame.K_5:
                    # Повороты осей
                    glRotatef(-25, 1, 0, 0)  # Поворот на 30 градусов вокруг оси X
                    glRotatef(60, 0, 1, 0)  # Поворот на 70 градусов вокруг оси Y
                    task = 5
                if event.key == pygame.K_6:
                    task = 6
                if event.key == K_SPACE and task==6:
                    glRotatef(30, 1, 0, 0)
                    glRotatef(70, 0, 1, 0)

        if fill_mode:
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        else:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        # Поворот фигуры для лучшего обзора
        #glRotatef(1, 3, 1, 1)
            # Очистка экрана
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        if task == 1:
            draw_shapes()
        elif task == 2:
            draw_shapes2()
        elif task == 3:
            draw_tr_cube()
        elif task == 4:
            draw_wireframe_cube()
        elif task == 5:

            draw_colored_cube()
        elif task == 6:
            if fill_mode:
                glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
                draw_colored_cube()
            else:
                glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
                draw_wireframe_cube()

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()