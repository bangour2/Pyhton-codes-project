__author__ = 'mohammad bangoura'

import psycopg2

conn = psycopg2.connect(host = "localhost",user="birt", password="birt")
print ("{:<25s} {:50s}{:35s}".format('Customer number',
'Customer name','available credit'))

with conn as crs:
    cmd = '''
         select customerNumber,customerName, creditLimit
         from customers

        '''''
    crs = conn .cursor()
    crs.execute(cmd)
    customer_list = crs.fetchall()
# remaining rows of a query result, returning them as a list of tuples

    for cust in customer_list: # skip

        cmd = '''
            select amount from payments
            where customerNumber = %s

        '''
   # calcute payment total
        crs.execute(cmd,(cust[0],)) # repeated customer number
        payment_list = crs.fetchall()
        total_payment = 0

        for payment in payment_list:
            total_payment += payment[0] # add repeated


    # join Order table
        cmd = '''
            select orderNumber
            from orders
            where  customerNumber = %s

        '''
        crs.execute(cmd,(cust[0],))
        order_list = crs.fetchall()
        Order_Made = 0
    # get oderdetails table
        for order in order_list:
            cmd = '''
            select priceEach, quantityOrdered
            from orderdetails
            where orderNumber = %s
        '''
            crs.execute(cmd,(order[0],))
            order_orderList = crs.fetchall()

            for totalOrder in order_orderList:
                Order_Made += totalOrder[0]*totalOrder[1] # 1st column * 2nd column
            available_credit = (cust[2] + total_payment) - Order_Made


        if ((total_payment + cust[2]) < Order_Made):

            line_template = " {:<25d} {:<50s} {:<21.2f}"
            line = line_template.format(cust[0],cust[1], available_credit )
            print (line)



