import sys
from PyQt5.Qt import *
from frm_main import *
from test import *
from dl_br import *
from tableModel import *



class DlgBr(QDialog,Ui_dlg_br):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


    def listviewBr(self):
        br_name=Br()
        viewBr= br_name.br_list()
        self.listview(self.list_Br,viewBr)

    def listview(self, listName, listStr):
        slm = QStringListModel()
        slm.setStringList(listStr)
        listName.setModel(slm)

    def view_br(self):
        self.listviewBr()
        self.show()


class MyWindow(QMainWindow, Ui_MainWindow):
    cur_dic = {}
    cur_list = []

    temp_dic = {}
    temp_list = []

    phoneID=""
    str_guzhang=""
    str_Edit=""
    str_Date=""


    def __init__(self, parent=None):
        # super(MyWindow, self).__init__(parent)
        super().__init__()
        self.setupUi(self)
        self.list_guzhang_view()
        self.Cal.setVisible(False)
        self.lbl_danhao.setText(dan_hao())

        # 事件
        self.list_br.clicked.connect(self.list_br_clicked)
        self.list_phone.clicked.connect(self.list_phone_clicked)
        self.list_guzhang.itemClicked.connect(self.select_guzhang_clicked)
        self.btnAdd.clicked.connect(self.select_guzhang_clicked)
        self.btnDate.clicked.connect(self.E_clicked)
        self.Cal.clicked.connect(self.Cal_select)
        self.me_br.triggered.connect(self.br_add)
        self.btn_print.clicked.connect(self.phoneSave)

    def br_add(self):
        br_dlg=DlgBr()
        br_dlg.view_br()

        br_dlg.exec_()


    # 通过获得字典方式显示list中的值
    def brView_dic(self):
        sql = "select * from br"
        self.cur_dic, self.cur_list = selectList(sql, 1)
        # print(self.cur_dic)
        self.listview(self.list_br, self.cur_list)

    # list_br点击
    def list_br_clicked(self, index):
        str_brID = str(self.cur_dic[index.row()][0])
        sql = "select ID,phName from phone where brID=" + str_brID

        self.temp_dic, self.temp_list = selectList(sql, 1)

        self.listview(self.list_phone, self.temp_list)

    # list_phone点击
    def list_phone_clicked(self, index):
        str_phID = str(self.temp_dic[index.row()][0])
        # print(str_phID)
        global phoneID
        phoneID = str_phID

    # listview通过列表名称和字符列表更新显示
    def listview(self, listName, listStr):
        slm = QStringListModel()
        slm.setStringList(listStr)
        listName.setModel(slm)

    def list_guzhang_view(self):

        session=Session()
        user = session.query(EditPs)
        temp_list=[]
        for u in user:
            temp_list.append(u.Name)

        for i in temp_list:
            box = QCheckBox(i)
            item = QListWidgetItem()
            self.list_guzhang.addItem(item)
            self.list_guzhang.setItemWidget(item, box)

    def select_guzhang_clicked(self):
        """
        得到备选统计项的字段
        :return: list[str]
        """

        count = self.list_guzhang.count()  # 得到QListWidget的总个数
        cb_list = [self.list_guzhang.itemWidget(self.list_guzhang.item(i))
                   for i in range(count)]  # 得到QListWidget里面所有QListWidgetItem中的QCheckBox
        # print(cb_list)
        chooses = []  # 存放被选择的数据
        for cb in cb_list:
            if cb.isChecked():
                chooses.append(cb.text())
        choose = "，".join(chooses)
        # print(choose)
        self.txtGz.setText("")
        self.txtGz.setText(choose)
        global str_guzhang
        str_guzhang=choose

        # return choose

    def E_clicked(self):
        self.Cal.setVisible(True)

    def Cal_select(self):
        self.le_Date.setText(self.Cal.selectedDate().toString("yyyy-MM-dd"))
        self.Cal.setVisible(False)

    def CreatID(self):
        return dan_hao()

    def getEdit_str(self):

        if self.list_br.currentIndex().row() == -1:
            QMessageBox.critical(self,"请检查","请选择品牌",QMessageBox.Yes)
            return
        if self.list_phone.currentIndex().row() == -1:
            QMessageBox.critical(self, "请检查", "请选择机型", QMessageBox.Yes)
            return
        if len(self.txtGz.toPlainText())==0:
            QMessageBox.critical(self, "请检查", "请生成故障现象", QMessageBox.Yes)
            return
        if len(self.textEdit.toPlainText())==0:
            QMessageBox.critical(self, "请检查", "维修项目未录入", QMessageBox.Yes)
            return

    def phoneSave(self):
        global phoneID
        global str_guzhang
        self.getEdit_str()
        # print(phoneID,str_guzhang,self.getEdit_str())

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    win = MyWindow()
    win.brView_dic()
    win.CreatID()
    win.show()
    sys.exit(app.exec_())
