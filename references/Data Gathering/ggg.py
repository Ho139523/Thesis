import xlsxwriter

s = """25.9
25.9 1.1530
22.9 1.1398
22.9 1.1398
29.9 1.1404
29.9 1.1404
37.5 1.1401
37.5 1.1401
90.8 1.2974
90.8 1.2974
90.8 1.2974
90.8 1.2974
90.8 1.2974
68.0 1.2601
68.0 1.2601
163.1 1.4437
163.1 1.4437
152.1 1.4626
169.3 1.5161
169.3 1.5161
169.3 1.5161
167.8 1.6050
167.8 1.6050
167.8 1.8050
167.8 1.6050
315.0 2.0710
315.0 2.0710
315.0 2.0710
315.0 2.0710
404.6 2.4360
404.6 2.4360"""

s = [ float(i) for i in (s.replace(' ', '\n')).split('\n')]
s.insert(1, 1.1530)
s1 = s[::2]
s2 = s[1::2]

workbook = xlsxwriter.Workbook('new.xlsx')

print(workbook)
worksheet = workbook.add_worksheet("Pressure drop")

print(worksheet)

for row in range(7,38):
    
    worksheet.write(row, 10, s1[(row-7)])
    worksheet.write(row, 11, s2[(row-7)])

workbook.close()

