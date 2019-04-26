import os
import sys

orders_list = []

def push_order(dirname):
    for (path, dir, files) in os.walk(dirname):
        for filename in files:
            if filename.endswith('_orders.py'):
                orders_list.append(path+'\\'+filename)

push_order('./orders')

print('Importng: ')

f = open('orders_import.py', 'w')

f.write('orders_list = []\n')

for ele in orders_list:
    ele = ele.replace('./', '').replace('\\', '.').replace('.py', '')
    f.write('import ' + ele + '\n')
    f.write('orders_list.append(' + ele + '.orders)\n')
    print(ele)

#orders_list.append(orders.test_orders.orders)