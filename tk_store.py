# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.ttk as ttk
from datasource import Database
from tkinter.messagebox import askokcancel

class Store_App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion de Tienda")
        self.resizable(0, 0)
        
        self.dB = Database()
        
        frm = tk.Frame(self)
        frm.pack()
        
        frm1 = tk.LabelFrame(frm, text="  Información de clientes  ")
        frm1_table = tk.Frame(frm1)
        frm1_details = tk.Frame(frm1)
        frm1_table.pack(side=tk.LEFT, padx=5, pady=5, anchor=tk.N)
        frm1_details.pack(side=tk.LEFT, padx=5, pady=5, anchor=tk.N)
        
        frm2 = tk.Frame(frm)
        frm1.pack(padx=10, pady=10, anchor=tk.N)
        frm2.pack(padx=10, pady=10)
        
        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure("Treeview.Heading", background="black", foreground="white")
        
        self.var_id = tk.StringVar()
        self.var_name = tk.StringVar()
        self.var_address = tk.StringVar()
        self.var_city = tk.StringVar()
        self.var_country = tk.StringVar()
        self.var_contact = tk.StringVar()
        self.var_orders = tk.StringVar()
        self.click_update = False
        
        self.protocol("WM_DELETE_WINDOW", self.quit_app)
        
        # ------------------------------- frm1 ----------------------------------------
        self.scr_table = tk.Scrollbar(frm1_table)
        self.cust_table = ttk.Treeview(frm1_table, columns=[1, 2], yscrollcommand=self.scr_table.set)
        self.scr_table.config(command=self.cust_table.yview)
        self.cust_table.pack(side=tk.LEFT)
        self.scr_table.pack(side=tk.LEFT, expand=True, fill=tk.Y)
        
        self.cust_table.heading("#0", text="ID")
        self.cust_table.heading("#1", text="País", anchor=tk.W)
        self.cust_table.heading("#2", text="Nombre Completo", anchor=tk.W)
        
        self.cust_table.column("#0", width=50, minwidth=50, stretch=tk.NO, anchor=tk.W)
        self.cust_table.column("#1", width=80, minwidth=80, stretch=tk.NO)
        self.cust_table.column("#2", width=280, minwidth=280, stretch=tk.NO)
        
        # Se define la etiqueta "par" para las filas pares en la tabla
        self.cust_table.tag_configure('par', background='lightgray')
        
        # Llena la tabla con todos los clientes de la tienda ordenados por ID
        self.load_table_data()
        
        self.lblCustomerId = tk.Label(frm1_details, text="ID:")
        self.lblCustomerName = tk.Label(frm1_details, text="Nombre:")
        self.lblAddress = tk.Label(frm1_details, text="Dirección:")
        self.lblCity = tk.Label(frm1_details, text="Ciudad:")
        self.lblCountry = tk.Label(frm1_details, text="País:")
        self.lblContactName = tk.Label(frm1_details, text="Contacto:")
        self.lblNroOrders = tk.Label(frm1_details, text="Ordenes Act:")
        self.entCustomerId = tk.Entry(frm1_details, textvariable=self.var_id, width=30, state='disable')
        self.entCustomerName = tk.Entry(frm1_details, textvariable=self.var_name, width=30, state='disable')
        self.entAddress = tk.Entry(frm1_details, textvariable=self.var_address, width=30, state='disable')
        self.entCity = tk.Entry(frm1_details, textvariable=self.var_city, width=30, state='disable')
        self.entCountry = tk.Entry(frm1_details, textvariable=self.var_country, width=30, state='disable')
        self.entContactName = tk.Entry(frm1_details, textvariable=self.var_contact, width=30, state='disable')
        self.entNroOrders = tk.Entry(frm1_details, textvariable=self.var_orders, width=30, state='disable')

        self.lblCustomerId.grid(row=0, column=1, padx=5, pady=5, sticky=tk.E)
        self.lblCustomerName.grid(row=1, column=1, padx=5, pady=5, sticky=tk.E)
        self.lblAddress.grid(row=2, column=1, padx=5, pady=5, sticky=tk.E)
        self.lblCity.grid(row=3, column=1, padx=5, pady=5, sticky=tk.E)
        self.lblCountry.grid(row=4, column=1, padx=5, pady=5, sticky=tk.E)
        self.lblContactName.grid(row=5, column=1, padx=5, pady=5, sticky=tk.E)
        self.lblNroOrders.grid(row=6, column=1, padx=5, pady=5, sticky=tk.E)
        self.entCustomerId.grid(row=0, column=2, padx=5, pady=5, sticky=tk.E)
        self.entCustomerName.grid(row=1, column=2, padx=5, pady=5, sticky=tk.E)
        self.entAddress.grid(row=2, column=2, padx=5, pady=5, sticky=tk.E)
        self.entCity.grid(row=3, column=2, padx=5, pady=5, sticky=tk.E)
        self.entCountry.grid(row=4, column=2, padx=5, pady=5, sticky=tk.E)
        self.entContactName.grid(row=5, column=2, padx=5, pady=5, sticky=tk.E)
        self.entNroOrders.grid(row=6, column=2, padx=5, pady=5, sticky=tk.E)
        
        # ------------------------------- frm2 ----------------------------------------
        self.btnOrdenarId = tk.Button(frm2, text="Ordenar por ID", width=18, command=lambda: self.load_table_data(0))
        self.btnOrdenarNombre = tk.Button(frm2, text="Ordenar por Pais", width=18, command=lambda: self.load_table_data(1))
        self.btnCambiarContacto = tk.Button(frm2, text="Actualizar Contacto", width=18, command=self.update_contact, state='disable')
        self.btnConsultarOrdenes = tk.Button(frm2, text="Ordenes de Compra", width=18, command=self.orders_window, state='disable')
        self.btnSalir = tk.Button(frm2, text="Salir", width=18, command=self.quit_app)
        
        self.btnOrdenarId.grid(row=0, column=0, padx=5, pady=5)
        self.btnOrdenarNombre.grid(row=0, column=1, padx=5, pady=5)
        self.btnCambiarContacto.grid(row=0, column=2, padx=5, pady=5)
        self.btnConsultarOrdenes.grid(row=0, column=3, padx=5, pady=5)
        self.btnSalir.grid(row=0, column=4, padx=10, pady=5)
        
        # -------------------------------- Binds -----------------------------------------
        self.cust_table.bind("<<TreeviewSelect>>", self.fill_details)
        
        
    def load_table_data(self, order_by=0):
        ''''Carga la lista de clientes con los datos de las columnas de la tabla de 
        clientes, ordenados por ID o por Pais, así como limpia los Entries. 
        Utilice la etiqueta "par" para las filas pares de la tabla'''
        self.cust_table.delete(*self.cust_table.get_children())
        
        data = []

        for item in self.dB.list_customers(order_by):
            data.append(item)
        
        for item in data:
            self.cust_table.insert("", tk.END, text=item[0], values=[item[1],item[2]])
    
          
    def fill_details(self, event):
        '''Carga los Entries los datos del cliente, como resultado de hacer click sobre 
        una de las filas de la tabla. Si el cliente registra ordenes, se habilita 
        el boton "Consultar Ordenes". De lo contrario, se deshabilita'''
        
        cust_id,nombre,direccion,ciudad,pais,contacto = self.dB.details_customer(self.cust_table.item(self.cust_table.selection())['text'])
        
        self.var_id.set(cust_id)
        self.var_name.set(nombre)
        self.var_address.set(direccion)
        self.var_city.set(ciudad)
        self.var_country.set(pais)
        self.var_contact.set(contacto)
        
        self.var_orders.set(self.dB.number_orders_by_client(cust_id))
        
        self.btnCambiarContacto.config(state='normal')
        
        if self.var_orders.get() == '0':
            self.btnConsultarOrdenes.config(state='disable')
        else:
            self.btnConsultarOrdenes.config(state='normal')
        
    
    def update_contact(self):
        '''Si los Entries tienen contenido, se habilita el campo "Contacto" para 
        editar su contenido. Al grabar, se actualiza la base de datos. Deshabilitar 
        los botones en tiempo de edición y habilitar al terminar (ver documentacion)'''
        if self.click_update:
            
            if self.entContactName.get():
                self.dB.update_contact(self.var_id.get(),self.var_contact.get())
                
            else:
                showerror("Error en el registro", 
                          "Los campos no estan completos.\nEl cambio no se guarda en la base de datos")
            
            self.btnOrdenarId.config(state='normal')
            self.btnOrdenarNombre.config(state='normal')
            self.btnCambiarContacto.config(text='Actualizar Contacto')
            self.btnConsultarOrdenes.config(state='normal')
            self.btnSalir.config(state='normal')
            self.entContactName.config(state='disable')
            self.click_update = False
        
        else:
            self.btnOrdenarId.config(state='disable')
            self.btnOrdenarNombre.config(state='disable')
            self.btnCambiarContacto.config(text='Guardar Cambios')
            self.btnConsultarOrdenes.config(state='disable')
            self.btnSalir.config(state='disable')
            
            self.entContactName.config(state='normal')
            
            self.click_update = True
        
    
    def orders_window(self):
        '''Abre la ventana secundaria con los detalles de las Ordenes de Compra'''
        Orders_Window(self.dB,self.var_id.get()).mainloop()
    
    
    def quit_app(self):
        if askokcancel(title="Salir", message="¿Desea salir del aplicación?"):
            self.destroy()
            

