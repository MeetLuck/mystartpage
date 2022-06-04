from import_components import *
from functools import partial
from starthelp.starthelp import *
from mycal.mycalendar import MyCalendar
from datetime import datetime,timedelta
import os

#Window.clearcolor = (0.5,0.5,0.5,1)
LabelBase.register(name='NanumGothic', fn_regular='NanumGothic.ttf',fn_bold='NanumGothicBold.ttf')

class MyLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = 0.6,0.6,0.6,1
        self.size = self.texture_size
        self.font_name='NanumGothic'
        self.bind(size=self.setter('text_size'))    
        
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 5
        self.padding = 5
        self.spacing = 5
        self.create_layout()

    def create_layout(self):
        self.theday       = MyLabel(text='0',size_hint=(0.2,1),halign= 'center')
        self.dayteam      = MyLabel(text='1',size_hint=(0.1,1),halign= 'center')
        self.dayworkers   = MyLabel(text='2',size_hint=(0.3,1),halign='left')
        self.nightteam    = MyLabel(text='3',size_hint=(0.1,1),halign='center')
        self.nightworkers = MyLabel(text='4',size_hint=(0.3,1),halign='left')
        self.add_widget(self.theday)
        self.add_widget(self.dayteam)
        self.add_widget(self.dayworkers)
        self.add_widget(self.nightteam)
        self.add_widget(self.nightworkers)

    def update(self,off): # [6/1,A1,이종화, B1,서광석]
        self.theday.text        = off[0]
        self.dayteam.text       = off[1]
        self.dayworkers.text    = off[2]
        self.dayteam.text       = off[3]
        self.nightworkers.text  = off[4]


class OffBox(MDBoxLayout):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 0
        self.spacing = 5
        self.create_layout()

    def create_layout(self,date=datetime(2022,6,1)):
        for off in convert_offworkers(date):
            grid = MyGrid()
            grid.update(off)
            self.add_widget(grid)

    def update_offworkers(self,date):
        root = App.get_running_app().root
        print('==>',self.parent)
        print('================>',App.get_running_app().root)
        #print('================>',root.date)
        off = convert_offworkers(datetime(*date))
        for i,grid in enumerate( reversed(self.children) ):
            for j,label in enumerate(reversed(grid.children) ):
                label.text = off[i][j]
                label.bold = True


if __name__ ==  '__main__':

    kv = '''
<RootWidget@MDBoxLayout>:
    orientation:'vertical'
<OffBox@MDBoxLayout>:
    orientation:'vertical'

<RootWidget>:
    myoffworkers:id_myoffworkers
    OffBox:
        id: id_myoffworkers
    Button:
        text:'change date'
        on_press: root.on_press()
    '''
    Builder.load_string(kv)
    Window.size = 600,400 #kvfile = join(dirname(__file__),'mycalendar.kv')
    Window.clearcolor = 0,0,0,1
    class RootWidget(MDBoxLayout):
        #date = ObjectProperty()
        def __init__(self,**kwargs):
            super().__init__(**kwargs)
            self.date = (2022,6,1)
            print( datetime( *self.date))
        def on_press(self):
            self.date = (2022,6,12)
            self.myoffworkers.update_offworkers(self.date)

    class TestApp(MDApp):
        def build(self):
            return RootWidget()

    TestApp().run()
