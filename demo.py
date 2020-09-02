import sys
from PyQt5.Qt import *
from ORM应用 import *

from frm_main import *
from br_main import *

class menu_ex(QMainWindow,Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Cal.setVisible(False)
        self.lbl_danhao.setText(test.dan_hao())
        self.menu.triggered[QAction].connect(self.br_add)


    def br_add(self,QAction):
        # print(QAction.text())
        if QAction.text()=='品牌维护':
            self.frm_br=DL_br()

            self.frm_br.show()


        if QAction.text()=='机型维护':
            print('点击机型维护')
        if QAction.text()=='故障现象维护':
            print('点击故障现象维护')


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app=QApplication(sys.argv)
    win=menu_ex()

    # win.menu.triggered[QAction].connect(win.br_add)
    win.show()
    sys.exit(app.exec_())