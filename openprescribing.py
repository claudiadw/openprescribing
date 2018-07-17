from __future__ import with_statement
from __future__ import absolute_import
import csv
import requests
import pandas

print
bnf_code = input("BNF code: ")
year = input("Year: ")

csv_url = u'https://openprescribing.net/api/1.0/spending/?code='+bnf_code+u'&format=csv'

with requests.Session() as s:
    download = s.get(csv_url)
    decoded = download.content.decode(u'utf-8')
    cr = csv.reader(decoded.splitlines(), delimiter=',')
    lists = list(cr)
    table = list(lists[1:])
    df = pandas.DataFrame(table)

date_column=list(df.iloc[:,1])

def index_containing_substring(the_list, substring):
    for i, s in enumerate(the_list):
        if substring in s:
              return i
            
date_index = index_containing_substring(date_column,year)
print

actual_cost_list=df.iloc[date_index:date_index+12,0]
actual_cost = 0
for x in actual_cost_list:
    y = float(x)
    actual_cost+= y
print (u"Actual cost = "),(unichr(163)),(unicode(round(actual_cost,2)))

items_list=df.iloc[date_index:date_index+12,2]
items = 0
for x in items_list:
    y = int(x)
    items+= y
print (u'Items = ')+(unicode(items))

quantity_list=df.iloc[date_index:date_index+12,3]
quantity = 0
for x in quantity_list:
    y = int(x)
    quantity+= y
print (u'Quantity = ')+(unicode(quantity))

print
