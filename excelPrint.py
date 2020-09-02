
import win32com.client
import time
import sys


class ExPr():

    def ex2Pr(self,filename):
        path=sys.path[0] #获取当前目录
        strpath = path+"\\"+filename # 获取所需文件全路径
        excel = win32com.client.Dispatch('Excel.Application')
        excel.Visible = 0 # 1.可见  0. 不可见
        myBook = excel.Workbooks.Open(strpath)
        mySheet = myBook.Worksheets('Sheet1')
        time.sleep(2)
        # mySheet.PrintPreview(True) # 打印预览，必须在可见状态下
        mySheet.PrintOut() # 直接用系统默认打印机打印


if __name__ == '__main__':
    expr = ExPr()
    expr.ex2Pr('a.xlsx')