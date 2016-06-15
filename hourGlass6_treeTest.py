from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import Layout
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.clock import Clock
from kivy.app import App
from kivy.animation import Animation

Builder.load_string('''

<RootWidget>:
    HourGlassWidget:
        pos:200,300

<HourGlassWidget>:
    Image:
        id:topSand
        source: 'images\cake.png'
        allow_stretch: True
        keep_ratio: False
    Image:
        id:middleSand
        source: 'images\cake.png'
        allow_stretch: True
        keep_ratio: False
    Image:
        id:bottomSand
        source: 'images\cake.png'
        allow_stretch: True
        keep_ratio: False
''')

class RootWidget(Widget):
    pass

class HourGlassWidget (Widget):
    def __init__(self, **kwargs):
        super(HourGlassWidget, self).__init__(**kwargs)
        self.delta=0
        #self.animate_sand()
        Clock.schedule_interval(self.after_init,1)  #only after init is done ids can be accessed


    def after_init(self, *args):
        self.counter = 60
        self.topSand = self.ids['topSand']
        self.middleSand = self.ids['middleSand']
        self.bottomSand = self.ids['bottomSand']
        self.init = False
        self.do_layout()
        Clock.schedule_interval(self.update_sand_clock, 1)
        return False


    def do_layout(self, *args):
        if (not self.init):
            print("rootWidget")
            self.size = 400, 400
            self.pos = 300, 300
            self.delta = (self.height * 0.2) / 60.0
            self.topSand.size = self.width * 0.2, self.height * 0.2
            self.topSand.pos = self.width * 0.2, self.height * 0.6 - self.height * 0.2
            self.middleSand.size = self.width * 0.01, self.height * 0.2
            self.middleSand.pos = self.width * 0.25, self.height * 0.4 - self.height * 0.2
            self.bottomSand.size = self.width * 0.2, self.height * 0
            self.bottomSand.pos = self.width * 0.2, self.height * 0.2 - self.height * 0.2
            self.init = True
            print("self.x", self.x)
            print("do_layout height", self.height)
            print("delta", self.delta)

    def update_sand_clock(self, *args):
        print("update ", self.counter)
        self.topSand.height = self.topSand.height - self.delta
        self.bottomSand.height = self.bottomSand.height + self.delta
        self.counter -= 1
        if self.counter <= 0:
            return False
        return True

class RootWidgetApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    RootWidgetApp().run()
