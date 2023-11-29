-- Script init
CREATE DATABASE IF NOT EXISTS qro;


USE qro;

-- first table
CREATE TABLE IF NOT EXISTS clientes (
    clienteID INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Ap_pat VARCHAR(50) NOT NULL,
    Ap_mat VARCHAR(50) NOT NULL,
    RFC VARCHAR(20) NOT NULL
);

-- second table
CREATE TABLE IF NOT EXISTS Direcciones (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,
    clienteID INT NOT NULL,
    numero INT NOT NULL,
    calle VARCHAR(50) NOT NULL,
    colonia VARCHAR(50) NOT NULL,
    estado VARCHAR(30) NOT NULL,
    CP INT(5) NOT NULL,
    FOREIGN KEY (clienteID) REFERENCES clientes(clienteID)
);
