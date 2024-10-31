import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
from math import cos, sin, pi



# Компилируем шейдеры
def compile_shadersVBO():
    vertex_shader_source = """
    #version 330 core
    layout(location = 0) in vec3 position;
    layout(location = 1) in vec3 color;
    out vec3 fragColor;
    void main()
    {
        gl_Position = vec4(position, 1.0);
        fragColor = color;
    }
    """

    fragment_shader_source = """
    #version 330 core
    in vec3 fragColor;
    out vec4 finalColor;
    void main()
    {
        finalColor = vec4(fragColor, 1.0);
    }
    """

    vertex_shader = compileShader(vertex_shader_source, GL_VERTEX_SHADER)
    fragment_shader = compileShader(fragment_shader_source, GL_FRAGMENT_SHADER)
    shader_program = compileProgram(vertex_shader, fragment_shader)
    return shader_program

# Компилируем шейдеры
def compile_shaders():
    vertex_shader_source = """
    #version 330
    layout(location = 0) in vec2 position;
    void main()
    {
        gl_Position = vec4(position, 0.0, 1.0);
    }
    """
    fragment_shader_source = """
    #version 330
    out vec4 FragColor;
    void main()
    {
        FragColor = vec4(0.0, 1.0, 0.0, 1.0);  // Зеленый цвет
    }
    """

    vertex_shader = compileShader(vertex_shader_source, GL_VERTEX_SHADER)
    fragment_shader = compileShader(fragment_shader_source, GL_FRAGMENT_SHADER)
    shader_program = compileProgram(vertex_shader, fragment_shader)
    return shader_program

# Функция для вычисления координат вершин правильного n-угольника
def compute_polygon_vertices(n, radius):
    vertices = []
    for i in range(n):
        # Угол для каждой вершины
        angle = 2 * pi * i / n
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

    # Компилируем и используем шейдеры


def random_color():
    #print([random.random() for _ in range(3)])
    a = [0.471263322161369, 0.2974430471189735, 0.8830779091187262]
    return a


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

def draw_triangle_fan():
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.0, 0.0)  # Центральная вершина веера

    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(1, 0)  # Вторая вершина

    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(1, 0.7)  # Третья вершина

    glColor3f(0.5, 0.5, 0.0)
    glVertex2f(0.3, 0.3)  # Четвертая вершина (автоматически замкнется на первую)

    glColor3f(0, 0.5, 0.5)
    glVertex2f(-0.4, 0.7)

    glColor3f(0.5, 0, 0.5)
    glVertex2f(-1, 0.2)

    glColor3f(1, 1, 1)
    glVertex2f(-0.7, -0.7)

    glColor3f(0.2, 0.7, 0.4)
    glVertex2f(0.2, -1)
    glEnd()

def draw_triangle_strip():
    glBegin(GL_TRIANGLE_STRIP)

    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(1, 0)  # Вторая вершина

    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(1, 0.7)  # Третья вершина

    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.0, 0.0)  # Центральная вершина веера

    glColor3f(0.5, 0.5, 0.0)
    glVertex2f(0.3, 0.3)  # Четвертая вершина (автоматически замкнется на первую)

    glColor3f(0, 0.5, 0.5)
    glVertex2f(-0.4, 0.7)

    glColor3f(0.5, 0, 0.5)
    glVertex2f(-1, 0.2)

    glColor3f(1, 1, 1)
    glVertex2f(-0.7, -0.7)

    glColor3f(0.2, 0.7, 0.4)
    glVertex2f(0.2, -1)
    glEnd()

def draw_triangle_simple():
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(1, 0)  # Вторая вершина
    glVertex2f(1, 0.7)  # Третья вершина
    glVertex2f(0.0, 0.0)  # Центральная вершина веера

    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(1, 0.7)  # Третья вершина
    glVertex2f(0.0, 0.0)  # Центральная вершина веера
    glVertex2f(0.3, 0.3)  # Четвертая вершина (автоматически замкнется на первую)

    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.0, 0.0)  # Центральная вершина веера
    glVertex2f(0.3, 0.3)  # Четвертая вершина (автоматически замкнется на первую)
    glVertex2f(-0.4, 0.7)

    glColor3f(0, 0.5, 0.5)
    glVertex2f(-0.4, 0.7)
    glVertex2f(0.0, 0.0)  # Центральная вершина веера
    glVertex2f(-1, 0.2)

    glColor3f(1, 1, 1)
    glVertex2f(0.0, 0.0)  # Центральная вершина веера
    glVertex2f(-1, 0.2)
    glVertex2f(-0.7, -0.7)

    glColor3f(0.2, 0.7, 0.4)
    glVertex2f(-0.7, -0.7)
    glVertex2f(0.0, 0.0)  # Центральная вершина веера
    glVertex2f(0.2, -1)
    glEnd()

