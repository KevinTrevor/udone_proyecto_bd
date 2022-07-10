CREATE DATABASE IF NOT EXISTS chikkins
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Venezuela.1252'
    LC_CTYPE = 'Spanish_Venezuela.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

CREATE TABLE IF NOT EXISTS cliente(
    cedula VARCHAR(10) PRIMARY KEY NOT NULL,
    nombre VARCHAR(100),
    whatsapp VARCHAR(12) UNIQUE,
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