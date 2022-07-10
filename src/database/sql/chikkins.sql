CREATE DATABASE IF NOT EXISTS chikkins;

CREATE TABLE IF NOT EXISTS cliente(
    cedula VARCHAR(10) PRIMARY KEY NOT NULL,
    nombre VARCHAR(100),
    whatsapp VARCHAR(20) UNIQUE,
    email VARCHAR(100) UNIQUE
);

CREATE TABLE IF NOT EXISTS pedidos(
    id SERIAL PRIMARY KEY,
    cedula VARCHAR(10) REFERENCES cliente (cedula),
    cantidad INTEGER NOT NULL,
    monto_delivery MONEY GENERATED ALWAYS AS (5 * cantidad) STORED NOT NULL,
    total MONEY NOT NULL,
    screenshot BYTEA,
    estado VARCHAR(20) NOT NULL,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    direccion VARCHAR(100) NOT NULL,
    ciudad VARCHAR(50) NOT NULL,
    municipio VARCHAR(50) NOT NULL,
    observaciones VARCHAR(500) NOT NULL
);