__author__ = 'mohammad bangoura'

import psycopg2

conn = psycopg2.connect(host = "localhost",user="birt", password="birt")
print ("{:<25s} {:50s}{:35s} {:38s}{:20s}{:20s}".format('Customer number',
'Customer name', 'Total of payments made', 'Total value of all orders made',
'Credit limit', 'Amount of available credit'))

with conn as crs:
    cmd = '''
         select customerNumber,customerName, creditLimit
         from customers

        '''''
    crs = conn .cursor()
    crs.execute(cmd)
    customer_list = crs.fetchall() # intialize to new table

    for cust in customer_list:

        cmd = '''
            select amount from payments
            where customernumber = %s

        '''
   # calcute payment total
        crs.execute(cmd,(cust[0],)) # just repeated customer number
        payment_list = crs.fetchall()  # initialize new  table
        total_payment = 0

        for payment in payment_list:
            total_payment += payment[0] # add repeated
    # join Order table
        cmd = '''
            select orderNumber
            from orders
            where  customernumber = %s

        '''
        crs.execute(cmd,(cust[0],)) # just repeated customer number
        order_list = crs.fetchall() # initialize new arranged table
        Order_Made = 0

    # get oderdetails table
        for order in order_list:
            cmd = '''
            select  quantityordered, priceeach
            from orderdetails
            where ordernumber = %s
        '''
            crs.execute(cmd,(order[0],))
            order_orderList = crs.fetchall()


            for totalOrder in order_orderList:
                Order_Made += (totalOrder[0]*totalOrder[1]) # 1st column * 2nd column
                available_credit = (cust[2] + total_payment) - Order_Made


        line_template = " {:<25d} {:35s}{:35.2f} {:40.2f}{:20.2f}{:20.2f}"
        line = line_template.format(cust[0],cust[1],total_payment,Order_Made,cust[2], available_credit )
        print (line)



