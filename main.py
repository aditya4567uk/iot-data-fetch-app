from kivy.factory import Factory
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivymd.uix.card import MDCard
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from twilio.rest import Client
import webbrowser



Window.size = (450, 670)



class MainApp(MDApp):

    def show_custom_bottom_sheet(self,image,labels,rate):
        bottom_sheet=Factory.ContentCustomSheet()
        bottom_sheet.rate=rate # values of different measuring parameters
        bottom_sheet.image=image
        bottom_sheet.labels=labels #oxygen , o2, heart rate, blood pressure
        self.custom_sheet = MDCustomBottomSheet(screen=bottom_sheet)
        self.custom_sheet.open()
    
    def dial(self):
        try:
            callto='1962' # Helpline number by govt of India
            callfrom='6299098884'
            account_sid = 'ACc3175e8475472fbbc2ab2147a250e8c8'
            auth_token = 'ec329c0176f329492929b116363f90a7'
            client=Client(account_sid,auth_token)
            call = client.calls.create(
                twiml='<Response><Say>Hello Animal helpline</Say><Response>',
                to=callto,
                from_=callfrom)
            print("Code Success!")
            print(call.sid)
        except NameError:
            print(NameError)
            raise TypeError(NameError)
    
    def oxygenbrowse(self):
        url='https://www.pnas.org/doi/10.1073/pnas.1400547111'
        webbrowser.open(url)
    
    def heartratebrowse(self):
        url='https://www.msdvetmanual.com/multimedia/table/resting-heart-rates'
        webbrowser.open(url)
    
    def bpbrowse(self):
        url='https://carrington.edu/blog/high-blood-pressure-in-animals/'
        webbrowser.open(url)
    
    def temperaturebrowse(self):
        url='https://www.msdvetmanual.com/multimedia/table/normal-rectal-temperature-ranges'
        webbrowser.open(url)
        
    
    def build(self):
        self.title = 'Bezubaan Monitor App'
        self.theme_cls.primary_palette = "Orange"

MainApp().run()


# get animal health status ,Profile ,best doctors nearby ,call emergency number
