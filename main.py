import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.image import Image as CoreImage

kivy.require('1.9.0')


class OpenScreen (BoxLayout):
    pass


class IntroTaskScreen (BoxLayout):
    pass


# the app definition
class KivyTangramGameApp (App):
    def build(self):
        # connect internal variables to forms
        self.open_screen = OpenScreen()
        self.intro_task_screen = IntroTaskScreen()
        # define the screen manager, moves between forms
        self.sm = ScreenManager()
        # connect each form to a screen
        screen = Screen(name="openScreen")
        screen.add_widget(self.open_screen)
        self.sm.add_widget(screen)
        screen = Screen(name="introTaskScreen")
        screen.add_widget(self.intro_task_screen)
        self.sm.add_widget(screen)
        return self.sm

    # functions connecting to button pressed
    def enter_open_screen(self):
        print("enter_open_screen")
        self.sm.current = "openScreen"

    def enter_intro_task_screen(self):
        print("introTaskScreen")
        self.sm.current = "introTaskScreen"

if __name__ == '__main__':
    KivyTangramGameApp().run()