import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader
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
        self.load_sounds()
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
        self.play_sound("TangramOpen_myFriend")
        return self.sm
    # functions connecting to button pressed
    def enter_open_screen(self):
        print("enter_open_screen")
        self.sm.current = "openScreen"


    def enter_intro_task_screen(self):
        print("introTaskScreen")
        self.sm.current = "introTaskScreen"
        self.play_sound("TangramOpen_click")

    def load_sounds(self):
        self.sounds={}
        self.sounds[0] = SoundLoader.load("sounds\TangramOpen_myFriend.m4a")
        self.sounds[1] = SoundLoader.load("sounds\TangramOpen_click.m4a")

    def callback(self):
        print('rinat')

    def play_sound(self, soundName):
        if soundName == "TangramOpen_myFriend":
            sound = self.sounds.get(0)
            #Clock.schedule_once(self.callback(), 0)

        elif soundName == "TangramOpen_click":
            sound = self.sounds.get(1)
        if sound is not None:
                sound.volume = 0.5
                sound.play()

if __name__ == '__main__':
    KivyTangramGameApp().run()