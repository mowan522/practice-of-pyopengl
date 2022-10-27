import glfw
from OpenGL.GL import *

def main():

    #initialize glfw
    if not glfw.init():
        return 

    window = glfw.create_window(800,600,"My OpenGL window", None, None)

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    #show version
    print('Vendor :', glGetString(GL_VENDOR))
    print('GPU :', glGetString(GL_RENDERER))
    print('OpenGL version :', glGetString(GL_VERSION))

    #main application loop
    while not glfw.window_should_close(window):
        glfw.poll_events()
        glfw.swap_buffers(window)
        
    glfw.terminate()


if __name__ == "__main__":
    main()