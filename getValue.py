import xml.etree.ElementTree as ET
import xlwt

# create table
table = xlwt.Workbook() 
# create sheet
sheet = table.add_sheet('sheet1')
sheet_2 = table.add_sheet('sheet2')

# read from static.xml
tree = ET.parse('static.xml')
root = tree.getroot()
# read from dynamic.xml
tree2 = ET.parse('dynamic.xml')
root2 = tree2.getroot()

# using Element.iter() to get routeid & roadsection
# write into spped.xls
counter = 0
for info in root.iter('Info'):
    sheet.write(counter,0,info.attrib['routeid'])
    sheet.write(counter,1,info.attrib['roadsection'])
    for info2 in root2.iter('Info'):
        if info2.attrib['routeid'] == info.attrib['routeid']:
            sheet.write(counter,2,info2.attrib['value'])
            sheet.write(counter,3,info2.attrib['datacollecttime'])
            break
    counter = counter + 1 

# save table
table.save('getValue.xls')



