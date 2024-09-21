import threading
import dearpygui.dearpygui as gui
import glfw
import win32gui
import OpenGL.GL as gl
import win32con, time
import keyboard
import tkinter, os
import dearpygui.dearpygui as gui
from OpenGL.GL import *







color = (100,100,100) #https://www.rapidtables.com/web/color/RGB_Color.html
color1 = 'white'
if color1 == "black":
    color = (0,0,0)
else:
    None



    

    
    
    
def corshair(screenx,screeny):   
    app = tkinter.Tk()


    screenx = app.winfo_screenwidth()
    screeny = app.winfo_screenheight()
    thickness = gui.get_value('thick')
    size = gui.get_value('size')
    gap = gui.get_value('gap')
    glfw.init()
    glfw.window_hint(glfw.TRANSPARENT_FRAMEBUFFER, True)
    glfw.window_hint(glfw.FLOATING, True)
    glfw.window_hint(glfw.DECORATED, False) 
        
    window = glfw.create_window(screenx, screeny, 'tracers', None , None)
    glfw.make_context_current(window)
    gl.glOrtho(0, screenx, 0, screeny, -1, 1)
        
    handle = win32gui.FindWindow(0, 'tracers')
        
    exStyle = win32gui.GetWindowLong(handle, win32con.GWL_EXSTYLE)
    win32gui.SetWindowLong(handle, win32con.GWL_EXSTYLE, exStyle | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT)
    
    color1 = color   
    
    while True:
        color1 = (gui.get_value('r'),gui.get_value('g'),gui.get_value('b'))
        thickness = gui.get_value('thick')
        size = gui.get_value('size')
        gap = gui.get_value('gap')
        x = screenx/2
        y = screeny/2
        
        
        glfw.swap_buffers(window)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        glfw.poll_events()
        time.sleep(0.001)
        
        gl.glLineWidth(thickness)
                
        gl.glBegin(gl.GL_LINES)

        
        gl.glColor3b(*color1)

        
        
        gl.glVertex2f(x - (size+gap), y)
        gl.glVertex2f(x - gap, y)

        
        gl.glVertex2f(x + (size+gap), y)
        gl.glVertex2f(x + gap, y)




        
        
        
        
        
        gl.glVertex2d(x, y - (size+gap))
        gl.glVertex2d(x, y - gap)

        gl.glVertex2d(x, y + (size+gap))
        gl.glVertex2d(x, y + gap)
        time.sleep(0.0001)
        
        
        
        
        gl.glEnd()


    























gui.create_context()
gui.create_viewport(title='cross', width=400, height=400)
gui.setup_dearpygui()
gui.set_viewport_always_top(True)
gui.set_viewport_resizable(False)


with gui.window(label='cross', width=400,height=400,no_title_bar=True,no_resize=True, no_move=True, show=True):
    with gui.tab_bar(label='cross'):
        
        
        with gui.tab(label='cross'):
            gui.add_slider_int(label='size', tag='size', min_value=1, max_value=50, default_value=6)
            gui.add_slider_int(label='gap', tag='gap', min_value=1, max_value=50, default_value=4)
            gui.add_slider_int(label='thick', tag='thick', min_value=1, max_value=10, default_value=2)
            gui.add_text(label='Color')
            gui.add_slider_int(label='red', tag='r', min_value=0, max_value=126, default_value=100)
            gui.add_slider_int(label='green', tag='g', min_value=0, max_value=126, default_value=100)
            gui.add_slider_int(label='blue', tag='b', min_value=0, max_value=126, default_value=100)            
            gui.add_button(label='generate',callback=corshair)
            
            
        



gui.show_viewport()
gui.start_dearpygui()
gui.destroy_context()