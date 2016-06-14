from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import Layout
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.clock import Clock
from kivy.app import App


Builder.load_string('''
<RootWidget>:
    HourGlassWidget:
        pos: 300,200
<HourGlassWidget>:
    Image:
        id:topSand
        pos: root.width * 0.2, root.height * 0.6-root.height*0.2
        source: 'images\cake.png'
        allow_stretch: True
        keep_ratio: False
    Image:
        id:middleSand
        pos: root.width * 0.25, root.height * 0.4 - root.height*0.2
        source: 'images\cake.png'
        allow_stretch: True
        keep_ratio: False
    Image:
        id:bottomSand
        pos: root.width * 0.2, root.height * 0.2 - root.height*0.2
        source: 'images\cake.png'
        allow_stretch: True
        keep_ratio: False
''')

class RootWidget(Widget):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        #self.start_clock()
        print("root", self.ids)
        #self.topSand = self.ids['topSand']
        # self.middleSand = self.ids['middleSand']
        # self.bottomSand = self.ids['bottomSand']

class HourGlassWidget (Widget):
    def __init__(self, **kwargs):
        super(HourGlassWidget, self).__init__(**kwargs)
        self.start_clock()
        print("hour", self.ids)
        #self.topSand = self.ids['topSand']
        #self.middleSand = self.ids['middleSand']
        #self.bottomSand = self.ids['bottomSand']
        self.init = False
        print("init height",self.height )
        self.delta=0

    def do_layout(self, *args):
        if (not self.init):
            self.delta = (self.height * 0.2) / 60.0
            self.topSand.size = self.width * 0.2, self.height * 0.2
            self.topSand.pos = self.width*0.2,  self.height*0.6-self.height*0.2
            self.middleSand.size = self.width * 0.01, self.height * 0.2
            self.middleSand.pos = self.width*0.25, self.height* 0.4- self.height * 0.2
            self.bottomSand.size = self.width * 0.2, self.height * 0
            self.bottomSand.pos = self.width * 0.2, self.height * 0.2 - self.height*0.2
            self.init = True
            print("self.x", self.x)
            print("do_layout height", self.height)
            print("delta", self.delta)

    def on_size(self, *args):
        #self.do_layout()
        print("on_size")

    def on_pos(self, *args):
        print("on_pos")
        #self.do_layout()
        self.init = False

    def update_sand(self):
        print("update ", self.counter)
        self.topSand.height = self.topSand.height - self.delta
        self.bottomSand.height = self.bottomSand.height + self.delta

    def start_clock(self):
        self.counter = 60
        print self.counter
        Clock.schedule_interval(self.timer, 1)

    def timer(self, dt):
        self.counter -= 1
        #print self.counter
        self.update_sand()
        if self.counter <= 0:
            return False
        return True

class RootWidgetApp(App):  # The name of the class will make it search for learning2.kv
    def build(self):
        return RootWidget()

#runTouchApp(RootWidget())
if __name__ == "__main__":
    RootWidgetApp().run()
