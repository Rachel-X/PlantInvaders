import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder


# sign in information is from 
class SignIn(Screen):
    pass


class FilePicker(Screen):
    pass


class CommentsScreen(Screen):
    pass


class Manager(ScreenManager):
    pass


kv = Builder.load_file("Login.kv")


class LoginApp(App):
    def build(self):
        return kv


LoginApp().run()
