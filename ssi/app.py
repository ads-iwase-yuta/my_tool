# 参考: https://qiita.com/toriiico/items/0b26ef583e176eecce5d

import os
import sys
import wx
import wx.adv

TRAY_TOOLTIP = 'SSI'
TRAY_ICON = 'resources/logo.ico'


def resourcePath(filename):
  if hasattr(sys, "_MEIPASS"):
      return os.path.join(sys._MEIPASS, filename)
  return os.path.join(filename)

def create_menu_item(menu, label, func):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    menu.AppendItem(item)

    return item


class TaskBarIcon(wx.adv.TaskBarIcon):

    def __init__(self, frame):
        self.frame = frame
        super(TaskBarIcon, self).__init__()
        self.set_icon(resourcePath(TRAY_ICON))
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DCLICK, self.on_open_site)

    def CreatePopupMenu(self):
        menu = wx.Menu()
        menu.AppendSeparator()
        create_menu_item(menu, 'Exit', self.on_exit)

        return menu

    def set_icon(self, path):
        icon = wx.Icon(wx.Bitmap(path))
        self.SetIcon(icon, TRAY_TOOLTIP)

    def on_open_site(self, event):
        open_site()

    def on_exit(self, event):
        print('exit')
        wx.CallAfter(self.Destroy)
        self.frame.Close()
        os._exit(0) # wx停止時、全体も終了させる


class App(wx.App):

    def OnInit(self):
        frame=wx.Frame(None)
        self.SetTopWindow(frame)
        TaskBarIcon(frame)

        return True