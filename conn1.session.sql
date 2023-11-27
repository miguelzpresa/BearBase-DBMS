USE qro;
SELECT * FROM clientes;

INSERT INTO Direcciones (OrderID, clienteID, numero, calle, colonia, estado, CP)
VALUES
(1, 1001, 3, 'Calle Principal', 'Centro', 'Ciudad México', 55000),
(2, 1002, 2, 'Avenida Juárez', 'Zona Norte', 'Monterrey', 64000),
(3, 1003, 4, 'Calle Independencia', 'Zona Sur', 'Guadalajara', 45100);