#/usr/bin/env python
# coding: utf-8
#######################################################################
#
# Performance Excel chart with Python and XlsxWriter.
#
# by lp 2016.6.24
#
import xlsxwriter
import sys
reload(sys)
sys.setdefaultencoding('utf8')
workbook = xlsxwriter.Workbook('chart.xlsx')
worksheet = workbook.add_worksheet()
#　格式一“加粗、紫色填充、字体大小为10、宋体”
format1 = workbook.add_format({'bold':True}) #设置加粗
format1.set_pattern(1)
format1.set_bg_color('#8552a1')  #设置单元格填充颜色
format1.set_font_size(10)   #设置字体大小
format1.set_font_color('#FFFF99') #设置字体颜色
format1.set_align('left') #设置对齐方式
format1.set_align('vcenter') #设置对齐方式
format1.set_border(1)  #设置边框格式
#format1.set_shrink() #缩小字体适应单元格
#worksheet.set_row(0, 45) #设置单元格长度
worksheet.set_column(0, 0, 30) #设置单元格宽度
# Create a new Chart object.
chart = workbook.add_chart({'type': 'column'})

#设置单元格大小
#setrow_format = workbook.add_format({'bold': True})
#worksheet.set_row(1, 45, setrow_format)

#title 格式， 合并单元格
title_format = workbook.add_format({
    'bold':     True,
    'border':   1,
    'font_size': 14,
    'font_color': '#FFFF99',
    'align':    'center',
    'valign':   'vcenter',
    'fg_color': '#333399',
})
#测试信息格式
info_format = workbook.add_format({
    'bold': False,
    'border': 1,
    'font_size': 10,
    'align': 'left',
    'valign': 'vcenter',
    'fg_color': '#B8CCE4',
})
#worksheet.merge_range('B3:D4', 'Merged Cells', merge_format)
ltitle_format = workbook.add_format({
    'bold': True,
    'border': 1,
    'font_size': 12,
    'align': 'left',
    'valign': 'vcenter',
    'fg_color': '#339966',
})
# Write some data to add to plot on the chart.
data = [
    ["OS", "isoft_desktop 4.0", "fedora23", "deepin", "neokylin"],
    ["type1", 1, 2, 3, 4],
    ["type2", 2, 4, 6, 8],
    ["type3", 3, 6, 9, 12],
    ["type4", 4, 8, 12, 16],
    ["type5", 5, 10, 15, 2000],
]
#第一行写入“处理器运算性能结果”ｔｉｔｌｅ
worksheet.merge_range('A1:E1', "处理器运算性能", title_format)
worksheet.set_row(0, 45)
#第二行写入“测试工具名称”
worksheet.merge_range('A2:E2', "测试工具：SPEC CPU 2000", info_format)
#第二行写入“性能指标”
worksheet.merge_range('A3:E3',"性能指标： Spec2000 包括 SPECint2000、SPECfp2000、SPECint_rate2000、 SPECfp_rate2000 4个测试项", info_format)
worksheet.merge_range('A4:E4', "对比说明：其中的得分越大说明CPU性能越高", info_format)
worksheet.merge_range('A5:E5', "测试参数： runspec -c test.cfg -i ref -n 3 -r -u 4 -I all; runspec -c test.cfg -i ref -n 3 -I all", info_format)
for i in range(1,5):
    worksheet.set_row(i,21)
#第７行写入副标题
worksheet.merge_range('A7:E7', "SPEC2000 测试数据", ltitle_format)
worksheet.set_row(6, 24)
#worksheet.write_column('A1', data[0],format1)
#worksheet.write_column('B1', data[1], format1)
#worksheet.write_column('C1', data[2], format1) 
#worksheet.write_column('D1', data[3], format1)
#worksheet.write_column('E1', data[4], format1)
#worksheet.write_column('F1', data[5], format1)
# Configure the charts. In simplest case we just add some data series.

#制作表格
'''
chart.add_series({
    'name' : '=Sheet1!$A$2', #系列名称
    'categories': '=Sheet1!$B$1:$F1', #对比项目名称
    'values': '=Sheet1!$B$2:$F$2', 
    'gap': 200,
})
chart.add_series({
    'name' : '=Sheet1!$A$3',
    'values': '=Sheet1!$B$3:$F$3'
})
chart.add_series({
    'name' : '=Sheet1!$A$4',
    'values': '=Sheet1!$B$4:$F$4'
})
chart.add_series({
    'name' : '=Sheet1!$A$5',
    'values': '=Sheet1!$B$5:$F$5'
})
chart.set_size({'width': 540, 'height': 376})
chart.set_x_axis({
    'position_axis': 'between',
})
chart.set_title({'name': 'Spec2000'})
# 增加图形下方表格
#cahart.set_table()
# Insert the chart into the worksheet.
worksheet.insert_chart('A7', chart)
#workbook.add_chart({'type': 'bar', 'subtype': 'stacked'})
'''
workbook.close()
