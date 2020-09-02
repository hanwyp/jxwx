import sys
import dal

from PyQt5.Qt import *
from tableModel import *
from frm_main import *
from br_main import *

# 全局变量
data_list = []
data_dic = {}
phone_list = []
phone_dic = {}
phone_edit = PhEdit()
gu_ke = Guke()


class MyWin(QMainWindow, Ui_MainWindow):
    # 窗口初始化
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.Cal.setVisible(False)
        self.br_listview()
        self.list_guzhang_view()
        self.lbl_danhao.setText(test.dan_hao())

        # 信号绑定
        self.list_br.clicked.connect(self.list_br_clicked)
        self.list_phone.clicked.connect(self.list_phone_clicked)
        self.btnAdd.clicked.connect(self.select_guzhang_clicked)
        self.btn_print.clicked.connect(self.prSave)
        self.btnDate.clicked.connect(self.E_clicked)
        self.Cal.clicked.connect(self.Cal_select)
        self.rd_gkSex1.toggled.connect(self.sex_select)
        self.rd_gkSex0.toggled.connect(self.sex_select)
        self.menu.triggered[QAction].connect(self.br_add)
    # 菜单点击
    def br_add(self,QAction):
        # print(QAction.text())
        if QAction.text()=='品牌维护':
            self.frm_br=DL_br()
            self.frm_br.my_Signal.connect(self.br_listview)
            self.frm_br.show()



        if QAction.text()=='机型维护':
            print('点击机型维护')
        if QAction.text()=='故障现象维护':
            print('点击故障现象维护')

    # 列表框填充数据
    def ref_listview(self, listName, listDate):
        slm = slm = QStringListModel()
        slm.setStringList(listDate)
        listName.setModel(slm)

    # 填充品牌列表
    def br_listview(self):
        global data_dic
        global data_list
        data_dic, data_list = dal.date_all(Br, 'brID', 'brName')
        self.ref_listview(self.list_br, data_list)

    # 填充故障选择列表
    def list_guzhang_view(self):
        global str_guzhang
        str_guzhang = ""
        # temp_list=[]
        #
        # for i in temp_list:
        #     box = QCheckBox(i)
        #     item = QListWidgetItem()
        #     self.list_guzhang.addItem(item)
        #     self.list_guzhang.setItemWidget(item, box)

        _, temp_list = dal.date_all(EditPs, 'id', 'Name')
        for i in temp_list:
            box = QCheckBox(i)
            item = QListWidgetItem()
            self.list_guzhang.addItem(item)
            self.list_guzhang.setItemWidget(item, box)

    # 品牌列表左键单击
    def list_br_clicked(self, index):

        global data_dic
        global data_list
        global phone_dic
        global phone_list
        global phone_edit

        phone_edit.phID = None

        temp_dic = {}
        for k, v in data_dic.items():
            temp_dic[v] = k

        str_br = data_list[index.row()]
        str_id = str(temp_dic[str_br])
        str_filter = "Phone.brID==" + str_id

        phone_dic, phone_list = dal.date_select(Phone, 'id', 'phName', str_filter)
        self.ref_listview(self.list_phone, phone_list)

    # 手机列表左键单击
    def list_phone_clicked(self, index):
        global phone_dic
        global phone_list
        global phone_edit

        temp_dic = {}
        for k, v in phone_dic.items():
            temp_dic[v] = k
        str_ph = phone_list[index.row()]
        # str_id=temp_dic[str_ph]
        phone_edit.phID = temp_dic[str_ph]

    # 选择故障后按钮事件
    def select_guzhang_clicked(self):
        """
        得到备选统计项的字段
        :return: list[str]
        """
        global phone_edit

        count = self.list_guzhang.count()  # 得到QListWidget的总个数
        cb_list = [self.list_guzhang.itemWidget(self.list_guzhang.item(i))
                   for i in range(count)]  # 得到QListWidget里面所有QListWidgetItem中的QCheckBox
        chooses = []  # 存放被选择的数据
        for cb in cb_list:
            if cb.isChecked():
                chooses.append(cb.text())
        choose = "，".join(chooses)
        str_t = self.txtGz.toPlainText()
        self.txtGz.setText(str_t + choose)
        # phone_edit.guzhang = choose

    # 显示日期选择窗口
    def E_clicked(self):
        self.Cal.setVisible(True)

    # 日期窗口点击
    def Cal_select(self):
        self.txt_date.setText(self.Cal.selectedDate().toString("yyyy-MM-dd"))
        self.Cal.setVisible(False)

    # 顾客性别选择
    def sex_select(self):

        if self.rd_gkSex0.isChecked() == True:
            gu_ke.sex = '女士'
        if self.rd_gkSex1.isChecked() == True:
            gu_ke.sex = '先生'
        return gu_ke.sex

    # 控件初始化
    def view_init(self):
        self.br_listview()
        self.list_guzhang.clear()
        self.list_guzhang_view()
        self.ref_listview(self.list_phone, [])
        self.txtGz.setText("")
        self.textEdit.setText("")
        self.txt_gkName.setText("")
        self.txt_date.setText("")
        self.txt_cost.setText("")
        self.txt_gkphone.setText("")
        self.lbl_danhao.setText(test.dan_hao())

    # 检查所有控件的值
    def check_up(self):
        if self.list_br.currentIndex().row() == -1:
            QMessageBox.critical(self, "请检查", "请选择品牌", QMessageBox.Yes)
            return False
        if self.list_phone.currentIndex().row() == -1:
            QMessageBox.critical(self, "请检查", "请选择机型", QMessageBox.Yes)
            return False
        if len(self.txtGz.toPlainText()) == 0:
            QMessageBox.critical(self, "请检查", "请生成故障现象", QMessageBox.Yes)
            return False
        if len(self.textEdit.toPlainText()) == 0:
            QMessageBox.critical(self, "请检查", "维修项目未录入", QMessageBox.Yes)
            return False
        if len(self.txt_cost.text()) == 0:
            QMessageBox.critical(self, "请检查", "请输入收费", QMessageBox.Yes)
            return False
        if len(self.txt_date.text()) == 0:
            QMessageBox.critical(self, "请检查", "请输入日期", QMessageBox.Yes)
            return False
        if len(self.txt_gkName.text()) == 0:
            QMessageBox.critical(self, "请检查", "请输入顾客姓名", QMessageBox.Yes)
            return False
        if len(self.txt_gkphone.text()) == 0:
            QMessageBox.critical(self, "请检查", "请输入顾客电话", QMessageBox.Yes)
            return False
        if self.rd_gkSex1.isChecked() or self.rd_gkSex0.isChecked():
            return True
        else:
            QMessageBox.critical(self, "请检查", "请选择顾客性别", QMessageBox.Yes)
            return False

        # print(self.rd_gkSex0.isChecked())
        return True

    # 打印按钮单击
    def prSave(self):
        global phone_edit
        global gu_ke

        if self.check_up():
            gu_ke.Name = self.txt_gkName.text()
            gu_ke.dianhua = self.txt_gkphone.text()
            phone_edit.phedit = self.textEdit.toPlainText()
            phone_edit.jiage = self.txt_cost.text()
            phone_edit.rq = self.txt_date.text()
            phone_edit.id = self.lbl_danhao.text()
            phone_edit.guzhang = self.txtGz.toPlainText()
            gu_ke.sex = self.sex_select()
            # Sess = sessionmaker(bind=engine)
            # ss = Sess()
            # ss.add(phone_edit)
            # ss.add(gu_ke)
            # ss.commit()

            print(phone_edit.id,
                  phone_edit.phID,
                  phone_edit.guzhang,
                  phone_edit.phedit,
                  phone_edit.jiage,
                  phone_edit.rq,
                  gu_ke.Name,
                  gu_ke.sex,
                  gu_ke.dianhua
                  )

            phone_edit = PhEdit()
            gu_ke = Guke()
            self.view_init()


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    win = MyWin()
    win.show()
    sys.exit(app.exec_())
