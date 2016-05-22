from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
import random

class ScatterTextWidget (BoxLayout):
    text_color = ListProperty([1, 0, 0, 1])

    def __init__(self, **kwargs):

    def change_label_color(self, *args):
        color = [random.random() for i in xrange(3)]+[1]
        self.text_color = color

class Learning3App(App):  #The name of the class will make it search for learning2.kv
    def build(self):
        return ScatterTextWidget ()

if __name__ == "__main__":
    Learning3App().run()
