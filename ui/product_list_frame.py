import wx


class ProductListFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='请选择商品', size=(1000, 700))
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetSizer(self.create_top_box())

    def create_top_box(self):
        """顶部布局"""
        text = wx.StaticText(self.panel, label='请选择类别')
        category_list = ['鸟类', '鱼类', '猫类', '狗类', '爬行类']
        category_choice = wx.Choice(self.panel, -1, choices=category_list)
        search_button = wx.Button(self.panel, label='查找', id=1)
        reset_button = wx.Button(self.panel, label='重置', id=2)
        top_box = wx.BoxSizer()
        top_box.AddSpacer(200)
        top_box.AddMany([
            (text, 1, wx.FIXED_MINSIZE | wx.ALL, 10),
            (category_choice, 1, wx.EXPAND | wx.ALL, 5),
            (search_button, 1, wx.EXPAND | wx.ALL, 5),
            (reset_button, 1, wx.EXPAND | wx.ALL, 5)
        ])
        top_box.AddSpacer(260)

        return top_box

    def create_left_panel(self, parent):
        panel = wx.Panel(parent)
        