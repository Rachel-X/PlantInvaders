# from: https://kivycoder.com/image-view-with-filechoosericonview-and-filechooserlistview-python-kivy-gui-tutorial-23/

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.lang import Builder

# Designate Our .kv design file
# Builder.load_file('menu.kv')

class FileLayout(Widget):

    def selected(self, filename):
        try:
            self.ids.plant_image.source = filename[0]
            # print(filename[0])
        except:
            pass


class FileWindow(Screen):
    pass


class ImageWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("menu.kv")

class PlantInvaderApp(App):
    def build(self):
        # return FileLayout()
        return kv


if __name__ == '__main__':
    PlantInvaderApp().run()
