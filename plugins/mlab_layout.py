import pcbnew
import os

import wx
import wx.xrc

class Mywin(wx.Frame): 
   
   
            
   def __init__(self, parent, title): 
        super(Mywin, self).__init__(parent, title = title,size = (300,200))  

        self.pcbnew_version = int(pcbnew.Version()[0])
        if self.pcbnew_version == 7:
            self.ui_mm = pcbnew.PCB_IU_PER_MM
            self.VECTOR_MM = pcbnew.VECTOR2I_MM
        elif self.pcbnew_version == 6:
            self.ui_mm = pcbnew.IU_PER_MM
            self.VECTOR_MM = pcbnew.wxPointMM
        else:
            print("Nepodporovana verze KICAD PCBNEW")
            exit();

        self.InitUI() 
         
   def InitUI(self):    
        self.count = 0 
        pnl = wx.Panel(self) 
        vbox = wx.BoxSizer(wx.VERTICAL) 

        hbox1 = wx.BoxSizer(wx.HORIZONTAL) 
        hbox2 = wx.BoxSizer(wx.HORIZONTAL) 
        hbox3 = wx.BoxSizer(wx.HORIZONTAL) 

        self.sizex = wx.SpinCtrl(pnl, size = (250, 25), initial = 3)
        self.sizey = wx.SpinCtrl(pnl, size = (250, 25), initial = 3)
        self.holes = wx.TextCtrl(pnl, size = (250, 25), value = "M1,M2,M3,M4")
        self.btn1 = wx.Button(pnl, label = "Prepare module layout") 
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.btn1) 

        hbox1.Add(wx.StaticText(pnl, label = "Pattern width  ")) 
        hbox1.Add(self.sizex, flag = wx.ALIGN_CENTRE) 
        hbox2.Add(wx.StaticText(pnl, label = "Pattern height  ")) 
        hbox2.Add(self.sizey, flag = wx.ALIGN_CENTRE) 
        hbox3.Add(wx.StaticText(pnl, label = "Hole names")) 
        hbox3.Add(self.holes, flag = wx.ALIGN_CENTRE) 

        vbox.Add((0, 2)) 
        vbox.Add(hbox1, flag = wx.ALIGN_CENTRE) 
        vbox.Add((0, 2)) 
        vbox.Add(hbox2, flag = wx.ALIGN_CENTRE) 
        vbox.Add((0, 2)) 
        vbox.Add(hbox3, flag = wx.ALIGN_CENTRE) 
        vbox.Add((0, 5)) 
        vbox.Add(self.btn1, flag = wx.ALIGN_CENTRE) 
        #vbox.Add(hbox2, proportion = 1, flag = wx.ALIGN_CENTRE) 


        pnl.SetSizer(vbox) 
        self.Centre() 
        self.Show(True)
		
   def OnClick(self, e):
        print("Parameters from input form")
        size = (self.sizex.GetValue(), self.sizey.GetValue())
        print("Prepare MLAB module with pattern {}x{}".format(*size))

        board = pcbnew.GetBoard()

        for d in board.GetDrawings():
            #print(d, d.GetLayer())
            if d.GetLayer() == pcbnew.Edge_Cuts:
                board.Remove(d)

        #offset = (board.GetCenter()[0]/self.ui_mm-10.16*(size[0]+1)/2, board.GetCenter()[1]/self.ui_mm-10.16*(size[1]+1)/2)
        offset = (297/2-10.16*(size[0]+1)/2, 210/2-10.16*(size[1]+1)/2)

        ed = pcbnew.PCB_SHAPE(board)
        ed.SetShape(pcbnew.SHAPE_T_RECT)
        ed.SetFilled(False)
        ed.SetStart(self.VECTOR_MM(offset[0]+0.254, offset[1]+0.254))
        ed.SetEnd(self.VECTOR_MM(offset[0]+10.16*(size[0]+1) - 0.254, offset[1]+10.16*(size[1]+1) - 0.254))
        ed.SetLayer(pcbnew.Edge_Cuts)
        ed.SetWidth(int(pcbnew.DEFAULT_PCB_EDGE_THICKNESS * self.ui_mm))
        board.Add(ed)

        components = self.holes.GetValue()
        coord = [ (0.5, 0.5),
                  (0.5 + size[0], 0.5),
                  (0.5, 0.5 + size[1]),
                  (0.5 + size[0], 0.5 + size[1]),
                ]
        for i, comp in enumerate(components.split(",")):
            print(i, comp)
            co = board.FindFootprintByReference(comp)
            co.SetPosition(self.VECTOR_MM(coord[i][0]*10.16+offset[0], coord[i][1]*10.16+offset[1]))

        print("ORIGIN....")
        bset = board.GetDesignSettings()
        opos = self.VECTOR_MM(offset[0]+10.16*(-0.5), offset[1]+10.16*(size[1]+1.5))
        bset.SetGridOrigin(opos)
        bset.SetAuxOrigin(opos)
        #board.RefillBoardAreas()
        pcbnew.Refresh()

        self.Close() 

class SimplePlugin(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "MLAB PCB layout generator"
        self.category = "Board generator"
        self.description = "Prepares the PCB layout of the MLAB boards in the right size and shape"
        self.show_toolbar_button = False
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'simple_plugin.png')

    def Run(self):
        ex = wx.App() 
        Mywin(None,'MLAB layout generator') 
        ex.MainLoop()

SimplePlugin().register() 
