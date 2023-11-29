CREATE USER IF NOT EXISTS 'adminqro'@'localhost' IDENTIFIED BY 'patos104';
--CREATE USER IF NOT EXISTS 'adminmore'@'localhost' IDENTIFIED BY 'jojo555';
grant select,insert,update,delete on qro.* to 'adminqro'@'localhost';

flush privileges;

CREATE DATABASE IF NOT EXISTS qro;

SHOW DATABASES;
USE qro;
--INT AUTO_INCREMENT PRIMARY KEY,
-- first table
CREATE TABLE IF NOT EXISTS clientes (
	    clienteID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    Nombre VARCHAR(50) NOT NULL,
    Ap_pat VARCHAR(50) NOT NULL,
    Ap_mat VARCHAR(50) NOT NULL,
    RFC VARCHAR(20) NOT NULL
);

-- second table AUTO_INCREMENT PRIMARY KEY
CREATE TABLE IF NOT EXISTS Direcciones (
    OrderID INT AUTO_INCREMENT PRIMARY KEY NOT NULL, 
    clienteID INT NOT NULL,
    numero INT NOT NULL,
    calle VARCHAR(50) NOT NULL,
    colonia VARCHAR(50) NOT NULL,
    estado VARCHAR(30) NOT NULL,
    CP INT(5) NOT NULL,
    FOREIGN KEY (clienteID) REFERENCES clientes(clienteID)
);

USE qro;

LOAD DATA LOCAL INFILE '/home/sistemas/projects/BearBase-DBMS/clientes.csv'
INTO TABLE clientes
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS;



INSERT INTO Direcciones (OrderID, clienteID, numero, calle, colonia, estado, CP)
VALUES
(1, 1, 101, 'Calle Principal', 'Centro', 'Ciudad México', 55000),
(2, 4, 202, 'Avenida Juárez', 'Zona Norte', 'Monterrey', 64000),
(3, 3, 303, 'Calle Independencia', 'Zona Sur', 'Guadalajara', 45100);



CREATE DATABASE IF NOT EXISTS morelia;

SHOW DATABASES;
USE morelia;
--INT AUTO_INCREMENT PRIMARY KEY,
-- first table
CREATE TABLE IF NOT EXISTS clientes (
	    clienteID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    Nombre VARCHAR(50) NOT NULL,
    Ap_pat VARCHAR(50) NOT NULL,
    Ap_mat VARCHAR(50) NOT NULL,
    RFC VARCHAR(20) NOT NULL
);

-- second table AUTO_INCREMENT PRIMARY KEY
CREATE TABLE IF NOT EXISTS Direcciones (
    OrderID INT AUTO_INCREMENT PRIMARY KEY NOT NULL, 
    clienteID INT NOT NULL,
    numero INT NOT NULL,
    calle VARCHAR(50) NOT NULL,
    colonia VARCHAR(50) NOT NULL,
    estado VARCHAR(30) NOT NULL,
    CP INT(5) NOT NULL,
    FOREIGN KEY (clienteID) REFERENCES clientes(clienteID)
);

USE morelia;

LOAD DATA LOCAL INFILE '/home/sistemas/projects/BearBase-DBMS/clientes.csv'
INTO TABLE morelia
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS;



INSERT INTO Direcciones (OrderID, clienteID, numero, calle, colonia, estado, CP)
VALUES
(1, 1, 101, 'Calle Principal', 'Centro', 'Ciudad México', 55000),
(2, 4, 202, 'Avenida Juárez', 'Zona Norte', 'Monterrey', 64000),
(3, 3, 303, 'Calle Independencia', 'Zona Sur', 'Guadalajara', 45100);
