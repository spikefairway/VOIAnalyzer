#!/usr/bin/env python
# coding : utf-8

"""
GUI interface for VOI analyzer.
"""

import wx
import os

from VOIAnalyzer.base import _analysis

class VOIAnalyzerGUI(wx.Frame):
    """ Frame for VOIAnalyzer.
    """
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,
                          "VOIAnalyzer",
                          size=(400, 500))
        # Panel
        self.panel = VOIAnalyzerGUIPanel(self, wx.ID_ANY,
                                         size=(400, 500))

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
        self.button_plus_img.Bind(wx.EVT_BUTTON, self.OnPushButton_img_plus)
        self.button_minus_img.Bind(wx.EVT_BUTTON, self.OnPushButton_img_minus)

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
        style4text = wx.TE_READONLY|wx.HSCROLL|wx.TE_RIGHT
        self.text_voi = wx.TextCtrl(self, wx.ID_ANY,
                                    style=style4text)

        # Button to open VOI map file
        self.button_voi = wx.BitmapButton(self, wx.ID_ANY,
                wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN))
        self.button_voi.Bind(wx.EVT_BUTTON, self.OnPushButton_VOI)

        # Layout for VOI map
        box_voi = wx.StaticBox(self, wx.ID_ANY, "VOI map")
        layout_voi = wx.StaticBoxSizer(box_voi, wx.HORIZONTAL)
        layout_voi.Add(self.text_voi, flag=wx.EXPAND,
                       proportion=12)
        layout_voi.Add(self.button_voi,
                       proportion=1)

        # Text control for table
        self.text_tab = wx.TextCtrl(self, wx.ID_ANY,
                                    style=style4text)

        # Button to open output file
        self.button_tab = wx.BitmapButton(self, wx.ID_ANY,
                wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN))
        self.button_tab.Bind(wx.EVT_BUTTON, self.OnPushButton_out)

        # Layout for output file
        box_tab = wx.StaticBox(self, wx.ID_ANY,
                               "Output CSV file")
        layout_tab = wx.StaticBoxSizer(box_tab, wx.HORIZONTAL)
        layout_tab.Add(self.text_tab, flag=wx.EXPAND,
                       proportion=12)
        layout_tab.Add(self.button_tab,
                       proportion=1)

        # Text control for VOI look-up table file
        self.text_lut = wx.TextCtrl(self, wx.ID_ANY,
                                    style=style4text)

        # Button to open VOI look-up table file
        self.button_lut = wx.BitmapButton(self, wx.ID_ANY,
                wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN))
        self.button_lut.Bind(wx.EVT_BUTTON, self.OnPushButton_LUT)

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
        self.button_analyze.Bind(wx.EVT_BUTTON, self.OnPushButton_analyze)
        self.button_close = wx.Button(self, wx.ID_ANY, "Close")
        self.button_close.Bind(wx.EVT_BUTTON, self.OnPushButton_close)
        
        # Layout for buttons to analyze
        layout_ana = wx.BoxSizer(wx.HORIZONTAL)
        layout_ana.Add(self.button_analyze)
        layout_ana.Add(self.button_close)

        # Layout for panel
        layout_main = wx.BoxSizer(wx.VERTICAL)
        layout_main.Add(layout_imglist, flag=wx.EXPAND,
                        proportion=5)
        layout_main.Add(layout_voi, flag=wx.EXPAND,
                        proportion=2)
        layout_main.Add(layout_tab, flag=wx.EXPAND,
                        proportion=2)
        layout_main.Add(layout_lut, flag=wx.EXPAND,
                        proportion=2)
        layout_main.Add(layout_ana, flag=wx.ALIGN_RIGHT,
                        proportion=1)

        self.SetSizer(layout_main)

    def OnPushButton_img_plus(self, evt):
        """ Callback for plus button
        """
        # File dialog
        dlg = wx.FileDialog(self, style=wx.FD_OPEN|wx.FD_MULTIPLE|wx.FD_FILE_MUST_EXIST)
        res = dlg.ShowModal()
        if res == wx.ID_OK:
            flist = dlg.GetPaths()

            # Append files
            self.listbox_img.Append(flist)
        dlg.Destroy()

        return None

    def OnPushButton_img_minus(self, evt):
        """ Callback for minus button
        """
        idx_selected = self.listbox_img.GetSelections()
        [self.listbox_img.Delete(idx) for idx in reversed(idx_selected)]

        return None

    def open_file(self, style=wx.FD_OPEN|wx.FD_FILE_MUST_EXIST, **kwargs):
        """ Pop-up dialog to open file.
        """
        dlg = wx.FileDialog(self, style=style, **kwargs)
        res = dlg.ShowModal()
        if res == wx.ID_OK:
            fname = dlg.GetFilename()
            dirname = dlg.GetDirectory()
            fpath = os.path.join(dirname, fname)
        else:
            fpath = None
        dlg.Destroy()

        return fpath

    def OnPushButton_VOI(self, evt):
        """ Callback for open button for VOI.
        """
        # Open dialog
        fpath = self.open_file(message="Open VOI map file",
                               wildcard="NIfTI image (.nii)|.nii")

        if fpath is not None:
            self.text_voi.SetValue(fpath)

        return None

    def OnPushButton_out(self, evt):
        """ Callback for open button for look-up table file.
        """
        # Open dialog
        fpath = self.open_file(message="Select file to output",
                               style=wx.FD_SAVE)

        if fpath is not None:
            self.text_tab.SetValue(fpath)

        return None

    def OnPushButton_LUT(self, evt):
        """ Callback for open button for look-up table file.
        """
        # Open dialog
        fpath = self.open_file(message="Open VOI look-up table file")

        if fpath is not None:
            self.text_lut.SetValue(fpath)

        return None

    def OnPushButton_analyze(self, evt):
        """ Callback for analyze button.
        """
        # Image files
        img_list = self.listbox_img.GetItems()

        # VOI map
        voi_file = self.text_voi.GetValue()
        voi_mat, aff = utils.loadImage(voi_file)[:2].astype(np.int16)
        vno_list = np.unique(voi_mat)
        nVOI = vno_list.size

        # Volume per voxel (unit: cm3)
        vol_per_vox = np.abs(np.prod(np.diag(aff[:3, :3])))

        # Maximum progress
        progress_max = nVOI * len(img_list) + 1
        cur_progress = 0

        # Output file
        out_file = self.text_tab.GetValue()

        # Show progress dialog
        self.progress = wx.ProgressDialog("Analyzing...",
                                          "Initiate analysis",
                                          maximum=progress_max,
                                          parent=self)
        self.progress.ShowModal()

        # VOI analysis
        tab_list = []
        for img_path in img_list:
            img_mat, img_aff = utils.loadImage(img_path)[:2]

            # Check shape
            if not np.all(img_aff == aff):
                dlg = wx.MessageDialog(self,
                                       "Image orientation and size must be same as VOI map",
                                       "Caution",
                                       wx.OK|wx.ICON_EXCLAMATION)
                dlg.ShowModal()
                self.progress.Destroy()
                
                return None
            
            img_file = os.path.basename(img_path)
            
            for vno in vno_list:
                # Progress
                msg = "Extracting value on VOI #{0:d}, {1:s}".format(vno, img_file)
                self.progress.Update(cur_progress,
                                     newmsg=msg)

                # Extract
                tab0 = _analysis(img_mat, voi_mat, vno)
                tab_list.append(tab0)

                cur_progress += 1

        out_tab = pd.concat(tab_list)

        # Calculate volumes (unit: cm3)
        self.progress.Update(cur_progress,
                             newmsg="Calculating VOI volumes")
        out_tab.loc[:, "Volume"] = out_tab.loc[:, "No. of voxels"].values * vol_per_vox / 1000.
        cur_progress += 1

        # LUT file
        self.progress.Update(cur_progress,
                             newmsg="Applying look-up table")
        if not self.text_lut.IsEmpty:
            lut_file = self.text_lut.GetValue()
            lut = utils.loadLUT(lut_file)
            out_tab.loc[:, "VOI"] = out_tab.loc[:, "VOI No."].map(lut)
        cur_progress += 1

        # Output
        out_tab.to_csv(out_file, index=False)
        self.progress.Update(progress_max,
                             newmsg="Complete.")

        dlg = wx.MessageDialog(self,
                               "Complete.",
                               "Message",
                               wx.OK|wx.ICON_INFORMATION)
        dlg.ShowModal()

        return None

    def OnPushButton_close(self, evt):
        """ Callback for close button.
        """
        self.parent.Destroy()
        self.Destroy()
    

if __name__ == "__main__":
    app = wx.App(False)
    VOIAnalyzerGUI()
    app.MainLoop()
