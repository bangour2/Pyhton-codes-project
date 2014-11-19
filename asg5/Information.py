#!C:\Python34\python.exe
__author__ = 'bango_000'

import cgi
import cgitb
cgitb.enable()
from jinja2 import Environment, FileSystemLoader

import psycopg2


fldr = FileSystemLoader("templates")
jenv = Environment(loader=fldr)

fldstor = cgi.FieldStorage()
customername_List = fldstor.getlist("customername")
customername = str(customername_List[0])

# basic info
conn = psycopg2.connect(host = "localhost",user="birt", password="birt")
crs = conn.cursor()

#1 single row of customer name and other info
cmd_1 = ''' select customernumber, contactlastname,
contactfirstname, phone, addressline1 from customers
where customername = %s '''
crs.execute(cmd_1, (customername,))
customer_list_1 = crs.fetchall()

#sales man
for emp in customer_list_1:
    cmd_2 = '''select firstname, lastname from employees FULL JOIN customers
    ON employees.employeenumber  = customers.salesrepemployeenumber where
    customername = %s'''
    crs.execute(cmd_2, (customername,))
    customer_list_2 = crs.fetchall()

cmd_3 = '''
    select orderNumber, orderdate from orders FULL JOIN customers ON
    orders.customernumber = customers.customernumber where  customername = %s
'''
crs.execute(cmd_3,(customername,))
order_number = crs.fetchall()

for order in order_number:
    cmd_4 = '''select priceEach, quantityOrdered from orderdetails, orders, customers
    where orderdetails.ordernumber = orders.ordernumber
    and orders.customernumber = customers.customernumber and customername = %s'''
    crs.execute(cmd_4,(customername,))
    order_List = crs.fetchall()
    Order_Made = 0

    for totalOrder in order_List:
        Order_Made += totalOrder[0]*totalOrder[1]


crs.execute("DROP TABLE IF EXISTS dummy;")
cmd_5 = '''CREATE TABLE dummy (Order_Made text);'''
crs.execute(cmd_5)
cmd_6 = '''insert into dummy (Order_Made) values ('''+str(Order_Made)+''') '''
crs.execute(cmd_6)
crs.execute("select * from dummy")
order_List = crs.fetchall()


crs.execute('''
select checknumber, paymentdate, amount from payments FUll JOIN customers ON
payments.customernumber = customers.customernumber where customername = %s''', (customername,))

pay_list = crs.fetchall()

    # create page
print("Content-Type: text/html; charset=UTF-8")
print("")
template = jenv.get_template("Information.html")
template_rendered = template.render(customername = customername,
    customer_list_1 = customer_list_1, customer_list_2 = customer_list_2,
    order_number = order_number, order_List = order_List, pay_list = pay_list)

print(template_rendered)

crs.execute("DROP TABLE IF EXISTS dummy;")
conn.commit()
conn.close()