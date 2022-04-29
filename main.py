# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 11:46:13 2018

@author: Alabi Abiodun
"""

import wx
import wx.adv


class Example(wx.Frame):

    def __init__(self, parent, title, style):
        super(Example, self).__init__(parent, title=title, style = style)

        self.InitUI()
        self.Centre()
        
        
        ico = wx.Icon('ico.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(ico)

#        self.tbicon = wx.adv.TaskBarIcon()
#        self.tbicon.SetIcon(ico, "Compound Interest")
#        self.tbicon.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.OnTaskBarClose)
        #wx.adv.EVT_TASKBAR_LEFT_DOWN(self.tbicon, self.OnTaskBarRight)                

    
    def InitUI(self):

        self.panel = wx.Panel(self)
        self.sizer = wx.GridBagSizer(0, 0)

        self.text1 = wx.StaticText(self.panel, label="Principal")
        self.sizer.Add(self.text1, pos=(0, 0), flag=wx.ALL, border=10)
        
        self.text2 = wx.StaticText(self.panel, label="Rate (%)")
        self.sizer.Add(self.text2, pos=(1, 0), flag=wx.ALL, border=10)
        
        self.text3 = wx.StaticText(self.panel, label="Number of Years")
        self.sizer.Add(self.text3, pos=(2, 0), flag=wx.ALL, border=10)

        self.tc1 = wx.TextCtrl(self.panel)
        self.sizer.Add(self.tc1, pos=(0, 1), span=(1, 5),
            flag=wx.EXPAND|wx.ALL, border=10)
        
        self.tc2 = wx.TextCtrl(self.panel)
        self.sizer.Add(self.tc2, pos=(1, 1), span=(1, 5),
           flag=wx.EXPAND|wx.ALL, border=10)
        
        self.tc3 = wx.TextCtrl(self.panel)
        self.sizer.Add(self.tc3, pos=(2, 1), span=(1, 5),
            flag=wx.EXPAND|wx.ALL, border=10)
        
        self.button1 = wx.Button(self.panel, label="COMPUTE", size=(90, 28))
        self.sizer.Add(self.button1, pos=(4, 2),flag = wx.ALIGN_RIGHT|wx.ALL,border=5)
        
        self.button2 = wx.Button(self.panel, label="CLEAR", size=(90, 28))
        self.sizer.Add(self.button2, pos=(4, 3),flag = wx.ALL,border=5)
        
        self.tc4 = wx.TextCtrl(self.panel,style = wx.TE_MULTILINE|wx.ALIGN_LEFT|wx.TE_READONLY|wx.HSCROLL)
        self.sizer.Add(self.tc4, pos=(3, 0), span=(1, 5),
            flag=wx.EXPAND|wx.ALL,border=10)

        
        self.sizer.AddGrowableCol(0)
        self.sizer.AddGrowableCol(1)
        self.sizer.AddGrowableCol(2)
        self.sizer.AddGrowableRow(3)
        
        self.panel.SetSizer(self.sizer)
        self.button1.Bind(wx.EVT_BUTTON,self.Compute)
        self.button2.Bind(wx.EVT_BUTTON,self.Clear)
               
        #tc4.SetValue('Number of Years\t\t\tAmount')
        
    def Compute(self,event):
        self.P = float(self.tc1.GetValue())
        self.R = float(self.tc2.GetValue())
        self.n = int(float(self.tc3.GetValue()))
        
        self.tc4.SetValue('Number of Years\t\tAmount\n')
            
        for i in range(1, self.n + 1):
            self.Amount = self.P * ((1 + self.R) ** i)           
            self.tc4.AppendText('\t%s\t\t%s\n'%(str(i),str('%0.3f'%self.Amount)))
                     
    def Clear(self,event):
        self.tc1.Clear()
        self.tc2.Clear()
        self.tc3.Clear()
        self.tc4.Clear()
        
        self.tc1.SetFocus()
        
#    def OnTaskBarClose(self, event):
#        #self.Hide()
#        self.tbicon.Destroy()
#        #self.Destroy()
#        wx.Exit()
        
          
def main():
    app = wx.App()
    ex = Example(None, title='Compound Interest', style = wx.SYSTEM_MENU|wx.CAPTION|wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.CLOSE_BOX)
    ex.Show()
    ex.CenterOnScreen()
    app.MainLoop()
    del app

if __name__ == '__main__':
    main()