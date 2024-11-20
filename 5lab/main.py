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
glClearColor(0, 0, 0, 1)  # Черный фон

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
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)

    # Основной свет (один источник света)
    glEnable(GL_LIGHT0)
    light_pos0 = [2, 2, 0, 1]  # Позиция света
    light_color0 = [1, 1, 1, 1]  # Белый свет
    ambient_light0 = [0.3, 0.3, 0.3, 1]  # Амбиентное освещение
    diffuse_light0 = [1.0, 1.0, 1.0, 1]  # Диффузное освещение
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos0)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse_light0)
    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient_light0)

# Функция для отрисовки модели из списка отображения
def draw_model():
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, [1, 1, 1, 1])
    glCallList(model_display_list)  # Используем заранее созданный список для отрисовки

# Функция для отрисовки пола
def draw_floor():
    glBegin(GL_QUADS)
    glColor3f(0.5, 0.5, 0.5)  # Светло-серый цвет для пола
    # Пол будет располагаться на уровне z = 0
    glVertex3f(-50, 0, -50)  # Левый задний угол
    glVertex3f(50, 0, -50)   # Правый задний угол
    glVertex3f(50, 0, 50)    # Правый передний угол
    glVertex3f(-50, 0, 50)   # Левый передний угол
    glEnd()

# Включаем освещение
init_lighting()

# Главный цикл
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Считывание состояния клавиш
    keys = pygame.key.get_pressed()

    # Управление объектом и камерой
    if keys[K_LEFT]:
        camera_angle += 5
    if keys[K_RIGHT]:
        camera_angle -= 5
    if keys[K_UP]:
        camera_distance -= 0.5
    if keys[K_DOWN]:
        camera_distance += 0.5
    if keys[K_a]:
        object_position_x -= 0.1
    if keys[K_d]:
        object_position_x += 0.1
    if keys[K_w]:
        object_rotation += 5
    if keys[K_s]:
        object_rotation -= 5

    # Очистка экрана
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Установка камеры
    gluPerspective(FOV, (display[0] / display[1]), NEAR_CLIP, FAR_CLIP)
    glTranslatef(0, 0, -camera_distance)
    glRotatef(camera_angle, 0, 1, 0)



    # Отрисовка пола
    draw_floor()

    # Рисуем объект (тележку)
    glPushMatrix()
    glTranslatef(object_position_x, 0, 0)
    glRotatef(object_rotation, 0, 1, 0)
    draw_model()  # Используем список отображения
    glPopMatrix()

    # Обновляем экран
    pygame.display.flip()
    clock.tick(60)  # Ограничение FPS для стабильной работы

# Завершение
pygame.quit()
