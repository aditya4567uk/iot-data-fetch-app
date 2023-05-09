from kivy.factory import Factory
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivymd.uix.card import MDCard
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window


Window.size = (450, 670)



class MainApp(MDApp):

    def show_custom_bottom_sheet(self,image,price,rate):
        bottom_sheet=Factory.ContentCustomSheet()
        bottom_sheet.rate=rate
        bottom_sheet.image=image
        bottom_sheet.price=price
        self.custom_sheet = MDCustomBottomSheet(screen=bottom_sheet)
        self.custom_sheet.open()
    def build(self):
        self.title = 'Bezubaan Monitor App'
        self.theme_cls.primary_palette = "Orange"

MainApp().run()


# get animal health status ,Profile ,best doctors nearby ,call emergency number