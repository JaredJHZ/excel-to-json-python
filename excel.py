from xlrd import open_workbook
import json
data = {}
wb = open_workbook('book2.xlsx')
values = []

for s in wb.sheets():
    #print 'Sheet:',s.name
    for row in range(1, s.nrows):
        col_names = s.row(0)
        col_value = []
        for name, col in zip(col_names, range(s.ncols)):
            value  = (s.cell(row,col).value)
            try : 
                value = str(float(value))
            except : 
                pass
            col_value.append(value)
        values.append(col_value)

for valor in values:
    data[valor[0]] = {
        "familia": valor[2],
        "precio":valor[1]
    }

with open('windows.json', 'w') as outfile:
    json.dump(data, outfile)