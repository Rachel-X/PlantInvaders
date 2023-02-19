import json

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

from kivymd.uix.card import MDCard
from kivy.properties import StringProperty


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
                    likes=data[username]['likes'],
                    comments=data[username]['comments'],
                    posted_ago=data[username]['posted_ago']
                ))


class MainApp(MDApp):
    def build(self):
        Window.size = [300, 600]
        Builder.load_file('TryingThings/home_page.kv')
        return HomePage()

    def on_start(self):
        self.root.dispatch('on_enter')


if __name__ == "__main__":
    MainApp().run()
