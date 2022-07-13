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
    monto_delivery FLOAT NOT NULL,
    modo_pago VARCHAR(20) NOT NULL,
    total FLOAT NOT NULL,
    screenshot VARCHAR(500),
    estado VARCHAR(20) NOT NULL,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    ciudad VARCHAR(50) NOT NULL,
    municipio VARCHAR(50) NOT NULL,
    observaciones VARCHAR(500) NOT NULL
);