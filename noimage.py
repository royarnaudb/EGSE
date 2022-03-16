from openpyxl import load_workbook

book = load_workbook('jumia_computers_dirty.xlsx')
sheet = book.active

for cell in sheet["E"]:
    if cell.value == "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7":
        cell.value = 'n'
book.save(filename="jumia_computers.xlsx")