def draw_task7():
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.3, -1)
    glVertex2f(1, -1)
    glVertex2f(0.8, 1)

    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0.3, -1)
    glVertex2f(0.3, 0)
    glVertex2f(0.8, 1)

    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(-0.1, 0.3)
    glVertex2f(0.3, 0)
    glVertex2f(0.8, 1)

    glColor3f(0.5, 0.5, 0.0)
    glVertex2f(-0.1, 0.3)
    glVertex2f(0.3, 0)
    glVertex2f(0.0, 0)

    glColor3f(0.471263322161369, 0.2974430471189735, 0.8830779091187262)
    glVertex2f(-1, 0.7)
    glVertex2f(-0.1, 0.3)
    glVertex2f(0.0, 0)

    glColor3f(0, 0.5, 0.5)
    glVertex2f(-1, 0.7)
    glVertex2f(-1, 0.2)
    glVertex2f(0.0, 0)

    glColor3f(0.5, 0, 0.5)
    glVertex2f(-0.6, -0.5)
    glVertex2f(-1, 0.2)
    glVertex2f(-1, -1)

    glColor3f(1, 1, 1)
    glVertex2f(-0.6, -0.5)
    glVertex2f(0, -1)
    glVertex2f(-1, -1)

    glColor3f(0.2, 0.7, 0.4)
    glVertex2f(-0.6, -0.5)
    glVertex2f(0, 0)
    glVertex2f(-1, 0.2)

    glEnd()
def draw_task6(n, radius=0.5):
    angle_step = 2 * pi / n  # Шаг угла для каждой вершины
    glBegin(GL_TRIANGLE_FAN)

    # Центральная вершина многоугольника
    #glColor3fv(0.471263322161369, 0.2974430471189735, 0.8830779091187262)
    glVertex2f(0.0, 0.0)  # Центр

    # Вершины многоугольника по окружности
    for i in range(n + 1):  # Проходим по каждой вершине (n + 1 чтобы замкнуть фигуру)
        angle = i * angle_step
        x = radius * cos(angle)
        y = radius * sin(angle)
        #glColor3fv(0.471263322161369, 0.2974430471189735, 0.8830779091187262)  # Новый цвет для каждой вершины
        glVertex2f(x, y)

    glEnd()

# Функция для отрисовки через ленту треугольников
def draw_points(vertices, point_size):
    glPointSize(point_size)
    glBegin(GL_POINTS)
    glColor3f(1.0, 1.0, 1.0)  # Красный цвет точек
    for vertex in vertices:
        glVertex2f(vertex[0], vertex[1])
    glEnd()

# Функция для рисования многоугольника с помощью линий
def draw_polygon(vertices):
    glBegin(GL_LINE_LOOP)
    glColor3f(1.0, 1.0, 1.0)
    for vertex in vertices:
        glVertex2f(vertex[0], vertex[1])
    glEnd()



def main():
    n = 6 # Количество вершин n-угольника
    radius = 0.5  # Радиус многоугольника
    point_size = 10  # Начальный размер точек
    max_point_size = 50  # Максимальный размер точек для эксперимента

    task5_versions = [draw_triangle_fan, draw_triangle_strip]

    init_pygame_opengl()
    vertices = compute_polygon_vertices(n, radius)

    task = 0
    version = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    shader_program = compile_shaders()
                    glUseProgram(shader_program)
                    task = 1
                if event.key == pygame.K_2:
                    shader_program = compile_shaders()
                    glUseProgram(shader_program)
                    task = 2
                if event.key == pygame.K_0:
                    shader_program = compile_shaders()
                    glUseProgram(shader_program)
                    task = 0
                if event.key == pygame.K_3:
                    shader_program = compile_shaders()
                    glUseProgram(shader_program)
                    task = 3
                if event.key == pygame.K_4:
                    shader_program = compile_shaders()
                    glUseProgram(shader_program)
                    task = 4
                if event.key == pygame.K_5:
                    shader_program = compile_shadersVBO()
                    glUseProgram(shader_program)
                    task = 5
                if event.key == pygame.K_6:
                    shader_program = compile_shaders()
                    glUseProgram(shader_program)
                    task = 6
                if event.key == pygame.K_7:
                    shader_program = compile_shaders()
                    glUseProgram(shader_program)
                    task = 7
                if event.key == pygame.K_q:
                    glShadeModel(GL_SMOOTH)
                if event.key == pygame.K_w:
                    glShadeModel(GL_FLAT)

                if task == 5:
                    if event.key == pygame.K_a:
                        version = 0
                    if event.key == pygame.K_s:
                        version = 1
                    if event.key == pygame.K_d:
                        version = 2


                elif event.key == pygame.K_UP:
                    point_size += 1  # Увеличиваем размер точек
                elif event.key == pygame.K_DOWN:
                    point_size = max(1, point_size - 1)  # Уменьшаем размер точек



        # Очистка экрана
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        if task == 1:
            draw_points(vertices, point_size)
        elif task == 2:
            draw_polygon(vertices)
        elif task == 3:
            draw_task3()
        elif task == 4:
            draw_task4()
        elif task == 5:
            draw_triangle_fan()
            if version == 0:
                draw_triangle_fan()
            if version == 1:
                draw_triangle_strip()
            if version == 2:
                draw_triangle_simple()
        elif task == 6:
            draw_task6(n,radius)


        elif task == 7:
            draw_task7()




        # Обновляем экран
        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()


if __name__ == "__main__":
    main()
