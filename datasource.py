# -*- coding: utf-8 -*-
import sqlite3

class Database:
    datafile = "northwind.db"
    def __init__(self):
        self.conn = sqlite3.connect(Database.datafile)
        self.cur = self.conn.cursor()
        
        
    def __del__(self):
        self.conn.close()
    

    def list_customers(self, col_number=0):
        '''Retorna una lista de tuplas con (id_cliente, pais, nombre_cliente),
        ordenadas por el id_cliente o el pais segun el numero de
        columna (col_number 0 para id, col_number 1 para pais). Valor 0 
        por defecto'''
        if col_number==0:
            self.cur.execute("SELECT CustomerID, Country, CustomerName FROM Customers ORDER BY CustomerID")
            return [item for item in self.cur]
        elif col_number==1:
            self.cur.execute("SELECT CustomerID, Country, CustomerName FROM Customers ORDER BY Country")
            return [item for item in self.cur]
    

    def details_customer(self, cust_id):
        '''Retorna una tupla con los detalles de un cliente segun id. La tupla contiene
        los datos (id_cliente, nombre_cliente, direccion, ciudad, pais, nombre_contacto)'''
        self.cur.execute('''SELECT CustomerID,CustomerName,Address,City,Country,ContactName
                         FROM Customers
                         WHERE CustomerID = ?''',(cust_id,))
        return self.cur.fetchone()
    

    def number_orders_by_client(self, cust_id):
        '''Retorna el numero de Ordenes de Compra activa de un cliente
        segun el cust_id'''
        self.cur.execute("SELECT COUNT(OrderID) FROM Orders WHERE CustomerID = ?",(cust_id,))
        return self.cur.fetchone()[0]
    

    def orders_by_client(self, cust_id):
        '''Retorna una lista con los numeros de orden de todas las ordenes 
        de compra de un cliente en la tienda segun cust_id: 
        [10248, 10249, 10251, ...]'''
        self.cur.execute("SELECT OrderID FROM Orders WHERE CustomerID = ?",(cust_id,))
        return [item[0] for item in self.cur.fetchall()]


    def update_contact(self, cust_id, name):
        '''Actualiza el nombre del contacto de un cliente en función del cust_id'''
        self.cur.execute("""UPDATE Customers 
                            SET ContactName = ?
                            WHERE CustomerID = ?""", (name, cust_id))
        self.conn.commit()
    
   
    def order_info(self, order_id):
        '''Retorna una tupla con la siguente información:
            (apellido_empleado, nombre_empleado, fecha, empresa_transporte)'''
        self.cur.execute('''SELECT Employees.LastName,Employees.FirstName,
                            Orders.OrderDate,Shippers.ShipperName
                            FROM Employees
                            JOIN Orders
                            JOIN Shippers
                            ON Employees.EmployeeID = Orders.EmployeeID AND
                            Orders.ShipperID = Shippers.ShipperID
                            WHERE Orders.OrderID = ?''',(order_id,))
        return self.cur.fetchone()
    

    def order_details(self, order_id):
        '''Retorna una lista de tuplas con los detalles de los productos 
        asociado a una orden de compra, ordenado por el nombre del producto: 
        [(nombre_producto, cantidad, precio_unitario, precio_total), (...), ...]'''
        self.cur.execute('''SELECT Products.ProductName,OrderDetails.Quantity,Products.Price,
                             (Products.Price*OrderDetails.Quantity)
                            FROM OrderDetails JOIN Products
                            ON OrderDetails.ProductID = Products.ProductID
                            WHERE OrderDetails.OrderID = ?
                            ORDER BY Products.ProductName''',(order_id,))
        return self.cur.fetchall()
    

    def order_total_price(self, order_id):
        '''Retorna el valor total de una orden'''
        self.cur.execute('''SELECT SUM(Products.Price*OrderDetails.Quantity)
                            FROM OrderDetails JOIN Products
                            ON OrderDetails.ProductID = Products.ProductID
                            WHERE OrderDetails.OrderID = ?''',(order_id,))
        return self.cur.fetchone()[0]
    

    
def main():
    print("Testing Class Database...")
    print()
    # Script de Prueba de la clase Database.
    # Se especifican los valores de retorno de las pruebas para que 
    # valide rapidamente la clase Database
    #
    # Pruebe deshabilitar las pruebas eliminando el comentario para
    # probar los diferentes métodos de la clase.
    dB = Database()
    
    # Debe imprimir 5 TUPLAS con la siguiete informacion:
    # (12, 'Argentina', 'Cactus Comidas para llevar')
    # (54, 'Argentina', 'Océano Atlántico Ltda.')
    # (64, 'Argentina', 'Rancho grande')
    # (20, 'Austria', 'Ernst Handel')
    # (59, 'Austria', 'Piccolo und mehr')
    
    #for item in dB.list_customers(1)[:10]:
    #    print(item)
    #else:
    #    print()
    
    # Debe imprimr 1 TUPLA con la sigueinte informacion:
    # (75, 'Split Rail Beer & Ale', 'P.O. Box 555', 'Lander', 'USA', 'Art Braunschweiger')
    
    #print(dB.details_customer(75)); print()
    
    # Debe imprimr el valor "6"
    
    #print(dB.number_orders_by_client(75)); print()
    
    # Debe de imprimir los siguientes valores:
    # 10271
    # 10329
    # 10349
    # 10369
    # 10385
    # 10432
    
    #for item in dB.orders_by_client(75):
    #    print(item)
    #else:
    #    print()
    
    # Debe imprimir una TUPLA con la siguiente información
    # ('Steven', 'Buchanan', '1996-07-04', 'Federal Shipping')
   
    #print(dB.order_info(10248)); print()
    
    # Debe imprimir 3 TUPLAS con la siguiente información:
    # ('Mozzarella di Giovanni', 5, 34.8, 174.0)
    # ('Queso Cabrales', 12, 21, 252)
    # ('Singaporean Hokkien Fried Mee', 10, 14, 140)
    
    #for item in dB.order_details(10248):
        #print(item)
    #else:
        #print()
    
    # Debe imprimir el valor "566.0"
    
    #print(dB.order_total_price(10248))
    
    del(dB)


if __name__ == "__main__":
    main()