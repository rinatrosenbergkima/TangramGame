from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.clock import Clock

Builder.load_string('''

<HourGlassWidget>:
    font_size: 150
    Image:
        id:topSand
        source: 'images\sand.jpg'
        allow_stretch: True
        keep_ratio: False

    Image:
        id:middleSand
        pos: root.width * 0.25, root.height * 0.3
        size: root.width * 0.1, root.height * 0.2
        source: 'images\cake.png'
        allow_stretch: True
        keep_ratio: False
    Image:
        id:bottomSand
        pos: root.width * 0.2, root.height * 0.2
        size: root.width*0.2, root.height*0.2
        source: 'images\cake.png'
        allow_stretch: True
        keep_ratio: False
''')



class HourGlassWidget(Label):
    def rinat (self, **kwargs):
        #super(HourGlassWidget, self).__init__(**kwargs)
        self.start_clock()
        self.topSand = self.ids['topSand']
        self.middleSand = self.ids['middleSand']
        self.bottomSand = self.ids['bottomSand']
        self.delta = (self.height * 0.2) / 50.0

        self.topSand.pos = self.x, self.y
        self.topSand.size = self.width, self.height
        self.middleSand.pos = self.width*0.25, self.height * 0.5
        self.middleSand.size = self.width*0.01, self.height*0.1
        self.bottomSand.pos = self.width * 0.2, self.height * 0.1
        self.bottomSand.size = self.width * 0.1, self.height * 0

        print("height",self.height)
        print("delta",self.delta)

    def do_layout(self, *args):
        self.topSand = self.ids['topSand']
        self.middleSand = self.ids['middleSand']
        self.bottomSand = self.ids['bottomSand']
        self.delta = (self.height * 0.2) / 50.0

        self.topSand.pos = self.x, self.y
        self.topSand.size = self.width, self.height
        self.middleSand.pos = self.width * 0.25, self.height * 0.5
        self.middleSand.size = self.width * 0.01, self.height * 0.1
        self.bottomSand.pos = self.width * 0.2, self.height * 0.1
        self.bottomSand.size = self.width * 0.1, self.height * 0

        print("height", self.height)
        print("delta", self.delta)

    def on_size(self, *args):
        self.do_layout()

    def on_pos(self, *args):
        self.do_layout()

    def add_widget(self, widget):
        super(HourGlassWidget, self).add_widget(widget)
        self.do_layout()

    def remove_widget(self, widget):
        super(HourGlassWidget, self).remove_widget(widget)
        self.do_layout()

    def update_sand(self):
        #print("update")
        self.topSand.y = self.topSand.y - self.delta
        self.topSand.height = self.topSand.height - self.delta
        self.bottomSand.y = self.bottomSand.y + self.delta
        self.bottomSand.height = self.bottomSand.height + self.delta
        print ("topHeight:", self.topSand.height,", topPos:", self.topSand.y)
        print ("bottomHeight: ", self.bottomSand.height, ", bottomPos:", self.bottomSand.y)

    def start_clock(self):
        self.counter = 50
        #print self.counter
        Clock.schedule_interval(self.timer, 1)

    def timer(self, dt):
        self.counter -= 1
        #print self.counter
        #self.update_sand()
        if self.counter <= 0:
            return False
        return True

runTouchApp(HourGlassWidget())