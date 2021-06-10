# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class WelcomeFrame
###########################################################################

class WelcomeFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 641,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Selamat Datang ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 24, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Andalus" ) )

		bSizer11.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Di Toko \"Selalu Makjos\" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 34, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Andalus" ) )

		bSizer11.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button11 = wx.Button( self, wx.ID_ANY, u"Login Sek Lurr", wx.DefaultPosition, wx.Size( 175,40 ), 0 )
		self.m_button11.SetFont( wx.Font( 16, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Andalus" ) )

		bSizer11.Add( self.m_button11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer11 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button11.Bind( wx.EVT_BUTTON, self.btn_login )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_login( self, event ):
		event.Skip()


###########################################################################
## Class FrameLogin
###########################################################################

class FrameLogin ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 300,250 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"LOGIN DULU BOSSS!!!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		self.m_staticText21.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial Black" ) )

		bSizer21.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		bSizer21.Add( self.m_staticText22, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.input_username = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.input_username, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		bSizer21.Add( self.m_staticText23, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.input_pw = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.input_pw, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.tombol_login = wx.Button( self, wx.ID_ANY, u"LOGIN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tombol_login.SetBackgroundColour( wx.Colour( 0, 255, 0 ) )

		bSizer21.Add( self.tombol_login, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer21 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.tombol_login.Bind( wx.EVT_BUTTON, self.btn_login )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_login( self, event ):
		event.Skip()


###########################################################################
## Class FrameKaryawanMgr
###########################################################################

class FrameKaryawanMgr ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 770,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Menu Karyawan" ), wx.VERTICAL )

		fgSizer14 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer14.SetFlexibleDirection( wx.BOTH )
		fgSizer14.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText22 = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"Data Karyawan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		self.m_staticText22.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Narrow" ) )

		bSizer8.Add( self.m_staticText22, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		fgSizer14.Add( bSizer8, 1, wx.EXPAND, 5 )

		fgSizer15 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer15.SetFlexibleDirection( wx.BOTH )
		fgSizer15.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer14.Add( fgSizer15, 1, wx.EXPAND, 5 )

		self.tabel_karyawan = wx.grid.Grid( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tabel_karyawan.CreateGrid( 3, 7 )
		self.tabel_karyawan.EnableEditing( True )
		self.tabel_karyawan.EnableGridLines( True )
		self.tabel_karyawan.EnableDragGridSize( False )
		self.tabel_karyawan.SetMargins( 0, 0 )

		# Columns
		self.tabel_karyawan.EnableDragColMove( False )
		self.tabel_karyawan.EnableDragColSize( True )
		self.tabel_karyawan.SetColLabelSize( 30 )
		self.tabel_karyawan.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabel_karyawan.EnableDragRowSize( True )
		self.tabel_karyawan.SetRowLabelSize( 80 )
		self.tabel_karyawan.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabel_karyawan.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer14.Add( self.tabel_karyawan, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_button24 = wx.Button( sbSizer7.GetStaticBox(), wx.ID_ANY, u"Tambah Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button24, 0, wx.ALL, 5 )


		fgSizer14.Add( bSizer9, 1, wx.EXPAND, 5 )


		sbSizer7.Add( fgSizer14, 1, wx.EXPAND, 5 )


		sbSizer7.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		fgSizer16 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer16.SetFlexibleDirection( wx.BOTH )
		fgSizer16.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button27 = wx.Button( sbSizer7.GetStaticBox(), wx.ID_ANY, u"<< Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.m_button27, 0, wx.ALL, 5 )

		self.m_button26 = wx.Button( sbSizer7.GetStaticBox(), wx.ID_ANY, u"Selesai >>", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.m_button26, 0, wx.ALL, 5 )


		sbSizer7.Add( fgSizer16, 1, wx.EXPAND, 5 )


		self.SetSizer( sbSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.tabel_karyawan.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.tabel_karyawanOnGridCmdSelectCell )
		self.m_button24.Bind( wx.EVT_BUTTON, self.btn_tambah )
		self.m_button27.Bind( wx.EVT_BUTTON, self.btn_back )
		self.m_button26.Bind( wx.EVT_BUTTON, self.btn_end )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def tabel_karyawanOnGridCmdSelectCell( self, event ):
		event.Skip()

	def btn_tambah( self, event ):
		event.Skip()

	def btn_back( self, event ):
		event.Skip()

	def btn_end( self, event ):
		event.Skip()


###########################################################################
## Class FrameInputKry
###########################################################################

class FrameInputKry ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Frame Input Karyawan", pos = wx.DefaultPosition, size = wx.Size( 465,339 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer20 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer20.SetFlexibleDirection( wx.BOTH )
		fgSizer20.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		fgSizer20.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.input_user = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.input_user, 0, wx.ALL, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		fgSizer20.Add( self.m_staticText33, 0, wx.ALL, 5 )

		self.input_pass = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.input_pass, 0, wx.ALL, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Nama Karyawan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		fgSizer20.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.input_nama = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.input_nama, 0, wx.ALL, 5 )

		self.m_staticText35 = wx.StaticText( self, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )

		fgSizer20.Add( self.m_staticText35, 0, wx.ALL, 5 )

		self.input_gender = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.input_gender, 0, wx.ALL, 5 )

		self.m_staticText37 = wx.StaticText( self, wx.ID_ANY, u"Tanggal Lahir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )

		fgSizer20.Add( self.m_staticText37, 0, wx.ALL, 5 )

		self.input_ttl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.input_ttl, 0, wx.ALL, 5 )

		self.m_staticText38 = wx.StaticText( self, wx.ID_ANY, u"Alamat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )

		fgSizer20.Add( self.m_staticText38, 0, wx.ALL, 5 )

		self.input_alamat = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.input_alamat, 0, wx.ALL, 5 )

		self.m_staticText301 = wx.StaticText( self, wx.ID_ANY, u"No Telepon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText301.Wrap( -1 )

		fgSizer20.Add( self.m_staticText301, 0, wx.ALL, 5 )

		self.input_telp = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.input_telp, 0, wx.ALL, 5 )

		self.m_button26 = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.m_button26, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer20 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button26.Bind( wx.EVT_BUTTON, self.btn_simpan )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_simpan( self, event ):
		event.Skip()


###########################################################################
## Class FrameBarangMgr
###########################################################################

class FrameBarangMgr ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 675,331 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		sbSizer41 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Menu Barang" ), wx.VERTICAL )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText21 = wx.StaticText( sbSizer41.GetStaticBox(), wx.ID_ANY, u"Data Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		self.m_staticText21.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer4.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		fgSizer5.Add( bSizer4, 1, wx.EXPAND, 5 )

		fgSizer8 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer5.Add( fgSizer8, 1, wx.EXPAND, 5 )

		self.tabel_barang = wx.grid.Grid( sbSizer41.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tabel_barang.CreateGrid( 5, 5 )
		self.tabel_barang.EnableEditing( True )
		self.tabel_barang.EnableGridLines( True )
		self.tabel_barang.EnableDragGridSize( False )
		self.tabel_barang.SetMargins( 0, 0 )

		# Columns
		self.tabel_barang.EnableDragColMove( False )
		self.tabel_barang.EnableDragColSize( True )
		self.tabel_barang.SetColLabelSize( 30 )
		self.tabel_barang.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabel_barang.EnableDragRowSize( True )
		self.tabel_barang.SetRowLabelSize( 80 )
		self.tabel_barang.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabel_barang.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer5.Add( self.tabel_barang, 0, wx.ALL, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_button33 = wx.Button( sbSizer41.GetStaticBox(), wx.ID_ANY, u"Tambah Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button33, 0, wx.ALL, 5 )

		self.m_button32 = wx.Button( sbSizer41.GetStaticBox(), wx.ID_ANY, u"Cek Laporan", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button32, 0, wx.ALL, 5 )


		fgSizer5.Add( bSizer3, 1, wx.EXPAND, 5 )


		sbSizer41.Add( fgSizer5, 1, wx.EXPAND, 5 )


		sbSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		fgSizer9 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button37 = wx.Button( sbSizer41.GetStaticBox(), wx.ID_ANY, u"<< Back ", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_button37, 0, wx.ALL, 5 )

		self.m_button27 = wx.Button( sbSizer41.GetStaticBox(), wx.ID_ANY, u"Selesai >>", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_button27, 0, wx.ALL, 5 )


		sbSizer41.Add( fgSizer9, 1, wx.EXPAND, 5 )


		self.SetSizer( sbSizer41 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.tabel_barang.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.tabel_barangOnGridCmdSelectCell )
		self.m_button33.Bind( wx.EVT_BUTTON, self.btn_tambah )
		self.m_button32.Bind( wx.EVT_BUTTON, self.btn_cek )
		self.m_button37.Bind( wx.EVT_BUTTON, self.btn_back )
		self.m_button27.Bind( wx.EVT_BUTTON, self.btn_end )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def tabel_barangOnGridCmdSelectCell( self, event ):
		event.Skip()

	def btn_tambah( self, event ):
		event.Skip()

	def btn_cek( self, event ):
		event.Skip()

	def btn_back( self, event ):
		event.Skip()

	def btn_end( self, event ):
		event.Skip()


###########################################################################
## Class FrameInputBrg
###########################################################################

class FrameInputBrg ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Input Data Barang", pos = wx.DefaultPosition, size = wx.Size( 372,276 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer19 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer19.SetFlexibleDirection( wx.BOTH )
		fgSizer19.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"No Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		fgSizer19.Add( self.m_staticText25, 0, wx.ALL, 5 )

		self.input_no = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer19.Add( self.input_no, 0, wx.ALL, 5 )

		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"Nama Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )

		fgSizer19.Add( self.m_staticText26, 0, wx.ALL, 5 )

		self.input_nama = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer19.Add( self.input_nama, 0, wx.ALL, 5 )

		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"Jenis Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		fgSizer19.Add( self.m_staticText27, 0, wx.ALL, 5 )

		self.input_jenis = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer19.Add( self.input_jenis, 0, wx.ALL, 5 )

		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"Harga Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		fgSizer19.Add( self.m_staticText28, 0, wx.ALL, 5 )

		self.input_harga = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer19.Add( self.input_harga, 0, wx.ALL, 5 )

		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"Stok Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		fgSizer19.Add( self.m_staticText29, 0, wx.ALL, 5 )

		self.input_stok = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer19.Add( self.input_stok, 0, wx.ALL, 5 )

		self.m_button24 = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer19.Add( self.m_button24, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer19 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button24.Bind( wx.EVT_BUTTON, self.btn_simpan )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_simpan( self, event ):
		event.Skip()


###########################################################################
## Class FrameBarang
###########################################################################

class FrameBarang ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 627,297 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		sbSizer41 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Menu Barang" ), wx.VERTICAL )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText21 = wx.StaticText( sbSizer41.GetStaticBox(), wx.ID_ANY, u"Data Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		self.m_staticText21.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer4.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		fgSizer5.Add( bSizer4, 1, wx.EXPAND, 5 )

		fgSizer8 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer5.Add( fgSizer8, 1, wx.EXPAND, 5 )

		self.tabel_barang = wx.grid.Grid( sbSizer41.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tabel_barang.CreateGrid( 5, 5 )
		self.tabel_barang.EnableEditing( True )
		self.tabel_barang.EnableGridLines( True )
		self.tabel_barang.EnableDragGridSize( False )
		self.tabel_barang.SetMargins( 0, 0 )

		# Columns
		self.tabel_barang.EnableDragColMove( False )
		self.tabel_barang.EnableDragColSize( True )
		self.tabel_barang.SetColLabelSize( 30 )
		self.tabel_barang.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabel_barang.EnableDragRowSize( True )
		self.tabel_barang.SetRowLabelSize( 80 )
		self.tabel_barang.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabel_barang.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer5.Add( self.tabel_barang, 0, wx.ALL, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_button21 = wx.Button( sbSizer41.GetStaticBox(), wx.ID_ANY, u"Laporkan", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button21, 0, wx.ALL, 5 )


		fgSizer5.Add( bSizer3, 1, wx.EXPAND, 5 )


		sbSizer41.Add( fgSizer5, 1, wx.EXPAND, 5 )


		sbSizer41.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		fgSizer9 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button37 = wx.Button( sbSizer41.GetStaticBox(), wx.ID_ANY, u"<< Back ", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_button37, 0, wx.ALL, 5 )

		self.m_button28 = wx.Button( sbSizer41.GetStaticBox(), wx.ID_ANY, u"Selesai >>", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_button28, 0, wx.ALL, 5 )


		sbSizer41.Add( fgSizer9, 1, wx.EXPAND, 5 )


		self.SetSizer( sbSizer41 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.tabel_barang.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.tabel_barangOnGridCmdSelectCell )
		self.m_button21.Bind( wx.EVT_BUTTON, self.btn_lapor )
		self.m_button37.Bind( wx.EVT_BUTTON, self.btn_back )
		self.m_button28.Bind( wx.EVT_BUTTON, self.btn_end )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def tabel_barangOnGridCmdSelectCell( self, event ):
		event.Skip()

	def btn_lapor( self, event ):
		event.Skip()

	def btn_back( self, event ):
		event.Skip()

	def btn_end( self, event ):
		event.Skip()


###########################################################################
## Class FrameInputLaporan
###########################################################################

class FrameInputLaporan ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Input Data Laporan", pos = wx.DefaultPosition, size = wx.Size( 379,185 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer21 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"No Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		fgSizer21.Add( self.m_staticText41, 0, wx.ALL, 5 )

		self.input_no = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.input_no, 0, wx.ALL, 5 )

		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"Nama Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		fgSizer21.Add( self.m_staticText29, 0, wx.ALL, 5 )

		self.input_nama = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.input_nama, 0, wx.ALL, 5 )

		self.m_staticText42 = wx.StaticText( self, wx.ID_ANY, u"User Karyawan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )

		fgSizer21.Add( self.m_staticText42, 0, wx.ALL, 5 )

		self.input_user = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.input_user, 0, wx.ALL, 5 )

		self.m_button29 = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.m_button29, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer21 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button29.Bind( wx.EVT_BUTTON, self.btn_simpan )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_simpan( self, event ):
		event.Skip()


###########################################################################
## Class FrameLaporMgr
###########################################################################

class FrameLaporMgr ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 410,301 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		sbSizer42 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Menu Laporan" ), wx.VERTICAL )

		fgSizer55 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer55.SetFlexibleDirection( wx.BOTH )
		fgSizer55.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer45 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText212 = wx.StaticText( sbSizer42.GetStaticBox(), wx.ID_ANY, u"Data Laporan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText212.Wrap( -1 )

		self.m_staticText212.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer45.Add( self.m_staticText212, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		fgSizer55.Add( bSizer45, 1, wx.EXPAND, 5 )

		fgSizer81 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer81.SetFlexibleDirection( wx.BOTH )
		fgSizer81.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer55.Add( fgSizer81, 1, wx.EXPAND, 5 )

		self.tabel_lapor = wx.grid.Grid( sbSizer42.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tabel_lapor.CreateGrid( 5, 3 )
		self.tabel_lapor.EnableEditing( True )
		self.tabel_lapor.EnableGridLines( True )
		self.tabel_lapor.EnableDragGridSize( False )
		self.tabel_lapor.SetMargins( 0, 0 )

		# Columns
		self.tabel_lapor.EnableDragColMove( False )
		self.tabel_lapor.EnableDragColSize( True )
		self.tabel_lapor.SetColLabelSize( 30 )
		self.tabel_lapor.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabel_lapor.EnableDragRowSize( True )
		self.tabel_lapor.SetRowLabelSize( 80 )
		self.tabel_lapor.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabel_lapor.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer55.Add( self.tabel_lapor, 0, wx.ALL, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_button212 = wx.Button( sbSizer42.GetStaticBox(), wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button212, 0, wx.ALL, 5 )


		fgSizer55.Add( bSizer3, 1, wx.EXPAND, 5 )


		sbSizer42.Add( fgSizer55, 1, wx.EXPAND, 5 )


		sbSizer42.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		fgSizer9 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button37 = wx.Button( sbSizer42.GetStaticBox(), wx.ID_ANY, u"<< Back ", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_button37, 0, wx.ALL, 5 )

		self.m_button29 = wx.Button( sbSizer42.GetStaticBox(), wx.ID_ANY, u"Selesai >>", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_button29, 0, wx.ALL, 5 )


		sbSizer42.Add( fgSizer9, 1, wx.EXPAND, 5 )


		self.SetSizer( sbSizer42 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.tabel_lapor.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.tabel_barangOnGridCmdSelectCell )
		self.m_button212.Bind( wx.EVT_BUTTON, self.btn_tambah )
		self.m_button37.Bind( wx.EVT_BUTTON, self.btn_back )
		self.m_button29.Bind( wx.EVT_BUTTON, self.btn_end )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def tabel_barangOnGridCmdSelectCell( self, event ):
		event.Skip()

	def btn_tambah( self, event ):
		event.Skip()

	def btn_back( self, event ):
		event.Skip()

	def btn_end( self, event ):
		event.Skip()


###########################################################################
## Class FrameLaporan
###########################################################################

class FrameLaporan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 349,295 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Menu Laporan" ), wx.VERTICAL )

		fgSizer20 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer20.SetFlexibleDirection( wx.BOTH )
		fgSizer20.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText32 = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Data Laporan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer14.Add( self.m_staticText32, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		fgSizer20.Add( bSizer14, 1, wx.EXPAND, 5 )

		fgSizer21 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer20.Add( fgSizer21, 1, wx.EXPAND, 5 )

		self.tabel_lapor = wx.grid.Grid( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tabel_lapor.CreateGrid( 5, 3 )
		self.tabel_lapor.EnableEditing( True )
		self.tabel_lapor.EnableGridLines( True )
		self.tabel_lapor.EnableDragGridSize( False )
		self.tabel_lapor.SetMargins( 0, 0 )

		# Columns
		self.tabel_lapor.EnableDragColMove( False )
		self.tabel_lapor.EnableDragColSize( True )
		self.tabel_lapor.SetColLabelSize( 30 )
		self.tabel_lapor.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabel_lapor.EnableDragRowSize( True )
		self.tabel_lapor.SetRowLabelSize( 80 )
		self.tabel_lapor.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabel_lapor.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer20.Add( self.tabel_lapor, 0, wx.ALL, 5 )


		sbSizer8.Add( fgSizer20, 1, wx.EXPAND, 5 )


		sbSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		fgSizer24 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer24.SetFlexibleDirection( wx.BOTH )
		fgSizer24.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button23 = wx.Button( sbSizer8.GetStaticBox(), wx.ID_ANY, u"<< Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer24.Add( self.m_button23, 0, wx.ALL, 5 )

		self.m_button30 = wx.Button( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Selesai >>", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer24.Add( self.m_button30, 0, wx.ALL, 5 )


		sbSizer8.Add( fgSizer24, 1, wx.EXPAND, 5 )


		self.SetSizer( sbSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button23.Bind( wx.EVT_BUTTON, self.btn_back )
		self.m_button30.Bind( wx.EVT_BUTTON, self.btn_end )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_back( self, event ):
		event.Skip()

	def btn_end( self, event ):
		event.Skip()


###########################################################################
## Class FrameMenuMgr
###########################################################################

class FrameMenuMgr ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		sbSizer31 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Daftar Menu Pilihan :" ), wx.VERTICAL )

		self.m_staticText31 = wx.StaticText( sbSizer31.GetStaticBox(), wx.ID_ANY, u"Menu Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		sbSizer31.Add( self.m_staticText31, 0, wx.ALL, 5 )

		self.m_toggleBtn31 = wx.ToggleButton( sbSizer31.GetStaticBox(), wx.ID_ANY, u"Barang >>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_toggleBtn31.SetBackgroundColour( wx.Colour( 0, 255, 128 ) )

		sbSizer31.Add( self.m_toggleBtn31, 0, wx.ALL, 5 )

		self.m_staticText32 = wx.StaticText( sbSizer31.GetStaticBox(), wx.ID_ANY, u"Menu Karyawan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		sbSizer31.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.m_toggleBtn32 = wx.ToggleButton( sbSizer31.GetStaticBox(), wx.ID_ANY, u"Karyawan >>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_toggleBtn32.SetValue( True )
		self.m_toggleBtn32.SetBackgroundColour( wx.Colour( 0, 255, 128 ) )

		sbSizer31.Add( self.m_toggleBtn32, 0, wx.ALL, 5 )


		sbSizer31.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button31 = wx.Button( sbSizer31.GetStaticBox(), wx.ID_ANY, u"<< Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button31.SetBackgroundColour( wx.Colour( 255, 255, 0 ) )

		sbSizer31.Add( self.m_button31, 0, wx.ALL, 5 )


		self.SetSizer( sbSizer31 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_toggleBtn31.Bind( wx.EVT_TOGGLEBUTTON, self.btn_barang )
		self.m_toggleBtn32.Bind( wx.EVT_TOGGLEBUTTON, self.btn_karyawan )
		self.m_button31.Bind( wx.EVT_BUTTON, self.btn_back )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_barang( self, event ):
		event.Skip()

	def btn_karyawan( self, event ):
		event.Skip()

	def btn_back( self, event ):
		event.Skip()


###########################################################################
## Class EndFrame
###########################################################################

class EndFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 450,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Terima Kasih", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 24, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Andalus" ) )

		bSizer11.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Sudah Mampir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 34, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Andalus" ) )

		bSizer11.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button11 = wx.Button( self, wx.ID_ANY, u"Login Lagi?", wx.DefaultPosition, wx.Size( 140,30 ), 0 )
		self.m_button11.SetFont( wx.Font( 16, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Andalus" ) )

		bSizer11.Add( self.m_button11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button111 = wx.Button( self, wx.ID_ANY, u"Selesai", wx.DefaultPosition, wx.Size( 100,25 ), 0 )
		self.m_button111.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Andalus" ) )

		bSizer11.Add( self.m_button111, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer11 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button11.Bind( wx.EVT_BUTTON, self.btn_login )
		self.m_button111.Bind( wx.EVT_BUTTON, self.btn_end )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_login( self, event ):
		event.Skip()

	def btn_end( self, event ):
		event.Skip()


