from openpyxl import load_workbook
wb = load_workbook("sample_formular.xlsx", data_only=True) # 수식이 아닌 실제 데이터 가지고 옴
ws = wb.active
for row in ws.values:
    for cell in row:
        print(cell)

#evaluate  되지 않은 상태의 데이터는 None 이라고표시, 실제 excel 들어가면, excel 이 자동으로 계산을 해줌, 그리고 저장할것인지 물어봄, 저장하면 데이터로 출력됨.