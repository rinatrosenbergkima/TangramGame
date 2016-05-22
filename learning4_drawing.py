from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.properties import ListProperty

from kivy.graphics.vertex_instructions import (Rectangle,
                                               Ellipse,
                                               Line)
from kivy.graphics.context_instructions import (Color)

import random

class ScatterTextWidget (BoxLayout):
    text_color = ListProperty([1, 0, 0, 1])

    def __init__(self, **kwargs):
        super(ScatterTextWidget,self).__init__(**kwargs)

        with self.canvas.before:
            Color(0,1,0,1)
            Rectangle(pos=(0, 100), size=(300,100))
            Ellipse(pos=(0, 400), size=(300, 100))
            Line(points=[0, 0, 500, 600, 400, 300],
                 close=True,
                 width=3)

    def press_scatter(self):
        print ("press scatter")

    def change_label_color(self, *args):
        color = [random.random() for i in xrange(3)]+[1]
        self.text_color = color

    def on_event(self,obj):
        print ("event from:", obj)

class Learning4App(App):  #The name of the class will make it search for learning2.kv
    def build(self):
        return ScatterTextWidget ()

if __name__ == "__main__":
    Learning4App().run()
