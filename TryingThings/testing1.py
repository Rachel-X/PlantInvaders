import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.uix.widget import Widget


# sign in information is from https://github.com/deniscraciungabriel/CreateAccountPage-kivy-
class SignIn(Screen):
    pass


class FileLayout(Widget):
    pass


class FilePicker(Screen):
    pass


class CommentsScreen(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("Login.kv")


class LoginApp(App):
    def build(self):
        return kv


LoginApp().run()
