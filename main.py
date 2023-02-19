import json

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

from kivymd.uix.card import MDCard
from kivy.properties import StringProperty

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


class PostCard(MDCard):
    profile_pic = StringProperty()
    avatar = StringProperty()
    username = StringProperty()
    post = StringProperty()
    caption = StringProperty()
    likes = StringProperty()
    comments = StringProperty()
    posted_ago = StringProperty()


class HomePage(MDScreen):
    profile_picture = 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80'

    def on_enter(self):
        self.list_posts()

    def list_posts(self):
        with open('assets/posts.json') as f_obj:
            data = json.load(f_obj)
            for username in data:
                self.ids.timeline.add_widget(PostCard(
                    username=username,
                    avatar=data[username]['avatar'],
                    profile_pic=self.profile_picture,
                    post=data[username]['post'],
                    caption=data[username]['caption'],
                    likes=data[username]['likes'],
                    comments=data[username]['comments']
                ))


class HomeApp(MDApp):
    def build(self):
        Window.size = [300, 600]
        Builder.load_file('home_page.kv')
        return HomePage()

    def on_start(self):
        self.root.dispatch('on_enter')


class WindowManager(ScreenManager):
    pass


class PlantApp(MDApp):
    def build(self):
        Window.size = [300, 600]
        kv = Builder.load_file("Login.kv")
        return kv


if __name__ == '__main__':
    PlantApp().run()
