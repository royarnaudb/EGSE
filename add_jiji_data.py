from openpyxl import load_workbook

book = load_workbook('jiji_computers.xlsx')
sheet = book.active
id = 0
file = open('jiji_opensearch_format_data.bulk', 'w+')

for row in sheet:
    file.write('{ "index": { "_index" : "computers", "_type" : "_doc", "_id": "jiji_% s" }}\n' % id)
    file.write('{"url":"% s", "name": "% s", "price": "% s", "from": "Jiji.ug", "image_url": "% s"}\n' % (row[6].value.split('?', 1)[0], row[2].value, row[3].value, row[4].value))
    id += 1

file.close()
