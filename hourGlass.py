from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.properties import ListProperty

from kivy.graphics.vertex_instructions import (Rectangle,
                                               Ellipse,
                                               Line)
from kivy.graphics.context_instructions import (Color)

import random

class HourGlassWidget (BoxLayout):
    text_color = ListProperty([1, 0, 0, 1])

    def __init__(self, **kwargs):
        super(HourGlassWidget,self).__init__(**kwargs)
        self.start_clock()
        self.topRec = self.ids['topRec']
        self.middleRec = self.ids['middleRec']
        self.bottomRec = self.ids['bottomRec']

    def run_hourglass (self, *args):
        self.topRec.size_hint_y = self.topRec.size_hint_y - 0.02


    def on_event(self,obj):
        print ("event from:", obj)

    def start_clock(self):
        self.counter = 60
        print self.counter
        Clock.schedule_interval(self.timer, 1)

    def timer(self, dt):
        self.counter -= 1
        print self.counter
        #self.run_hourglass()
        if self.counter <= 0:
            return False
        return True


class HourGlassApp(App):  #The name of the class will make it search for learning2.kv
    def build(self):
        return HourGlassWidget ()

if __name__ == "__main__":
    HourGlassApp().run()
