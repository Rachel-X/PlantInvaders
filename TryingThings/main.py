import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.uix.widget import Widget


# sign in information is from https://github.com/deniscraciungabriel/CreateAccountPage-kivy-
# switching between screens code is from https://www.techwithtim.net/tutorials/kivy-tutorial/multiple-screens/
# the FilePicker's init function is from the best answer on https://stackoverflow.com/questions/30632327/kivy-adding-widget-to-a-screen
class SignIn(Screen):
    pass


class FilePicker(Widget):

    def selected(self, filename):
        try:
            self.ids.plant_image.source = filename[0]  # todo: make this a global variable or something?
            # print(filename[0])
        except:
            pass


class Files(Screen):
    def __init__(self, **kwargs):
        super(Files, self).__init__(**kwargs)
        self.picker = FilePicker()
        self.add_widget(self.picker)


class Comments(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("Login.kv")


class PlantApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    PlantApp().run()
