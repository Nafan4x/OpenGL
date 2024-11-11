import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import pywavefront

# Параметры камеры
FOV = 30  # Угол вертикального обзора
NEAR_CLIP = 6  # Передняя плоскость отсечения
FAR_CLIP = 100  # Задняя плоскость отсечения

# Начальная позиция камеры и объекта
camera_distance = 10
camera_angle = 0
object_rotation = 0
object_position_x = 0

# Инициализация Pygame и OpenGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(FOV, (display[0] / display[1]), NEAR_CLIP, FAR_CLIP)
glTranslatef(0.0, 0.0, -camera_distance)

# Установка цвета фона
glClearColor(0.5, 0.7, 0.9, 1)  # Светлый голубой фон (замените на нужный цвет)

# Загрузка модели и создание списка отображения
model = pywavefront.Wavefront('model.obj', create_materials=True, collect_faces=True)
model_display_list = glGenLists(1)

glNewList(model_display_list, GL_COMPILE)
glBegin(GL_TRIANGLES)
for mesh in model.mesh_list:
    for face in mesh.faces:
        for vertex_i in face:
            glVertex3fv(model.vertices[vertex_i])
glEnd()
glEndList()


# Функция для инициализации освещения
def init_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)

    # Параметры света
    light_pos = [4, 4, 4, 1]
    light_color = [1, 1, 1, 1]
    ambient_light = [0.2, 0.2, 0.2, 1]

    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_color)
    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient_light)


# Функция для отрисовки модели из списка отображения
def draw_model():
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, [1, 1, 1, 1])
    glCallList(model_display_list)  # Используем заранее созданный список для отрисовки


# Включаем освещение
init_lighting()

# Главный цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Управление камерой и объектом
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                object_position_x -= 0.1
            elif event.key == K_RIGHT:
                object_position_x += 0.1
            elif event.key == K_UP:
                camera_distance -= 0.5
            elif event.key == K_DOWN:
                camera_distance += 0.5
            elif event.key == K_a:
                camera_angle -= 5
            elif event.key == K_d:
                camera_angle += 5
            elif event.key == K_w:
                object_rotation += 5
            elif event.key == K_s:
                object_rotation -= 5

    # Очистка экрана
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Установка камеры
    gluPerspective(FOV, (display[0] / display[1]), NEAR_CLIP, FAR_CLIP)
    glTranslatef(0, 0, -camera_distance)
    glRotatef(camera_angle, 0, 1, 0)

    # Рисуем объект (тележку)
    glPushMatrix()
    glTranslatef(object_position_x, 0, 0)
    glRotatef(object_rotation, 0, 1, 0)
    draw_model()  # Используем список отображения
    glPopMatrix()

    # Обновляем экран
    pygame.display.flip()
    pygame.time.wait(10)

# Завершение
pygame.quit()
