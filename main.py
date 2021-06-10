import wx
import noname as gui
import Data

class FrameWelcome(gui.WelcomeFrame):
    def __init__(self,parent):
        gui.WelcomeFrame.__init__(self,parent)
    def btn_login( self, event ):
        FrameLogin.Show()
        FrameWelcome.Hide()

class Login(gui.FrameLogin):
    def __init__(self,parent):
        gui.FrameLogin.__init__(self,parent)

    def btn_login( self, event ):
        self.manager = Data.Manager()
        self.karyawan = Data.Karyawan()
        mgrlist = self.manager.getDataManager()
        krylist = self.karyawan.getDataKaryawan()
        username = self.input_username.GetValue()
        password = self.input_pw.GetValue()
        Uname = []
        Pass = []
        Nama = []
        Jabatan = []

        for x in mgrlist:
            Uname.append(x[1])
            Pass.append(x[2])
            Nama.append(x[3])
            Jabatan.append(x[4])

        for y in krylist:
            Uname.append(y[1])
            Pass.append(y[2])
            Nama.append(y[3])
            Jabatan.append(y[4])

        for i in range(len(Uname)):
            if username == Uname[i] and password == Pass[i]:
                if Jabatan[i] == "Manager":
                    FrameMgr.Show()
                    FrameLogin.Hide()
                elif Jabatan[i] != "Manager" :
                    FrameKry.Show()
                    FrameLogin.Hide()


class FrameKaryawan(gui.FrameKaryawanMgr):
    def __init__(self,parent):
        gui.FrameKaryawanMgr.__init__(self,parent)
        self.showDataKaryawan()
        self.AddBtnKaryawan()

    def showDataKaryawan(self):
        n_cols = self.tabel_karyawan.GetNumberCols()
        n_rows = self.tabel_karyawan.GetNumberRows()
        if n_cols > 0:
            self.tabel_karyawan.DeleteCols(0, n_cols, True)
        if n_rows > 0:
            self.tabel_karyawan.DeleteRows(0, n_rows, True)

        kolom = ['Username', 'Password', 'Nama', 'Gender', 'Tanggal Lahir', 'Alamat', 'No Telepon']
        self.tabel_karyawan.AppendCols(len(kolom))

        self.kry = Data.Karyawan()
        listKry = self.kry.getDataKaryawan()
        row = 0

        self.listIdKry = []
        for col in range(len(kolom)):
            self.tabel_karyawan.SetColLabelValue(col, kolom[col]) 
        for row_kry in listKry:
            self.tabel_karyawan.AppendRows(1)
            id, username, password, nama_karyawan, jenis_kelamin, tanggal_lahir, alamat, no_telepon = row_kry
            self.tabel_karyawan.SetCellValue(row, 0, username)
            self.tabel_karyawan.SetCellValue(row, 1, password)
            self.tabel_karyawan.SetCellValue(row, 2, nama_karyawan)
            self.tabel_karyawan.SetCellValue(row, 3, jenis_kelamin)
            self.tabel_karyawan.SetCellValue(row, 4, tanggal_lahir)
            self.tabel_karyawan.SetCellValue(row, 5, alamat)
            self.tabel_karyawan.SetCellValue(row, 6, no_telepon)
            self.listIdKry.append(id)
            row += 1

    def btn_back( self, event ):
        FrameMgr.Show()
        FrameKaryawan.Hide()

    def btn_tambah( self, event ):
        dlg = dlgAddKaryawan(self)
        dlg.ShowModal()

    def insertDataKry(self, username, password, nama_karyawan, jenis_kelamin, tanggal_lahir, alamat, no_telepon):
        self.kry.addDataKaryawan(username, password, nama_karyawan, jenis_kelamin, tanggal_lahir, alamat, no_telepon)
        self.showDataKaryawan()
        self.AddBtnKaryawan()
    
    def updateDataKry(self, id, username, password, nama_karyawan, jenis_kelamin, tanggal_lahir, alamat, no_telepon):
        self.kry.updateDataKaryawan(id, username, password, nama_karyawan, jenis_kelamin, tanggal_lahir, alamat, no_telepon)
        self.showDataKaryawan()
        self.AddBtnKaryawan()

    def AddBtnKaryawan (self):
        jmlKolom = self.tabel_karyawan.GetNumberCols()
        self.tabel_karyawan.AppendCols(2)
        colEdit = jmlKolom
        colDelete = jmlKolom + 1

        self.tabel_karyawan.SetColLabelValue(colEdit, '')
        self.tabel_karyawan.SetColLabelValue(colDelete, '')

        for row in range(self.tabel_karyawan.GetNumberRows()):
            self.tabel_karyawan.SetCellValue(row, colEdit, 'Edit')
            self.tabel_karyawan.SetCellBackgroundColour(row, colEdit, wx.BLUE)
            self.tabel_karyawan.SetCellTextColour(row, colEdit, wx.WHITE)

            self.tabel_karyawan.SetCellValue(row, colDelete, 'Delete')
            self.tabel_karyawan.SetCellBackgroundColour(row, colDelete, wx.RED)
            self.tabel_karyawan.SetCellTextColour(row, colDelete, wx.WHITE)

        self.tabel_karyawan.Fit()

    def tabel_karyawanOnGridCmdSelectCell( self, event ):
        baris = event.GetRow()
        kolom = event.GetCol()
        if kolom == 7:
            id = self.listIdKry[baris]
            dlg = dlgAddKaryawan(self, id)
            un = self.tabel_karyawan.GetCellValue(baris, 0)
            pasw = self.tabel_karyawan.GetCellValue(baris, 1)
            nama = self.tabel_karyawan.GetCellValue(baris, 2)
            gender = self.tabel_karyawan.GetCellValue(baris, 3)
            ttl = self.tabel_karyawan.GetCellValue(baris, 4)
            alamat = self.tabel_karyawan.GetCellValue(baris, 5)
            telp = self.tabel_karyawan.GetCellValue(baris, 6)
            dlg.fillDataKaryawan(un, pasw, nama, gender, ttl, alamat, telp)
            dlg.ShowModal()
        elif kolom == 8:
            dlg = wx.MessageDialog(
                self, 'Hapus data', 'Informasi', style=wx.YES_NO)
            retval = dlg.ShowModal()
            if retval == wx.ID_YES:
                print('hapus')
                self.kry.deleteDataKaryawan(self.listIdKry[baris])
                self.showDataKaryawan()
                self.AddBtnKaryawan()

