from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.clock import Clock

Builder.load_string('''

<HourGlassWidget>:
    font_size: 150
    Image:
        id:topSand
        pos: 0.5 * root.width, 0.7 * root.height
        size: root.width * 0.15, root.height * 0.2
        source: 'images\sand.jpg'
        allow_stretch: True
        keep_ratio: False
    Image:
        id:middleSand
        pos: 0.57 * root.width , 0.5 * root.height
        size: root.width * 0.01, root.height * 0.2
        source: 'images\sand.jpg'
        allow_stretch: True
        keep_ratio: False
    Image:
        id:bottomSand
        pos: 0.5 * root.width , 0.1 * root.height
        size: root.width * 0.15, 0
        source: 'images\sand.jpg'
        allow_stretch: True
        keep_ratio: False
''')



class HourGlassWidget(Label):
    def __init__(self, **kwargs):
        super(HourGlassWidget, self).__init__(**kwargs)
        self.start_clock()
        self.topSand = self.ids['topSand']
        self.middleSand = self.ids['middleSand']
        self.bottomSand = self.ids['bottomSand']
        self.posX = self.width * 0.5
        self.posY_top = self.height * 0.7
        self.posY_middle = self.height * 0.5
        self.posY_bottom = self.height * 0.3
        self.height_top = self.height * 0.2
        self.height_middle = self.height * 0.2
        self.height_bottom = self.height * 0.2
        self.delta = self.height * 0.2 / 60.0
        print(self.delta)

    def update_sand(self):
        #print("update")
        self.topSand.y = self.topSand.y - self.delta
        self.topSand.height = self.topSand.height - self.delta
        self.bottomSand.y = self.bottomSand.y + self.delta
        self.bottomSand.height = self.bottomSand.height + self.delta
        #print ("top:", self.topSand.height)
        #print ("bottom: ", self.bottomSand.height)

    def start_clock(self):
        self.counter = 60
        #print self.counter
        Clock.schedule_interval(self.timer, 1)

    def timer(self, dt):
        self.counter -= 1
        print self.counter
        self.update_sand()
        if self.counter <= 0:
            return False
        return True

runTouchApp(HourGlassWidget())