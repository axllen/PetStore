import wx

from dao.account_dao import AccountDao
from ui.product_list_frame import ProductListFrame


class LoginFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='登录', size=(340, 230))
        self.Center()
        self.panel = wx.Panel(self)
        self.icon = wx.Icon('resources\\icon\\dog4.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

        # 用户名密码输入界面
        user_text = wx.StaticText(self.panel, label='用户名：')
        password_text = wx.StaticText(self.panel, label='密码：')
        self.user_tc = wx.TextCtrl(self.panel)
        self.password_tc = wx.TextCtrl(self.panel, style=wx.TE_PASSWORD)
        login_grid = wx.FlexGridSizer(2, 2, 2)
        login_grid.AddMany([
            user_text,
            (self.user_tc, 1, wx.EXPAND),
            password_text,
            (self.password_tc, 1, wx.EXPAND)
        ])
        login_grid.AddGrowableCol(0, 1)
        login_grid.AddGrowableCol(1, 4)
        login_grid.AddGrowableRow(0, 1)
        login_grid.AddGrowableRow(1, 1)

        # 登录按钮
        submit_button = wx.Button(parent=self.panel, label='确定')
        self.Bind(wx.EVT_BUTTON, self.submit_button_onclick, submit_button)
        cancel_button = wx.Button(parent=self.panel, label='取消')
        self.Bind(wx.EVT_BUTTON, self.cancel_button_onclick, cancel_button)
        horizontal_box = wx.BoxSizer()
        horizontal_box.Add(submit_button, 1, wx.CENTER | wx.ALL | wx.EXPAND, border=10)
        horizontal_box.Add(cancel_button, 1, wx.CENTER | wx.ALL | wx.EXPAND, border=10)

        # 垂直布局界面
        vertical_box = wx.BoxSizer(wx.VERTICAL)
        vertical_box.Add(login_grid, 1, wx.CENTER | wx.ALL | wx.EXPAND, 25)
        vertical_box.Add(horizontal_box, 1, wx.CENTER | wx.BOTTOM, 20)

        self.panel.SetSizer(vertical_box)

    def submit_button_onclick(self, event):
        dao = AccountDao()
        account = dao.find_by_id(self.user_tc.GetValue())
        input_password = self.password_tc.GetValue()
        if account and account['password'] == input_password:
            print('登录成功')
            next_frame = ProductListFrame()
            next_frame.Show()
            self.Destroy()
        else:
            print('登录失败')
            dialog = wx.MessageDialog(self, '用户名或密码错误', '登录失败')
            dialog.ShowModal()
            dialog.Destroy()

    def cancel_button_onclick(self, event):
        self.Destroy()


class App(wx.App):
    def OnInit(self):
        login_frame = LoginFrame()
        login_frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()
