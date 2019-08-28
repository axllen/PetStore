import wx


class ProductListFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, '请选择商品', (800, 600))
        self.Center()
        self.panel = wx.Panel(self)

        # 商品列表
