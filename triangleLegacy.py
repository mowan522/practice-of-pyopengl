import glfw
import numpy as np
from math import sin,cos
from OpenGL.GL import *

def main():

    #initialize glfw
    if not glfw.init():
        raise Exception("glfw can not be initialized!")

    window = glfw.create_window(1280,720,"My OpenGL window", None, None)

    if not window:
        glfw.terminate()
        raise Exception("glfw window can not be created!")

    glfw.make_context_current(window)

    #pos and col of triangle
    vertices = [-0.5, -0.5, 0.0,
                0.5,  -0.5, 0.0,
                0.0,  0.5,  0.0 ]

    colors  =  [1.0,  0.0, 0.0,
                0.0,  1.0, 0.0,
                0.0,  0.0,  1.0 ]

    vertices = np.array(vertices, dtype = np.float32)
    colors = np.array(colors, dtype = np.float32)

    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, vertices)

    glEnableClientState(GL_COLOR_ARRAY)
    glColorPointer(3, GL_FLOAT,0,colors)


    glClearColor(0, 0.1, 0.1, 1)

    #show version
    print('Vendor :', glGetString(GL_VENDOR))
    print('GPU :', glGetString(GL_RENDERER))
    print('OpenGL version :', glGetString(GL_VERSION))

    #main application loop
    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT)

        ct = glfw.get_time() #returns the elapses time, since init was called

        glLoadIdentity()
        glScale(abs(sin(ct)), abs(sin(ct)), 1)
        glRotatef(sin(ct) *45,0, 0, 1)
        glTranslatef(sin(ct),cos(ct),0)

        glDrawArrays(GL_TRIANGLES, 0, 3)
        


        glfw.swap_buffers(window)
        
    glfw.terminate()


if __name__ == "__main__":
    main()