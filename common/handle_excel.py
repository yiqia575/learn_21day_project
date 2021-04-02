# -*- encoding: utf-8 -*-
"""
================================
@File    : demo05_read_excel封装1.py
@Time    : 2021/3/22 14:26
@Author  : 测试工程师：刘坤
@Email   : 609127365@qq.com
@Software: PyCharm
================================
"""
import openpyxl
class Excel:
    def __init__(self,filename,sheet_name):
        self.filename = filename
        self.sheet_name = sheet_name
    def open(self):
        # 第一步：将excel文件加载到一个工作簿对象中
        self.wb = openpyxl.load_workbook(self.filename)
        # 第二步：选择文件中的表单
        self.sh = self.wb[self.sheet_name]

    def read_data(self):
        self.open()
        res = list(self.sh.rows)
        title = [c.value for c in res[0]]     #获取第一行的单元格的数据
        case_data = []
        for row in res[1:]:
            data = [c.value for c in row]     #获取遍历出来这一行的数据
            # data = []
            # for c in row:
            #     data.append(c.value)
            case = dict(zip(title, data))
            case_data.append(case)
        return case_data
    def write_data(self,row,column,value):
        """ 写数据"""

        self.open()

        # 第三步：往表格中写入数据
        self.sh.cell(row=row, column=column, value=value)
        # 第四步：保存
        self.wb.save(self.filename)
if __name__ == '__main__':
    pass