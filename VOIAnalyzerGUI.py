#!/usr/bin/env python
# coding : utf-8

"""
GUI interface for VOI analyzer.
"""

import wx

from VOIAnalyzer.base import voi_analysis

class VOIAnalyzerGUI(wx.Frame):
    """ Frame for VOIAnalyzer.
    """
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,
                          "VOIAnalyzer",
                          size=(400, 400))
        # Panel
        self.panel = VOIAnalyzerGUIPanel(self, wx.ID_ANY,
                                         size=(400, 400))

        # Layout
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(self.panel, flag=wx.EXPAND)

        self.SetSizer(layout)

        self.Show()

class VOIAnalyzerGUIPanel(wx.Panel):
    """ Panel for VOIAnalyzerGUI.
    """
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)

        self.parent = self.GetParent()

        # Border size
        self.bdsize = 5

        # List for image to extract
        self.listbox_img = wx.ListBox(self, wx.ID_ANY,
                style=wx.LB_HSCROLL|wx.LB_NEEDED_SB|wx.LB_EXTENDED)

        # Buttons to control image list
        self.button_plus_img = wx.BitmapButton(self, wx.ID_ANY,
                wx.ArtProvider.GetBitmap(wx.ART_PLUS))
        self.button_minus_img = wx.BitmapButton(self, wx.ID_ANY,
                wx.ArtProvider.GetBitmap(wx.ART_MINUS))
        font4imgbutton = wx.Font(18, wx.FONTFAMILY_DEFAULT,
                                 wx.FONTSTYLE_NORMAL,
                                 wx.FONTWEIGHT_NORMAL)
        self.button_plus_img.SetFont(font4imgbutton)
        self.button_minus_img.SetFont(font4imgbutton)

        # Layout for buttons to control image
        layout_imgbutton = wx.BoxSizer(wx.VERTICAL)
        layout_imgbutton.Add(self.button_plus_img,
                             flag=wx.EXPAND)
        layout_imgbutton.Add(self.button_minus_img,
                             flag=wx.EXPAND)

        # Layout for image list
        box_imglist = wx.StaticBox(self, wx.ID_ANY, "Images to analyze")
        layout_imglist = wx.StaticBoxSizer(box_imglist, wx.HORIZONTAL)
        layout_imglist.Add(self.listbox_img, flag=wx.EXPAND,
                           proportion=12)
        layout_imglist.Add(layout_imgbutton, flag=wx.EXPAND,
                           proportion=1)

        # Text control for VOI map file
        self.text_voi = wx.TextCtrl(self, wx.ID_ANY,
                                    style=wx.TE_READONLY)

        # Button to open VOI map file
        self.button_voi = wx.BitmapButton(self, wx.ID_ANY,
                wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN))

        # Layout for VOI map
        box_voi = wx.StaticBox(self, wx.ID_ANY, "VOI map")
        layout_voi = wx.StaticBoxSizer(box_voi, wx.HORIZONTAL)
        layout_voi.Add(self.text_voi, flag=wx.EXPAND,
                       proportion=12)
        layout_voi.Add(self.button_voi,
                       proportion=1)

        # Text control for VOI look-up table file
        self.text_lut = wx.TextCtrl(self, wx.ID_ANY,
                                    style=wx.TE_READONLY)

        # Button to open VOI look-up table file
        self.button_lut = wx.BitmapButton(self, wx.ID_ANY,
                wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN))

        # Layout for VOI map
        box_lut = wx.StaticBox(self, wx.ID_ANY,
                               "Look-up table (optional)")
        layout_lut = wx.StaticBoxSizer(box_lut, wx.HORIZONTAL)
        layout_lut.Add(self.text_lut, flag=wx.EXPAND,
                       proportion=12)
        layout_lut.Add(self.button_lut,
                       proportion=1)

        # Button to analyze and close
        self.button_analyze = wx.Button(self, wx.ID_ANY, "Analyze")
        self.button_close = wx.Button(self, wx.ID_ANY, "Close")
        
        # Layout for buttons to analyze
        layout_ana = wx.BoxSizer(wx.HORIZONTAL)
        layout_ana.Add(self.button_analyze)
        layout_ana.Add(self.button_close)

        # Layout for panel
        layout_main = wx.BoxSizer(wx.VERTICAL)
        layout_main.Add(layout_imglist, flag=wx.EXPAND,
                        proportion=5)
        layout_main.Add(layout_voi, flag=wx.EXPAND,
                        proportion=1)
        layout_main.Add(layout_lut, flag=wx.EXPAND,
                        proportion=1)
        layout_main.Add(layout_ana, flag=wx.ALIGN_RIGHT,
                        proportion=1)

        self.SetSizer(layout_main)

if __name__ == "__main__":
    app = wx.App(False)
    VOIAnalyzerGUI()
    app.MainLoop()
