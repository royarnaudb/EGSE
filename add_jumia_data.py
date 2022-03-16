from openpyxl import load_workbook

book = load_workbook('jumia_computers.xlsx')
sheet = book.active
id = 0
file = open('jumia_opensearch_format_data.bulk', 'w+')

for row in sheet:
    file.write('{ "index": { "_index" : "computers", "_type" : "_doc", "_id": "jumia_% s" }}\n' % id)
    file.write('{"url":"% s", "name": "% s", "price": "% s", "from": "Jumia.ug", "image_url": "% s"}\n' % (row[6].value.replace('"', ''), row[2].value.replace('"', '').replace("<br />",'').replace("\n",''), row[3].value.replace('"', ''), row[4].value.replace('"', '')))
    id += 1

file.close()