class Orders_Window(tk.Toplevel):
    '''Clase de la ventana Secundaria. Debe de recibir los siguietes parametros:
            - Base de Datos
            - Id de cliente
            
        Debe de definir el diseño de la ventana y el funcionamiento de esta
        (ver documentación)
    '''
    def __init__(self, dB, cust_id):
        super().__init__()
        self.title("Ordenes por cliente")
        self.resizable(0, 0)
        self.focus()
        self.grab_set()
        
        self.dB = dB
        self.cust_id = cust_id
        
        self.var_orden = tk.StringVar()
        self.var_empleado = tk.StringVar()
        self.var_fecha = tk.StringVar()
        self.var_transporte = tk.StringVar()
        
        frm = tk.Frame(self)
        frm.pack()
        
        frm1 = tk.LabelFrame(frm, text="  Ordenes de Compra  ")
        frm1.pack(padx=10,pady=10)
        
        frm2 = tk.LabelFrame(frm, text="Productos")
        frm2.pack(padx=10,pady=10)
        
        #------------------------------------frm1----------------------------------------
        
        self.cboOrdenes = ttk.Combobox(frm1, state='readonly', 
                                      values=self.dB.orders_by_client(cust_id))
        self.lblOrden = tk.Label(frm1, text="Nro. Orden:")
        self.lblEmpleado = tk.Label(frm1, text="Empleado:")
        self.lblFecha = tk.Label(frm1, text="Fecha:")
        self.lblTransporte = tk.Label(frm1, text="Transporte:")
        self.entOrden = tk.Entry(frm1, width=20, textvariable=self.var_orden, state='disable')
        self.entEmpleado = tk.Entry(frm1, width=20, textvariable=self.var_empleado, state='disable')
        self.entFecha = tk.Entry(frm1, width=20, textvariable=self.var_fecha, state='disable')
        self.entTransporte = tk.Entry(frm1, width=20, textvariable=self.var_transporte, state='disable')
        self.btnDetalles = tk.Button(frm1, text="Detalles", width=20, state='disable', command=self.btn_detalles)
        
        self.cboOrdenes.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.lblOrden.grid(row=0, column=1, padx=5, pady=5, sticky=tk.E)
        self.lblEmpleado.grid(row=1, column=1, padx=5, pady=5, sticky=tk.E)
        self.lblFecha.grid(row=2, column=1, padx=5, pady=5, sticky=tk.E)
        self.lblTransporte.grid(row=3, column=1, padx=5, pady=5, sticky=tk.E)
        self.entOrden.grid(row=0, column=2, padx=5, pady=5, sticky=tk.E)
        self.entEmpleado.grid(row=1, column=2, padx=5, pady=5, sticky=tk.E)
        self.entFecha.grid(row=2, column=2, padx=5, pady=5, sticky=tk.E)
        self.entTransporte.grid(row=3, column=2, padx=5, pady=5, sticky=tk.E)
        self.btnDetalles.grid(row=0, column=3, padx=5, pady=5, sticky=tk.E)
        
        self.cboOrdenes.bind("<<ComboboxSelected>>", self.order_selected)
        
        #------------------------------------frm2------------------------------------------
        
        self.prodScroll = tk.Scrollbar(frm2)
        self.prodTable = ttk.Treeview(frm2, columns=("#1","#2","#3"), yscrollcommand=self.prodScroll.set)
        self.prodScroll.config(command=self.prodTable.yview)
        self.prodTable.pack(side=tk.LEFT)
        self.prodScroll.pack(side=tk.LEFT, expand=True, fill=tk.Y)
        
        self.prodTable.heading("#0", text="Nombre", anchor=tk.W)
        self.prodTable.heading("#1", text="Cantidad", anchor=tk.W)
        self.prodTable.heading("#2", text="Precio Unit", anchor=tk.W)
        self.prodTable.heading("#3", text="Precio Total", anchor=tk.W)
        
        self.prodTable.column("#0", width=260, minwidth=260, stretch=tk.NO, anchor=tk.W)
        self.prodTable.column("#1", width=80, minwidth=80, stretch=tk.NO, anchor=tk.E)
        self.prodTable.column("#2", width=80, minwidth=80, stretch=tk.NO, anchor=tk.E)
        self.prodTable.column("#3", width=80, minwidth=80, stretch=tk.NO, anchor=tk.E)
        
    def order_selected(self, event):
        ''''Carga los datos del cliente con respecto a la orden seleccionada'''
        apellido,nombre,fecha,transporte = self.dB.order_info(self.cboOrdenes.get())
        
        self.var_orden.set(self.cboOrdenes.get())
        self.var_empleado.set(f"{nombre} {apellido}")
        self.var_fecha.set(fecha)
        self.var_transporte.set(transporte)
        
        self.btnDetalles.config(state='normal')
        
    def btn_detalles(self):
        '''Limpia y luego rellena la tabla con los detalles de la orden del cliente'''
        
        self.prodTable.delete(*self.prodTable.get_children())
        
        data = []
        suma = 0

        for item in self.dB.order_details(self.cboOrdenes.get()):
            data.append(item)
            suma+=item[3]
        
        for item in data:
            self.prodTable.insert("", tk.END, text=item[0], values=[item[1],f"{item[2]:.2f}",f"{item[3]:.2f}"])
        self.prodTable.insert("", tk.END, text="TOTAL", values=["","",f"{suma:.2f}"])
        
Store_App().mainloop()