class dlgAddKaryawan(gui.FrameInputKry):
    def __init__(self, parent, id=-1):
        gui.FrameInputKry.__init__(self, parent)
        self.parent=parent
        self.id = id

    def btn_simpan( self, event ):
        dlg= wx.MessageDialog(self, 'simpan data', 'Informasi', style=wx.YES_NO)
        retval= dlg.ShowModal()

        if self.id == -1:
            self.parent.insertDataKry(self.input_user.GetValue(), self.input_pass.GetValue(),
            self.input_nama.GetValue(), self.input_gender.GetValue(), self.input_ttl.GetValue(),
            self.input_alamat.GetValue(), self.input_telp.GetValue())
        else:
            self.parent.updateDataKry(self.id, self.input_user.GetValue(), self.input_pass.GetValue(),
            self.input_nama.GetValue(), self.input_gender.GetValue(), self.input_ttl.GetValue(),
            self.input_alamat.GetValue(), self.input_telp.GetValue())
        self.Destroy()

    def fillDataKaryawan (self, username, password, nama_karyawan, jenis_kelamin, tanggal_lahir, alamat, no_telepon):
        self.input_user.SetValue(username)
        self.input_pass.SetValue(password)
        self.input_nama.SetValue(nama_karyawan)
        self.input_gender.SetValue(jenis_kelamin)
        self.input_ttl.SetValue(tanggal_lahir)
        self.input_alamat.SetValue(alamat)
        self.input_telp.SetValue(no_telepon)


