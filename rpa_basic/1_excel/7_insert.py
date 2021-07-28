from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# ws.insert_rows(8) # 8번쨰 줄이 비워짐

# ws.insert_rows(8, 5) # 8번쨰 줄 위치에 5줄 추가

ws.insert_cols(2, 3) # B 번쨰 3열 빈열 추가

wb.save("sample_insert_cols.xlsx")