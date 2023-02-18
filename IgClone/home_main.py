import json

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

from kivymd.uix.card import MDCard
from kivy.properties import StringProperty


class CircularAvatarImage(MDCard):
    avatar = StringProperty()
    name = StringProperty()


class PostCard(MDCard):
    profile_pic = StringProperty()
    avatar = StringProperty()
    username = StringProperty()
    post = StringProperty()
    caption = StringProperty()
    up_votes = StringProperty()
    down_votes = StringProperty()
    comments = StringProperty()


class HomePage(MDScreen):
    profile_picture = 'https://avatars.githubusercontent.com/u/89080192?v=4'

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
                    up_votes=data[username]['up_votes'],
                    down_votes=data[username]['down_votes'],
                    comments=data[username]['comments']
                ))


class MainApp(MDApp):
    def build(self):
        Window.size = [300, 600]
        Builder.load_file('home_page.kv')
        return HomePage()

    def on_start(self):
        self.root.dispatch('on_enter')


if __name__ == "__main__":
    MainApp().run()
