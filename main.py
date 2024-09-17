import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GL.shaders import *


vertices = [

    -0.8, 0, 0.0,
    -0.5, 0.8, 0.0,
    -0.2, 0.0, 0.0,


    0.8, 0, 0.0,
    0.5, 0.8, 0.0,
    0.2, 0.0, 0.0,


    -0.4, -0.8, 0.0,
    0.4, -0.8, 0.0,
    0.0, 0.2, 0.0
]


vertex_shader_source = """
#version 400
in vec3 vp;
void main() {
    gl_Position = vec4(vp, 1.0);
}
"""


fragment_shader_1 = """
#version 400
out vec4 color;
void main() {
    color = vec4(1.0, 0.0, 0.0, 1.0); // Красный
}
"""

fragment_shader_2 = """
#version 400
out vec4 color;
void main() {
    color = vec4(0.0, 1.0, 0.0, 1.0); // Зеленый
}
"""

fragment_shader_3 = """
#version 400
out vec4 color;
void main() {
    color = vec4(0.0, 0.0, 1.0, 1.0); // Синий
}
"""


def compile_shader(source, shader_type):

    shader = glCreateShader(shader_type)
    glShaderSource(shader, source)
    glCompileShader(shader)

    return shader


def create_shader_program(vertex_shader_source, fragment_shader_source):

    vertex_shader = compile_shader(vertex_shader_source, GL_VERTEX_SHADER)
    fragment_shader = compile_shader(fragment_shader_source, GL_FRAGMENT_SHADER)

    shader_program = glCreateProgram()
    glAttachShader(shader_program, vertex_shader)
    glAttachShader(shader_program, fragment_shader)
    glLinkProgram(shader_program)

    glDeleteShader(vertex_shader)
    glDeleteShader(fragment_shader)

    return shader_program


def main():

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption('Laba1')


    glViewport(0, 0, display[0], display[1])


    shader_program_1 = create_shader_program(vertex_shader_source, fragment_shader_1)
    shader_program_2 = create_shader_program(vertex_shader_source, fragment_shader_2)
    shader_program_3 = create_shader_program(vertex_shader_source, fragment_shader_3)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        glClear(GL_COLOR_BUFFER_BIT)


        glUseProgram(shader_program_1)
        glBegin(GL_TRIANGLES)
        for i in range(3):
            glVertex3fv(vertices[i * 3:i * 3 + 3])
        glEnd()


        glUseProgram(shader_program_2)
        glBegin(GL_TRIANGLES)
        for i in range(3):
            glVertex3fv(vertices[9 + i * 3:9 + i * 3 + 3])
        glEnd()


        glUseProgram(shader_program_3)
        glBegin(GL_TRIANGLES)
        for i in range(3):
            glVertex3fv(vertices[18 + i * 3:18 + i * 3 + 3])
        glEnd()

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
