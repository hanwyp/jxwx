import sys

import dal
from dl_br import *
from PyQt5.Qt import *
from tableModel import *


class DL_br(QDialog, Ui_dlg_br):

    data_list=[]


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.br_listview()
        self.btnAdd.clicked.connect(self.br_add)
        self.list_Br.clicked.connect(self.list_clicked)
        self.btnDel.clicked.connect(self.br_del)

    my_Signal=QtCore.pyqtSignal(str)

    def sendEditContent(self):
        content='1'
        self.my_Signal.emit(content)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.sendEditContent()

    # 刷新列表框
    def ref_listview(self, listName, listDate):
        slm = slm = QStringListModel()
        slm.setStringList(listDate)
        listName.setModel(slm)

    # 填充列表框
    def br_listview(self):
        global data_list
        data_dic, data_list = dal.date_all(Br, 'brID', 'brName')
        self.ref_listview(self.list_Br, data_list)

    # 添加事件
    def br_add(self):
        br = Br()
        br.brName = self.txt_br.text()
        print(br.brName)
        Sess = sessionmaker(bind=engine)
        ss = Sess()
        # print("------"+str(dal.checks(Br, "亿")))
        if dal.checks(Br,self.txt_br.text())==0 and len(self.txt_br.text())!=0:
            ss.add(br)
            ss.commit()
            self.br_listview()
            self.txt_br.setText('')
        else:
            QMessageBox.critical(self, "请检查", "品牌没有输入或已经存在", QMessageBox.Yes)

    # 品牌列表左键单击
    def list_clicked(self, index):

        self.txt_br.setText(self.list_Br.selectionModel().selectedIndexes()[0].data())
        # str_select_del=self.list_Br[index.row()]
        # print(str_select_del)
        # print(self.list_Br[index.row()])

    def br_del(self):
        if self.list_Br.currentIndex().row() == -1:
            QMessageBox.critical(self, "请检查", "请选择品牌", QMessageBox.Yes)
        else:
            br=Br()
            Sess = sessionmaker(bind=engine)
            ss = Sess()
            str=self.list_Br.selectionModel().selectedIndexes()[0].data()
            # print(str)
            filterStr='Br.brName=="{}"'.format(self.txt_br.text())
            print(filterStr)
            result=ss.query(Br).filter(eval(filterStr)).first()
            print(result)
            ss.delete(result)
            ss.commit()
            self.txt_br.setText('')
            self.br_listview()


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)

    win = DL_br()
    win.show()

    sys.exit(app.exec_())