class FrameBarang1 (gui.FrameBarangMgr):
    def __init__(self,parent):
        gui.FrameBarangMgr.__init__(self,parent)
        self.showDataBarang()
        self.AddBtnBarang()

    def showDataBarang(self):
        n_cols = self.tabel_barang.GetNumberCols()
        n_rows = self.tabel_barang.GetNumberRows()
        if n_cols > 0:
            self.tabel_barang.DeleteCols(0, n_cols, True)
        if n_rows > 0:
            self.tabel_barang.DeleteRows(0, n_rows, True)

        kolom = ['No Barang', 'Nama Barang', 'Jenis Barang', 'Harga Barang', 'Stok Barang']
        self.tabel_barang.AppendCols(len(kolom))

        self.barang = Data.Barang()
        listBarang = self.barang.getDataBarang()
        row = 0

        self.listIdBarang = []
        for col in range(len(kolom)):
            self.tabel_barang.SetColLabelValue(col, kolom[col]) 
        for row_barang in listBarang:
            self.tabel_barang.AppendRows(1)
            id, no_barang, nama_barang, jenis_barang, harga_barang, stok_barang = row_barang
            no_item=str(no_barang)
            hrg=str(harga_barang)
            stok=str(stok_barang)
            self.tabel_barang.SetCellValue(row, 0, no_item)
            self.tabel_barang.SetCellValue(row, 1, nama_barang)
            self.tabel_barang.SetCellValue(row, 2, jenis_barang)
            self.tabel_barang.SetCellValue(row, 3, hrg)
            self.tabel_barang.SetCellValue(row, 4, stok)
            self.listIdBarang.append(id)
            row += 1

    def btn_back( self, event ):
        FrameMgr.Show()
        FrameBarang1.Hide()

    def btn_tambah( self, event ):
        dlg = dlgAddBarang(self)
        dlg.ShowModal()

    def btn_cek( self, event ):
        FrameLapor.Show()
        FrameBarang1.Hide()

    def insertDataBrg(self, no_barang, nama_barang, jenis_barang, harga_barang, stok_barang):
        self.barang.addDataBarang(no_barang, nama_barang, jenis_barang, harga_barang, stok_barang)
        self.showDataBarang()
        self.AddBtnBarang()
    
    def updateDataBrg(self, id, no_barang, nama_barang, jenis_barang, harga_barang, stok_barang):
        self.barang.updateDataBarang(id, no_barang, nama_barang, jenis_barang, harga_barang, stok_barang)
        self.showDataBarang()
        self.AddBtnBarang()

    def AddBtnBarang (self):
        jmlKolom = self.tabel_barang.GetNumberCols()
        self.tabel_barang.AppendCols(2)
        colEdit = jmlKolom
        colDelete = jmlKolom + 1

        self.tabel_barang.SetColLabelValue(colEdit, '')
        self.tabel_barang.SetColLabelValue(colDelete, '')

        for row in range(self.tabel_barang.GetNumberRows()):
            self.tabel_barang.SetCellValue(row, colEdit, 'Edit')
            self.tabel_barang.SetCellBackgroundColour(row, colEdit, wx.BLUE)
            self.tabel_barang.SetCellTextColour(row, colEdit, wx.WHITE)

            self.tabel_barang.SetCellValue(row, colDelete, 'Delete')
            self.tabel_barang.SetCellBackgroundColour(row, colDelete, wx.RED)
            self.tabel_barang.SetCellTextColour(row, colDelete, wx.WHITE)

        self.tabel_barang.Fit()

    def tabel_barangOnGridCmdSelectCell( self, event ):
        baris = event.GetRow()
        kolom = event.GetCol()
        if kolom == 5:
            id = self.listIdBarang[baris]
            dlg = dlgAddBarang(self, id)
            no = self.tabel_barang.GetCellValue(baris, 0)
            nama = self.tabel_barang.GetCellValue(baris, 1)
            jenis = self.tabel_barang.GetCellValue(baris, 2)
            harga = self.tabel_barang.GetCellValue(baris, 3)
            stk = self.tabel_barang.GetCellValue(baris, 4)
            dlg.fillDataBarang(no, nama, jenis, harga, stk)
            dlg.ShowModal()
        elif kolom == 6:
            dlg = wx.MessageDialog(
                self, 'Hapus data', 'Informasi', style=wx.YES_NO)
            retval = dlg.ShowModal()
            if retval == wx.ID_YES:
                print('hapus')
                self.barang.deleteDataBarang(self.listIdBarang[baris])
                self.showDataBarang()
                self.AddBtnKaryawan()

