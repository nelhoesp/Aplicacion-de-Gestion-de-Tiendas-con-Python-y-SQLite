## Gestión de órdenes con Python

Se desarrolla una aplicación completa para la gestión de las órdenes de compra de los clientes de una tienda, en una interfaz gráfica y una base de datos con la información de la empresa.

### Descripción
La aplicación a desarrollar consta de dos ventanas de usuario: la ventana principal y la ventana secundaria.
### Ventana Principal
Al ejecutar el programa se mostrará la Ventana Principal, que contiene un Treeview, una colección de Labels y Entrys, así como cinco botones.

![principal](https://github.com/nelhoesp/Gestion-de-ordenes-con-Python/assets/156467223/b0c8f5c2-0b83-4d33-aaec-515b7829ef9d)

El Treeview muestra el listado de los clientes en la tienda, ordenados por ID de cliente.
La información de la tabla se puede reordenar en función de los botones “Ordenar por ID”, y “Ordenar por País” para permitirle al usuario hacer una búsqueda de un cliente en función de una de estas columnas. Estos botones vuelven a cargar la tabla con los datos ordenados según la columna.
En la siguiente imagen se muestra la Ventana Principal luego de hacer presionar el botón “Ordenar por País”.

![ordenado](https://github.com/nelhoesp/Gestion-de-ordenes-con-Python/assets/156467223/7e37338e-b21b-456e-be74-8b27c1aaefd4)

El botón “Actualizar Contacto, permite editar el campo asociado a la información de Contacto. Al hacer click en el botón, si es que existen registros en los campos este habilita el campo, cambia el nombre del botón por “Guardar Cambios” y deshabilita los demás botones para evitar que otras funciones interfieran esta acción.

![actualizar](https://github.com/nelhoesp/Gestion-de-ordenes-con-Python/assets/156467223/56ee1c57-018d-4583-8401-be92791c4435)

Si se hace click , regresa a su condición “Actualizar Contacto” y a habilitar los botones y deshabilitar el campo “Contacto”. Esta modificación se registra en la Base de Datos.

![editado](https://github.com/nelhoesp/Gestion-de-ordenes-con-Python/assets/156467223/abf243a9-3360-4bde-b52e-37ae12fa81a6)

### Ventana Secundaria
El botón “Órdenes de Compra” se habilita solamente si en el campo “Ordenes Act” se tiene un valor mayor a 0. Este botón abre una Ventana Secundaria que muestra el listado de las Órdenes de Compra del cliente y el detalle de los productos asociado a esta Orden.
Las Órdenes de Compra se muestran en el Combobox.

![imagen](https://github.com/nelhoesp/Gestion-de-ordenes-con-Python/assets/156467223/15d9a831-d2ab-4fb9-962a-d76631e9f29d)

Al seleccionar un elemento de la lista, se cargan en los Entries la información del número de orden, el empleado que registro la orden, la fecha de registro y la empresa de transporte encargada de llevar la orden al cliente.

![imagen](https://github.com/nelhoesp/Gestion-de-ordenes-con-Python/assets/156467223/c4edb867-4a16-46d9-893e-578a11006d2a)

Si existe información en estos campos, el botón “Detalles” se habilita. Al hacer click en el botón, se llena una tabla Treeview con los detalles de los productos asociados a la orden de compra y el total de la orden. Esta tabla muestra información ordenada por el nombre del producto.
Al cerrar esta ventana se retorna a la Ventana Principal.

![imagen](https://github.com/nelhoesp/Gestion-de-ordenes-con-Python/assets/156467223/9d358e48-66ea-4c8d-930f-08508ff57ce1)

