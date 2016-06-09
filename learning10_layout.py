from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.base import runTouchApp

Builder.load_string('''

<RootWidget>:
    font_size: 150
    Image:
        pos: root.x, root.y
        size: root.width * 0.5, root.height
        source: 'images\cake.png'
        allow_stretch: True
        keep_ratio: False
    Image:
        pos: root.x + 0.5*root.width, root.y
        size: root.width * 0.5, root.height
        source: 'images\cake.png'
        allow_stretch: True
        keep_ratio: False


''')

class RootWidget(Label):

    def do_layout(self, *args):
        number_of_children = len(self.children)
        width = self.width
        width_per_child = width / number_of_children
        positions = range(0,width, width_per_child)
        for position, child in zip(positions, self.children):
            child.height = self.height
            child.x = self.x + position
            child.y = self.y
            child.width = width


runTouchApp(RootWidget())