class dlgAddBarang(gui.FrameInputBrg):
    def __init__(self, parent, id=-1):
        gui.FrameInputBrg.__init__(self, parent)
        self.parent=parent
        self.id = id

    def btn_simpan( self, event ):
        dlg= wx.MessageDialog(self, 'simpan data', 'Informasi', style=wx.YES_NO)
        retval= dlg.ShowModal()

        if self.id == -1:
            self.parent.insertDataBrg(self.input_no.GetValue(), self.input_nama.GetValue(
            ), self.input_jenis.GetValue(), self.input_harga.GetValue(), self.input_stok.GetValue())
        else:
            self.parent.updateDataBrg(self.id, self.input_no.GetValue(), self.input_nama.GetValue(
            ), self.input_jenis.GetValue(), self.input_harga.GetValue(), self.input_stok.GetValue())
        self.Destroy()

    def fillDataBarang(self, no_barang, nama_barang, jenis_barang, harga_barang, stok_barang):
        self.input_no.SetValue(no_barang)
        self.input_nama.SetValue(nama_barang)
        self.input_jenis.SetValue(jenis_barang)
        self.input_harga.SetValue(harga_barang)
        self.input_stok.SetValue(stok_barang)


class FrameBarang2 (gui.FrameBarang):
    def __init__(self,parent):
        gui.FrameBarang.__init__(self,parent)
        self.showDataBarang()

    def btn_lapor( self, event ):
        frame1 = FrameLapor(self)
        frame2 = FrameBarang2(self)
        frame2.Destroy()
        frame1.Show()

    def showDataBarang(self):
        n_cols = self.tabel_barang.GetNumberCols()
        n_rows = self.tabel_barang.GetNumberRows()
        if n_cols > 0:
            self.tabel_barang.DeleteCols(0, n_cols, True)
        if n_rows > 0:
            self.tabel_barang.DeleteRows(0, n_rows, True)

        kolom = ['No Barang', 'Nama Barang', 'Jenis Barang', 'Harga Barang', 'Stok Barang']
        self.tabel_barang.AppendCols(len(kolom))

        self.barang = Data.Barang()
        listBarang = self.barang.getDataBarang()
        row = 0

        self.listIdBarang = []
        for col in range(len(kolom)):
            self.tabel_barang.SetColLabelValue(col, kolom[col]) 
        for row_barang in listBarang:
            self.tabel_barang.AppendRows(1)
            id, no_barang, nama_barang, jenis_barang, harga_barang, stok_barang = row_barang
            no_item=str(no_barang)
            hrg=str(harga_barang)
            stok=str(stok_barang)
            self.tabel_barang.SetCellValue(row, 0, no_item)
            self.tabel_barang.SetCellValue(row, 1, nama_barang)
            self.tabel_barang.SetCellValue(row, 2, jenis_barang)
            self.tabel_barang.SetCellValue(row, 3, hrg)
            self.tabel_barang.SetCellValue(row, 4, stok)
            self.listIdBarang.append(id)
            row += 1

