from import_components import *

class MyFoldersButton(MDRectangleFlatIconButton):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.icon = "folder"
        self.pos_hint = {"center_x":.5,"center_y":.5}
        #self.size_hint_x = None
        #self.width: 190
        #self.text_size = self.size
        self.font_size = 14
        #self.theme_icon_size = "Custom"
        self.md_bg_color =0,0,0,0
        #self.icon_size = '256sp'
        self.text_color = Color.folders.fg
        self.icon_color = Color.folders.bg
        self.font_name = 'NotoSerifKR'
        self.line_color = 0,0,0,0
        self.padding = 0
#        self.on_press = self.text_color = [1,0,0,1]
#        self.on_release = self.text_color =  [0,0,1,1]

class MyFoldersBox(MDGridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 4
        self.rows = 3
        self.padding = 0,0,0,0
        self.spacing = 5,0
        #self.root = MDApp.get_running_app().root
        self.create_layout()

    def create_layout(self):
        #print(minwonfile)
        self.workfolderbtn          = MyFoldersButton(text='업무문서',on_press=self.on_press)
        self.commutefolderbtn       = MyFoldersButton(text='출근부',on_press=self.on_press)
        self.weeklyreportfolderbtn  = MyFoldersButton(text='주간업무',on_press=self.on_press)
        self.incidentfolderbtn      = MyFoldersButton(text='사건사고',on_press=self.on_press)
        self.Afolderbtn             = MyFoldersButton(text='A조',on_press=self.on_press)
        self.excellinkfolderbtn     = MyFoldersButton(text='엑셀링크',on_press=self.on_press)
        self.infofolderbtn          = MyFoldersButton(text='안내문',on_press=self.on_press)
        self.dummy1btn              = MyFoldersButton(text=' ',on_press=self.on_press)
        self.parkfolderbtn          = MyFoldersButton(text='박종우',on_press=self.on_press)
        self.cctvfolderbtn          = MyFoldersButton(text='CCTV',on_press=self.on_press)
        self.startfolderbtn         = MyFoldersButton(text='startpage',on_press=self.on_press)
        self.dummy2btn              = MyFoldersButton(text=' ',on_press=self.on_press)
        self.add_widget(self.workfolderbtn)
        self.add_widget(self.commutefolderbtn)
        self.add_widget(self.weeklyreportfolderbtn)
        self.add_widget(self.incidentfolderbtn)
        self.add_widget(self.infofolderbtn)
        self.add_widget(self.Afolderbtn)
        self.add_widget(self.excellinkfolderbtn)
        self.add_widget(self.dummy1btn)
        self.add_widget(self.parkfolderbtn)
        self.add_widget(self.cctvfolderbtn)
        self.add_widget(self.startfolderbtn)
        self.add_widget(self.dummy2btn)

    def on_press(self,btn):
        root = Path(__file__).parent
        if btn == self.minwonreportbtn: os.system( 'python {}'.format(minwonpyfile) )
        if btn == self.minwonDBbtn:     os.system( 'python {}'.format(minwondbfile) )
        if btn == self.dBBrowserbtn:    os.startfile(dbbrowserfile)
        if btn == self.HPScanbtn:       os.startfile(hpscanfile)

if __name__ == '__main__':

    class Test(MDApp):
        def build(self):
            return MyFoldersBox()
    Test().run()