class FrameLapor(gui.FrameLaporMgr):
    def __init__(self, parent):
        gui.FrameLaporMgr.__init__(self, parent)
        self.showDataLapor()
    
    def btn_tambah(self,event):
        dlg= dlgAddLapor(self)
        dlg.ShowModal() 
        
    def btn_back( self, event ):
        FrameBarang1.Show()
        FrameLapor.Hide()
    
    def showDataLapor(self):
        n_cols = self.tabel_lapor.GetNumberCols()
        n_rows = self.tabel_lapor.GetNumberRows()
        if n_cols > 0:
            self.tabel_lapor.DeleteCols(0, n_cols, True)
        if n_rows > 0:
            self.tabel_lapor.DeleteRows(0, n_rows, True)

        kolom = ['No Barang', 'Nama Barang', 'Username']
        self.tabel_lapor.AppendCols(len(kolom))

        self.data_lapor = Data.Lapor()
        listLaporan = self.data_lapor.getDataLapor()
        row = 0

        self.listIdLpr = []
        for col in range(len(kolom)):
            self.tabel_lapor.SetColLabelValue(col, kolom[col]) 
        for row_laporan in listLaporan:
            self.tabel_lapor.AppendRows(1)
            id, no_barang, nama_barang, username = row_laporan
            no_item=str(no_barang)
            nama=str(nama_barang)
            user=str(username)
            self.tabel_lapor.SetCellValue(row, 0, no_item)
            self.tabel_lapor.SetCellValue(row, 1, nama)
            self.tabel_lapor.SetCellValue(row, 2, user)
            self.listIdLpr.append(id)
            row += 1
        
        self.tabel_lapor.Fit()

    def insertDataLapor(self, no_barang, nama_barang, username):
        self.data_lapor.addDataLapor(no_barang, nama_barang ,username)
        self.showDataLapor()

class dlgAddLapor(gui.FrameInputLaporan):
    def __init__(self, parent, id=-1):
        gui.FrameInputLaporan.__init__(self, parent)
        self.parent=parent
        self.id = id

    def btn_simpan( self, event ):
        dlg= wx.MessageDialog(self, 'simpan data', 'Informasi', style=wx.YES_NO)
        retval= dlg.ShowModal()

        if self.id == -1:
            self.parent.insertDataLapor(self.input_no.GetValue(), self.input_nama.GetValue(),
            self.input_user.GetValue())
        self.Destroy()

    def fillDataLapor(self, no_barang, nama_barang, username):
        self.input_no.SetValue(no_barang)
        self.input_nama.SetValue(nama_barang)
        self.input_user.SetValue(username)


class FrameMgr(gui.FrameMenuMgr):
    def __init__(self,parent):
        gui.FrameMenuMgr.__init__(self,parent)
    def btn_barang( self, event ):
        FrameBarang1.Show()
        FrameMgr.Hide()
    def btn_karyawan( self, event ):
        FrameKaryawan.Show()
        FrameMgr.Hide()
    def btn_back( self, event ):
        FrameLogin.Show()
        FrameMgr.Hide()

class FrameKry(gui.FrameMenuKry):
    def __init__(self,parent):
        gui.FrameMenuKry.__init__(self,parent)
    def btn_barang1(self, event):
        FrameBarang2.Show()
        FrameKry.Hide()
    def btn_profil( self, event ):
        FrameProfil.Show()
        FrameKry.Hide()
    def btn_back( self, event ):
        FrameLogin.Show()
        FrameKry.Hide()


class FrameInputKr(gui.FrameInputKry):
    def __init__(self,parent):
        gui.FrameInputKry.__init__(self,parent)


class FrameProfil(gui.FrameProfilKry):
    def __init__(self,parent):
        gui.FrameProfilKry.__init__(self,parent)
    def btn_back( self, event ):
        FrameKry.Show()
        FrameProfil.Hide()



app=wx.App()
FrameWelcome=FrameWelcome(None)
FrameLogin=Login(None)
FrameMgr=FrameMgr(None)
FrameKry=FrameKry(None)
FrameKaryawan=FrameKaryawan(None)
FrameBarang1=FrameBarang1(None)
FrameBarang2=FrameBarang2(None)
FrameProfil=FrameProfil(None)
FrameLapor=FrameLapor(None)

FrameWelcome.Show()
# FrameLogin.Show()
# FrameMgr.Show()
# FrameKry.Show()
# FrameKaryawan.Show()
# FrameBarang1.Show()
# FrameBarang2.Show()
# FrameInput.Show()
# FrameProfil.Show()
# FrameInputLp.Show()
# FrameInputKr.Show()
# FrameLapor.Show()

app.MainLoop()